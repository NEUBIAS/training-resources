# Basics of Bioimage Analysis: Concepts (MorpholibJ) and Workflows (KNIME)

## Duration

2-4 days

## Schedule

1-2 days: Learn concepts of bioimage analysis, using MorphoLibJ (ImageJ Plugin)
1-2 days: Build bioimage analysis workflows, using KNIME.

## Why is this workshop very useful?

Using ImageJ to teach bioimage analysis concepts has the great advantage that most people are already familiar with the ImageJ user interface. Thus, one can fully focus on bioimage analysis concepts and is not distracted by other technical hurdles that naturally arise when using a new software (or even a new programming language).

The ImageJ user interface is very minimal, maximally focussing the attention on interactive exploration of the currently active image, and many image processing operations have an interactive preview functionality. Taken together these features also help to teach and learn image analysis concepts without much distraction.
 
Using the MorpholibJ ImageJ plugin has the advantage that basic important concepts like "connected components analysis" are explicitely executed as one single step (and not hidden inside some convenience meta-functionality that combine many concepts in one step). Moreover, MorpholibJ works both in 2D and 3D, has great documentation, and also offers many advanced functionalities that can be explored further on.

Following up the above conceptual teaching with bioimage analysis workflow building in KNIME is a very natural fit. The reason is  that KNIME's image analysis nodes often literally have the same names as the menu entries in ImageJ and specificially as in MorphoLibJ. Thus, course participants will see the same concepts occuring a second time, which helps memorizing important concepts. Moreover, KNIME is a great tool for data science in general and thus definitely worth learning. 


## Topics taught

The number of topics can be variied, depending on whether this course should be taught in 2,3, or 4 days.

- Image data types
- Image segmentation by thresholding
	- Manual
	- Automated?
- Binary images
- Connected component analysis
- Label masks
- Object shape measurements
- Object intensity measurements
- Convolutional filters
- Rank filters
	- Applied on binary images
	- Applied on grayscale images
- Local background subtraction algorithms
- Distance transform
- Object splitting by watershed
	- Intensity based watershed
	- Distance map based watershed
- Machine learning based image segmentation
	

## Notes

- Running this workshop it is useful to fine-tune what exactly is taught in the two parts, in order to maximise the overlap of bioimage analysis concepts.
- ImageJ macro programming is on purpose not taught, because it would dilute the teaching of image analysis concepts with (very distracting) programming tasks.
 
