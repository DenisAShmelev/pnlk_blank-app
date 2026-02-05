import streamlit as st
import pandas as pd
import numpy as np

# 1. Настройка макета
st.set_page_config(
    page_title="Широкая таблица",
    layout="wide"
)

# 2. Дополнительный CSS (опционально)
st.markdown(
    """
    <style>
    .block-container {padding-left: 2rem; padding-right: 2rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Контент
st.title("Таблица на всю ширину экрана")

data = pd.DataFrame(
    np.random.randn(5, 10),
    columns=[f"Столбец {i}" for i in range(1, 11)]
)

st.dataframe(data, use_container_width=True)  # Важно!
