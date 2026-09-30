<h4 id="act2"><a href="#act2">Drive the same microscope from code</a></h4>

Everything you just clicked is available as a function call on the same instrument. This equivalence is the foundation of microscope automation: a script is not "another program", it is the same clicks issued by code.

- With the GUI still open, perform the same operations from Python and watch the GUI react: snap an image, switch the objective, switch the channel, change the exposure
- Read and change device properties from code, as in the Device Property Browser, and move the stage
- Retrieve a snapped image as a plain array and display it yourself
- Appreciate that GUI buttons and script commands issue the same control calls on the same microscope. Automation is scripted clicking, and on a real microscope the setup is identical: the GUI in front, your script behind, one shared core
