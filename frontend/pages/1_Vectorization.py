import os
import streamlit as st
from ingestion.vectorize import vectorize_pdf



st.title('Vectorization')


pdf_to_vectorize = st.selectbox('Select a pdf', options=os.listdir('data/pdf'))
pdf_path = f'data/pdf/{pdf_to_vectorize}'

name_of_vector = st.text_input("Vector_name")


if pdf_to_vectorize:
    if st.button('Vectorize'):
        vectorize_pdf(pdf_path, pdf_to_vectorize if not name_of_vector else name_of_vector)
        st.badge('Successfully vectorized')