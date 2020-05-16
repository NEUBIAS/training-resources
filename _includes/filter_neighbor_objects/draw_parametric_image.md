```
drawResult(label_map, measurement);

function drawResult(label_map, measurement) {
	// replace label in the label map with corresponding measurements
	Ext.<a href="https://clij.github.io/clij2-docs/reference_replaceIntensities">CLIJ2_replaceIntensities</a>(label_map, measurement, parametric_image);
	// show the parametric image
	Ext.CLIJ2_pull(parametric_image);
	setMinAndMax(50, 100);
	run("Fire");
}
```
