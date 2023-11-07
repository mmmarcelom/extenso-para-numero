import streamlit as st

from functions import *

st.title('Converta um número em extenso')
texto = st.text_input(label='Digite o texto a ser convertido', key='entrada')

st.text_area('Seu número convertido', value=converter(texto))