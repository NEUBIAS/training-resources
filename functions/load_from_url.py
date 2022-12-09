import os, tempfile
import urllib
from aicsimageio import AICSImage
from aicsimageio.readers import BioformatsReader

def load_from_url(url):

    with tempfile.TemporaryDirectory() as tempdir:
        # extract image name
        fname = os.path.join(tempdir, url.rsplit('/', 1)[1])
        # download image from url and save it with the same name
        r = urllib.request.urlretrieve(url, fname)
        # load image using AICSImage to retrieve metadata
        image = AICSImage(fname, reader=BioformatsReader)
        _ = image.data # this is to make sure the image is loaded into memory
    
    return image

if __name__=='__main__':
    url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif'
    image = load_from_url(url)
    print(image.data)
    print(image.physical_pixel_sizes)

