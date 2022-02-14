function zoomin(nrtimes ){
	for (i = 0; i < nrtimes; i++) {
		run("In [+]");
	}
}
run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__for_open_and_close.tif");
rename("binary");
zoomin(5);

run("8-bit");
run("Duplicate...", "title=dilate");
run("Dilate");
zoomin(5);
selectWindow("binary")
run("Duplicate...", "title=erode");
run("Erode");
zoomin(5);

selectWindow("dilate")
closing = "dilate+erode=Closing"
run("Duplicate...", "title=" + closing);
run("Erode");
zoomin(5);

selectWindow("erode")
opening = "dilate+erode=Opening"
run("Duplicate...", "title=" + opening);
run("Dilate");
zoomin(5);

run("Tile");

