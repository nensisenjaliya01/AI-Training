import sys
import os
import streamlit as st

# ==========================================
# 1. PATH FIX (Must be at the very top)
# ==========================================
# This ensures Python sees the 'utils' and 'modules' folders
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# ==========================================
# 2. MODULAR IMPORTS
# ==========================================
try:
    from utils.styles import apply_custom_css
    from utils.helpers import clear_history
    from modules import (
        math_logic, calculus, linear_algebra, 
        units, graphing, constants, finance, stats
    )
except ImportError as e:
    st.error(f"❌ Critical Import Error: {e}")
    st.info("Ensure your function names (like apply_custom_css) match exactly in their files.")
    st.stop()

# ==========================================
# 3. CONFIGURATION & SESSION STATE
# ==========================================
st.set_page_config(page_title="NensiCalc Pro", layout="wide", page_icon="🧮")

# Apply the custom styles from utils/styles.py
apply_custom_css()

if 'history' not in st.session_state:
    st.session_state.history = []

# ==========================================
# 4. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("🚀 NensiCalc Pro")
st.sidebar.subheader("Advanced Scientific Suite")

menu = st.sidebar.radio("Select Module", [
    "Basic & Advanced Math",
    "Calculus Engine",
    "Linear Algebra",
    "Unit Converter",
    "Graphing Suite",
    "Physics/Chemistry Constants",
    "Financial Math",
    "Statistical Analysis"
])

st.sidebar.markdown("---")
if st.sidebar.button("Clear History"):
    clear_history()

st.sidebar.write("### 📜 History")
# Display the last 10 operations
for item in st.session_state.history[:10]:
    st.sidebar.caption(item)

# ==========================================
# 5. MODULE ROUTING
# ==========================================
if menu == "Basic & Advanced Math":
    math_logic.show_math()

elif menu == "Calculus Engine":
    calculus.show_calculus()

elif menu == "Linear Algebra":
    linear_algebra.show_linear_algebra()

elif menu == "Unit Converter":
    units.show_units()

elif menu == "Graphing Suite":
    graphing.show_graphing()

elif menu == "Physics/Chemistry Constants":
    constants.show_constants()

elif menu == "Financial Math":
    finance.show_finance()

elif menu == "Statistical Analysis":
    stats.show_stats()

# ==========================================
# 6. FOOTER
# ==========================================
st.sidebar.markdown("---")
st.sidebar.caption("NensiCalc Pro v2.1 | Powered by Streamlit")