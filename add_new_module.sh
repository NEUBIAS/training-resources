cp -n _modules/template.md _modules/$1.md
perl -i -pe"s/template/${1}/g" _modules/$1.md
cp figures/template.png figures/$1.png
mkdir -p _includes/$1
touch _includes/$1/act01.md
touch _includes/$1/act01_imagejgui.md
touch _includes/$1/act01_python.md
