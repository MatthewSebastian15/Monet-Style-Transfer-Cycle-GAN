# Image Style Transfer CycleGAN for Photo to Monet Transformation
Explores artistic style transfer using CycleGAN to convert photographs into Monet-style paintings. CycleGAN, a type of Generative Adversarial Network (GAN), was employed to learn the mapping between the two unpaired image domains: real-world photos and Monet paintings. The model was trained to generate visually convincing Monet-style renditions from input photographs. The quality and realism of the generated images were evaluated using the Structural Similarity Index (SSIM), which measures the perceived similarity between the original and stylized images based on structural information.

# Introduction
Artistic style transfer has garnered significant interest in both creative industries and AI research. This project implements a CycleGAN model to convert photos into Monet-style paintings using an unpaired dataset of photos and Monet artworks. Two generator–discriminator pairs were trained to perform transformations in both directions: Photo → Monet and Monet → Photo.

# Methodology
## Data Preparation
- **Dataset :** Approximately 7,338 images, equally divided between photos and Monet paintings.
- **Preprocessing :**
    - Resizing to 256x256 pixels
    - Normalizing pixel values to [-1, 1]
    - Augmentation: horizontal flips, random cropping for variability

## Model Architecture
### Generator (Photo → Monet / Monet → Photo)
- Input: 256x256x3 RGB image
- Architecture:
    - Downsampling with Conv2D + InstanceNormalization
    - Residual blocks (ResNet-like)
    - Upsampling with transposed convolutions and skip connections
- Output activation **tanh**
 
### Discriminator (PatchGAN)
- Classifies overlapping patches as real or fake
- Convolutional architecture with:
    - LeakyReLU activations
    - InstanceNormalization
    - Patch output (not scalar)

### Loss Functions
- Adversarial Loss: Distinguishes real from fake samples
- Cycle Consistency Loss: Enforces Photo → Monet → Photo ≈ original Photo
- Identity Loss: Encourages content and color preservation
- Combined using weighted sum of L1 and L2 losses

# Training and Evaluation
- **Platform** : Training was conducted using Jupyter Notebook.
- **Epochs** : 65 epochs
- **Batch Size** : 1
- **Optimizer** : Adam with Cosine Decay Restarts as learning rate schedule
- **Evaluation Metric** : Structural Similarity Index (SSIM)

# Technologies and Tools
- **Language** : Python
- **Framework** : TensorFlow, Keras
- **Libraries** : TensorFlow Addons (InstanceNormalization), NumPy, OpenCV, Matplotlib, PIL, Scikit-Image
- **Environment** : Jupyter Notebook

# Conclusion
CycleGAN effectively translated real-world photographs into Monet-style paintings without needing paired data. The model preserved structural content while successfully applying artistic textures. Although the results were visually compelling, further improvements are needed in texture clarity and structural fidelity.

# Recommendations
- Integrate self-attention or attention-gated modules to enhance texture detail
- Train on higher-resolution images (e.g., 512×512 or larger)
- Support variable input and output resolutions using a fully convolutional architecture.
- Experiment with perceptual loss (e.g., using VGG features) or CLIP-based losses for style semantics
- Explore multi-style models for broader artistic transfer (e.g., Monet, Van Gogh, Cezanne).
