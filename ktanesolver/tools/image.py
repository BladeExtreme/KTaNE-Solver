import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams

fig = None; flag = False

def img_initialize(module_name: str, lst: list[str], rows: int, cols: int, new_path: str|None=None):
    global fig

    rcParams['toolbar'] = 'none'

    loaded_images = {}
    for name in lst:
        key = name.lower().replace(' ', '_')
        path = f"ktanesolver/resources/{module_name.replace(' ', '')}/{key}.png" if new_path is None else new_path+f'/{key}.png'
        loaded_images[key] = mpimg.imread(path)

    images = [name.lower().replace(' ', '_') for name in lst]
    fig, axs = plt.subplots(rows, cols, figsize=(6, 6))
    axs = axs.flatten()
    for i, key in enumerate(images):
        ax = axs[i]
        img = loaded_images[key]
        ax.imshow(img)
        ax.set_title(f"{lst[i].capitalize()}", fontsize=8)
        ax.axis('off')
        ax.set_navigate(False)
    for j in range(i + 1, len(axs)):
        axs[j].axis('off')

def img_close():
    plt.close(fig)

def img_open():
    plt.tight_layout()
    plt.show(block=False)