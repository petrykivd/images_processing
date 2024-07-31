import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import math

from config import settings


def display_result(selected_images, best_match_image, cropped_images):
    num_selected = len(selected_images)
    num_cropped = len(cropped_images)
    num_cols = 3
    num_rows_selected = math.ceil(num_selected / num_cols)
    num_rows_cropped = math.ceil(num_cropped / num_cols)

    fig, axes = plt.subplots(num_rows_selected + num_rows_cropped + 2, num_cols,
                             figsize=(15, 5 * (num_rows_selected + num_rows_cropped + 2)))

    for ax in axes.flatten():
        ax.axis('off')

    plt.suptitle("Selected images", fontsize=16, y=0.99)
    for i, path in enumerate(selected_images):
        img = mpimg.imread(os.path.join(settings.DOWNLOAD_FOLDER, path))
        ax = axes[i // num_cols, i % num_cols]
        ax.imshow(img, interpolation='nearest', aspect='auto')
        ax.axis('off')

    ax_best = axes[num_rows_selected, num_cols // 2]
    img_best = mpimg.imread(os.path.join(settings.DOWNLOAD_FOLDER, selected_images[best_match_image]))
    ax_best.imshow(img_best, interpolation='nearest', aspect='auto')
    ax_best.set_title("Best match", fontsize=12)
    ax_best.axis('off')

    plt.text(0.5, 0.5, "Cropped images", fontsize=16,
             ha='center', va='center', transform=fig.transFigure)

    start_row = num_rows_selected + 2
    for i, path in enumerate(cropped_images):
        img = mpimg.imread(path)
        ax = axes[start_row + i // num_cols, i % num_cols]
        ax.imshow(img, interpolation='nearest', aspect='auto')
        ax.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1, w_pad=0.5)
    plt.savefig('result.png', dpi=300, bbox_inches='tight')
    plt.show()
