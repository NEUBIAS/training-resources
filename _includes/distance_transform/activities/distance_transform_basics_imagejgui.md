### Load and presettings
* open [xy_8bit_binary__dist_trafo_a.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_labels__dist_trafo_a/xy_8bit_binary__dist_trafo_a.tif)
* **[Image > Rename]** 
    * "binary"    
*  **[Process > Binary > Options...]**, this sets the binary convention
    * `[x] black`

### Distance map using default ImageJ distance transform
* **[Image > Duplicate...]**
  * `Title: "Distance Map"`
* **[Process › Binary › Distance Map]**, note that the resulting image is 8-bit

* Select the `binary` window
* **[Image > Duplicate...]**
  * `Title: "inverted"`
* **[Edit > Invert]**
* **[Image > Duplicate...]**
  * `Title: "Distance Map inverted"`
* **[Process › Binary › Distance Map]**, discuss the results and how far away pixels have always a value 255!

### Distance map using MorphoLibJ
* Select window `inverted`
* **[Plugins › MorphoLibJ › Binary Images › Chamfer Distance Map]**
  * Discuss the menu and the fact that there are different options for the metric. 
  * Preview the different distances and how you get unexpected values for certain distances
  * Run the distance transform with following options
  * `Distances: Borgefors (3,4)`
  * `Output Type: 16 bits`
  * `[x] Normalize weights`
* **[Image > Rename]** 
    * "Borgefors" 
* **[Plugins › MorphoLibJ › Binary Images › Chamfer Distance Map]**
  * Discuss the menu and the fact that there are different options for the metric. 
  * Preview the different distances and how you get unexpected values for certain distances
  * Run the distance transform with following options
  * `Distances: Chessknight (5,7,11)`
  * `Output Type: 16 bits`
  * `[x] Normalize weights`
* **[Image > Rename]** 
    * "Chessknight"  
* Discuss the obtained values