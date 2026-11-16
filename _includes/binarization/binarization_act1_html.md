1. Inspect the two cells in the **Original Image** below.
2. Drag the **Threshold (t)** slider to find a value that segments **both** the bright and dim nuclei.
3. Increase the threshold value further until **only** the brighter nucleus remains segmented.

<script src="{{ site.baseurl }}/assets/js/UTIF.js"></script>

<div style="border: 1px solid #ddd; padding: 15px; border-radius: 6px; margin: 15px 0; text-align: center; background: #fafafa;">
  <div style="display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; margin-bottom: 15px;">
    <div>
      <canvas id="act1OrigCanvas" style="border: 1px solid #ccc; width: 220px; height: auto; image-rendering: pixelated;"></canvas>
      <div style="font-size: 0.9em; color: #555;">Original Image (xy_8bit__two_cells.tif)</div>
    </div>
    <div>
      <canvas id="act1BinCanvas" style="border: 1px solid #ccc; width: 220px; height: auto; image-rendering: pixelated;"></canvas>
      <div style="font-size: 0.9em; color: #555;">Binary Mask (t = <span id="act1ThreshVal">73</span>)</div>
    </div>
  </div>

  <label for="act1ThreshSlider"><strong>Threshold (t):</strong> </label>
  <input type="range" id="act1ThreshSlider" min="0" max="255" value="73" style="width: 60%; vertical-align: middle;">
</div>

<script>
(function() {
  const origCanvas = document.getElementById('act1OrigCanvas');
  const binCanvas = document.getElementById('act1BinCanvas');
  const origCtx = origCanvas.getContext('2d');
  const binCtx = binCanvas.getContext('2d');
  const slider = document.getElementById('act1ThreshSlider');
  const threshLabel = document.getElementById('act1ThreshVal');

  let originalImageData = null;
  const tiffUrl = "{{ site.baseurl }}/image_data/xy_8bit__two_cells.tif";

  fetch(tiffUrl)
    .then(response => response.arrayBuffer())
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
    });

  function applyThreshold(threshold) {
    if (!originalImageData) return;
    const src = originalImageData.data;
    const output = binCtx.createImageData(originalImageData.width, originalImageData.height);
    const dst = output.data;

    for (let i = 0; i < src.length; i += 4) {
      const val = src[i] >= threshold ? 255 : 0;
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
