Open a new script editor
1. From ImageJ GUI open a script [ File > New > Script...]
2. Choose the language IJ1 Macro
3. Define variable 1 as "nuclei"
4. Define variable 2 as 6
5. Concatenate the variables to get the final string "nuclei_6"
6. Print the final string

> ## Solution
> ```
> //defining variables
> str1 = "nuclei";
> num1 = 6;
> //concatenating strings
> str2 = str1 + "_" + num1;
> //printing the results
> print(str2);
> ```
{: .solution}
