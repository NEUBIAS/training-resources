import os
import glob
import yaml
import openpyxl

def extract_metadata_from_md(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or not lines[0].strip().startswith('---'):
        return None
    yaml_lines = []
    for line in lines[1:]:
        if line.strip().startswith('---'):
            break
        yaml_lines.append(line)
    try:
        meta = yaml.safe_load(''.join(yaml_lines))
        if not meta:
            return None
        tags = meta.get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        # Exclude drafts and outdated
        if any(tag.lower() in ['draft', 'outdated', 'course'] for tag in tags):
            return None
        title = meta.get('title', os.path.basename(md_path))
        objectives = meta.get('objectives', None)
        if isinstance(objectives, list):
            objectives_str = ' '.join(obj.strip().rstrip('.') + '.' for obj in objectives)
        elif isinstance(objectives, str):
            objectives_str = objectives.strip().rstrip('.') + '.'
        else:
            objectives_str = ''
        filename = os.path.splitext(os.path.basename(md_path))[0]
        return {
            'title': title,
            'objectives': objectives_str,
            'tags': [t.lower() for t in tags],
            'filename': filename
        }
    except Exception as e:
        print(f"Error parsing {md_path}: {e}")
        return None

def sort_key(module):
    tags = module['tags']
    if 'workflow' in tags:
        return (2, module['title'].lower())
    if 'scripting' in tags:
        return (3, module['title'].lower())
    return (1, module['title'].lower())

def main():
    modules_dir = os.path.join(os.path.dirname(__file__), '..', '_modules')
    md_files = glob.glob(os.path.join(modules_dir, '*.md'))
    modules = []
    for md_file in md_files:
        meta = extract_metadata_from_md(md_file)
        if meta:
            modules.append(meta)
    modules.sort(key=sort_key)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Objectives"
    ws.append(["Module title", "Learning objectives"])
    for module in modules:
        url = f"https://neubias.github.io/training-resources/{module['filename']}"
        cell = ws.cell(row=ws.max_row + 1, column=1, value=module['title'])
        cell.hyperlink = url
        cell.style = "Hyperlink"
        ws.cell(row=cell.row, column=2, value=module['objectives'])
    wb.save("module_objectives.xlsx")

if __name__ == "__main__":
    main()