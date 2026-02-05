import streamlit as st
import pandas as pd
import numpy as np

st.title("Таблица 10×5: случайные числа")

# Создаём DataFrame с 5 строками и 10 столбцами
data = pd.DataFrame(
    np.random.randn(5, 10),  # случайные числа из нормального распределения
    columns=[f"Столбец {i+1}" for i in range(10)],
    index=[f"Строка {i+1}" for i in range(5)]
)

st.dataframe(data, height=300)





# Исходные данные
data2 = {
    f"Поле_{i}": [f"Значение {i}-{j}" for j in range(1, 6)]
    for i in range(1, 11)
}
df = pd.DataFrame(data2)

# Редактор с возможностью изменения ячеек
edited_df = st.data_editor(df, num_rows="dynamic")

st.write("Изменённые данные:")
st.write(edited_df)
