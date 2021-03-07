import sys
import os
from PIL import Image

#grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

print(path, directory)

#check if new exists, if not creat it
if not os.path.exists(directory):
    os.makedirs(directory)

#loop through Pokedex and save to new folder
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]  #removing .jpg from image names
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
  # convert to png 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')


#######
#######

#### Aditional tools: PDFs, watermarks, emails, security, hackers, passwords, APIs, twitter,
#### SMS
