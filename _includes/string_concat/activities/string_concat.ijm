// log message
i = 11;
n = 100;
print("Analyzing image "+i+"/"+n+"...");

// paths
tmpFolder = getDirectory("temp");
fileName = "nuclei.tif";
path = tmpFolder + File.separator + fileName;
print(path);

// escape character and special characters
print("\\"); // print("\"); will throw an error

print("\"\\\"");

print("Line 1.\nLine 2.");

print("1\t2\t3");
