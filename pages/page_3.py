import streamlit as st
import pandas as pd
import numpy as np

st.title("Цветная таблица 10×5")

# Данные
np.random.seed(42)
data = np.random.randint(1, 100, size=(5, 10))
df = pd.DataFrame(data, columns=[f"C{i}" for i in range(1, 11)])

# Стилизация: фон в зависимости от значения
def color_background(val):
    color = "green" if val > 50 else "red"
    return f"background-color: {color}; color: white; font-weight: bold"

styled_df = df.style.applymap(color_background)

st.dataframe(styled_df, height=300)
