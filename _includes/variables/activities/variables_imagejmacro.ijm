// ImageJ Macro language is typeless 

// Define variable symbol and initiate/assign a value
number1 = 10;
number2 = 20;

// Use of variables. Store result of sum in a new variable
sum_of_numbers = number1 + number2; 

// Display results
print(sum_of_numbers);

// Naming conventions:
// NO SPACES ! NO SPACES ! NO SPACES !
// No capital at the start of the varible
// Use a name that allow to understand what the variable is for

// Underscore naming
welcome_message = "Welcome to this course!"

// Camel case naming
welcomeMessage = "Welcome again to this course!"

print(welcome_message);
print(welcomeMessage);

// Use variables in macro function with & operator
radius_median = 15
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif");
run("Duplicate...", "title=Median");
run("Median...", "radius=&radius_median"); // The & operator does not always work

// Use variables in macro functions with string concatenation
radius_median = 15
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_very_noisy.tif");
run("Duplicate...", "title=Median");
run("Median...", "radius=" + radius_median);




