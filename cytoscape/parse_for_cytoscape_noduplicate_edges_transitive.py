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
    tags = front_matter.get('tags', [])
    return {
        'title': title,
        'prerequisites': prerequisites,
        'learn_next': learn_next,
        'tags' : tags
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
                
        link = link.replace('../', "")
        link = link.replace('./', "")
        return link, title
    else:
        return "", ""

def create_cytoscape_json(files_data):
    """
    Creates a Cytoscape.js JSON representation of the file dependencies.  Ensures
    that each edge appears only once in the output.

    Args:
        files_data (dict): A dictionary where keys are file paths and values are
                          dictionaries containing 'title', 'prerequisites', and
                          'learn_next' lists.

    Returns:
        list: A list representing the Cytoscape.js JSON data.
    """
    nodes = []
    edges = []
    edge_set = set()  # Use a set to track unique edges

    for filepath, data in files_data.items():
        # Ensure data is not None (from parsing error)
        if data is None:
            continue

        if 'Template' in data['title'] or 'DRAFT' in data['title']:
            continue
        if  data.get('tags', []) is not None:
            if 'draft' in data.get('tags', []):
                continue
        # Add the node for the current file.  Use the filename if no title.
        node_id = filepath
        node_title = data['title'] or os.path.basename(filepath)
        nodes.append({
            'data': {
                'id': node_id,
                'label': node_title,
                'file_path': filepath,
            }
        })
    # 2.  Build adjacency list (dependencies) first just all elemenet
    adjacency_list = {}
    for filepath, data in files_data.items():
        if data is None:
            continue
        if 'Template' in data['title'] or 'DRAFT' in data['title']:
            continue
        if  data.get('tags', []) is not None:
            if 'draft' in data.get('tags', []):
                continue
        adjacency_list[filepath] = set()
    for filepath, data in files_data.items():
        if data is None:
            continue
        if 'Template' in data['title'] or 'DRAFT' in data['title']:
            continue
        if  data.get('tags', []) is not None:
            if 'draft' in data.get('tags', []):
                continue
        if data['prerequisites'] is not None:
            for prereq in data['prerequisites']:
                if prereq is not None:
                    if 'TODO' in prereq:
                        continue
                prereq_link, _ = extract_link_and_title(prereq)
                if prereq_link and prereq_link in files_data:
                    adjacency_list[filepath].add(prereq_link)
        if data['learn_next'] is not None:
            for next_item in data['learn_next']:
                if next_item is not None:
                    if 'TODO' in next_item:
                        continue
                next_link, _ = extract_link_and_title(next_item)
                if next_link and next_link in files_data and 'Template' not in files_data.get(next_link, {}).get('title', '') and 'TODO' not in next_item:
                    adjacency_list[next_link].add(filepath)  # Corrected: Add to *next_link*


    # 3. Transitive Reduction
    def transitive_reduction(adj_list):
        """
        Reduces the given adjacency list by removing transitive edges.
        """
        reduced_adj_list = {node: set(neighbors) for node, neighbors in adj_list.items()}
        for node in adj_list:
            for neighbor in list(adj_list[node]):  # Iterate over a copy
                for other_neighbor in adj_list[neighbor]:
                    if other_neighbor in reduced_adj_list[node]:
                        reduced_adj_list[node].remove(other_neighbor)
        return reduced_adj_list

    reduced_adjacency_list = transitive_reduction(adjacency_list)

    # 4. Create edges from the reduced adjacency list
    for node, neighbors in reduced_adjacency_list.items():
        for neighbor in neighbors:
            edge_tuple = (neighbor, node)
            if edge_tuple not in edge_set:
                edges.append({
                    'data': {
                        'source': neighbor,
                        'target': node,
                        'label': 'Dependency',
                    }
                })
                edge_set.add(edge_tuple)
    layout = {
            'name': 'klay',  # Use the Klay layout algorithm
             'klay': {
                 'nodeLayering': 'NETWORK_SIMPLEX',  # Options: 'NETWORK_SIMPLEX', 'LONGEST_PATH', 'INTERACTIVE'
                 'aspectRatio': 0.2,
                 'compactComponents': True,
                 'direction': 'DOWN',
                 'edgeRouting': 'ORTHOGONAL',
                 'edgeSpacingFactor':0.2,
                 'crossingMinimization': 'LAYER_SWEEP', # // Add this for edge crossing reduction  
                 'nodePlacement':'BRANDES_KOEPF' , # options 'LINEAR_SEGMENTS', 'BRANDES_KOEPF'
                 'randomizationSeed': 1, # 0 will change the graph at every reload
                 'spacing': 40,
                 'thoroughness': 10,

             },
        }

    return {
        'elements': {
            'nodes': nodes,
            'edges': edges
        },
        'layout': layout
    }



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
                filepath_key = filepath_key.replace('../', '')
                filepath_key = filepath_key.replace('./', '')

                file_data = parse_markdown_file(original_filepath)
                if file_data:  # Only add if parsing was successful
                    files_data[filepath_key] = file_data
                #  else: parse_markdown_file already prints error
    return files_data



if __name__ == "__main__":
    # Specify the directory containing your Markdown files.
    markdown_directory = ('./_modules')  # Replace with the actual path to your directory
    # changed to './' so it works in any directory

    files_data = process_markdown_files(markdown_directory)
    if files_data:
        cytoscape_data = create_cytoscape_json(files_data)
        # Output the Cytoscape.js JSON data to a file.
        output_file = './cytoscape/cytoscape_data.json'
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                json.dump(cytoscape_data, outfile, indent=2)
            print(f"Cytoscape.js data successfully written to {output_file}")
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")
    else:
        print("No Markdown files found or error processing files.")
