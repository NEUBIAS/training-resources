# Teaching tips

The material in this repository can be used in various ways. We have used as it pure online material, hybrid with lectures, or hands-on in person. 

The material consists of modules that explain basic concepts of bioimage analysis or more complex example workflows. 

The modules can be combined into various courses. [Here are some courses](https://github.com/NEUBIAS/training-resources/tree/master/courses) that have been taught using this material.

## Know your audience

If possible try to find out who will be your students:
* What is their background 
* Education level (PostDoc, bachelor, ...)
* Which kind of images do they typically generate (modality, instrument, ...)
* ...

## Know your teaching aims

Clarify what the aim your course is

After taking the course the participants should be able to:
* Independently open and inspect image data in Fiji
* Interact with images in napari via the napari python shell
* Record IJ-macro scripts in Fiji
* ...

## Motivate and contextualise teaching modules by workflows

To help students understand what the concepts are useful for, it is good to provide a broader context. For example, by placing the concepts within a larger workflow of image analysis. 
For example, one could:

1. Show the figure in the [nuclei shape measurement workflow](https://neubias.github.io/training-resources/workflow_segment_2d_nuclei_measure_shape/index.html) and roughly explain the steps and provide some biological context.
2. Conclude that to start implementing such an analysis workflow it is first necessary to understand how an image is represented in the computer and how to inspect it. This introduction is followed by  teaching the corresponding modules (image basics and LUTs).
3. Go back to the workflow, one is now ready to do the first step, which is fore-ground and back-ground segmentation, and then teach this module.
4. Again go back to the workflow and ...

Essentially, go back and forth between teaching modules and where we are right now in the workflow.

## Teaching a module

### Motivation

Is is good to explain why the content of this specific module is important. As mentioned above, a good way is to contextualise it in some bigger analysis workflow.

In addition, there is a short text at the beginning of each module that explains the importance. This content of this text should be communicated to the students.

### Concept

Each module should be first taught without dwelling too much on the software implementation (Fiji does it this way, python is like this and so on). The goal is that students should at least remember why you need a specific concept, when to apply it and in the best cases also how (technical part). 

We typically start with the concept map that contains the essential ideas which are independent of the software implementation. The Figure is like a slide that helps illustrate the concept. Ideally the figure should have a biological example and a if needed a technical explanation (some figures should be improved in this respect; we could also discuss whether we may want have two figures, e.g. technical concept and application examples). 

For online teaching going through the concept map and figure is an option.

For in-person teaching it can work even better to explain the concepts on a white board. In this case the module figure and concept map are only used for the teacher to check that nothing important is forgotten while teaching on the white board.

### Activities for specific analysis platforms

After this introduction we present one or several activities that illustrate the concept within the given software implementation. Each activity has a general description and several software implementation, which correspond to a solution. 

It is critical to familiarise yourself with the various activities before teaching and carefully select which activities you want to teach. Depending on the course you may teach just one or several of the activities. 

Two screens are helpful for the teacher. The teacher can move the respective window (code, GUI, browser) on the presenter screen when needed. 

## Motivate each individual module biologically

Ideally the example images for the activities in the teaching modules should be biologically relevant and motivating. Currently this is not always the case and this should be improved in the future (open for good suggestions). 

## Teach the first activity of a module click-along style (GUI activity)

Most modules contain several activities; for GUI based activities it works well if one shows the first activity slow enough such that students click-along. This ensures that one teaches slow enough and also that one does not loose students. 

## Enagage your audience

Whenever there is an opportunity **engage the participants**; it is much more fun for everyone! 

For example [this activity about image data types](https://neubias.github.io/training-resources/datatypes/index.html#explore) is quite repetetive; you could demo what needs to be done for the first image and then ask the participants: "Please open the second image on your own and inspect it: What do you find special about this image? How does it differ from the image before.

In general, look for places where you can teach a new concept by asking a question.

## Teaching code containing activity 

For a code containing activity (e.fg. skimage-napari) it is hard to perform a write-along. It can also be very dry if you exactly explain the code syntax. So ideally, one should explain just enough of the syntax or library used (for instance by referring to online documentation). The main part of the activity should concentrate on illustrating the concept.   

## Group work using the teaching material

It works well to let students do the module assessments or some of the activities on their own in very small groups (of two persons). In an online context this can be done as break-out rooms. 
A possible teaching instruction is that only one of the two students is allowed to touch the computer. This promotes interactivity and discussions.

Some module activities contain further text indications, where students can try out new features that have not been included in the solution. 

## Group work on students images

This way of group work is fun and works well in a in person context for a several day course (2-3 days). For example:

* Day 1: Students present projects connected to their research. This shoudl contain the images they generate and what they would like to measure. 
* Day 1-2: Go through essential modules and modules that may fit well with the students project. 
* Day 2-3: Pick some projects and discuss how we can solve the problems with the knowledge we have. Make groups of 2-3 people and help students to work through the projects.

## Teaching only a workflow

If you don't have much time but still want to teach something it can also be an option to only pick one of the workflows and just go through that workflow without explicitly teaching the individual modules. This will allow you to very fast get across the overall concepts but you will miss some details. 

