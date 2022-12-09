import os, tempfile
import requests
from aicsimageio import AICSImage
from aicsimageio.readers import BioformatsReader

def load_from_url(url, verbose=False):

    with tempfile.TemporaryDirectory() as tempdir:
        # extract image name
        fname = os.path.join(tempdir, url.rsplit('/', 1)[1])

        if verbose:
            print('Saving file\n', fname, '\nin:\n', tempdir)

        # download image from url and save it with the same name
        r = requests.get(url)
        open(fname, "wb").write(r.content)
        # load image using AICSImage to retrieve metadata
        image_aics = AICSImage(fname, reader=BioformatsReader)
        _ = image_aics.data # this is to make sure the image is loaded into memory
    
    return image_aics

if __name__=='__main__':
    url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif'
    image = load_from_url(url, verbose=True)
    print(image.data)
    print(image.physical_pixel_sizes)

