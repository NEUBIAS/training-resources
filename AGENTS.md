# AGENTS.md — AI Agent Entry Point

This file is the primary entry point for AI coding agents contributing to the **Bioimage Analysis Training Resources** repository.

**Live site:** https://neubias.github.io/training-resources/  
**GitHub repo:** https://github.com/NEUBIAS/training-resources  
**Preprint:** https://zenodo.org/records/17669862 (Tischer, Politi et al., 2025)

---

## What this project is

A modular, open-access collection of bioimage analysis teaching modules, designed to help trainers deliver live in-person or online courses. Each module covers one concept (30–45 min teaching time) and provides activities in multiple software platforms (ImageJ GUI, ImageJ Macro, Python/skimage/napari, Galaxy, MATLAB). The site is built with Jekyll and hosted on GitHub Pages.

---

## Repository layout

```
_modules/           # One .md file per teaching module (YAML frontmatter + optional Markdown body)
_includes/          # Per-module subfolder with activity .md files and platform implementations (.py, .ijm, etc.)
_courses/           # Course definition files (ordered lists of modules)
_layouts/           # Jekyll HTML layouts (do not edit unless working on site structure)
_config.yml         # Jekyll config; also defines global module_order list
figures/            # PNG figures referenced by modules (one per module, same base name)
image_data/         # Example images used in activities (loaded by URL in scripts)
image_data_big/     # Larger example images
functions/          # Shared Python helpers (on PYTHONPATH via python.env)
test_python/        # pytest suite that runs all _includes/**/*.py scripts
.github/workflows/  # CI: test-python-scripts.yml, website.yml
```

Key files:
- `CONTRIBUTING.md` — step-by-step guide for adding/editing content
- `TEACHING_TIPS.md` — pedagogical guidance for instructors
- `_modules/template.md` — canonical template for a new module
- `_config.yml` — `module_order` list controls ordering in the All Modules page

---

## Module anatomy

Each module lives in two places:

### 1. `_modules/<name>.md` — module definition file

YAML frontmatter (required fields):

```yaml
---
title: Human-readable title
layout: module          # never change
tags: []                # optional: ["scripting"], ["workflow"], ["draft"]
prerequisites:
  - "[Module title](../module_name)"
objectives:
  - "Verb-first learning objective (use Bloom's taxonomy verbs)"
motivation: |
  Why is this important? Written in Markdown.
concept_map: >
  graph TD               # Mermaid.js flowchart
    A("Concept A") --> B("Concept B")
figure: /figures/<name>.png
figure_legend: Caption for the figure.
multiactivities:
  - ["<name>/act01.md", [
      ["ImageJ GUI",    "<name>/act01_imagejgui.md"],
      ["ImageJ Macro",  "<name>/act01_imagejmacro.ijm"],
      ["skimage napari","<name>/act01_skimage_napari.py"]
    ]]
assessment: |
  ### Question
  ...
  > ## Solution
  > ...
  {: .solution}
learn_next:
  - "[Title](../module_name)"
external_links:
  - "[Text](https://url)"
---
```

Optional free Markdown body beneath the closing `---` appears on the rendered page between the figure and the Activities section.

### 2. `_includes/<name>/` — activity files

For each entry in `multiactivities`:

| File | Purpose |
|---|---|
| `<name>/act01.md` | Software-agnostic description of the activity; includes example image links |
| `<name>/act01_imagejgui.md` | Step-by-step ImageJ GUI instructions |
| `<name>/act01_imagejmacro.ijm` | ImageJ Macro code |
| `<name>/act01_skimage_napari.py` | Python script using skimage + napari (jupytext `# %%` cell format) |
| `<name>/act01_galaxy.md` | Galaxy instructions (optional) |
| `<name>/act01_matlab.m` | MATLAB code (optional) |

---

## Adding a new module — checklist

1. Run the scaffold script (optional but recommended):
   ```bash
   ./add_new_module.sh <module_name>
   ```
