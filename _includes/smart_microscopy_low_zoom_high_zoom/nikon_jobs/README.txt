Targeted imaging — Nikon NIS-Elements JOBS example
==================================================

Files in this folder
--------------------
targeted_imaging.bin                the JOBS workflow
targeted_imaging_segmentation.ga    the General Analysis recipe used by the job


Saved from
----------
NIS-Elements version:      <FILL IN, e.g. AR 5.42.04 64-bit>
Required modules:          JOBS (licensed), General Analysis
                           General Analysis 3 is NOT required
Contributed by:            Mike Abanto, DBM Microscopy Core Facility /
                           Nikon Center of Excellence, University of Basel


Before you run this
-------------------
The job contains the capture definitions it was built with, and those call optical
configurations that exist only on the microscope it was made on. They will not match
your system. After importing, open each capture definition and point it at your own
optical configuration.

Optical configurations this job expects:

  low resolution / overview:   <FILL IN name, objective, filter set, exposure>
  high resolution / detail:    <FILL IN name, objective, filter set, exposure>

Also check, before running on hardware:
  - focus-height and XY offsets between the two objectives
  - clearance of the high-magnification objective against your slide or plate holder
  - whether you are mixing air and immersion objectives at the same XY position

The job can be built and tested without a microscope by simulating a camera in
standard NIS-Elements.


Sample it was designed for
--------------------------
A standard slide with DAPI staining — chosen because it is cheap, bright and
fluorescent and almost every lab has it. Any sample with a robust, high signal can
be substituted, but the segmentation threshold in the .ga recipe will need adjusting.


Licence
-------
CC-BY 4.0, matching the rest of this repository.
