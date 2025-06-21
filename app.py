import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🎨 Navigation Menu")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/page_1.py", label="🖼️ Photo → 🎨 Monet")
    st.page_link("pages/page_2.py", label="🎨 Monet → 📸 Photo")
    st.page_link("pages/page_3.py", label="🗂️ Gallery 📷🎨")

st.markdown("<h1 style='text-align: center; margin-top: -10px;'>🎨 Apps Monet Style Transfer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Transforming Photos into Monet-style Paintings Using Deep Learning Technology</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h4 style='text-align: center;'>🔄 Example of Transformation Results</h4>", unsafe_allow_html=True)

arrow_html = """
<div style='display: flex; align-items: center; justify-content: center; height: 100%; min-height: 200px;'>
    <span style='font-size: 30px;'>→</span>
</div>
"""

cols = st.columns([1, 0.15, 1, 0.15, 1])

with cols[0]:
    if os.path.exists("original.jpg"):
        st.image("original.jpg", caption="📷 Original", use_container_width=True)

with cols[1]:
    st.markdown(arrow_html, unsafe_allow_html=True)

with cols[2]:
    if os.path.exists("monet_gen.png"):
        st.image("monet_gen.png", caption="🎨 Monet Style", use_container_width=True)

with cols[3]:
    st.markdown(arrow_html, unsafe_allow_html=True)

with cols[4]:
    if os.path.exists("photo_gen.png"):
        st.image("photo_gen.png", caption="📸 Reconstructed Photo", use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>✨ Transformation from photo to Monet painting and back again ✨</p>", unsafe_allow_html=True)
