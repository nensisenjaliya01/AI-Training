import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def show_graphing():
    st.title("📈 Advanced Graphing")
    mode = st.radio("Plot Type", ["2D Function", "3D Surface"])
    
    if mode == "2D Function":
        expr = st.text_input("Function (e.g., np.sin(x))", value="np.sin(x)")
        x = np.linspace(-10, 10, 500)
        try:
            y = eval(expr)
            fig = px.line(x=x, y=y, title=f"Plot of {expr}")
            fig.update_layout(template="plotly_dark")
            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("3D Visualization Active")
        x = y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig)