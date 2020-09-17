import numpy as np
import pandas as pd
import streamlit as st
import pickle

f = open("df.pkl", "rb")
df = pickle.load(f)
f.close()

st.title("CEREAL WORLD")
st.write("Find Your Dream Cereal")
sugar = st.slider("Max Sugar", -1, 15)
cals = st.slider("Max Calories", 50, 160)
sodium = st.slider("Max Sodium", 0, 320)
protein = st.slider("Min Protein", 1, 6)
fiber = st.slider("Min Fiber", 0, 14)
potass = st.slider("Min Potassium", -1, 330)

cereals = df.loc[(df["sugars"] <= sugar) & (df["calories"] <= cals) & (df["sodium"] <= sodium) &
                 (df["protein"] >= protein) & (df["fiber"] >= fiber) & df["potass"] >= potass]
cereal_names = cereals["name"]
your_cereal = np.random.choice(cereal_names)

generate = st.button("Find My Dream Cereal")
if generate:
    st.write(your_cereal)
    image = your_cereal + ".jpg"
    st.image(image)
