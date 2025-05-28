import os
import streamlit as st
from chat_models.chat_models import prepare_chat_model, chat_with_pdf


st.title('Chat with PDF')

pdf_vector = st.selectbox('Select the PDF vector', os.listdir('Local_vectors'))
path = f'Local_vectors/{pdf_vector}'
rag_llm = prepare_chat_model(path)

st.badge(f'Successfully loaded {path}')

query = st.chat_input("Enter your questions here")

if query:
    answer = chat_with_pdf(rag_llm, query)
    st.chat_message('user').write(query)
    st.chat_message('ai').write(answer)