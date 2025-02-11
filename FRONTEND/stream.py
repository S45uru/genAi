import streamlit as st
from langchain_groq import ChatGroq

llm=ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)

st.title("Simple LLm Chatbot")
st.write("Enter your query below;")

user_input=st.text_input("Your question:","")  

if st.button("Get Answer"):
    response=llm.invoke(user_input)  
    st.write("### Response:")
    st.write(response)