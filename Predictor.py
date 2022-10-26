# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:24:56 2022

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
            
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    st.header("The Need for Spam Detection")
    st.text("""
        Spam detection algorithms are used to detect and filter junk and spam emails with a high level of accuracy.
        It is said that around half of all emails are spam, depending on the user. 
        These emails can include scams or viruses intended to cause harm.
        """)

    st.header("Data Source")
    st.text("""
        Data Source: Preprocessed TREC 2007 Public Corpus Dataset. 
        Link: https://www.kaggle.com/datasets/imdeepmind/preprocessed-trec-2007-public-corpus-dataset
        
        """)
    
    st.header("Any Feedback? Let us know.")
    contact_form = """

    <form action="https://formsubmit.co/ftdsjune@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required> 
         <input type="text" name="message"  placeholder="Input your feedback" required> 
         <button type="submit">Send</button>
    </form>

    """
    
    st.markdown(contact_form, unsafe_allow_html = True)

if __name__ == "__main__":
    main()
     
