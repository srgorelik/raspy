#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------------
#
# uncompressed_size.py
#
"""Print the uncompressed estimated file size of a compressed GeoTIFF dataset (in a human-readable string)."""
#
# Usage:
#   ./uncompressed_size.py <src_dataset>
#
# ------------------------------------------------------------------------------------------

import argparse
from raspy import *

def human_readable_size(size, decimal_places = 2):
	"""Returns a human-readable string representation of bytes. Credit: https://stackoverflow.com/a/43690506/9118975"""
	for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
		if size < 1024.0 or unit == 'PB':
			break
		size /= 1024.0
	return f"{size:.{decimal_places}f} {unit}"

def get_unc_size(f):
	num_cols, num_rows, num_bands = get_dims(f)
	dtype = get_dtype(f)
	bit_depth = dtype_bit_depth(dtype)
	size_bytes = num_bands * num_rows * num_cols * (bit_depth / 8)
	print(human_readable_size(size_bytes), flush = True)

def main():
	usage = '%(prog)s <src_dataset>'
	parser = argparse.ArgumentParser(usage = usage, description = __doc__, add_help = True)
	parser.add_argument('src', metavar = 'src_dataset', type = str, nargs = 1, help = 'the source dataset file name')
	args_dict = vars(parser.parse_args())
	src_file = args_dict['src'][0]
	if not os.path.isfile(src_file): 
		parser.exit(status = 2, message = 'Error: {} does not exist.\n'.format(src_file))
	else:
		get_unc_size(src_file)

if __name__ == '__main__':
	main()
