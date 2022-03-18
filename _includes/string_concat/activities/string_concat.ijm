// log message
i = 11;
n = 100;
print("Analyzing image "+i+"/"+n+"...");
// paths
tmpFolder = getDirectory("temp");
fileName = "nuclei.tif";
path = tmpFolder + File.separator + fileName;
print(path);
// exploring the escape character
print("\\"); // print("\"); will throw an error

print("\"\\\"");

print("Line 1.\nLine 2.");
