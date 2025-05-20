import os
import re

def count_napari_calls_per_file(directory):
    """
    Searches for .py files (excluding those with "jython" in the name)
    within the specified directory and its subdirectories, and counts the
    occurrences of 'napari.Viewer()' and 'viewer.close()' for each file.

    Args:
        directory (str): The root directory to start the search from.
    """
    total_viewer_count = 0
    total_close_count = 0
    files_analyzed = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and "jython" not in file:
                files_analyzed += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                        viewer_calls = len(re.findall(r"Viewer\(", content))
                        close_calls = len(re.findall(r"viewer\.close\(", content))

                        if (viewer_calls != close_calls):
                            print(f"File: {file_path}")
                            print(f"  'napari.Viewer()' calls: {viewer_calls}")
                            print(f"  'viewer.close()' calls: {close_calls}")
                            total_viewer_count += viewer_calls
                            total_close_count += close_calls

                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    print("\n--- Summary ---")
    print(f"Number of Python files analyzed: {files_analyzed}")
    print(f"Total 'napari.Viewer()' calls found across all files: {total_viewer_count}")
    print(f"Total 'viewer.close()' calls found across all files: {total_close_count}")

def find_plt_close(directory):
    """
    Searches for .py files (excluding those with "jython" in the name)
    within the specified directory and its subdirectories, and checks if
    those files contain both "napari" and "viewer.close()".

    Args:
        directory (str): The root directory to start the search from.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and "jython" not in file:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                        #if "napari" in content and "viewer.close()" in content:
                        #    print(f"Found 'napari' and 'viewer.close()' in: {file_path}")
                        if "matplotlib" in content and not "plt.close('all')" in content:
                            print(f"Found 'matplotlib' but no 'plt.close('all')' in: {file_path}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    # Replace this with the directory you want to search
    search_directory = "../_includes"  # Current directory
    count_napari_calls_per_file(search_directory)
    find_plt_close(search_directory)




