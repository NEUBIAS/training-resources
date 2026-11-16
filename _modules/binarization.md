---
title: Thresholding
layout: module
tags: ["segmentation", "binarization"]
prerequisites:
  - "[Digital image basics](../pixels)"
  - "[Data types](../datatypes)"
  - "[Segmentation overview](../segmentation)"
objectives:
  - "Describe the relationship between an intensity image and a derived binary image"
  - "Apply threshold to segment an image into foreground and background regions"
motivation: |
  Finding objects/regions of interest in an image is one of the most common goals in image analysis. Since an image is an array of pixel values, one can assign certain pixel values to objects/regions of interest.  One strategy to achieve this, is to first distinguish so-called background pixels, which do not contain objects or interesting regions from foreground pixels, which mark the areas of interest, by means of a single **threshold** value. This process is called **two class semantic segmentation** and is often referred to as **image binarization**. The foreground regions can then be further processed, e.g. to detect objects or perform intensity measurements.

concept_map: >
  graph TD
    I("Image") --> T("Threshold (value)")
    T --> BI("Binary image / Binary mask")
    BI --- BG("Background pixels (false, 0)")
    BI --- FG("Foreground pixels (true, 1, 255)")

figure: /figures/binarization.png
figure_legend: Image before and after applying a threshold of 73 gray values.

multiactivities:
  - ["binarization/binarization_act1.md", [["Interactive HTML", "binarization/binarization_act1_html.md"], ["ImageJ GUI", "binarization/binarization_act1_imagejgui.md"], ["ImageJ Macro", "binarization/binarization_act1_imagejmacro.ijm"], ["ImageJ Jython", "binarization/binarization_act1_jython.py"], ["skimage napari", "binarization/binarization_act1_skimage_napari.py", "python"],["Galaxy", "binarization/binarization_act1_galaxy.md"]] ]
  - ["binarization/binarization_act2.md", [["ImageJ GUI", "binarization/binarization_act2_imagejgui.md"], ["ImageJ Macro", "binarization/binarization_act2_imagejmacro.ijm"], ["ImageJ Jython", "binarization/binarization_act2_jython.py"], ["ImageJ Jython + input parameters", "binarization/binarization_act2_jython_inputparameters.py"], ["skimage napari", "binarization/binarization_act2_skimage_napari.py"],["Galaxy", "binarization/binarization_act2_galaxy.md"]]]
  - ["binarization/binarization_act3.md", [["ImageJ GUI", "binarization/binarization_act3_imagejgui.md"]]]


assessment: >

  ### Fill in the blanks

    - Pixels in a binary image can have maximally ___ different values.
    - If the threshold is larger than the maximal pixel value in the intensity image, all pixels in the binary image have a value of ___.

    > ## Solution
    >   - Pixels in a binary image can have maximally **2** different values.
    >   - If the threshold is larger than the maximal pixel value in the intensity image,
    > all pixels in the binary image have a value of **0**.
    {: .solution}

  ### True or False
    - There is only one correct threshold value in order to convert an intensity image into a binary image.
    - Binary images are always unsigned 8-bit where the foreground is 255.

    > ## Solution
    >   - There is only one correct threshold value in order to convert an intensity image into a binary image. **False**
    >   -  Binary images are always unsigned 8-bit where the foreground is 255. **False**
    {: .solution}

learn_next:
  - "[Automatic thresholding](../auto_threshold)"
  - "[Connected component labeling](../connected_components)"

external_links:
  - "[Wikipedia: Binary image](https://en.wikipedia.org/wiki/Binary_image)"

---
A common algorithm for binarization is thresholding. A threshold value `t` is chosen, either manually or automatically,
and all pixels with intensities below `t` are set to 0, whereas pixels with intensities `>= t` are set to the value for the foreground.
Depending on the software the foreground value can be different (e.g. 1 in MATLAB or 255 in ImageJ). At any pixel `(x,y)`:

`p_im(x,y) < t` `->` `p_bin(x,y) = 0`

`p_im(x,y) >= t` `->` `p_bin(x,y) = 1`

where, `p_im` and `p_bin` are the intensity and binary images respectively.

For binarization, it is also possible to define an interval of threshold values, i.e. a lower and upper threshold value. Pixels with intensity values within this interval belong to the foreground and vice versa.

<script src="{{ site.baseurl }}/assets/js/UTIF.js"></script>

<div style="border: 1px solid #ddd; padding: 15px; border-radius: 6px; margin: 20px 0; text-align: center; background: #fafafa;">
  <p><strong>Interactive Thresholding Demo (TIFF)</strong></p>
  
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 15px;">
    <div>
      <canvas id="origCanvas" style="border: 1px solid #ccc; max-width: 100%;"></canvas>
      <div style="font-size: 0.9em; color: #555;">Original Image</div>
    </div>
    <div>
      <canvas id="binCanvas" style="border: 1px solid #ccc; max-width: 100%;"></canvas>
      <div style="font-size: 0.9em; color: #555;">Binary Mask (t = <span id="threshVal">73</span>)</div>
    </div>
  </div>

  <label for="threshSlider"><strong>Threshold (t):</strong> </label>
  <input type="range" id="threshSlider" min="0" max="255" value="73" style="width: 60%; vertical-align: middle;">
</div>

<script>
(function() {
  const origCanvas = document.getElementById('origCanvas');
  const binCanvas = document.getElementById('binCanvas');
  const origCtx = origCanvas.getContext('2d');
  const binCtx = binCanvas.getContext('2d');
  const slider = document.getElementById('threshSlider');
  const threshLabel = document.getElementById('threshVal');

  let originalImageData = null;

  // Make sure this filename matches an actual .tif file in your image_data/ folder
  const tiffUrl = "{{ site.baseurl }}/image_data/xy_8bit__nuclei_noisy_different_intensity.tif";

  fetch(tiffUrl)
    .then(response => {
      if (!response.ok) throw new Error("HTTP " + response.status + " loading " + tiffUrl);
      return response.arrayBuffer();
    })
    .then(buffer => {
      const ifds = UTIF.decode(buffer);
      UTIF.decodeImage(buffer, ifds[0]);
      const rgba = UTIF.toRGBA8(ifds[0]);
      const width = ifds[0].width;
      const height = ifds[0].height;

      origCanvas.width = binCanvas.width = width;
      origCanvas.height = binCanvas.height = height;

      originalImageData = new ImageData(new Uint8ClampedArray(rgba), width, height);
      origCtx.putImageData(originalImageData, 0, 0);

      applyThreshold(parseInt(slider.value, 10));
    })
    .catch(err => console.error("Failed to load TIFF:", err));

  function applyThreshold(threshold) {
    if (!originalImageData) return;
    const src = originalImageData.data;
    const output = binCtx.createImageData(originalImageData.width, originalImageData.height);
    const dst = output.data;

    for (let i = 0; i < src.length; i += 4) {
      const intensity = src[i];
      const val = intensity >= threshold ? 255 : 0;
      dst[i] = val;
      dst[i + 1] = val;
      dst[i + 2] = val;
      dst[i + 3] = 255;
    }
    binCtx.putImageData(output, 0, 0);
  }

  slider.addEventListener('input', function() {
    const t = parseInt(this.value, 10);
    threshLabel.textContent = t;
    applyThreshold(t);
  });
})();
</script>


