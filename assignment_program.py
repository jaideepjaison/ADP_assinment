#Design and Implement the python program for Adding Bullets to Wiki Markup

import pyperclip

pyperclip.copy("hello world")

text=pyperclip.paste()

lines=text.split('\n')

for i in range(len(lines)):

lines[i]='*'+lines[i]
text='\n'.join(lines)

pyperclip.copy(text)

print(text)
