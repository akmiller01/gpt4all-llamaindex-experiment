from langchain.llms import LlamaCpp
from llama_index import QuestionAnswerPrompt, LLMPredictor, ServiceContext, GPTSimpleVectorIndex, LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

embed_model = LangchainEmbedding(HuggingFaceEmbeddings())
llm_predictor = LLMPredictor(llm=LlamaCpp(model_path="../gpt4all/chat/gpt4all-lora-q-converted.bin"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embed_model)

index = GPTSimpleVectorIndex.load_from_disk('index.json', service_context=service_context)

query_str = "What factors have primarily caused driven changes in volumes of ODA in the last 10 years?"
QA_PROMPT_TMPL = (
    """
    Context:
    ---------------------
    {context_str}
    ---------------------
    Question: {query_str}
    Answer:
    """
)
QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

response = index.query(query_str, text_qa_template=QA_PROMPT)
print(response)
print(response.get_formatted_sources())

