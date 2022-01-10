Use "function_display_slice.ijm": and  display mean intensity values of slices without returning any values from the function.
1. Select two different slice indices of your choice .
2. Modify the function "calculateSliceMeanIntensity" in such a way that it returns nothing and displays mean intensity of each individual slice.

> ## Solution
> ```
>run("Close All"); // close all opened windows
>run("MRI Stack"); // load the example MRI image stack
>imageName = getTitle(); //get the image title
>
>//select first slice,calculate its mean intensity and display it
>selectWindow(imageName);
>sliceNumber = 5;
>calculateSliceMeanIntensity(sliceNumber);
>
>//select last slice,calculate its mean intensity and display it
>selectWindow(imageName);
>sliceNumber = 10;
>calculateSliceMeanIntensity(sliceNumber);
>
>// a function that calculates mean intensity of a specified slice in a stack and displays it
>function calculateSliceMeanIntensity(sliceNumber)
>{
>	setSlice(sliceNumber);
>	run("Duplicate...", "title=slice"+sliceNumber);
>	sliceName = "slice"+sliceNumber;
>	selectWindow(sliceName);
>	run("8-bit");
>	getStatistics(area, mean);
>	print("Slice#"+ sliceNumber + " has mean intensity: " + mean);
>}
> ```
{: .solution}
