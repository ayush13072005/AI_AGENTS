from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

st.header("Research Assistant")
user_input = st.text_input("Enter your query:")
if st.button("Summarize"):
    response = model.invoke(user_input)
    st.write("Response:")
    st.write(response.content)