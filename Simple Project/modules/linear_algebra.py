import streamlit as st
import numpy as np
from utils.helpers import add_to_history

def show_linear_algebra():
    st.title("🧬 Linear Algebra Suite")
    operation = st.selectbox("Select Operation", ["Matrix Arithmetic", "Determinant & Inverse"])

    if operation == "Matrix Arithmetic":
        cols = st.columns(2)
        with cols[0]:
            rows_a = st.number_input("Rows A", 1, 5, 2)
            cols_a = st.number_input("Cols A", 1, 5, 2)
            matrix_a = np.array([st.number_input(f"A[{i},{j}]", value=0.0) 
                               for i in range(rows_a) for j in range(cols_a)]).reshape(rows_a, cols_a)
        with cols[1]:
            rows_b = st.number_input("Rows B", 1, 5, 2)
            cols_b = st.number_input("Cols B", 1, 5, 2)
            matrix_b = np.array([st.number_input(f"B[{i},{j}]", value=0.0) 
                               for i in range(rows_b) for j in range(cols_b)]).reshape(rows_b, cols_b)
        
        if st.button("Multiply Matrices"):
            try:
                res = np.dot(matrix_a, matrix_b)
                st.write("Result:")
                st.dataframe(res)
                add_to_history("Matrix Multiplication", "Success")
            except Exception as e:
                st.error(f"Error: {e}")