from llama_index import SimpleDirectoryReader
from llama_index import LLMPredictor
from langchain.llms import LlamaCpp
from llama_index import SimpleDirectoryReader, GPTListIndex
from llama_index import LLMPredictor, ServiceContext


llm_predictor = LLMPredictor(llm=LlamaCpp(model_path="../gpt4all/chat/gpt4all-lora-q-converted.bin"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
documents = SimpleDirectoryReader('./data').load_data()
index = GPTListIndex.from_documents(documents, service_context=service_context)
index.save_to_disk("index.json")