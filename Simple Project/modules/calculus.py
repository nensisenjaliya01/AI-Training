import streamlit as st
import sympy as sp
from utils.helpers import add_to_history

def show_calculus():
    st.title("∫ Calculus Engine")
    calc_type = st.selectbox("Operation", ["Derivatives", "Integrals", "Limits"])
    expr_str = st.text_input("Enter Function f(x)", value="x**2 + sin(x)")
    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)
        if calc_type == "Derivatives":
            result = sp.diff(expr, x)
            st.latex(rf"\frac{{d}}{{dx}}({sp.latex(expr)}) = {sp.latex(result)}")
        elif calc_type == "Integrals":
            result = sp.integrate(expr, x)
            st.latex(rf"\int {sp.latex(expr)} dx = {sp.latex(result)} + C")
        
        if st.button("Log Result"):
            add_to_history(f"{calc_type}: {expr_str}", "Symbolic Result")
    except Exception as e:
        st.error(f"Error: {e}")