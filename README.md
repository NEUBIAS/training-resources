# Image Analysis Training Resources

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/manerotoni/training-resources)


**[Visit the rendered pages](https://manerotoni.github.io/training-resources).**

This project is intended to collect together various resources
that can be useful when planning/delivering training in image analysis.

Detailed guidance for contributing can be found in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository

Current repository structure:

- template things:
  - `_includes/`: among other things, contains folders holding activities and exercises specific to different platforms for image analysis, for each module
  - `_layouts/`, `_sass/`, `Gemfile`, `_config.yml`, `Makefile`, `assets`, `.gitignore`: material for building the webpages associated with this repository
- content things:
  - `_modules/`: all of the individual module pages are collected here
  - `_extras/`: additional pages to complement the modules
  - `figures/`: a collection of illustrations/diagrams used to help explain the concepts in each module.
  - `image_data/`: image files used in activities and exercises
  - `module_templates/`: template file(s) as an example for module pages
  - `src/`: code for image analysis
  - `workshops/`: information on workshops taught using this material
  - `example_images.md`: intended to contain links to images that would make good examples when teaching
  - `index.md`: content for the website landing page
- other pages (from Carpentries lesson template):
  - `aio.md`: an 'all-in-one' version of the material, combining all the modules into a single page
  - `reference.md`: currently blank but could be populated with a glossary/other reference material
  - `setup.md`: a page for setup instructions - currently blank but could be populated with instructions for relevant technical setup/installation
