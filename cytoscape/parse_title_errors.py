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


def order_modules_by_title(files_data):
    """
    Orders module paths based on their titles alphabetically.
    Modules with 'Draft' in their tags are moved to the end.

    Args:
        files_data (dict): A dictionary where keys are module paths and values
                           are dictionaries containing 'title' and 'tags'.

    Returns:
        list: A list of module paths, ordered by title, with Draft modules last.
    """
    # Create a list of (title, is_draft, path) tuples
    modules_for_sorting = []
    for path, data in files_data.items():
        title = data.get('title', '')
        # Ensure tags is a list and check if 'Draft' is in it (case-insensitive)
        if data.get('tags') is None:
            is_draft = False
            is_workflow = False
            is_scripting = False
            is_course = False
            is_outdated = False
        else:
            is_draft = 'Draft' in [tag.capitalize() for tag in data.get('tags', [])]
            is_workflow = 'Workflow' in [tag.capitalize() for tag in data.get('tags', [])]
            is_scripting = 'Scripting' in [tag.capitalize() for tag in data.get('tags', [])]
            is_course = 'Course' in [tag.capitalize() for tag in data.get('tags', [])]
            is_outdated = 'Outdated' in [tag.capitalize() for tag in data.get('tags', [])]
        if is_course or is_outdated:
            continue    
        
        modules_for_sorting.append((title.lower(), is_scripting, is_workflow, is_draft,  path)) # Sort by lowercased title

    # Sort the list:
    # 1. By 'is_draft' (False comes before True, so non-drafts come first)
    # 2. Then by 'title' (alphabetically)
    modules_for_sorting.sort(key=lambda x: (x[3], x[2], x[1], x[0]))

    # Extract just the ordered paths
    ordered_paths = [path for _, _, _, _, path in modules_for_sorting]
    return ordered_paths

if __name__ == "__main__":
    # Specify the directory containing your Markdown files.
    markdown_directory = ('./_modules')  # Replace with the actual path to your directory
    # changed to './' so it works in any directory

    files_data = process_markdown_files(markdown_directory)
    ordered_module_paths = order_modules_by_title(files_data)

    for path in ordered_module_paths:
        # Extract just the filename/module name from the path
        # Assuming paths look like 'path/to/module_name' and you want 'module_name'
        module_name = os.path.basename(path) # This gets 'module_name' from 'path/to/module_name'
        print(f"- {module_name}")
    if files_data:
        for current_path, data in files_data.items():
            current_module_title = data.get('title', 'NO_TITLE')
            #print(current_module_title)
            prerequisites = data.get('prerequisites', [])
            learn_next = data.get('learn_next', [])

            if prerequisites is not None  and len(prerequisites) > 0:
                for prereq_entry in prerequisites:
                    #print(prereq_entry)
                    linked_path, linked_title = extract_link_and_title(prereq_entry)
                    if 'TODO' in linked_title:
                        continue
                    if linked_path in files_data: 
                        actual_prereq_title = files_data[linked_path].get('title', 'NO_TITLE')
                        if actual_prereq_title != linked_title:
                            print(f"Mismatch in prerequisite for '{current_path}':")
                            print(f"  Referenced Module: {linked_path}")
                            print(f"  Title in Link: '{linked_title}'")
                            print(f"  Actual Module Title: '{actual_prereq_title}'")
            if learn_next is not None  and len(learn_next) > 0:
                for learn_next_entry in learn_next:
                    #print(prereq_entry)
                    linked_path, linked_title = extract_link_and_title(learn_next_entry)
                    if 'TODO' in linked_title:
                        continue
                    if linked_path in files_data: 
                        actual_learn_next_title = files_data[linked_path].get('title', 'NO_TITLE')
                        if actual_learn_next_title != linked_title:
                            print(f"Mismatch in learn_next for '{current_path}':")
                            print(f"  Referenced Module: {linked_path}")
                            print(f"  Title in Link: '{linked_title}'")
                            print(f"  Actual Module Title: '{actual_learn_next_title}'")
