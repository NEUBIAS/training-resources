<h4 id="act1"><a href="#act1">Explore the microscope through its GUI</a></h4>

You will operate the virtual microscope exactly like a real instrument, through the same graphical interface (napari-micromanager) that runs real Micro-Manager systems.

- Install the simulator and launch the microscope GUI with the **optogenetic** sample loaded (see the implementation tab for the exact commands)
- Explore the microscope interactively, like you would at a real instrument:
  - Snap an image; start Live mode and watch the cells move
  - Switch objectives (10x to 40x) and observe how the field of view shrinks while the image stays 512 x 512 pixels
  - Step through the channels (phase-contrast, miRFP, mVenus, mScarlet) and compare what each label shows, as in the channel gallery above
  - Change the exposure time and observe brightness and noise
  - Move the stage to a different field of view, and to the edge of the well
  - Open the Device Property Browser: find the properties that the Channel preset changes, and change the camera binning
