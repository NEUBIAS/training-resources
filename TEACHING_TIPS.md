# Teaching tips

The material in this repository can be used in various ways. We have used as it pure online material, hybrid with lectures online and hands-on in  person, 
or in person.  The material consists of modules that explain basic concepts of bioimage analysis or more complex example workflows. 
The teaching of each module including one or several activities takes about 30-45 min. 

## Motivate and contextualise modules by workflow
To help students understand what the concepts are useful for, it is good to provide a broader context. For example, by placing the concepts within a larger workflow of image analysis. 
For example, one could:

1. Show the figure in the [nuclei shape measurement workflow](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) and roughly explain the steps and provide some biological context.
2. Conclude that to start implementing such an analysis workflow it is first necessary to understand how an image is represented in the computer and how to inspect it. This introduction is followed by  teaching the corresponding modules (image basics and LUTs).
3. Go back to the workflow, one is now ready to do the first step, which is fore-ground and back-ground segmentation, and then teach this module.
4. Again go back to the workflow and ...

Essentially, go back and forth between teaching modules and where we are right now in the workflow.

## Teaching workflow for a module

Each module should be first tought without dwelling too much on the software implementation (Fiji does it this way, python is like this and so on). The goal is that students should at east remember why you need a specific concept, when to apply it and in the best cases also how (techinical part). 

We typically start with the concept map that contains the essential ideas which are independent of the software implementation. The Figure is like a slide that helps illustrate the concept. Ideally the figure should have a biological example and a if needed a technical explanation. 

After this introduction we present one or several activities that illustrate the concept within the given software implementation.  


## Motivate each individual module biologically

Ideally the example images for the activities in the teaching modules should be biologically relevant and motivating. Currently this is not always the case and this should be improved in the future (open for good suggestions). 


## Teach the first activity of a module click-along style (GUI activity)

Most modules contain several activities; for GUI based activities it works well if one shows the first activity slow enough such that students click-along. This ensures that one teaches slow enough and also that one does not loose students. 

## Teach code containing activity 

For a code containing activity (e.fg. skimage-napari) it is hard to perform a write-along. It can also be very dry if you exactly explain the code syntax. So ideally, one should explain just enough of the syntax or library used (for instance by referring to online documentation). The main part of the activity should concentrate on illustrating the concept.   

## Group work using the teaching material

It works well to let students do the module assessments or some of the activities on their own in very small groups (of two persons). In an online context this can be done as break-out rooms. 
A possible teaching instruction is that only one of the two students is allowed to touch the computer. This promotes interactivity and discussions.

## Group work on students images
This way of group work is fun and works well in a in person context for a several day course (2-3 days)
Day 1: students could present their research, the images they generate and what they would like to measure. Each of this could be a small project with example images and a goal.
Day 1-2: Teach basic concepts and perform activities as above.
Day 2 or 3: Pick some projects and discuss how we can solve the problems with the knowledge we have. Make groups of 2-3 people and help students to work through the projects.

## ...

