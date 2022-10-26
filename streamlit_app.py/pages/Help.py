# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 01:12:44 2022

@author: Neil
"""

import streamlit as st

def main():
    st.title("Help Page")


    st.header(':mailbox: Get in touch with us!')

    contact_form = """

    <form action="https://formsubmit.co/ftdsjune@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required> 
         <textarea name="message" placeholder="Details of your problem"></textarea>
         <button type="submit">Send</button>
    </form>

    """
    
    st.markdown(contact_form, unsafe_allow_html = True)
    
    st.text_area("Please let us know about any errors or other feedback.")
    

    if st.button("Submit"):
        st.success("Feedback/Error Submitted")
        
        
        
if __name__ == '__main__':
    main()