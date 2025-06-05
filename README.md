# Image Style Transfer CycleGAN for Photo to Monet Transformation
Explores artistic style transfer using CycleGAN to convert photographs into Monet-style paintings. CycleGAN, a type of Generative Adversarial Network (GAN), was employed to learn the mapping between the two unpaired image domains: real-world photos and Monet paintings. The model was trained to generate visually convincing Monet-style renditions from input photographs. The quality and realism of the generated images were evaluated using the Structural Similarity Index (SSIM), which measures the perceived similarity between the original and stylized images based on structural information.

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

# Training and Evaluation
- Platform : Training was conducted using Jupyter Notebook.
- Training Duration : 50 epochs
- Batch Size : 8
- Optimizer : Adam with learning rate decay schedule
- Evaluation Metric : Structural Similarity Index (SSIM)

## The CycleGAN model was trained using a custom training loop that included:
- Generator and Discriminator Architectures : Custom-built using TensorFlow and TensorFlow Addons (InstanceNormalization), with 8 downsampling layers, residual blocks, and 7 upsampling layers for the generators.
- Loss Functions : Generator and discriminator losses were calculated using binary cross-entropy. Additional components such as cycle consistency loss (a combination of L1 and L2 loss) and identity loss were incorporated to stabilize training and preserve content.
- Gradient Updates : Training was distributed using tf.distribute.MirroredStrategy to leverage multiple GPUs, with manual gradient computation and application.
- Preprocessing : Input images (256×256×3) were normalized to [-1, 1] and loaded into TensorFlow Datasets with caching, shuffling, batching, and prefetching.
- Loss Tracking : Average generator and discriminator losses for both Monet and Photo domains were recorded per epoch for post-training analysis.

The final model outputs were evaluated visually and quantitatively using SSIM, indicating the structural similarity between generated and real images. This metric was chosen for its sensitivity to changes in image structure, which aligns with the goal of stylistic transfer while preserving content.

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
