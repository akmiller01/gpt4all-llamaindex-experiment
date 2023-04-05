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
python3 index.py # Note, each document must be less than ~512 tokens
python3 query_without_index.py
python3 query_with_index.py
```

## Results
### Question: What role does the public sector play in rural development?

Without index:

1\. The Public Sector plays a crucial role in Rural Development by providing infrastructure, services and employment opportunities to the underprivileged population in rural areas. 2. They provide access to basic amenities such as roads, schools, health centres etc., which are essential for people's livelihood. 3. The Public Sector also helps in developing infrastructure like bridges, dams and water reservoirs that aid the farmers in boosting their agricultural output. 4. In terms of employment opportunities, public sector units located in rural areas offer jobs to local people who may not have access to private or corporate sectors. 5. These public sector units also help to empower the women folk and create a more gender-equal society.


With index:

The public sector plays a crucial role in rural development by providing investment and policy support to address market failures such as the under-provision of public goods and negative externalities. By investing in infrastructure and social services, the public sector can ensure access to markets and services for the poorest and most vulnerable populations. In addition, policies promoting sustainable agriculture and rural development can also play an important role in improving livelihoods in these areas.

### Question: What factors have primarily caused driven changes in volumes of ODA in the last 10 years?

Without index:

There are several factors that have contributed to driven changes in the volume of Official Development Assistance (ODA) over the last decade. These include global economic trends, political priorities and shifts in donor country policies. Here are some key drivers:

1\. Global Economic Trends: The global economy has been on an upswing since 2009, which has helped many developing countries achieve growth and stability. This has led to improvements in their economic conditions, resulting in less ODA dependency.

2\. Political Priorities: Donor governments have prioritized areas such as education, healthcare and climate change in recent years, leading to an increase in aid for those sectors. In addition, there has been a shift towards more sustainable approaches to development, which has led to increased investment in infrastructure that promotes long-term growth rather than just short-term gains.

3\. Shifts in Donor Country Policies: There have been changes in the policies of donors, such as the United Kingdom's "Aid for Trade" initiative and the United States' focus on private sector investment in foreign aid. These shifts have led to a more target

With index:

The primary factors that have contributed to driving changes in volumes of ODA in the last 10 years are the Millennium Development Goals (MDGs) and increased bilateral aid from major donor countries.