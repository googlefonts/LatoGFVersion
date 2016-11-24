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
    Test new font names match the src font names, apart from the unique ID
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
        for font in self.new_fonts:
            if font in self.src_fonts:
                # fsselection +128 because we have enabled UseTypoMetrics
                self.assertEqual(self.src_fonts[font]['OS/2'].fsSelection + 128,
                                 self.new_fonts[font]['OS/2'].fsSelection)

    def test_os2_winascent(self):
        for font in self.new_fonts:
            if font in self.src_fonts:
                self.assertNotEqual(self.src_fonts[font]['OS/2'].usWinAscent,
                                    self.new_fonts[font]['OS/2'].usWinAscent)

    def test_os2_windescent(self):
        for font in self.new_fonts:
            if font in self.src_fonts:
                self.assertNotEqual(self.src_fonts[font]['OS/2'].usWinDescent,
                                    self.new_fonts[font]['OS/2'].usWinDescent)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("NameComparison.test_names").setLevel(logging.DEBUG)
    unittest.main()
