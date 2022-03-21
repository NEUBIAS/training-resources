1. When you try to run the code below it will issue an error. Fix the variable naming for the file path. Use  the `camelCase` naming convention.
2. Change the name of the variables `a` and `b` so that it their names are meaningful and reflect their content. Use the `camelCase` naming convention.

```javascript
run("Close All");
FilePath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif";
a = 1;
b = 2;
open(filePath);
rename("input");
run("Duplicate...", "title=tophat");
run("Top Hat...", "radius=&b");
selectWindow("input");
run("Duplicate...", "title=");
run("Variance...", "radius=&a");
```

> ## Solutions
> ```javascript
> run("Close All");
> filePath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif";
> varianceRadius = 1;
> topHatRadius = 2;
> open(filePath);
> rename("input");
> run("Duplicate...", "title=tophat");
> run("Top Hat...", "radius=&topHatRadius");
> selectWindow("input");
> run("Duplicate...", "title=variance");
> run("Variance...", "radius=&varianceRadius");
> ```
{: .solution}



