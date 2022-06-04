#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip,sys
text = pyperclip.paste()
print("pasted text")
print(text)
delimiter = sys.argv[1]
print('my delimiter:' + delimiter)
# TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = delimiter + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print("modifed text")
print(text)
