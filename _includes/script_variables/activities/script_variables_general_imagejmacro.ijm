// ImageJ Macro variables general concepts
// ImageJ Macro language is typeless
// Run these commands one by one


number1; // This will create an error as number1 without = is not defined.

// Define variable symbol and initiate/assign a value
number1 = 10;
number2 = 20;


// Use of variables: e.g. store result of sum in a new variable
sumNumbers = number1 + number2;

// Display results. We are using the variable in a macro
print(sumNumbers);

// Change value of number1
number1 = 20;
print(number1); // value is different
print(sumNumbers); // value is the same as before.


// Use variables in ImageProcessing function with & operator
radiusMedian = 15
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif");
run("Duplicate...", "title=Median");
run("Median...", "radius=&radiusMedian"); // The & operator does not always work

// Other method to use variables in string function arguments is with string concatenation. See appropriate module



