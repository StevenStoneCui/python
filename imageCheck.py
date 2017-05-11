from os import listdir 
from PIL import Image
import os

for filename in listdir('./threefood/ScrambledEggWithTomato/'):
	if filename.endswith('.jpg'):
		try:
			img = Image.open('./threefood/ScrambledEggWithTomato/' + filename)
			img.verify()
			print('success:' + filename)
		except (IOError, SyntaxError) as e:
			print('fail:' + filename)
			os.remove('./threefood/ScrambledEggWithTomato/' + filename)
	else:
		print('wrong filename extension: ' + filename)
		os.remove('./threefood/ScrambledEggWithTomato/' + filename)


