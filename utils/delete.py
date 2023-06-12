import streamlit as st


# 워터마크 삭제

def watermark():
    st.markdown('''
    <style>
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }    
    </style>
    ''', unsafe_allow_html=True)    