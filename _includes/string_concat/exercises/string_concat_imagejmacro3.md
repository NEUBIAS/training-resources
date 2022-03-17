Create a macro that concatenates a path using file.separator command

1. [ File › Open Samples › Blobs ]
1. Save the image onto the Desktop of your computer
1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Define `folder` as a string variable pointing to **your** computer's desktop folder (it should be something like `"C:/Users/Desktop"` or `"/Users/Deskop"`)
1. Define `fileName` as a string representing a file name of the image that you just saved (it should be something like `"blobs.tiff"`)
1. Concatenate the variables to get a new string (`filePath`) representing the full file path (`folder + File.Separator + fileName`). 
1. Print the `filePath` variable
1. Also just print `File.separator` to see what's going on
1. Run the macro

> ## Solution
> ```
> // define the variables
> folder = "/Users/Desktop/"; // <= This must be replaced!
> fileName = "blobs.tiff"; // <= Maybe ".tif" for you?
> // concatenating, adding the file separator in the middle
> filePath = folder + File.separator + fileName;
> // print
> print(File.separator);
> print(filePath);
> ```
{: .solution}
