# Lato v2.0 for Google Fonts
by Lukasz Dziedzic with Adam Twardoch, Botio Nikoltchev and Marc Foley

This repository hot fixes the binary sources for [Lato v2.0](http://www.latofonts.com/2014/02/27/lato-2-0-released/)

## Changes from source
1. Change font names to fit within Google Font's api. We can only have weights from Thin to Black.
2. Recalculate win Ascent and win Descent
3. Enable OS/2 UseTypoMetrics flag


## Building fonts
```
$ cd build
$ sh build.sh
```

## Dependencies
[FontTools](https://github.com/fonttools/fonttools)
[Font Bakery](https://github.com/googlefonts/fontbakery)