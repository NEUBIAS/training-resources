run("Gaussian Blur...", "sigma=10");
run("Find Maxima...", "noise=50 output=[Segmented Particles]");
run("Analyze Particles...", "exclude add");