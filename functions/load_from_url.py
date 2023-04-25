import os, tempfile
import requests
from aicsimageio import AICSImage
from aicsimageio.readers import BioformatsReader

def load_from_url(url, verbose=False):

    with tempfile.TemporaryDirectory() as tempdir:
        # extract image name
        url_fname = url.rsplit('/', 1)[1]
        file_name, file_ext = os.path.splitext(url_fname)
        url_file_name, _ = os.path.splitext(url)
        fname = os.path.join(tempdir, file_name+file_ext) 

        if verbose:
            print('Saving file\n', fname, '\nin:\n', tempdir)

        # download url file and save it with the same name
        r = requests.get(url)
        open(fname, "wb").write(r.content)
        
        # if file is ics, download corresponding ids
        if file_ext=='.ics':
            r = requests.get(url_file_name+'.ids')
            ids_name = os.path.join(tempdir, file_name+'.ids')
            open(ids_name, "wb").write(r.content)

        # if file is xml, download corresponding h5
        if file_ext=='.xml':
            r = requests.get(url_file_name+'.h5')
            ids_name = os.path.join(tempdir, file_name+'.h5')
            open(ids_name, "wb").write(r.content)

        # load image using AICSImage to retrieve metadata
        image = AICSImage(fname, reader=BioformatsReader)
        _ = image.data # this is to make sure the image is loaded into memory
    
    return image


if __name__=='__main__':
    url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_8bit_calibrated__mri_full_head.tif'
    image = load_from_url(url, verbose=True)
    print(image.data)
    print(image.physical_pixel_sizes)

