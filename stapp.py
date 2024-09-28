import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Plot a Simple Graph")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)