open("/Users/tischi/Dropbox/Presentations_Courses/2015--Tischi--Kopenhagen/0000--PracticalImagej/data/autophagosomes/autophagosomes_raw.tif");
run("Gaussian Blur...", "sigma=10");
run("Find Maxima...", "noise=100 output=[Segmented Particles]");
run("Analyze Particles...", "size=100-Infinity exclude add");