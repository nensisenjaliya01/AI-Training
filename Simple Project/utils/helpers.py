import streamlit as st
from datetime import datetime

def add_to_history(operation, result):
    timestamp = datetime.now().strftime("%H:%M:%S")
    # Adds newest item to the top of the list
    st.session_state.history.insert(0, f"[{timestamp}] {operation} = {result}")

def clear_history():
    st.session_state.history = []