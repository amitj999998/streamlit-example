import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import chromadb

cc = chromadb.Client()

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
