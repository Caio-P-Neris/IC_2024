import streamlit as st
import streamlit.components.v1 as components

st.title(" Visualização do código")

notebook_url = "https://github.com/Caio-P-Neris/IC_2024/blob/main/main.ipynb"
nbviewer_url = f"https://nbviewer.org/url/{notebook_url.replace('https://', '')}"

# st.markdown(f"""
# <iframe src="{nbviewer_url}" width="100%" height="800"></iframe>
# """, unsafe_allow_html=True)
components.iframe(nbviewer_url, width=1000, height=800, scrolling=True)

#st.write("Disponível no  <a href="https://github.com/Caio-P-Neris/IC_2024" target="_blank"> GitHub </a> ")
