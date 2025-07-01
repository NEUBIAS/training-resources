---
title:     Bioimage Analysis Training Resources
layout:    page
permalink: /index.html
---

<br>

This resource consists of a collection of **[training modules](all-modules)** that have been used to teach **[a number of courses](https://github.com/NEUBIAS/training-resources/tree/master/courses)**.

Each module can be tought in 30-45 min and covers a specific aspect of image analysis. Links to prerequisite and suggestions what could be tought next are give for each module. This provides trainers guidance on how to combine modules into a longer workshop. See also the **[module dependencies network](#module_network)**.

The modules are meant to be taught hands-on, i.e. following the teacher's guidance, students execute the relevant steps in an image analysis software on their computers. The modules provide those steps for several major image analysis platforms, such as ImageJ GUI, ImageJ Macro, Python and Galaxy. Please see our **[teaching tips](TEACHING_TIPS.md)**.

We are a **[community of developers and trainers](https://github.com/NEUBIAS/training-resources/graphs/contributors)** and we welcome any kind of collaboration! Please see our **[contributors guide](CONTRIBUTING.md)** and get in touch by **[writing an issue](https://github.com/NEUBIAS/training-resources/issues)**.

To get a sense for how this material may be used we compiled a selection of consolidated courses:

<div class="course-cards">
  <div class="course-card">
    <div class="course-icon"><i class="fas fa-eye"></i></div>
    <h4><a href="basic-image-inspection-course">Basic Bioimage Inspection</a></h4>
    <p>Learn to inspect your images and visualize your data.</p>
    <div class="course-meta">
      <span class="course-modules">6 modules</span>
      <span class="course-duration">4.5 hours</span>
      <span class="course-credits">0.15 CP</span>
    </div>
  </div>
  
  <div class="course-card">
    <div class="course-icon"><i class="fas fa-file-image"></i></div>
    <h4><a href="image-data-formats-course">Image Data Formats</a></h4>
    <p>Learn how to open and handle different image data formats.</p>
    <div class="course-meta">
      <span class="course-modules">5 modules</span>
      <span class="course-duration">3.75 hours</span>
      <span class="course-credits">0.125 CP</span>
    </div>
  </div>
  
  <div class="course-card">
    <div class="course-icon"><i class="fas fa-microscope"></i></div>
    <h4><a href="basic-image-analysis-course">Basic Bioimage Analysis</a></h4>
    <p>Learn essential concepts of image analysis, such as segmentation, intensity measurements, and filtering.</p>
    <div class="course-meta">
      <span class="course-modules">12 modules</span>
      <span class="course-duration">9 hours</span>
      <span class="course-credits">0.3 CP</span>
    </div>
  </div>

  <div class="course-card">
    <div class="course-icon"><i class="fas fa-tasks"></i></div>
    <h4><a href="basic-batch-analysis-course">Basic Batch Analysis</a></h4>
    <p>Learn how to automatically process image analysis tasks on multiple images.</p>
    <div class="course-meta">
      <span class="course-modules">5 modules</span>
      <span class="course-duration">3.75 hours</span>
      <span class="course-credits">0.125 CP</span>
    </div>
  </div>
  
  <div class="course-card">
    <div class="course-icon"><i class="fas fa-cloud"></i></div>
    <h4><a href="cloud-based-analysis-course">Cloud Based Bioimage Analysis</a></h4>
    <p>Learn about executing bioimage analysis on remote compute resources.</p>
    <div class="course-meta">
      <span class="course-modules">2 modules</span>
      <span class="course-duration">1.5 hours</span>
      <span class="course-credits">0.05 CP</span>
    </div>
  </div>
  
  <div class="course-card">
    <div class="course-icon"><i class="fas fa-bolt"></i></div>
    <h4><a href="batch-analysis-essentials-crash-course">Bioimage Batch Analysis Essentials</a></h4>
    <p>Crash course to learn the essentials of how to devise a basic image analysis workflow and how automatically apply it on multiple images.</p>
    <div class="course-meta">
      <span class="course-modules">2 modules</span>
      <span class="course-duration">3 hours</span>
      <span class="course-credits">0.1 CP</span>
    </div>
  </div>
</div>
<div class="course-cards">
<div class="course-card">
<h4 id="module_network"><a href="#module_network">Module dependecies network</a></h4>
<p>Prerequiste dependencies between modules. <strong>Click</strong> on a module to highlight all his prerequisites. <strong>Ctrl-Click</strong> on a module to open a module in a new window/tab. <strong>Shift-Click</strong> to open a module in this subwindow.</p>
<iframe src="./cytoscape/cytoscape_module_network.html" width="100%" height="800px" style="border:1px solid #ccc;"></iframe>
</div>
</div>

<style>
.course-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 30px 0;
}

.course-card {
  flex: 1 1 300px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: #fff;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.15);
}

.course-icon {
  font-size: 2em;
  color: #0366d6;
  margin-bottom: 15px;
}

.course-card h4 {
  margin-top: 0;
  font-size: 1.3em;
}

.course-card p {
  color: #555;
  margin-bottom: 20px;
}

.course-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  font-size: 0.9em;
  border-top: 1px solid #eee;
  padding-top: 15px;
}

.course-meta span {
  display: inline-flex;
  align-items: center;
  color: #666;
}

.course-modules::before {
  content: "📚";
  margin-right: 5px;
}

.course-duration::before {
  content: "⏱️";
  margin-right: 5px;
}

.course-credits::before {
  content: "🏆";
  margin-right: 5px;
}
</style>

<br><br><br>

{% include links.md %}
