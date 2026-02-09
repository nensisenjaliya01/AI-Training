import streamlit as st
import numpy as np
import plotly.express as px

def show_stats():
    st.title("📊 Statistical Analysis")
    data_input = st.text_area("Enter data (comma separated)", value="10, 20, 20, 35, 50, 80")
    
    if st.button("Analyze"):
        try:
            data = np.fromstring(data_input, sep=',')
            c1, c2, c3 = st.columns(3)
            c1.metric("Mean", f"{np.mean(data):.2f}")
            c2.metric("Median", f"{np.median(data):.2f}")
            c3.metric("Std Dev", f"{np.std(data):.2f}")
            
            fig = px.histogram(data, title="Data Distribution", template="plotly_dark")
            st.plotly_chart(fig)
        except Exception as e:
            st.error("Please check your data format.")