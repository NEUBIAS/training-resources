<h4 id="act3"><a href="#act3">Exercise: assemble the cells into a letter</a></h4>

In the previous activities you steered all cells in a fixed direction. Now use the same feedback loop to make the cells **assemble into a target shape**, a letter of your choice. The exercise is modelled after the letter-assembly experiments of Hinderling et al. (2025), where we guided fibroblasts into letter-shaped patterns over several days. This is an open design problem: there is no single correct solution, and iterating toward one that works is the point of the exercise.

- Create a binary target image of a letter and display it on top of a snapped image
- Segment the cells. Tip: as cells crowd together on the letter, their bodies touch and merge under a simple threshold. Segment the *nuclei* instead: they stay separated because cells collide before their nuclei can touch, which is also why real workflows often segment nuclei rather than cell bodies
- Design a decision rule that steers each cell toward the letter, and run it in the feedback loop until the letter forms
- Quantify success. Two candidate metrics; which is fairer, and why?
  - fraction of target pixels covered by cells
  - fraction of cells whose centroid is on the target

With a working strategy, the population assembles into a clearly legible letter; perfect filling is impossible, see the questions below:

![expected letter assembly](/training-resources/figures/smart_microscopy_photomanipulation_exercise_letter_expected.png)

The implementation tab below provides the setup, a ladder of hints (read them one at a time, only when stuck), and a validated reference solution.

Going further (optional):

- Why can pixel coverage never reach 100%, even when most cells are on the letter? Think about the minimal distance between two cells, then look at the sharp corners of the letter, where crowding is worst
- Pick a letter with disconnected parts or enclosed holes ("i", "O"). Which parts of your strategy break, and why?
- Log your metric every cycle and plot it over time. Where does the strategy spend most of its time: recruiting distant cells, or resolving traffic jams?
- Make the rules state-dependent: once most positions are filled, switch to a "maintenance mode" that pushes surplus cells away from the letter so they stop crowding its boundary
