import streamlit as st

def show_finance():
    st.title("💰 Financial Math")
    mode = st.selectbox("Type", ["Compound Interest", "Loan Amortization"])
    
    if mode == "Compound Interest":
        p = st.number_input("Principal ($)", value=1000.0)
        r = st.number_input("Annual Rate (%)", value=5.0) / 100
        t = st.number_input("Time (Years)", value=10)
        n = st.number_input("Compounds per Year", value=12)
        amount = p * (1 + r/n)**(n*t)
        st.metric("Future Value", f"${amount:,.2f}")
    
    elif mode == "Loan Amortization":
        loan = st.number_input("Loan Amount", value=250000.0)
        rate = st.number_input("Interest Rate (%)", value=3.5) / 100 / 12
        months = st.number_input("Term (Months)", value=360)
        monthly = (loan * rate) / (1 - (1 + rate)**-months)
        st.metric("Monthly Payment", f"${monthly:,.2f}")