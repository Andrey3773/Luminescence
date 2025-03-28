import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import os


folder_path = 'input_files'
number = 0

for filename in os.listdir(folder_path):
    number += 1
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'r+') as file:
        content = file.read()
        if 'lambda, I' not in content:
            new_content = '\n\nlambda, I\n' + content.replace('\t', ', ')
            file.seek(0)
            file.write(new_content)
            file.truncate()

    spectrum_data = pd.read_csv(
        file_path,
        sep=",",
    )

    wavelength_list = np.array(spectrum_data["lambda"].to_list())
    intensity_list = np.array(spectrum_data[" I"].to_list())

    intensity_list_smoothed = np.array(savgol_filter(intensity_list, 65, 2))

    max_index = np.argmax(intensity_list_smoothed)
    max_intensity = intensity_list_smoothed[max_index]
    max_wavelength = wavelength_list[max_index]

    norm_intensity = intensity_list_smoothed / max_intensity

    wavelength = np.array(wavelength_list)
    intensity = np.array(intensity_list_smoothed)

    comment = (f'$max(I) = {max_intensity}$\n'
               f'$\lambda = {max_wavelength}$')

    plt.figure()
    plt.title(fr"$I(\lambda)_{str(number)}$")
    plt.plot(wavelength, intensity, '-', label=r"$I(\lambda)$",)
    plt.figtext(0.15, 0.8, comment, fontsize=11)
    plt.xlabel(r"$\lambda$", loc='right')
    plt.ylabel(r"$I$", loc='top')
    plt.legend()
    plt.savefig(f"output_files\graph_{filename}.jpg")
