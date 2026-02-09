from streamlit import st 
from numpy import np 
from utils.helpers import add_to_history

def show_math():
    st.title("🔢 Basic & Advanced Math")
    col1, col2 = st.columns([2, 1])
    with col1:
        exp_input = st.text_input("Enter expression", help="Use standard Python math syntax")
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("π"): exp_input += "np.pi"
        if c2.button("e"): exp_input += "np.e"
        
        if st.button("Calculate"):
            try:
                allowed = {"np": np, "sin": np.sin, "cos": np.cos, "sqrt": np.sqrt, "pi": np.pi}
                result = eval(exp_input, {"__builtins__": None}, allowed)
                st.success(f"Result: {result}")
                add_to_history(exp_input, result)
            except Exception as e:
                st.error(f"Error: {e}")
