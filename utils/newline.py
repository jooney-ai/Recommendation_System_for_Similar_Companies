import streamlit as st


def enter(height, sidebar=False) -> None:
    for _ in range(height):
        if sidebar:
            st.sidebar.write('\n')
        else:
            st.write('\n')

