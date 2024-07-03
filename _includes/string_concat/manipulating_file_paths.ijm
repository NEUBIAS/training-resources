// manipulating file paths
tmpFolder = getDirectory("temp");
print(tmpFolder);
fileName = "nuclei.tif";
path = tmpFolder + fileName;
print(path);

// Let's create a file name for a label image derived from the nuclei.tif
// such the file name will be nuclei_labels.tif.
filenameWithoutExtension = File.getNameWithoutExtension(path);
print(filenameWithoutExtension)
labelsPath = tmpFolder + filenameWithoutExtension + "_labels.tif";
print(labelsPath);

// Now we want to create a file name for a .csv file, that shares the
// file name up to the extension.
csvPath = tmpFolder + filenameWithoutExtension + ".csv";
print(csvPath);
