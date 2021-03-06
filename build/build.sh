# Modify the Lato 2.0 family for Google Fonts. 
# Sources available here: http://www.latofonts.com/2014/02/27/lato-2-0-released/

# WARNING: Font Bakery is needed for this script to run, https://github.com/googlefonts/fontbakery

# We may also need to add symlinks for certain scripts. FB should do this by default, if not, add the following symlinks:
#
# $ ln -s /your/path/to/fontbakery/fontbakery-nametable-from-filename.py /usr/local/bin/fontbakery-nametable-from-filename.py
# $ ln -s /your/path/to/fontbakery/fontbakery-check-bbox.py /usr/local/bin/fontbakery-check-bbox.py
# $ ln -s /your/path/to/fontbakery/fontbakery-fix-vertical-metrics.py /usr/local/bin/fontbakery-fix-vertical-metrics.py
#
# Permissions may need to be changed on these symlinks as well. To do this:
# $ chmod 744 /usr/local/bin/font-bakery-script


set -e # Stop script if we have any critical errors
cp -R ../src/. ../fonts
cd ../fonts


FONTS=$(ls *.ttf)

# Rename the font filenames to fit within our GF api Thin -> Black
echo Renaming font files
python ../build/rename_font_filenames.py

# Delete old ttfs and rename .ttf.renamed -> ttf
python ../build/cleanup.py

# Since fonts have been renamed we need to reassign the variable
FONTS=$(ls *.ttf) 

echo $FONTS

# Update font tables to reflect new filenames
echo renaming font tables, based on new font filenames
fontbakery-nametable-from-filename.py $FONTS

echo tidying up font files
# change .ttf.fix -> .ttf
python ../build/cleanup.py

# get ymin, ymax for win Ascent, win Descent
echo Getting yMin and yMax
YMAX=$(fontbakery-check-bbox.py --family --extremes --csv $FONTS |  awk -F, 'NR > 1 { print $3 }')
YMIN=$(fontbakery-check-bbox.py --family --extremes --csv $FONTS |  awk -F, 'NR > 1 { print $2 }')
echo ymin is $YMIN ymax is $YMAX

# Recalc Vertical Metrics
echo Updating Vertical metrics
fontbakery-fix-vertical-metrics.py -l=0 -aw=$YMAX -dw=$YMIN -at=1974 -dt=-426 $FONTS
python ../build/cleanup.py
fontbakery-fix-vertical-metrics.py $FONTS

# Enable UseTypoMetrics
echo Enabling UseTypoMetrics flag
fontbakery-fix-fsselection.py --usetypometrics --autofix $FONTS

echo tidying up font folder
# change .ttf.fix -> .ttf
python ../build/cleanup.py


echo Done. New files in fonts directory

echo Testing new fonts
cd ../build
python test.py
