Purpose is to creat a command line that does gaussian blur with a certain sigma value, for example 6 
Open a sample image
1. File > Open samples > Blobs
Open a new script editor
1. From ImageJ GUI open a script [ File > New > Script...]
2. Choose the language IJ1 Macro
3. Define variable1 as "sigma"
4. Define variable2 as a number, in this case 6
5. Concatenate the variables to get the final string (variable3), looking like this: "sigma=6"
6. run("Gaussian Blur...", variable3);
7. run the macro to see the effect on the image
8. You can change the variable 2 value and compare the effects

> ## Solution
> ```
> //defining variables
> variable1 = "sigma";
> variable2 = 6;
> //concatenating strings
> variable3 = variable1 + "=" + variable2;
> run("Gaussian Blur...", variable3);
> ```
{: .solution}
