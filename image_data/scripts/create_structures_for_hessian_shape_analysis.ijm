/**
 * ImageJ Macro
 * 
 * Hessian eigenvalue based structure determination.
 * Formulas inspired by: https://www.researchgate.net/publication/2388170_Multiscale_Vessel_Enhancement_Filtering
 * 
 * Required update sites:
 * - ImageScience
 * 
 * Issues:
 * - The Hessian is also doing (undesired) stuff at corners and edges; one should try whether employing the structure tensor helps...
 * 
 * Ideas:
 * - One could threshold the tubeness image and set all pixels in the membraneness image to zero that are above a threshold in the tubeness image
 * 
 */

//run("Close All");
//newImage("xyz_binary_shapes", "8-bit black", 200, 200, 20);
//setForegroundColor(255, 255, 255);
//setLineWidth(1);
//setSlice(10);

//// draw structures
//drawLine(57, 36, 32, 135);
//drawOval(52, 162, 1, 1);
//fillRect(88, 51, 85, 83);
//
//// adapt structure thickness
//run("Maximum 3D...", "x=1 y=1 z=1");

rename("image");

// hessian
run("FeatureJ Hessian", "largest middle smallest smoothing=1");

selectWindow("image largest Hessian eigenvalues");
setSlice(10);
selectWindow("image middle Hessian eigenvalues");
setSlice(10);
selectWindow("image smallest Hessian eigenvalues");
setSlice(10);

// structure
//selectWindow("image");
//run("FeatureJ Structure", "largest middle smallest smoothing=1 integration=1");
//selectWindow("image largest structure eigenvalues");
//setSlice(10);
//selectWindow("image middle structure eigenvalues");
//setSlice(10);
//selectWindow("image smallest structure eigenvalues");
//setSlice(10);

// parameters to match the intensity scale
s1 = 50;
s2 = s1*s1;

// spotiness (all EV very negative)
run("Image Expression Parser (Macro)", "expression=(A>0)*(1-exp(B/"+s1+"))*(1-exp(C/"+s1+"))*(1-exp(D/"+s1+")) a=image b=[image largest Hessian eigenvalues] c=[image middle Hessian eigenvalues] d=[image smallest Hessian eigenvalues]");
rename("spotiness");
setMinAndMax(0, 1);
setSlice(10);

// tubeness (largest EV close to zero, others very negative)
run("Image Expression Parser (Macro)", "expression=(A>0)*exp(-B*B/"+s2+")*(1-exp(C/"+s1+"))*(1-exp(D/"+s1+")) a=image b=[image largest Hessian eigenvalues] c=[image middle Hessian eigenvalues] d=[image smallest Hessian eigenvalues]");
rename("tubeness");
setMinAndMax(0, 1);
setSlice(10);

// membraneness (largest and middle EV close to zero, smallest very negative)
run("Image Expression Parser (Macro)", "expression=(A>0)*exp(-B*B/"+s2+")*exp(-C*C/"+s2+")*(1-exp(D/"+s1+")) a=image b=[image largest Hessian eigenvalues] c=[image middle Hessian eigenvalues] d=[image smallest Hessian eigenvalues]");
rename("membraneness");
setMinAndMax(0, 1);
setSlice(10);
