#@File labelImage

// open image
run("Close All");
open(labelImage);

// perform measurements
run("Particle Analysis 3D", "volume inertia surface_0=[Crofton (13 dirs.)] euler_0=C26");

// TODO: change font size: setFont
setFont("SansSerif", 4);

for ( i = 0; i < Table.size; ++i )
{
	volume = Table.get( "Volume", i );
	x = Table.get( "Elli.Center.X", i );
	y = Table.get( "Elli.Center.Y", i );
	z = Table.get( "Elli.Center.Z", i );
	
	toUnscaled(x, y, z);

	Overlay.drawString( volume, x, y );
	Overlay.setPosition( z );	
}

Overlay.show();




