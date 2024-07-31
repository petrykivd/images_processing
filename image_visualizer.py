import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config import settings


def display_result(selected_images):
    num_images = len(selected_images)
    num_cols = 3
    num_rows = (num_images + num_cols - 1) // num_cols

    fig, axes = plt.subplots(num_rows + 1, num_cols, figsize=(10, 3 * (num_rows + 1)))

    for ax in axes.flatten():
        ax.axis('off')

    for i, path in enumerate(selected_images):
        img = mpimg.imread(os.path.join(settings.DOWNLOAD_FOLDER, path))
        ax = axes.flatten()[i]
        ax.imshow(img, interpolation='nearest', aspect='auto')
        ax.axis('off')

    ax = axes[-1, num_cols // 2]
    img = mpimg.imread(os.path.join(settings.DOWNLOAD_FOLDER, selected_images[0]))
    ax.imshow(img, interpolation='nearest', aspect='auto')
    ax.set_title("Best match", fontsize=10)
    ax.axis('off')

    plt.suptitle("Selected images", fontsize=12)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=0.5, w_pad=0.5)

    plt.savefig('result.png', dpi=300, bbox_inches='tight')

    plt.show()
