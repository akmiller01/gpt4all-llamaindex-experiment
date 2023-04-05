from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
template = """Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = LlamaCpp(model_path="../gpt4all/chat/gpt4all-lora-q-converted.bin")
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What factors have primarily caused driven changes in volumes of ODA in the last 10 years?"
response = llm_chain.run(question)
print(response)