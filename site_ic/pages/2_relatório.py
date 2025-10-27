import streamlit as st
import base64
import os

st.title("Relatórios")

def embed_pdf(source, height=600):
    if os.path.isfile(source):
        # Se for arquivo local, converte para base64
        with open(source, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        src = f"data:application/pdf;base64,{base64_pdf}"
    elif "drive.google.com" in source:
        # Se for link do Drive, converte para formato de preview
        file_id = source.split("/d/")[1].split("/")[0]
        src = f"https://drive.google.com/file/d/{file_id}/preview"
    else:
        # Qualquer outro link direto
        src = source

    st.markdown(f'<iframe src="{src}" width="100%" height="{height}"></iframe>', unsafe_allow_html=True)

# PDF 1
st.subheader("📘 Relatório final")
embed_pdf("https://drive.google.com/file/d/18R60nRSwcoinc0KLscJxr1VWhshqARWI/view?usp=sharing")
#st.markdown('[Abrir no Google Drive](https://drive.google.com/drive/folders/1AUSkFfK8_nT4xZ2vNhzCK8B0zdatR_Hp?hl=pt-br)')

# PDF 2
st.subheader("📗 Desenvolvimento teórico estendido")
embed_pdf("https://drive.google.com/file/d/1J1DjHhEWkGbyC6XAhRK3NSLQbZGhWy6q/view")
#st.markdown('[Abrir no Google Drive](https://drive.google.com/file/d/1J1DjHhEWkGbyC6XAhRK3NSLQbZGhWy6q/view)')
