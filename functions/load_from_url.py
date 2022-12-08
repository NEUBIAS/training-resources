import os
import urllib
from aicsimageio import AICSImage
from aicsimageio.readers import BioformatsReader

def load_from_url(url):



    # extract image name
    fname = url.rsplit('/', 1)[1]
    # download image from url and save it with the same name
    r = urllib.request.urlretrieve(url, fname)
    # load image using AICSImage to retrieve metadata
    image = AICSImage(fname, reader=BioformatsReader)
    
    return image

if __name__=='__main__':
    url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_without_offset.tif'
    image = load_from_url(url)
