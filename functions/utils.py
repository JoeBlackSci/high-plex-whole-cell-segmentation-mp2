"""Functions for manipulating and visualising high-plex fluorescence images."""

import matplotlib.pyplot as plt
from tifffile import imwrite


def visimgs(imgs,
            imgnames=None,
            cols=4,
            plotsize=(20, 20),
            save=False,
            savename='tiffcomfig'):
    """Visualise images in a gridbased plot.

    Keyword arguments:
    imgs -- list; images as np arrays
    imgnames -- list; optional names for img titles
    cols -- int; columns for grid arrangement (default=4)
    plotsize -- tuple; size of grid (default=(20,20))
    save -- bool; save an image grid (default=False)
    savename -- string; path used for saving gid

    returns none
    """
    fig = plt.figure(figsize=plotsize)
    rows = -(-len(imgs) // cols)
    for i in range(1, len(imgs) + 1):
        fig.add_subplot(rows, cols, i)
        plt.imshow(imgs[i - 1])
        plt.axis('off')
        if imgnames:
            plt.title(imgnames[i - 1])
    if save:
        plt.savefig(savename+'.png', format='png')
    plt.show()


def tifcomb(imgs):
    """Additvly combine tiff imgs."""
    outimg = imgs[0]
    for i in range(1, len(imgs)):
        outimg += imgs[i]

    return outimg


def crop(imgs, rows, cols, savepath=None, imgnames=None):
    """Crop list of np arrays to specified rows and columns.

    - rows and cols should be list/tupple specifying the slice to crop to.
    - optional savepath will save images to the specified path.
    - optional imgnames should be list of names for imgs.
    """
    cropped = [img[rows[0]:rows[1], cols[0]:cols[1]] for img in imgs]

    if savepath:

        if not imgnames:
            imgnames = list(range(len(imgs)))
        elif len(imgnames) != len(imgs):
            raise ValueError("imgnames must be same length as imgs or None")

        for i, img in enumerate(cropped):
            imwrite(savepath + imgnames[i], img)

    return cropped
