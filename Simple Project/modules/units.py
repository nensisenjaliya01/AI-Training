import streamlit as st

def show_units():
    st.title("⚖️ Universal Unit Converter")
    
    category = st.selectbox("Category", ["Length", "Mass", "Digital Storage", "Temperature"])
    
    units = {
        "Length": {"Meters": 1, "KM": 1000, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254},
        "Mass": {"KG": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495},
        "Digital Storage": {"Bit": 1, "Byte": 8, "KB": 8000, "MB": 8e+6, "GB": 8e+9}
    }

    if category == "Temperature":
        val = st.number_input("Value", value=0.0)
        from_u = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_u = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
        if from_u == to_u: res = val
        elif from_u == "Celsius":
            res = (val * 9/5) + 32 if to_u == "Fahrenheit" else val + 273.15
        elif from_u == "Fahrenheit":
            res = (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
        else: # Kelvin
            res = val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32
        st.success(f"Result: {res:.4f} {to_u}")
    else:
        cat_units = units[category]
        val = st.number_input("Value", value=1.0)
        from_u = st.selectbox("From", list(cat_units.keys()))
        to_u = st.selectbox("To", list(cat_units.keys()))
        res = val * (cat_units[from_u] / cat_units[to_u])
        st.success(f"Result: {res:.4f} {to_u}")