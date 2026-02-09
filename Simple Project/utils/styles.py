import streamlit as st

def apply_custom_css():  # Fixed: Changed 'u' to 'o' to match main.py
    st.markdown("""
    <style>
    /* Main background and text */
    .main { 
        background-color: #0e1117; 
        color: #ffffff; 
    }
    
    /* Button styling */
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3em; 
        background-color: #262730; 
        color: white; 
        border: 1px solid #444444; /* Fixed: Valid hex code */
    }
    
    .stButton>button:hover { 
        border-color: #ff4b4b; 
        color: #ff4b4b; 
    }
    
    /* Calculator display area */
    .calc-display { 
        background-color: #1e1e1e; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #333; 
        margin-bottom: 20px; 
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #111b21;
    }
    </style>
    """, unsafe_allow_html=True)