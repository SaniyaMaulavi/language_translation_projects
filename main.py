from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# 1. Load Translation Models
en_to_hi = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")
hi_to_en = pipeline("translation_hi_to_en", model="Helsinki-NLP/opus-mt-hi-en")

# 2. Wrap them in LangChain
llm_en_to_hi = HuggingFacePipeline(pipeline=en_to_hi)
llm_hi_to_en = HuggingFacePipeline(pipeline=hi_to_en)

# 3. Input text
english_text = "Good morning, have a nice day!"
hindi_text = "आप कैसे हैं?"

# 4. Translate
result_hi = llm_en_to_hi(english_text)
result_en = llm_hi_to_en(hindi_text)

print("English:", english_text)
print("➡ Hindi:", result_hi)
print()
print("Hindi:", hindi_text)
print("➡ English:", result_en)
