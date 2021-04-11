run("Close All");

n = 512;

setForegroundColor(255, 255, 255);

newImage("grid", "8-bit black", n, n, 1);
drawGrid(n/50, 1);
drawGrid(n/10, 3);
run("Invert");

newImage("grid", "8-bit black", n, n, 1);
drawGrid(n/100, 1);
drawGrid(n/20, 3);
run("Invert");


function drawGrid(d, w)
{
	setLineWidth(w);
	for (x = 0; x < n; x+=d) {
		drawLine(x, 0, x, n);
	}
	for (y = 0; y < n; y+=d) {
		drawLine(0, y, n, y);
	}
}



