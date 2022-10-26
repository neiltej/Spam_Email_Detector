# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:24:11 2022

@author: Neil
"""

import streamlit as st
import pickle

from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


def predict(ham_spam):
    model = load_model(r'test_HSmodel_r.h5')
    with open('tokenizer.pickle','rb') as handle:
        tokenizer = pickle.load(handle)
        tokenizer.fit_on_texts(ham_spam)
        x_1 = tokenizer.texts_to_sequences([ham_spam])
        x_1 = pad_sequences(x_1, maxlen=525)
        predictions = model.predict(x_1)[0][0]
        return predictions

def main():
    #giving a title to our page
    st.title("Email Spam Detection Web Application :e-mail:")
    contents = st.text_area('Please enter email contents:')

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
     
