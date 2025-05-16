import os
import re
import json
import yaml  # Import the PyYAML library

def parse_markdown_file(filepath):
    """
    Parses a Markdown file to extract title, prerequisites, and learn_next entries.
    Handles errors gracefully, including file not found and YAML parsing issues.

    Args:
        filepath (str): The path to the Markdown file.

    Returns:
        dict: A dictionary containing the title, prerequisites, and learn_next entries,
              or None if the file cannot be parsed.  Title will be "" if not found.
              Prerequisites and learn_next will be [] if not found.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

    # Extract the YAML front matter.
    match = re.search(r"---\n(.*?)\n---", content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        # Replace tabs with spaces before parsing YAML
        yaml_content = yaml_content.replace('\t', '  ')
        try:
            front_matter = yaml.safe_load(yaml_content)  # Use yaml.safe_load
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {filepath}: {e}")
            return None
    else:
        front_matter = {}

    # Extract title, default to empty string if not found
    title = front_matter.get('title', "")

    # Extract prerequisites and learn_next, default to [] if not found
    prerequisites = front_matter.get('prerequisites', [])
    learn_next = front_matter.get('learn_next', [])

    return {
        'title': title,
        'prerequisites': prerequisites,
        'learn_next': learn_next,
    }

def extract_link_and_title(entry):
    """
    Extracts the link and title from a Markdown link entry.  Handles the case where
    the title or link might be missing or malformed.

    Args:
        entry (str): A Markdown link string, e.g., "[Link Title](link/path)".

    Returns:
        tuple: (link, title).  Returns ("", "") if the entry is not a valid link.
    """
    if not isinstance(entry, str):
        return "", ""

    match = re.search(r"\[(.*?)\]\((.*?)\)", entry)
    if match:
        title = match.group(1).strip()
        link = match.group(2).strip()
        return link, title
    else:
        return "", ""

def create_cytoscape_json(files_data):
    """
    Creates a Cytoscape.js JSON representation of the file dependencies.

    Args:
        files_data (dict): A dictionary where keys are file paths and values are
                          dictionaries containing 'title', 'prerequisites', and
                          'learn_next' lists.
    Returns:
        list: A list representing the Cytoscape.js JSON data.
    """
    nodes = []
    edges = []

    for filepath, data in files_data.items():
        # Ensure data is not None (from parsing error)
        if data is None:
            continue

        # Add the node for the current file.  Use the filename if no title.
        node_id = filepath  # Use the simplified filepath as the node ID
        node_title = data['title'] or os.path.basename(filepath)
        nodes.append({
            'data': {
                'id': node_id,
                'label': node_title,
                'file_path': filepath,  # Store the simplified file path
            }
        })

        # Add edges for prerequisites
        if data['prerequisites'] is not None:
            for prereq in data['prerequisites']:
                prereq_link, prereq_title = extract_link_and_title(prereq)
                if prereq_link and prereq_link in files_data:
                    edges.append({
                        'data': {
                            'source': prereq_link,
                            'target': filepath
                        }
                    })
        if data['learn_next'] is not None:
            # Add edges for "learn next"
            for next_item in data['learn_next']:
                next_link, next_title = extract_link_and_title(next_item)
                if next_link and next_link in files_data:
                    edges.append({
                        'data': {
                            'source': filepath,
                            'target': next_link
                        }
                    })

    return nodes + edges
def process_markdown_files(directory):
    """
    Processes all Markdown files in the given directory and its subdirectories,
    handling potential errors during file processing.

    Args:
        directory (str): The directory to search for Markdown files.

    Returns:
        dict: A dictionary of file data, suitable for create_cytoscape_json.
              Returns {} if no files are found or an error occurs.
    """
    files_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                filepath = os.path.join(root, file)
                # Keep the original filepath
                original_filepath = filepath
                # Modify the filepath for use as key in files_data
                filepath_key = os.path.splitext(filepath.replace('\\', '/').replace('_modules/', ''))[0]

                file_data = parse_markdown_file(original_filepath)
                if file_data:  # Only add if parsing was successful
                    files_data[filepath_key] = file_data
    return files_data

if __name__ == "__main__":
    # Specify the directory containing your Markdown files.
    markdown_directory = ('../_modules')  # Replace with the actual path to your directory
    # changed to './' so it works in any directory

    files_data = process_markdown_files(markdown_directory)
    if files_data:
        cytoscape_data = create_cytoscape_json(files_data)
        # Output the Cytoscape.js JSON data to a file.
        output_file = './cytoscape_data.json'
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                json.dump(cytoscape_data, outfile, indent=2)
            print(f"Cytoscape.js data successfully written to {output_file}")
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")
    else:
        print("No Markdown files found or error processing files.")

