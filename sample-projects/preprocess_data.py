from typing import List
from azure.storage.blob import BlobServiceClient
from constants.constants import *
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredPDFLoader, PyPDFDirectoryLoader, AzureBlobStorageFileLoader
import os
from PyPDF2 import PdfReader


class PreProcessData:

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len
        )

    def load_data(self, user_id: str) -> dict:
        blob_service_client = BlobServiceClient.from_connection_string(
            CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(user_id)

        blob_list = container_client.list_blob_names()
        docs = []
        metadata = {
            "doc_name": []
        }
        if not os.path.exists(f"./{user_id}"):
            os.mkdir(f"./{user_id}")

        for blob in blob_list:
            print(f"blob name - {blob}")
            print("\nDownloading blob to \n\t" + user_id)

            with open(file=os.path.join(rf'./{user_id}', blob), mode="wb") as download_file:
                download_file.write(
                    container_client.download_blob(blob).readall())
        return {"status": 200, "response": f"downloaded data to ./{user_id} dictionary"}

    def preprocess_data(self, user_id: str):

        # getting a specific page from the pdf file
        documents = []
        files = []
        chunked_list = []

        # Iterate directory
        for path in os.listdir(f"./{user_id}"):
            # check if current path is a file
            if os.path.isfile(os.path.join(f"./{user_id}", path)):
                files.append(path)

        for file in files:
            reader = PdfReader(f'./{user_id}/{file}')

            for page in reader.pages:
                text = page.extract_text()
                #documents.append(text)

                chunks = self.text_splitter.create_documents([text])
            # print(f"{chunks}\n\n")

                for chunk in chunks:
                    chunk.metadata = {"file_name": file}
                    chunked_list.append(chunk)

        return chunked_list

    def show_blob_list(self, user_id: str) -> list:
        blob_service_client = BlobServiceClient.from_connection_string(
            CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(user_id)

        return list(container_client.list_blob_names())



