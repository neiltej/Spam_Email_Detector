import streamlit as st

st.set_page_config(
page_title="Spam Email Detector"
)
   
st.title("Spam Email Detector")
    
st.sidebar.success("Select a page above.")

st.header("The Need for Spam Detection")
st.text("""
        Spam detection algorithms are used to detect and filter junk and spam emails with a high level of accuracy.
        It is said that around half of all emails are spam, depending on the user. These emails can include scams or viruses intended to cause harm.
        """)

st.header("Data Source")
st.text("""
        Data Source: Preprocessed TREC 2007 Public Corpus Dataset. 
        Link: https://www.kaggle.com/datasets/imdeepmind/preprocessed-trec-2007-public-corpus-dataset
        
        """)