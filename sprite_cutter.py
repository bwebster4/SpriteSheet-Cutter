import Image
import math
import os

# Source:
# http://stackoverflow.com/questions/6059217/cutting-one-image-into-multiple-images-using-the-python-image-library

def slice(image_path, out_name, out_dir, slice_size, padding):
	img = Image.open(image_path)
	width, height = img.size

	print width
	print height

	upper = 0
	left = 0

	count = 0
	while left < width:
		while upper < height:
			# If the bottom and right of the cropping box overruns the image.
			if upper + slice_size > height and left + slice_size > width:
				bbox = (left, upper, width, height)
            # If the right of the cropping box overruns the image
			elif left + slice_size > width:
				bbox = (left, upper, width, upper + slice_size)
            # If the bottom of the cropping box overruns the image
			elif (upper + slice_size > height):
				bbox = (left, upper, left + slice_size, height)
            # If the entire cropping box is inside the image,
            # proceed normally.
			else:
				bbox = (left, upper, left + slice_size, upper + slice_size)

			working_slice = img.crop(bbox)
			print count
			if working_slice.getbbox():
				working_slice.save(os.path.join(out_dir, out_name + '_' + str(count) + '.png'))

				upper += slice_size + padding
				count = count + 1
		left += slice_size + padding
		upper = 0


if __name__ == '__main__':

	image_path = input("Enter the path of the image: ")
	out_name = raw_input("Enter the output name of the image: ")
	out_dir = input("Enter the output directory of the image: ")

	slice(image_path, out_name, out_dir, 16, 1)

