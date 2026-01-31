import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_addons as tfa
import io
import os
from datetime import datetime
from model import ReflectionPadding2D  

st.set_page_config(page_title="Monet Style Transfer", page_icon="🎨", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎨 Photo → Monet Style Transfer</h1>", unsafe_allow_html=True)
st.markdown("---")

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
    st.page_link("Pages/page_1.py", label="🖼️ Photo → 🎨 Monet")
    st.page_link("Pages/page_2.py", label="🎨 Monet → 📸 Photo")
    st.page_link("Pages/page_3.py", label="🗂️ Gallery 📷🎨")

st.sidebar.markdown("## 📤 Upload Image")
uploaded_file = st.sidebar.file_uploader(label="", type=["png", "jpg", "jpeg"])

st.sidebar.markdown("**📁 File Requirements:**")
st.sidebar.markdown("""
- ✅ Format **PNG**, **JPG**, atau **JPEG**  
- 📐 Recommended size **256 x 256** or larger  
- 📦 Max size **50MB**
""")

default_original_path = "pages/1.jpg"
default_monet_path = "pages/2.jpg"

try:
    sample_original = Image.open(default_original_path)
except FileNotFoundError:
    sample_original = None

try:
    sample_monet = Image.open(default_monet_path)
except FileNotFoundError:
    sample_monet = None

@st.cache_resource
def load_generator_model():
    from tensorflow_addons.layers import InstanceNormalization
    custom_objects = {  
        "ReflectionPadding2D": ReflectionPadding2D,
        "InstanceNormalization": InstanceNormalization,
        "Addons>InstanceNormalization": InstanceNormalization
    }
    model = tf.keras.models.load_model("Model\Trained\monet_generator_model.h5", compile=False, custom_objects=custom_objects)
    return model

generator_model = load_generator_model()

def preprocess_image(image: Image.Image):
    image = image.resize((256, 256))
    image_array = np.array(image).astype(np.float32)
    image_array = (image_array / 127.5) - 1.0 
    return tf.expand_dims(image_array, axis=0)

def postprocess_image(image_tensor):
    image_array = image_tensor[0].numpy()
    image_array = (image_array + 1.0) * 127.5  
    image_array = np.clip(image_array, 0, 255).astype(np.uint8)
    return Image.fromarray(image_array)

def show_side_by_side(img1, caption1, img2, caption2):
    col_space_left, col1, col_gap, col2, col_space_right = st.columns([1, 5, 1, 5, 1])
    with col1:
        st.markdown(f"<div style='text-align:center;'><h5>{caption1}</h5></div>", unsafe_allow_html=True)
        st.image(img1, width=384)
    with col2:
        st.markdown(f"<div style='text-align:center;'><h5>{caption2}</h5></div>", unsafe_allow_html=True)
        st.image(img2, width=384)

if uploaded_file:
    user_image = Image.open(uploaded_file).convert("RGB")
    display_image = user_image.resize((384, 384))
    preprocessed = preprocess_image(user_image)

    with st.spinner("🎨 Generating Monet..."):
        output_tensor = generator_model(preprocessed, training=False)
        generated_image = postprocess_image(output_tensor)
        generated_image = generated_image.resize((384, 384))

    show_side_by_side(display_image, "📷 Original Photo", generated_image, "🎨 Generated Monet")

    st.sidebar.success("✅ Image Generated Successfully")

    os.makedirs("Output\Generated\monet", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = f"Output\Generated\monet\monet_{timestamp}.png"
    generated_image.save(save_path)

    buffer = io.BytesIO()
    generated_image.save(buffer, format="PNG")
    buffer.seek(0)

    st.sidebar.download_button(
        label="⬇️ Download Image",
        data=buffer,
        file_name="Monet_Style.png",
        mime="image/png"
    )

elif sample_original and sample_monet:
    sample_original = sample_original.resize((384, 384))
    sample_monet = sample_monet.resize((384, 384))
    show_side_by_side(sample_original, "📷 Original Sample", sample_monet, "🎨 Sample Monet-style")
else:
    st.info("📁 Silakan unggah gambar di sidebar untuk melihat hasil style transfer")
