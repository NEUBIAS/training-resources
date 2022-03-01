run("Close All");
open("https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__noisy_two_nuclei.tif");
run("Subtract...", "value=25");
//open("/Users/tischer/Documents/training-resources/image_data/xy_8bit_binary__one_foreground_pixel.tif");
n = 1;
filter( 3 );
run("Images to Stack", "name=Stack title=[] use");
run("Scale...", "x=10 y=10 z=1.0 interpolation=None average process create");
run("Make Montage...", "columns=4 rows=1 scale=1 border=5");
setMinAndMax(1, 157);
run("In [+]");


function filter( r )
{
	rename("input");
	
	selectWindow("input");
	run("Duplicate...", "title=mean" );
	run("Mean...", "radius=" + r);
	zoom( n ) ;

//	selectWindow("input");
//	run("Duplicate...", "title=var_" + r );
//	run("Variance...", "radius=" + r);
//	zoom( n ) ;
	
//	selectWindow("input");
//	run("Duplicate...", "title=gauss" );
//	run("Gaussian Blur...", "sigma=" + r);
//	zoom( n ) ;

	selectWindow("input");
	run("Duplicate...", "title=median" );
	run("Median...", "sigma=" + r);
	zoom( n ) ;
	
	if ( r == 1 )
	{
		selectWindow("input");
		run("Duplicate...", "title=edge" );
		run("Convolve...", "text1=[-1 -1 -1\n0 0 0\n+1 +1 +1\n\n]");
		zoom( n ) ;
	}

	if ( r == 2 )
	{
		selectWindow("input");
		run("Duplicate...", "title=edge" );
		run("Convolve...", "text1=[-1 -1 -1 -1 -1\n0 0 0 0 0\n1 1 1 1 1\n\n]");
		zoom( n ) ;
	}
	
	if ( r == 3 )
	{
		selectWindow("input");
		run("Duplicate...", "title=edge" );
		run("Convolve...", "text1=[-1 -1 -1 -1 -1 -1 -1\n0 0 0 0 0 0 0\n1 1 1 1 1 1 1\n\n]");
		zoom( n ) ;
	}
	if ( r == 5 )
	{
		selectWindow("input");
		run("Duplicate...", "title=edge" );
		run("Convolve...", "text1=[-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1\n0 0 0 0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1 1 1 1\n\n]");
		zoom( n ) ;
	}

	//selectWindow("input");
	//zoom( n ) ;
}

function zoom( n ) 
{
	title = getTitle();
	run("Scale...", "x="+n+" y="+n+" interpolation=None average create");
	close(title);
	rename(title);
	//for (i = 0; i < n; i++) { run("In [+]"); }
	//run("Enhance Contrast", "saturated=1");
	//run("Apply LUT", "");
}
