<h4 id="act1"><a href="#act1">Photoactivate a chosen subset of cells</a></h4>

In this first experiment you stimulate a chosen group of cells once and check that exactly these cells respond. It contains all steps of a photomanipulation experiment (image, compute a mask, stimulate, image again) without a loop yet.

- Image the field and detect the cells in the nuclear marker channel
- Check in the biosensor channel that all cells are resting (bright nuclei)
- Choose about half of the cells as targets, by any criterion (position, size, or random), and build a binary stimulation mask with a spot of light on each target
- Stimulate through the stimulation channel, wait a few seconds for the pathway to respond, then image the biosensor channel again
- Check that the targeted cells, and only those, responded (dark nuclei), and quantify it by measuring the activity of every cell before and after the stimulation
- Wait with the light off and check that the response reverses

The expected result is the photoactivation figure in the module introduction, with all cells in the left half of the field as targets.

Then turn it into a closed loop, still without tracking:

- The response decays within tens of seconds, so measure the activity every few seconds and stimulate again exactly the cells whose activity has dropped below a threshold
- The loop needs no cell identities: every cycle detects and measures the cells again, and decides based only on each cell's current state
- The expected activity traces are shown in the module introduction (single pulse versus closed loop)
