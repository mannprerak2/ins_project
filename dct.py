import scipy
import numpy as np
from numpy import r_
from numpy import zeros
import matplotlib.pyplot as plt
from scipy.fftpack import fft, dct, idct


def dct2(a):
    return dct(dct(a, axis=0, norm='ortho'))


def idct2(a):
    return idct(idct(a, axis=0, norm='ortho'))


def get_dct_coeffs(img_path):
    im = plt.imread("./data/lena_tiny.png")

    imsize = im.shape
    dct_res = np.zeros(imsize)

    # Do 8x8 DCT on image (in-place)
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            dct_res[i:(i+8), j:(j+8)] = dct2(im[i:(i+8), j:(j+8)])

    thresh = 0.00165
    dct_thresh = dct_res * (abs(dct_res) > (thresh * np.max(dct_res)))
    percent_nonzeros = np.sum(dct_thresh != 0.0) / (imsize[0] * imsize[1] * 1.0)

    dct_thresh = np.around(dct_thresh, 3)

    return dct_thresh.tolist()


def regenerate_images(dct_coeffs, path):
    dct_thresh = np.array(dct_coeffs)
    imsize = dct_thresh.shape

    im_dct = np.zeros(imsize)

    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            im_dct[i:(i+8), j:(j+8)] = idct2(dct_thresh[i:(i+8), j:(j+8)])

    plt.imsave(path, im_dct)
