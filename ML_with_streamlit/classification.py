import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache correct function
@st.cache_data
def get_iris():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = get_iris()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")

sepal_length = st.sidebar.slider(
    "Sepal length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.sidebar.slider(
    "Sepal width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.sidebar.slider(
    "Petal length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.sidebar.slider(
    "Petal width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# Prepare input
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.subheader("Prediction")
st.write(f"Predicted Species: **{predicted_species}**")
