import streamlit as st
from PIL import Image
import io

# --- Config ---
st.set_page_config(page_title="Monet Style Transfer", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🎨 Monet Style Transfer</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Sidebar Upload ---
st.sidebar.header("📥 Upload Image")
uploaded_file = st.sidebar.file_uploader(" ", type=["png", "jpg", "jpeg"])
st.sidebar.markdown("Limit : 200MB • PNG, JPG, JPEG")

# --- Sidebar Guidelines ---
with st.sidebar.expander("📘 Image Guidelines"):
    st.write("- Use clear, high-resolution images.")
    st.write("- Faces or landscapes work best")
    st.write("- Max size: 200MB")

# --- Load Default Sample ---
default_original_path = "0d6f893bc7.jpg"
default_monet_path = "monet_0051.jpg"

try:
    sample_original = Image.open(default_original_path)
    sample_original.thumbnail((200, 200))
except FileNotFoundError:
    sample_original = None

try:
    sample_monet = Image.open(default_monet_path)
    sample_monet.thumbnail((200, 200))
except FileNotFoundError:
    sample_monet = None

# --- Display Section ---
col1, col2 = st.columns(2)

if uploaded_file:
    # If user uploads a file, show that image instead of the sample
    user_image = Image.open(uploaded_file)

    # Resize user image for display
    user_display = user_image.copy()
    user_display.thumbnail((200, 200))

    # Placeholder for generated image (you should replace with real model output)
    generated_display = user_image.copy()
    generated_display.thumbnail((200, 200))

    with col1:
        st.markdown("<h5 style='text-align:center;'>📷 Original Photo</h5>", unsafe_allow_html=True)
        st.image(user_display, use_column_width=True)

    with col2:
        st.markdown("<h5 style='text-align:center;'>🎨 Monet Style Photo</h5>", unsafe_allow_html=True)
        st.image(generated_display, use_column_width=True)

    st.sidebar.success("Styled image generated!")
    st.sidebar.download_button(
        label="Download styled image",
        data=io.BytesIO(),  # Replace with actual image bytes
        file_name="monet_style.png",
        mime="image/png",
        disabled=True  # Set to False when ready
    )

else:
    with col1:
        st.markdown("<h5 style='text-align:center;'>📷 Contoh Gambar</h5>", unsafe_allow_html=True)
        if sample_original:
            st.image(sample_original, caption="Original Sample", use_column_width=True)
        else:
            st.warning("Contoh gambar tidak ditemukan")

    with col2:
        st.markdown("<h5 style='text-align:center;'>🎨 Hasil Monet</h5>", unsafe_allow_html=True)
        if sample_monet:
            st.image(sample_monet, caption="Monet-style Sample", use_column_width=True)
        else:
            st.warning("Contoh Monet-style tidak ditemukan")
