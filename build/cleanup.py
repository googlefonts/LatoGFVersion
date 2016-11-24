import re
import os


def fix_files_exist():
    for f in os.listdir('.'):
        if '.fix' in f:
            return True


if fix_files_exist():
    # deleting old ttfs
    for file in os.listdir('.'):
        if file.endswith('ttf'):
            os.remove(os.path.join('.', file))

# Rename fixed fonts to ttfs
for font in os.listdir('.'):
    font = os.path.join('.', font)
    os.rename(font, re.sub(r'.fix|.renamed', '', font))
