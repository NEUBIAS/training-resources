Fix the variable naming errors and inconsistencies, i.e. change to `camelCase` in the following code

```javascript
run("Close All");
fn = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif";
a = 1;
b = 2;
open(f);
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
> fileName = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__autophagosomes.tif";
> varianceRadius = 1;
> topHatRadius = 2;
> open(fileName);
> rename("input");
> run("Duplicate...", "title=tophat");
> run("Top Hat...", "radius=&topHatRadius");
> selectWindow("input");
> run("Duplicate...", "title=variance");
> run("Variance...", "radius=&varianceRadius");
> ```
{: .solution}



