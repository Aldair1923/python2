import imageio
filenames = ["imagenloki1.jpg","imagenloki2.jpg","imagenloki3.jpg"]
#puedes agregar cualquier tipo de imagen
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('gifloki.gif', images,'GIF',duration=1)
