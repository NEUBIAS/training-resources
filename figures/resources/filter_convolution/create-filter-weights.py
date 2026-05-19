import numpy as np
from scipy.ndimage import gaussian_laplace
from skimage.filters import gaussian
import matplotlib.pyplot as plt

def generate_gaussian_kernel(size, sigma):
    """Generate a Gaussian kernel of given size and sigma."""
    # Create a delta image
    image = np.zeros((size, size))
    image[size // 2, size // 2] = 1
    kernel = gaussian(image, sigma=sigma, mode='constant', truncate=3.0)
    return kernel

def generate_log_kernel(size, sigma):
    """Generate a Laplacian of Gaussian (LoG) kernel."""
    # Create coordinate grid
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    r2 = xx**2 + yy**2
    normalization = (r2 - 2 * sigma**2) / (sigma**4)
    gaussian_part = np.exp(-r2 / (2 * sigma**2))
    log_kernel = normalization * gaussian_part
    log_kernel -= log_kernel.mean()  # Normalize to zero mean
    return log_kernel

def plot_kernels_and_profiles(kernels, titles):
    """Plot kernel heatmaps and center row profiles."""
    fig, axes = plt.subplots(len(kernels), 2, figsize=(10, 2 * len(kernels)))

    for i, (kernel, title) in enumerate(zip(kernels, titles)):
        ax_heatmap = axes[i, 0]
        ax_profile = axes[i, 1]
        
        # Heatmap
        im = ax_heatmap.imshow(kernel, cmap='viridis', interpolation='none')
        ax_heatmap.set_title(f"{title} - Heatmap")
        fig.colorbar(im, ax=ax_heatmap, fraction=0.046, pad=0.04)

        # Line profile through center row
        center_row = kernel[kernel.shape[0] // 2, :]
        ax_profile.plot(center_row, marker='o')
        ax_profile.set_title(f"{title} - Center Row Profile")
        ax_profile.grid(True)

    plt.tight_layout()
    plt.show()


# Generate and print Gaussian kernels
gaussian_5x5 = generate_gaussian_kernel(5, sigma=1)
gaussian_7x7 = generate_gaussian_kernel(7, sigma=1)

# Generate and print LoG kernels
log_5x5 = - np.round(generate_log_kernel(5, sigma=1), 1)
log_7x7 = - np.round(generate_log_kernel(7, sigma=1), 1)

# Display results
print("Gaussian 5x5 Kernel:\n", gaussian_5x5)
print("\nGaussian 7x7 Kernel:\n", gaussian_7x7)
print("\nLoG 5x5 Kernel:\n", log_5x5)
print("\nLoG 7x7 Kernel:\n", log_7x7)

kernels = [gaussian_5x5, gaussian_7x7, log_5x5, log_7x7]
titles = ["Gaussian 5x5", "Gaussian 7x7", "LoG 5x5", "LoG 7x7"]
plot_kernels_and_profiles(kernels, titles)