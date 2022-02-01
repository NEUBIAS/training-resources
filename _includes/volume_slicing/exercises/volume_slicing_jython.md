- Open the multidimensional image [xyz_16bit_t1-head.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_t1-head.tif).
- Reslice the image from different directions, such that you can view the image stack from the side, from the top, and from the front.
- How do you think one could see the head from 3/4 view? Tip: there is a function called ‘rotate’ in ImageJ ([Image > Transform > Rotate]).

> ## Solution
> ```
># This jython script opens the head image stack and reslices it to view it from different angles (side, top, front, and 3/4 view)
>
># import classes
>from ij import IJ
>from ij.plugin import Slicer
>
># Close other open images
>IJ.run("Close All")
>
># open head image stack
>head = IJ.openImage("http://imagej.net/images/t1-head.zip")
>head.show() # shows head from the side
>head.setTitle("Head viewed from the side")
>
># Reslice the head image stack to view the head from the top and from the side
>IJ.run(head, "Reslice [/]...", "output=1.500 start=Top") # view head from the top
>head_top = IJ.getImage()
>head_top.setTitle("Head viewed from the top")
>IJ.run(head, "Reslice [/]...", "output=1.500 start=Left rotate") # view head from the front
>head_front = IJ.getImage()
>head_front.setTitle("Head viewed from the front")
>
># Rotate the head stack that is viewed from the top and reslice to obtain 3/4 view
>head_top2 = head_top.duplicate()
>IJ.run(head_top2, "Rotate... ", "angle=45 grid=1 interpolation=None enlarge stack") # rotate the stack
>IJ.run(head_top2, "Reslice [/]...", "output=1.500 start=Top")
>head_three_quarter = IJ.getImage()
>head_three_quarter.setTitle("Head in 3/4 view")
>head_three_quarter.show()
>
>IJ.run("Tile")
> ```
{: .solution}
