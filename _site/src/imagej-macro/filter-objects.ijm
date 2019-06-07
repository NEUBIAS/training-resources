// TODO: add user interface for opening a label image file (https://imagej.net/Script_Parameters)
// TODO: add user interface for min and max area

run("Region Morphometry");

minArea = 0;
maxArea = 200;

// TODO: Duplicate the label image, in order not to loose the original one

for ( i = 0; i < Table.size; ++i )
{
	area = Table.get( "Area", i );
	label = Table.getString( "Label", i );

	// TODO: Add some text output to tell the user what is happening...
	if ( area < minArea || area > maxArea )
	{
		run("Replace/Remove Label(s)", "label(s)="+label+" final=0");
	}
}

// TODO (Optional): Relabel the filtered label image such that labels start from 1 and none are missing




