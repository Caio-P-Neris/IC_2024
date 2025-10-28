import streamlit as st
import base64
import os
import streamlit.components.v1 as components

st.title("Relatórios")

def embed_pdf(source, height=600):
    if os.path.isfile(source):
        # Se for arquivo local, converte para base64
        with open(source, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        src = f"data:application/pdf;base64,{base64_pdf}"
    elif "drive.google.com" in source:
        # Converte link do Google Drive para formato de preview
        try:
            file_id = source.split("/d/")[1].split("/")[0]
            src = f"https://drive.google.com/file/d/{file_id}/preview"
        except Exception:
            st.error("⚠️ Link do Google Drive inválido.")
            return
    else:
        src = source

    # Usando o componente nativo, que é compatível com celular
    components.iframe(src, width=1000, height=height, scrolling=True)

# PDF 1
st.subheader("📘 Relatório final")
embed_pdf("https://drive.google.com/file/d/18R60nRSwcoinc0KLscJxr1VWhshqARWI/view?usp=sharing")

# PDF 2
st.subheader("📗 Desenvolvimento teórico estendido")
embed_pdf("https://drive.google.com/file/d/1J1DjHhEWkGbyC6XAhRK3NSLQbZGhWy6q/view")
