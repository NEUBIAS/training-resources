Open a new script editor
1. From ImageJ GUI open a script [ File > New > Script...]
2. Choose the language IJ1 Macro
3. Define a string variable with the content `"nucleus"`
4. Define a numerical variable with the content `6`
5. Concatenate the variables to get the final string `"nucleus_6"`
6. Print the final string

> ## Solution
> ```
> // define variables
> str = "nucleus";
> num = 6;
> // concatenate
> concat = str + "_" + num;
> // print the string to the log window
> print(concat);
> ```
{: .solution}
