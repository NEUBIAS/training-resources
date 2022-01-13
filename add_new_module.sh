cp -n _modules/binarization.md _modules/$1.md
mkdir _includes/$1
mkdir _includes/$1/activities
mkdir _includes/$1/exercises
cp -n _includes/binarization/activities/binarization_imagejgui.md _includes/$1/activities/$1_imagejgui.md
cp -n _includes/binarization/exercises/binarization_imagejgui.md _includes/$1/exercises/$1_imagejgui.md

