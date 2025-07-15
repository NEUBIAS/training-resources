#### Hardware and software requirements

This implementation required Zeiss microscope controlled by ZenBlue software. Macro programming module is not required, although preferential to simplify changing parameters of Zen macro.

#### Installation

- Install Fiji with AutoMicTools package on microscope running PC using [these guidelines](https://git.embl.org/halavaty/AutoMicTools/-/blob/master/Documentation/manual.md).
- Install zeiss_zenbLue_automation package using [these guidelines](https://git.embl.org/grp-almf/zeiss_zenblue_automation).

#### Step-by-step guidelines

- Set up imaging settings
	- Define settings for low zoom and high zoom imaging 
		- Each time activate “Tiles” option
		- Save settings as “Experiment setups” in ZenBlue
- Set up image analysis
	- Download example Fiji [macro](https://git.embl.org/halavaty/AutoMicTools/-/blob/master/script-and-macro-examples/online-segmentation/Segment_nuclei.ijm?ref_type=heads) and open it in Fiji (drag-and-drop)
	- Take example low zoom image and open it in Fiji (drag-and-drop)
	- Test macro by running it. As a result, segmented ROIs should be added to image overlay.
- Start AutoMicTools  distributor in Fiji
	- [ Plugins › Auto Mic Tools › Applications › Imaging › AF LowZoom HighZoom - script] 
	- Parameters of the first dialogue (General JobDistributor parameters):
		- Image File Extension: **czi**
		- Experiment Folder: ***{path to experimental folder where data will be stored}***
		- Microscope Commander: **ZenBlueCommander**
		- Other parameters: ***default values***
	- Second dialogue (processing parameters for autofocus job): keep all by default
	- Third dialogue (processing parameters for low zoom job):
		- Script path: ***path to the Fiji macro tested in step 2***
	- Configure parameters of ZenBlue script and run it
	- (Optional) Simulate acquisition workflow using pre-acquired data
