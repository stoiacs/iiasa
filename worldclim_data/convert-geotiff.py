import os
import time
import rasterio
import matplotlib.pyplot as plt

file_dir = 'wc2.1_30s_tavg'

for file in os.listdir(file_dir):
    with (rasterio.open(f'{file_dir}/{file}') as src):
        t1 = time.time()
        data = src.read(1)
        t2 = time.time()
        print(f"Read: {t2 - t1}")
        fig, ax = plt.subplots()
        cax = ax.imshow(data, cmap='coolwarm', vmax=40, vmin=-40)
        t3 = time.time()
        print(f"Plot: {t3 - t2}")
        fig.colorbar(cax)
        t4 = time.time()
        print(f"Colorbar: {t4 - t3}")
        fig.savefig(f'{file}.png', dpi=300, bbox_inches='tight')
        t5 = time.time()
        print(f"Save: {t5 - t4}")
