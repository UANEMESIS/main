import random
import io
import base64
import tkinter as tk
from urllib.request import urlopen

main_dict = {"Arcana" : "https://i.gyazo.com/2041e4b1f99df90aea57949901bf5ac2.png", "Common set" : "https://i.gyazo.com/a6fc402a72c3bc5c96afe8d499f7b485.png",
			"Rare set" : "https://i.gyazo.com/91bb3f7d1f6dc3002d0b43c6c158dd3f.png", "Mystic set" : "https://i.gyazo.com/20acb42a4d4359c5fd01839268a1c5f9.png",
			"Ancient chest" : "https://i.gyazo.com/2d276d26e4312716b0a83a5cba0a1c53.png", "Spin again" : "https://i.gyazo.com/c4fbbcf233da4e82b3c90edd56193275.png"
			}
#url = "https://i.gyazo.com/e1dd9c589c4ad84f096800a6e33a0ffb.png"
circle_of_rylai_items = ['Arcana', 'Common set', 'Rare set', 'Mystic set', 'Ancient chest', 'Spin again'] 

list_of_chances = [0.05, 0.6, 0.4, 0.3, 0.2, 0.1]

def show_image(img_url):
	root = tk.Tk()
	root.title("display a website image")
	# a little more than width and height of image
	w = 1000
	h = 600
	x = 80
	y = 100
	# use width x height + x_offset + y_offset (no spaces!)
	root.geometry("%dx%d+%d+%d" % (w, h, x, y))
	# this GIF picture previously downloaded to tinypic.com
	image_url = img_url
	image_byt = urlopen(image_url).read()
	image_b64 = base64.encodestring(image_byt)
	photo = tk.PhotoImage(data=image_b64)
	# create a white canvas
	cv = tk.Canvas(bg='white')
	cv.pack(side='top', fill='both', expand='yes')
	# put the image on the canvas with
	# create_image(xpos, ypos, image, anchor)
	cv.create_image(10, 10, image=photo, anchor='nw')
	root.mainloop()

def randomed(a, b):
	data = random.choices(a, weights=b)
	result = ''.join(data)
	print("Выпало: " + result)
	return result 

#print(randomed(circle_of_rylai_items, list_of_chances))
show_image(main_dict[randomed(circle_of_rylai_items, list_of_chances)])

