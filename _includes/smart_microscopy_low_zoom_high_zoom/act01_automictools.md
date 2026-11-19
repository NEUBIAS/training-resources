#### Explicit Goal of the procedure
Here we want to implement a simple pipeline to detect cells in a large widefield FoV and then focus on some of them with a high zoom in confocal.

Steps:
- Perform large FoV in widefield at different registered positions
- For all positions:
	- go to the position, perform autofocus (Fiji focus script).
	- acquire and detect cells in widefield (DAPI) large FoV (assisted by an external script on Fiji).
		- For a defined number of cells, switch to confocal high zoom and acquire.

#### Hardware and software requirements
This implementation required Zeiss microscope controlled by ZenBlue software. Macro programming is not required, it is better to just simply change parameters of the already written Zen macro. It requires as well Fiji with the AutoMicTools plugin (see Installation).

#### Sample requirement
The pipeline relies on finding nuclei (even if it can be directly use for other cases), therefore we recommend to prepare a Hela cells sample with DAPI and whatever other dyes you desire. The recommended magnification to use would be x20 to have a relatively large field of view (FoV).

#### Sources
- A video showcasing this tutorial can be found here.
- To investigate further on the programming of the JobDistributor.
- To investigate further on the scripting of a Job.

#### Installation
- Install Fiji with AutoMicTools package on microscope running PC using [these guidelines](https://git.embl.org/halavaty/AutoMicTools/-/blob/master/Documentation/manual.md).
- Install zeiss_zenblue_automation package by downloading the git repository of [this  link](https://git.embl.org/grp-almf/zeiss_zenblue_automation), unzip it, copy paste it in the local user Zen Blue folder: e.g. C:\Users\user\Documents\Carl Zeiss\ZEN\Documents\Macros

#### Step-by-step guidelines

1. Set up imaging settings (observation methods in ZenBlue)

   Define settings for autofocus, low zoom and high zoom imaging and another one to store the different positions where you want to perform the screening. Save the settings as individual "Experiment setup" in ZenBlue, using the table below as a reference. There is no need to specify image name and path in the observation methods, as they will be overwritten by the ZenBlue Macro Script that we will run later.

   | name to use | short description | Tiles | Zstack |
   | --- | --- | --- | --- |
   | `AMT_Position` | register position, using multiple Tiles | on ✅ | off ❌ |
   | `AMT_AF_Reflection` | defining the autofocus method, from laser, filters and z-range | off ❌ | on ✅ |
   | `AMT_LowZoom` | define the large FoV widefield DAPI method | on ✅ | off ❌ |
   | `AMT_HighZoom` | define the confocal high zoom final acquisition | on ✅ | on ✅ |

2. Set up image analysis (in Fiji)

   - Download the [example Fiji macro](https://git.embl.org/halavaty/AutoMicTools/-/blob/master/script-and-macro-examples/online-segmentation/Segment_nuclei.ijm?ref_type=heads) and open it in Fiji (drag-and-drop). The path to this script will be used later in step 3.

     > **Note:** no link anymore !

   - [Debug] Acquire a low zoom image with your `AMT_LowZoom` observation method and open it in Fiji (drag-and-drop)
   - [Debug] Test macro by running it. As a result, segmented ROIs should be added to image overlay.

3. Start AutoMicTools distributor in Fiji

   - `[ Plugins › Auto Mic Tools › Applications › Imaging › AF LowZoom HighZoom - script]`
   - Parameters for the first dialogue (General JobDistributor parameters):
     - Image File Extension: **`czi`**
     - Experiment Folder: **`{path to experimental folder where data will be stored}`**. *This path will be used in step 4.*
     - Microscope Commander: **`ZenBlueCommander`**
     - Other parameters: ***default values***
   - Second dialogue (processing parameters for autofocus job): keep all by default
   - Third dialogue (processing parameters for low zoom job):
     - Script path: ***path to the Fiji macro tested in step 2***

4. Setup and run ZenBlue Macro

   - Open the ZenBlue macro script `Pipeline_AF-LowZoom-HighZoom.py` previously downloaded in the zeiss_zenblue_automation package.
   - At the top of the script, update the `rootFolder` variable, with the path of the same folder that Fiji surveys defined in step 3: **`{path to experimental folder where data will be stored}`**
   - Below it, update the `defaultPositionsJobName` to be `AMT_Position`
   - Just below the comment `#defining jobs`, update the jobs name to be `AMT_AF_Reflection` for the AF line, `AMT_LowZoom` for the LowZoom line and `AMT_HighZoom` for the HighZoom line.
