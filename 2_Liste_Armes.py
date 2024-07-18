import streamlit as st
import pandas as pd
from shared_functions import *

armes = get_armes()

data = {
    "Arme": list(armes.keys()),
    "Lien Image": list(armes.values())
}

df = pd.DataFrame(data)

def image_formatter(url):
    return f'<img src="{url}" width=100 />'

df["Image"] = df["Lien Image"].apply(image_formatter)

df = df[["Arme", "Image"]]

st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
