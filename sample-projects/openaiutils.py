import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from constants.constants import *
from preprocess_data import PreProcessData
from utils import Utils
from metadata_resolver import MetadataResolver
from prompts import Prompts
from llm_utils import LLMUtils
import openai
from memory_buffer.memory_buffer import MemoryBuffer

preprocess_data = PreProcessData()
utils = Utils()
metadata_resolver = MetadataResolver()
prompts = Prompts()
llm_utils = LLMUtils()

# SET THESE IN THE DOCKER FILE
os.environ["OPENAI_API_BASE"] = ""
os.environ["AZURE_OPENAI_KEY"] = ""

openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")


class OpenaiUtils:

    def __init__(self) -> None:
        self.embeddings = OpenAIEmbeddings(
            client=any,
            deployment=DEPLOYMENT,
            model=MODEL,
            openai_api_base=OPENAI_API_BASE,
            openai_api_type=OPENAI_API_TYPE,
            chunk_size=1
        )
        self.memory = MemoryBuffer()

    def create_embeddings(self, user_id: str):

        # check whether index already exists
        try:
            if os.path.isdir(str(user_id)):
                utils.delete_folder(f"{user_id}-faiss-index")

            if not os.path.isdir(str(user_id)):

                preprocess_data.load_data(user_id)
                docs = preprocess_data.preprocess_data(user_id)

                faiss_index_name = f"{user_id}-faiss-index"
                print(f"creating index for {user_id}")
                faiss_index = FAISS.from_documents(docs, self.embeddings)
                faiss_index.save_local(faiss_index_name)

                # delete the folder containing documents after creating the faiss index
                utils.delete_folder(user_id)

                print(f"{user_id} documents deleted successfully!!")
                return {"status": 200, "response": "embedding creation done"}
            else:
                return {"status": 200, "response": "FAISS index already exists!!!"}

        except Exception as dir_exist:
            return dir_exist

    def vectordb_search(self, query):
        #  embeddings_test_query = "who is Oshadha Randika Jayawardana?"
        try:
            
            db = FAISS.load_local(f"faiss-index", self.embeddings)
            context = db.similarity_search_with_score(
                query, k=8)  # docs is a document object
            # context_meta_data = metadata_resolver.filter_metadata(context)
            return context

        except Exception as e:
            print(e)
            return {"output_text": "No FAISS Index found.. please train the documents"}

    def generate_response(self, context, query):

        bot_response, cost_per_query = llm_utils.chat_completion(
            context, query)
        return {"output_text": bot_response, "query_cost": cost_per_query}

# response = OpenaiUtils()
# response.create_embeddings("user_1")
# print(response.vectordb_search("what happened to SC APPEAL NO: SC/APPEAL/46/2018", "user_1"))
