import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="ReLU Activation Function",
    layout="wide",
)

st.title("ReLU Activation Function")
st.write(
    """
    This web app visualises the **Rectified Linear Unit (ReLU)** activation function.
    
    **Formula:**
    f(x) = max(0, x)
    """
)

st.sidebar.header("Settings")
x_min = st.sidebar.slider("Minimum x value", -10.0, 0.0, -5.0)
x_max = st.sidebar.slider("Maximum x value", 0.0, 10.0, 5.0)
num_points = st.sidebar.slider("Number of points", 100, 1000, 500, step=100)

x = np.linspace(x_min, x_max, num_points)
y = np.maximum(0, x)

st.subheader("ReLU Function Plot")

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("ReLU(x)")
ax.set_title("ReLU Activation Function")
ax.grid(True)

st.pyplot(fig)
