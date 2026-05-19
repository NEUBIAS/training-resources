import requests
from pathlib import Path
import os
from bioio import BioImage
import zipfile
def download_images(remote_url, local_file_path):
    # Eventually create subfolder
    out_path = os.path.dirname(local_file_path)
    if not os.path.exists(os.path.dirname(local_file_path)):
        os.makedirs()
    try:
        if os.path.exists(local_file_path):
            print(f"File already in: {local_file_path}")
            return
        print(f"Downloading file from: {remote_url}")
        response = requests.get(remote_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    
        with open(local_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    
        print(f"File downloaded successfully to: {local_file_path}")

        with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
            zip_ref.extractall()
            print(f"Zip file extracted successfully to: {extract_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Optional: Clean up the downloaded file after you're done
        # import os
        # if local_file_path.exists():
        #     os.remove(local_file_path)
        #     print(f"Downloaded file '{local_file_path}' removed.")
        pass


# +
# Define the URL of the remote file
main_url =  "https://github.com/NEUBIAS/training-resources/raw/master/image_data/"
image_list = ['xyz__multiple_images.czi','xyz_8bit__em_volume_tiff_series.zip']
urls = [main_url + img for img in image_list]

# Define the local file path where you want to save the downloaded file
local_file_paths = [Path("./example_images/"+img) for img in image_list]  # Saves in the current directory

download_images(urls[1], local_file_paths[1])
# -

local_file_paths



