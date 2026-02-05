import streamlit as st

st.title("Первая страница!")
st.write("Здесь будет контент вашей первой страницы.")

# Пример добавления графика
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["A", "B", "C"]
)
st.line_chart(data)
