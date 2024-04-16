import uvicorn
from fastapi import FastAPI
from openaiutils import OpenaiUtils
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from azureutils import AzureUtils
from preprocess_data import PreProcessData
from memory_buffer.memory_buffer import MemoryBuffer


app = FastAPI()

model = OpenaiUtils()
azure_client = AzureUtils()
preprocess_data = PreProcessData()
memory = MemoryBuffer()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query: str
    user_id: str
    metadata: list


class Container(BaseModel):
    user_id: str


class Train(BaseModel):
    user_id: str


@app.post("/train")
async def train(train: Train):
    response = model.create_embeddings(train.user_id)
    return response


@app.post("/ask")
async def ask_from_bot(query: Query):
    context = model.vectordb_search(query.query)
    bot_response = model.generate_response(context, query.query)

    # memory.add_to_history(query.query, context, bot_response["output_text"])
    # print(memory.show_history())

    return bot_response


@app.post("/create-container")
async def create_container(container: Container):
    user_id = container.user_id
    return azure_client.load_data_to_azure(user_id)


@app.post("/exists")
async def check_container_exists(container: Container):
    return azure_client.check_existing_container(container.user_id)


@app.post("/test")
async def test():
    return 200


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7005, proxy_headers=True)
