## Concatenatimg folder and file names

1. [ File › Open Samples › Blobs ]
1. Save the image onto the Desktop of your computer
1. Open the script editor: [ File > New > Script...]
1. Choose the language IJ1 Macro
1. Define `folder` as a string variable pointing to **your** computer's desktop folder (it should be something like `C:\Users\Desktop` or `/Users/Deskop`)
1. If you are on Windows, watch out: In order to have `C:\Users\Desktop` you will have to write `C:\\Users\\Desktop`, because `\` is a special character that needs to be "escaped"
1. Define `fileName` as a string representing the file name of the image that you just saved (it should be something like `"blobs.tiff"`)
1. Concatenate the variables to get a new string (`filePath`) representing the full file path (`folder + File.Separator + fileName`). 
1. Use the filePath variable to add code that prints something like "Opening C:\\Users\blobs.tiff"
1. Add `open(filePath);` to open the image.
1. Run the macro

> ## Solution
> ```javascript
> // define the variables
> folder = "/Users/Desktop/"; // <= This must be replaced!
> fileName = "blobs.tiff"; // <= Be careful: There is ".tiff" and ".tif"
> // concatenating, adding the file separator in the middle
> filePath = folder + File.separator + fileName;
> // print log message
> print("Opening " + filePath);
> // open the file
> open(filePath);
> ```
{: .solution}
