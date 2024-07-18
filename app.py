import streamlit as st

choisir_arme = st.Page("./1_Choisir_Arme.py", title="Tirer arme(s)", icon=":material/casino:")
liste_arme = st.Page("./2_Liste_Armes.py", title="Lister armes", icon=":material/format_list_bulleted:")

pg = st.navigation([choisir_arme, liste_arme])
pg.run()

