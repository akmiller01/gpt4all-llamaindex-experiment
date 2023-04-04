from llama_index import GPTListIndex
from llama_index import LLMPredictor
from langchain.llms import LlamaCpp
from llama_index import GPTListIndex
from llama_index import LLMPredictor, ServiceContext

llm_predictor = LLMPredictor(llm=LlamaCpp(model_path="../gpt4all/chat/gpt4all-lora-q-converted.bin"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

index = GPTListIndex.load_from_disk('index.json', service_context=service_context)

response = index.query("What role does the public sector play in rural development?")
print(response)