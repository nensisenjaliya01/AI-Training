import streamlit as st

def show_constants():
    st.title("⚛️ Scientific Constants")
    constants = {
        "Speed of Light (c)": "299,792,458 m/s",
        "Gravitational Constant (G)": "6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²",
        "Planck's Constant (h)": "6.62607015 × 10⁻³⁴ J·s",
        "Avogadro's Number (Nₐ)": "6.02214076 × 10²³ mol⁻¹",
        "Boltzmann Constant (k)": "1.380649 × 10⁻²³ J/K"
    }
    
    search = st.text_input("Search Constant", placeholder="e.g. Light")
    for name, val in constants.items():
        if search.lower() in name.lower():
            st.info(f"**{name}:** `{val}`")