import os
os.getcwd()
os.chdir('C:\\Users\\ALDAIR AGUIRRE\\Desktop\\Proyecto edit imagen')
from rembg import remove
from PIL import Image
input_path = 'maria-cocina.jpeg'
output_path = 'maria-solita.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)