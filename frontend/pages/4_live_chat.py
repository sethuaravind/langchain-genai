import streamlit as st
from chat_models.live_chat import live_chat

st.title('Live Chat')

query = st.chat_input("Enter your questions here")

if query:
    answer = live_chat(query)
    st.chat_message('user').write(query)
    st.chat_message('ai').write(answer)