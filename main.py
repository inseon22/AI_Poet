#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

import openai

openai.api_key='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'

# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(openai_api_key=openai.api_key)

# subject="AI"
# result = chat_model.invoke(subject+"에 대한 시를 써줘.")
# print(result.content)

import streamlit as st

st.title("인공지능 시인")
subject=st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
