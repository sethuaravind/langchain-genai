import os
import streamlit as st
from chat_models.chat_models import chat_with_csv


st.title('Chat with csv')

csv_file = st.selectbox('Select a csv', os.listdir('data/csv'))
csv_path = f'data/csv/{csv_file}'
question = st.chat_input('Input your question here')


if question:
    csv_agent = chat_with_csv(csv_path)
    res = csv_agent.invoke({'input': question})
    
    st.chat_message('user').write(question)
    st.chat_message('ai').write(res['output'])
