# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:24:56 2022

@author: Neil
"""

import streamlit as st
import numpy as np
import pickle

import tensorflow
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


def predict(ham_spam):
    model = load_model('/Users/neiltejnani/Downloads/test_whole_HSmodel.h5')
    with open('/Users/neiltejnani/Downloads/tokenizer.pickle','rb') as handle:
        tokenizer = pickle.load(handle)
        tokenizer.fit_on_texts(ham_spam)
        x_1 = tokenizer.texts_to_sequences([ham_spam])
        x_1 = pad_sequences(x_1, maxlen=525)
        predictions = model.predict(x_1)[0][0]
        return predictions


def main():
    #giving a title to our page
    st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
    st.title("Ham Spam Email Prediction Web App :e-mail:")
    contents = st.text_area('Enter email contents:')

    prediction = ''

    #Create a prediction button
    if st.button("Analyze Spam Detection Result"):
        prediction = predict(contents)

        if prediction < 0.5:
            st.success('The email is not spam')
        elif prediction > 0.5:
            st.success('The email is spam')
            


if __name__ == "__main__":
    main()
     