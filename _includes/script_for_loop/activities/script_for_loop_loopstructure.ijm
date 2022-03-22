
// Before the loop
print ("Starting the process");


// We use for loop to print the processing status of 10 images
for (i = 0; i < 10 ; i++) {
    // we are using string concatenation to make this message
    print ("Index: "+i);
}

// After processing
print("Process completed");


// Self referencing variable
counter = 1;
print("counter " + counter);
counter = counter + 1;
print("counter " + counter);
// is equivalent to
counter = 1;
print("counter " + counter);
counter++;
print("counter " + counter);

// You can also have a loop in a loop

for (j = 0; j < 10 ; j++) {

    for (i = 0; i < 10 ; i++) {
        // we are using string concatenation to make this message
        print ("Index big loop "+j + "; index small loop " + i);
    }
}

