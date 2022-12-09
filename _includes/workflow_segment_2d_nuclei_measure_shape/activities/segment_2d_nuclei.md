### Segment 2D nuclei
- Input images
  - [xy_8bit__mitocheck_incenp_t1.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t1.tif)
  - [xy_8bit__mitocheck_incenp_t70.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__mitocheck_incenp_t70.tif)
  - The images are two time points of a time lapse experiment where the INCENP gene was subjected to siRNA knock-down. The data are taken from the published [mitocheck screen](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3108885/). In this screen the authors carried out a genome-wide phenotypic profiling of each of the ~21,000 human protein-coding genes by two-day live imaging of fluorescently labelled chromosomes. Phenotypes were scored quantitatively by computational image processing, which allowed them to identify hundreds of human genes involved in diverse biological functions including cell division, migration and survival.
  - The analysis that we do here is, of course, simpler than what the authors did in the publication, but the essence is already very similar. In addition, to simplify the task we work here on images that were cropped and slightly denoised.
- Workflow
  - Apply the workflow outlined above (see concept map) to both images.
  - The modules listed in "Prerequisites" contain the information as to how to conduct each step of the workflow.
  - The nuclei in both images look quite different. Find shape measurements that quantify this.