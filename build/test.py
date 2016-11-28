import unittest
import logging
import os
import sys
from fontTools.ttLib import TTFont


class FontSetup(unittest.TestCase):

    def setUp(self):
        self.src_fonts = [f for f in os.listdir('../src') if 'ttf' in f]
        self.src_fonts = {f: TTFont(os.path.join('../src', f)) for f in self.src_fonts}

        self.new_fonts = [f for f in os.listdir('../fonts') if 'ttf' in f]
        self.new_fonts = {f: TTFont(os.path.join('../fonts', f)) for f in self.new_fonts}


class NameComparison(FontSetup):
    """
    Test new font names match the src font names, apart from the unique ID.
    Unique ID is created from scratch using scema based on Glyphsapp
    """
    def test_names(self):
        for font in self.new_fonts:
            if font in self.src_fonts:
                for i, name in enumerate(self.new_fonts[font]['name'].names):
                    if name.nameID is not 3:  # Ignore uniqueID
                        # Test all other name field match the source fonts
                        src_name = str(self.src_fonts[font]['name'].names[i])
                        new_name = str(self.new_fonts[font]['name'].names[i])
                        self.assertEqual(src_name, new_name)


class OS2Comparison(FontSetup):
    """
    Test the OS/2 table has the correct values
    """
    def test_os2_fsselection(self):
        '''Check UseTypoMetrics has been enabled'''
        for font in self.new_fonts:
            if font in self.src_fonts:
                # fsselection +128 because we have enabled UseTypoMetrics
                self.assertEqual(self.src_fonts[font]['OS/2'].fsSelection + 128,
                                 self.new_fonts[font]['OS/2'].fsSelection)

    def test_os2_winascent_windescent(self):
        for font in self.new_fonts:
            if font in self.src_fonts:
                self.assertNotEqual(self.src_fonts[font]['OS/2'].usWinAscent,
                                    self.new_fonts[font]['OS/2'].usWinAscent)
                self.assertNotEqual(self.src_fonts[font]['OS/2'].usWinDescent,
                                    self.new_fonts[font]['OS/2'].usWinDescent)

    def test_os2_linegap(self):
        """Should be 0"""
        for font in self.new_fonts:
            if font in self.src_fonts:
                self.assertEqual(0,
                                 self.new_fonts[font]['OS/2'].sTypoLineGap)

    def test_os2_ascender_descender(self):
        """OS/2 Ascender and Descender should equal hhea values"""
        for font in self.new_fonts:
            if font in self.src_fonts:
                self.assertEqual(self.new_fonts[font]['hhea'].ascent,
                                 self.new_fonts[font]['OS/2'].sTypoAscender)
                self.assertEqual(self.new_fonts[font]['hhea'].descent,
                                 self.new_fonts[font]['OS/2'].sTypoDescender)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("NameComparison.test_names").setLevel(logging.DEBUG)
    unittest.main()
