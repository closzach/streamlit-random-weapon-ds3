import streamlit as st
from shared_functions import *

nb_participants = st.number_input("Nombre de participants", step=1, min_value=1)

gen_arme = st.button("Jeter les dés")

if gen_arme:
    for i in range(nb_participants):
        col1, col2 = st.columns(2)
        arme, lien_img = get_arme_random(get_armes())
        col1.write(arme)
        col2.markdown(f"<img src=\"{lien_img}\">", unsafe_allow_html=True)
