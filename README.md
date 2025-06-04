# Image Style Transfer CycleGAN for Photo to Monet Transformation
Explores artistic style transfer using CycleGAN to convert photographs into Monet-style paintings. CycleGAN, a type of Generative Adversarial Network (GAN), was employed to learn the mapping between the two unpaired image domains: real-world photos and Monet paintings. The model was trained to generate visually convincing Monet-style renditions from input photographs. Evaluation metrics such as FID (Fréchet Inception Distance), SSIM (Structural Similarity Index), and PSNR (Peak Signal-to-Noise Ratio) were used to assess the quality and realism of generated images.

# Introduction
The transformation of photographs into artistic styles presents significant opportunities in the fields of art, design, and AI-driven creativity. This research aims to implement a CycleGAN model to transform photos into Monet-style artworks using the publicly available "Photo-to-Monet" dataset from the Kaggle or TensorFlow datasets. Two main components of the model are:
- Generators that map Photo → Monet and Monet → Photo
- Discriminators that distinguish between real and generated images in both domains

# Methodology
## Data Preparation
- **Dataset :** Approximately 7,338 images, equally divided between photos and Monet paintings.
- **Preprocessing :**
    - Resizing to 256x256 pixels
    - Normalizing pixel values to [-1, 1]
    - Augmentation: horizontal flips, random cropping for variability

## Model Architecture
### Generator
- Takes 256x256 RGB images as input
- Uses downsampling layers to extract low-level to high-level features
- Incorporates residual blocks (like ResNet) to preserve image content
- Uses upsampling layers with skip connections (similar to U-Net) to reconstruct the stylized image
- The output uses tanh activation to produce an image in the Monet style
  
### Discriminator
- Classifies image patches as real or fake, enabling localized feedback
- Uses convolutional layers with instance normalization and LeakyReLU
- Outputs a matrix (not a single value), aligning with the PatchGAN structure

### Loss Functions
- Adversarial Loss: Encourages generators to produce realistic images
- Cycle Consistency Loss: Ensures that translating an image to the other domain and back returns the original image
- Identity Loss: Ensures color and structure consistency when input is already in the target domain
- Combines L1 and L2 losses for more balanced optimization


# Technologies and Tools
- Language : Python
- Libraries : TensorFlow, Keras, NumPy, OpenCV
- Visualization : Matplotlib, PIL
- Platform : Jupyter Notebook

# Conclusion
CycleGAN effectively translated real-world photographs into Monet-style paintings without needing paired data. The model preserved structural content while successfully applying artistic textures. Although the results were visually compelling, further improvements are needed in texture clarity and structural fidelity.

# Recommendations
- Incorporate attention mechanisms to improve texture transfer.
- Train on higher-resolution images for more detailed outputs.
- Fine-tune using perceptual loss or CLIP-based metrics.
- Explore multi-style models for broader artistic transfer (e.g., Monet, Van Gogh, Cezanne).