2. Edit `_modules/<module_name>.md` using the YAML spec above (or copy from `_modules/template.md`).
3. Create `_includes/<module_name>/` and add activity files.
4. Add a figure at `figures/<module_name>.png`.
5. Add the module name to the `module_order` list in `_config.yml` at the appropriate position.
6. If adding example images, place them in `image_data/` and reference them by their raw GitHub URL in activity files.
7. Run the site locally to verify: `make serve` (requires Jekyll + bundler).
8. Ensure Python scripts pass CI: `pytest test_python/test_all_platforms.py`.

---

## Adding a Python activity — rules and conventions

- Use **jupytext `# %%` cell format** so scripts run both as plain Python and as notebooks.
- Load images via URL using `OpenIJTIFF`:
  ```python
  from OpenIJTIFF import open_ij_tiff
  image, *_ = open_ij_tiff("https://github.com/NEUBIAS/training-resources/raw/master/image_data/<file>.tif")
  ```
- Shared helpers live in `functions/` (on `PYTHONPATH` via `python.env`).
- Each `# %%` cell should have a brief comment explaining what it does.
- If a script requires user interaction (e.g. napari window), add it to the `known_failures` dict in `test_python/test_all_platforms.py` with an explanation.
- Standard conda dependencies: `python=3.12 napari=0.6.0 pyqt pytest notebook matplotlib jupytext scikit-image>=0.20 openijtiff` (see `.github/workflows/test-python-scripts.yml`).



---

## Adding/modifying a course

Course files are in `_courses/<course-name>.md`:

```yaml
---
title: Course Title
module_order: ["module_a", "module_b", "module_c"]
---
{% include base_path.html %}
{% include course_modules.html %}
```

Also add a course card to `index.md` if it should appear on the home page.

---

## Key conventions

- **Software-agnostic first:** concept descriptions in `_modules/` and activity headers in `_includes/` must not assume any specific software. Platform specifics belong only in the platform implementation files.
- **One concept per module:** keep modules tightly scoped (30–45 min). If content is getting long, consider splitting.
- **Prerequisite chain:** always fill in `prerequisites` so the dependency network (cytoscape graph on the home page) stays accurate.
- **`tags: ["draft"]`:** add this tag while a module is work-in-progress; it suppresses it from the main listing.
- **Figures:** one PNG per module, same base name as the module file. If the figure was made with PowerPoint, also add `figures/resources/<name>.pptx`.
- **License:** all content is CC-BY 4.0. Do not add content with incompatible licenses.
- **YAML linting:** validate YAML at http://www.yamllint.com/ before committing.

---

## Building and testing locally

```bash
# Build and serve the Jekyll site (http://127.0.0.1:4000/training-resources/)
make serve

# Before testing Python code, activate the tutorial environment
conda activate skimage-napari-tutorial

# Run Python script tests
pytest test_python/test_all_platforms.py -v
```

CI runs on every push/PR to `master` and `gh-pages` (see `.github/workflows/`).

---

## Common contribution tasks for agents

| Task | Key files to touch |
|---|---|
| Add a new module | `_modules/<name>.md`, `_includes/<name>/`, `figures/<name>.png`, `_config.yml` |
| Add a Python implementation to an existing activity | `_includes/<name>/<name>_<act>_skimage_napari.py`, `_modules/<name>.md` (multiactivities entry) |
| Add an ImageJ Macro implementation | `_includes/<name>/<name>_<act>_imagejmacro.ijm`, `_modules/<name>.md` |
| Fix a broken Python script | `_includes/<name>/<name>_<act>_skimage_napari.py`; run `pytest test_python/test_all_platforms.py` |
| Add a new course | `_courses/<course-name>.md`, optionally `index.md` |
| Update module prerequisites/learn_next | `_modules/<name>.md` YAML frontmatter |

---

## Resources

- Full contributor guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Teaching guidance: [TEACHING_TIPS.md](TEACHING_TIPS.md)
- Module template: [_modules/template.md](_modules/template.md)
- All modules overview: https://neubias.github.io/training-resources/all-modules
- GitHub issues (discuss new content): https://github.com/NEUBIAS/training-resources/issues
