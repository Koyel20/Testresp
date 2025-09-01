import streamlit as st
import pandas as pd
import numpy as np
import nltk

st.title("Streamlit Cloud with NLTK, NumPy, Pandas")

# NLTK example
nltk.download("punkt")
text = "Streamlit makes data apps easy!"
tokens = nltk.word_tokenize(text)
st.write("Tokenized text:", tokens)
