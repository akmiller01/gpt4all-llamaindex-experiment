from langchain.llms import LlamaCpp
from llama_index import LLMPredictor, ServiceContext, SimpleDirectoryReader, GPTSimpleVectorIndex, LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

embed_model = LangchainEmbedding(HuggingFaceEmbeddings())
llm_predictor = LLMPredictor(llm=LlamaCpp(model_path="../gpt4all/chat/gpt4all-lora-q-converted.bin"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embed_model)

documents = SimpleDirectoryReader('./data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
index.save_to_disk("index.json")