import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Home - Monet Style Transfer App",
    page_icon="🏠",
    layout="centered"
)

st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🎨 Menu Navigasi")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/page_1.py", label="🖼️ Photo ➜ 🎨 Monet")
    st.page_link("pages/page_2.py", label="🎨 Monet ➜ 📸 Photo")
    st.page_link("pages/page_3.py", label="🗂️ Gallery 📷🎨")

st.markdown("<h1 style='text-align: center;'>🏠 Selamat Datang di Aplikasi Monet Style Transfer</h1>", unsafe_allow_html=True)
st.markdown("## 🎨 Ubah foto Anda menjadi lukisan bergaya Monet dengan teknologi AI.")
st.markdown("---")