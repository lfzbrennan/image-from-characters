import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import run
import argparse
import sys

##################
'''
pooling = False
pooling_rate = .4. 		# only if pooling
extended = False 		# letters2 vs letters
n_characters = 50 		# width by # of characters
in_file = "./image.jpg"	# input file
block_size = 20			
out_file = "./out.jpg"	# out file
verbose = True
display = False
'''
##################

def filter(snippet, n_pool):
	mapping = {}
	for i in range(len(snippet)):
		for j in range(len(snippet)):
			mapping[(i, j)] = snippet[i, j]
	sort_map = {k: v for k, v in sorted(mapping.items(), key=lambda item: item[1], reverse=True)}
	count = 0
	for item in sort_map:
		snippet[item[0], item[1]] = 255
		count += 1
		if count == n_pool:
			break


def best_match(snippet, letter_snippets):
	if pooling:
		filter(snippet, n_pool)
	best_diff = np.sum(np.abs(letter_snippets['|'] - snippet))
	best_letter = '|'
	best_array = letter_snippets['|']

	for key in letter_snippets:
		value = letter_snippets[key]
		diff = np.sum(np.abs(value - snippet))
		if diff < best_diff:
			best_diff = diff 
			best_letter = key
			best_array = value
	
	return best_array, best_letter

def main(args):
	global pooling, n_pool

	parser = argparse.ArgumentParser(description='Create character image from base image')
	parser.add_argument('-p', '--pooling', default=False, type=bool, help='Whether or not pooling is used in character mapping')
	parser.add_argument('-pr', '--pooling_rate', default=.4, type=float, help='Pooling rate; only if pooling is True')
	parser.add_argument('-e', '--extended', default=False, type=bool, help='Whether or not to use extended character set')
	parser.add_argument('-n', '--n_characters', default=50, type=int, help='Number of characters WxH')
	parser.add_argument('-i', '--in_file', default="./image.jpg", type=str, help='Input image to create character image from')
	parser.add_argument('-o', '--out_file', default="./out.jpg", type=str, help='Output image file')
	parser.add_argument('-b', '--block_size', default=20, type=int, help='Character block size (pixel WxH of each character image)')
	parser.add_argument('-v', '--verbose', default=True, type=bool, help='Verbose')
	parser.add_argument('-d', '--display', default=False, type=bool, help='Display output image at end')
	args = parser.parse_args()


	pooling = args.pooling
	pooling_rate = args.pooling_rate 		
	extended = args.extended		
	n_characters = args.n_characters		
	in_file = args.in_file	
	block_size = args.block_size	
	out_file = args.out_file	
	verbose = args.verbose
	display = args.display

	if extended:
		letters_file = "letters.txt"
		paths_file = "paths.txt"
	else: 
		letters_file = "letters2.txt"
		paths_file = "paths2.txt"

	image_path = in_file
	images_dir = 'icons'

	block_size = 20
	image_size = block_size * n_characters
	n_pool = block_size * block_size * pooling_rate

	################## creating letter maps

	if verbose:
		print("Creating letter maps....")

	with open(letters_file, 'r') as file:
	    data = file.read()
	    letters = [char for char in data]

	with open(paths_file, 'r') as file:
	    data = file.read()
	    paths = data.split('\n')

	letters_to_paths = {}

	for i in range(len(letters)):
		letters_to_paths[letters[i]] = paths[i]

	letters_to_array = {}

	for key in letters_to_paths:
		value = letters_to_paths[key]
		image = cv2.imread(os.path.join(images_dir, value), cv2.IMREAD_UNCHANGED)
		letters_to_array[key] = image

	##################

	################## setting up output and edge detected image

	if verbose:
		print("Edging images...")

	out = np.zeros((image_size, image_size))

	image = run.edge_image(image_path)
	image = cv2.resize(image, (image_size, image_size))

	out_string = ""

	##################

	################## create snippet for each block

	if verbose:
		print("Creating new image...")

	for i in range(0, image_size, block_size):
		for j in range(0, image_size, block_size):
			snippet = image[i: i+block_size, j:j+block_size]

			out_snippet, cur_letter = best_match(snippet, letters_to_array)
			out[i: i+block_size, j:j+block_size] = out_snippet
			out_string += cur_letter


		out_string += "\n"

	if verbose:
		print(out_string)
		print("Writing...")

	cv2.imwrite(out_file, out)

	if display:
		plt.imshow(out, cmap='gray')
		plt.show()

	if verbose:
		print("Done")

if __name__ == "__main__":
    from sys import argv

    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()