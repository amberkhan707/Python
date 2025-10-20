import streamlit as st
import pandas as pd
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

feature = pd.DataFrame(iris.data, columns = iris.feature_names)
target = pd.DataFrame(iris.target, columns = ['species'])

model = RandomForestClassifier()
model.fit(feature.values,target.values.ravel())

# Ab streamlit se app tyyar krte h 
st.title("Flower Species Prediction")

def prediction(new_f):
    return model.predict(new_f)

st.sidebar.header("Select the features value")
sepal_length = st.sidebar.slider("sepal length", float(feature['sepal length (cm)'].min()), float(feature['sepal length (cm)'].max()), float(feature['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("sepal width", float(feature['sepal width (cm)'].min()), float(feature['sepal width (cm)'].max()), float(feature['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("petal length", float(feature['petal length (cm)'].min()), float(feature['petal length (cm)'].max()), float(feature['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("petal width", float(feature['petal width (cm)'].min()), float(feature['petal width (cm)'].max()), float(feature['petal width (cm)'].mean()))

new_f = np.array([[sepal_length,sepal_width,petal_length,petal_width]])

predic = prediction(new_f)
Predicted_flower = iris.target_names[predic[0]]

st.header("Flower prediction from the sidebar data selected by user:")

st.text(f"Flower with this feature is\n {Predicted_flower}")
