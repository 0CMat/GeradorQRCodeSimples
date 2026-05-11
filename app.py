import streamlit as st
import qrcode
from PIL import Image
import io

st.title("Gerador de QR Code")

text = st.text_input("Digite o texto ou URL para gerar o QR Code:")

if st.button("Gerar QR Code"):
    if text:
        img = qrcode.make(text)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        st.image(buf)
        st.download_button(label="Baixar QR Code", data=buf, file_name="qrcode.png", mime="image/png")
        st.success("QR Code gerado com sucesso!")
    else:
        st.error("Por favor, insira um texto.")