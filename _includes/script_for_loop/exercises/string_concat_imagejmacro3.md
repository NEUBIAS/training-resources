Create a macro that concatenates a path using file.separator command

1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Define `variable1` as a string representing a file path, for example `"C:/Users/A/Desktop/Repo"` in mac os
1. Define `variable2` as a string representing a file name example `"blobs.tiff"`
1. Concatenate the variables to get a new string (`variable3`) representing file path. you need to use File.separator for this
1. print variable3
1. Run the macro to see the fill file path

> ## Solution
> ```
> // Defining variables. In  a real image analysis case, software can ask for the input from the user. 
> // This way the user will navigate to and select the folder or the file.
> // The path or file name is then automatically stored inside variables.
> variable1 = "C:/Users/A/Desktop/Repo";
> variable2 = "blobs.tiff";
> // concatenating variables, adding the file separator in the middle
> variable3 = variable1 + File.separator + variable2;
> // print the full path
> print(variable3);
> ```
{: .solution}
