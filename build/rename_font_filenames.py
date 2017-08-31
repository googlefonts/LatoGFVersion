import os

REMAP_FONTS = [
    ("Lato-Hairline.ttf", "Lato-Thin.ttf.renamed"),
    ("Lato-HairlineItalic.ttf", "Lato-ThinItalic.ttf.renamed"),
    ("Lato-Thin.ttf", "Lato-ExtraLight.ttf.renamed"),
    ("Lato-ThinItalic.ttf", "Lato-ExtraLightItalic.ttf.renamed"),
    ("Lato-Light.ttf", "Lato-Light.ttf.renamed"),
    ("Lato-LightItalic.ttf", "Lato-LightItalic.ttf.renamed"),
    ("Lato-Regular.ttf", "Lato-Regular.ttf.renamed"),
    ("Lato-Italic.ttf", "Lato-Italic.ttf.renamed"),
    ("Lato-Medium.ttf", "Lato-Medium.ttf.renamed"),
    ("Lato-MediumItalic.ttf", "Lato-MediumItalic.ttf.renamed"),
    ("Lato-Semibold.ttf", "Lato-SemiBold.ttf.renamed"),
    ("Lato-SemiboldItalic.ttf", "Lato-SemiBoldItalic.ttf.renamed"),
    ("Lato-Bold.ttf", "Lato-Bold.ttf.renamed"),
    ("Lato-BoldItalic.ttf", "Lato-BoldItalic.ttf.renamed"),
    ("Lato-Black.ttf", "Lato-ExtraBold.ttf.renamed"),
    ("Lato-BlackItalic.ttf", "Lato-ExtraBoldItalic.ttf.renamed"),
    ("Lato-Heavy.ttf", "Lato-Black.ttf.renamed"),
    ("Lato-HeavyItalic.ttf", "Lato-BlackItalic.ttf.renamed"),
]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print('renamed %s to %s' % (old_name, new_name))
print('Done renaming')
