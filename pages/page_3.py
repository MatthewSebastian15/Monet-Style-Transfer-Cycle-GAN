import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="🗂️ Gallery 📷🎨", layout="wide")

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

st.title("🗂️ Gallery 📷🎨")

monet_dir = "generated/monet"
photo_dir = "generated/photo"

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            images.append(os.path.join(folder, filename))
    return images

monet_images = load_images_from_folder(monet_dir)
photo_images = load_images_from_folder(photo_dir)

st.subheader("🎨 Generated Monet")
cols = st.columns(4)
for idx, img_path in enumerate(monet_images):
    with cols[idx % 4]:
        st.image(Image.open(img_path), use_container_width=True)

st.subheader("📷 Generated Photos")
cols = st.columns(4)
for idx, img_path in enumerate(photo_images):
    with cols[idx % 4]:
        st.image(Image.open(img_path), use_container_width=True)