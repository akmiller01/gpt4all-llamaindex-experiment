# gpt4all-llamaindex-experiment

https://github.com/nomic-ai/gpt4all
https://github.com/jerryjliu/llama_index
https://blog.ouseful.info/2023/04/04/running-gpt4all-on-a-mac-using-python-langchain-in-a-jupyter-notebook/

## Setup
```
python3.9 -m virtualenv venv
source venv/bin/activate
pip install pyllamacpp
pip install llama-index
pip install PyPDF2
pip install pyllama
python3 -m llama.download --model_size 7B --folder llama/
pyllamacpp-convert-gpt4all ../gpt4all/chat/gpt4all-lora-quantized.bin llama/tokenizer.model ../gpt4all/chat/gpt4all-lora-q-converted.bin
pip uninstall -y langchain
pip install --upgrade git+https://github.com/hwchase17/langchain.git
pip install llama-cpp-python
pip install sentence_transformers
```

## Run
```
source venv/bin/activate
python3 index.py
python3 query_without_index.py
python3 query_with_index.py
```

## Results
Question: What role does the public sector play in rural development?

Without index:

The public sector plays a crucial role in rural development. This sector can provide vital services such as education, healthcare, transportation, and electricity to rural areas that are not well-equipped with these facilities. It can also offer support for developing small and medium enterprises (SMEs) in the agricultural and manufacturing sectors of rural communities. Additionally, the public sector can provide financial assistance through schemes such as microfinance loans and credit programs. This type of assistance helps improve the economic status of the rural community by empowering individuals with the necessary skills to start and run a business or become financially independent. Furthermore, it can also help in promoting tourism in the area that could lead to more employment opportunities. Overall, the public sector plays an instrumental role in promoting development and improving the quality of life for rural communities.


With index:

The public sector plays an important role in rural development by providing both investment and policy support to tackle persistent market failures such as the under-provision of public goods and negative externalities (such as adaptation to climate change). The public sector also addresses the lack of protection for the poorest and most vulnerable people through, for instance, social protection. Similarly, digitalization is mostly financed by government entities and the private sector but public investment and ODA in particular fill an important gap where the private sector lacks incentives to intervene, such as in countering the digital divide. Overall, ODA is a critical public international resource that can help governments achieve sectoral development objectives that feed into wider national objectives, such as poverty reduction and sustainable development.
