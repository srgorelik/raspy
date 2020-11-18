#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------------
#
# proj4string.py
#
"""Print PROJ4 string of a Shapefile or GeoTIFF dataset."""
#
# Usage:
#   ./proj4string.py <src_dataset>
#
# ------------------------------------------------------------------------------------------

import sys, os, argparse
from osgeo import gdal, ogr, osr

def get_ext(file):
	name, ext = os.path.splitext(file)
	return ext.replace('.', '')

def prj_ext(shp_file):
	name, ext = os.path.splitext(shp_file)
	prj_file = '{}.prj'.format(name)
	return prj_file

def get_shp_prj(prj_file):
	prj_src = open(prj_file, 'r')
	prj_txt = prj_src.read()
	srs = osr.SpatialReference()
	srs.ImportFromESRI([prj_txt])
	prj4str = srs.ExportToProj4().rstrip()
	prj4str = "'{}'".format(prj4str)
	print(prj4str, flush = True)

def get_ras_prj(ras_file):
	src = gdal.Open(ras_file)
	src_wkt = src.GetProjection()
	prj4str = osr.SpatialReference(wkt = src_wkt).ExportToProj4().rstrip()
	prj4str = "'{}'".format(prj4str)
	print(prj4str, flush = True)
	src = None

def main():

	usage = '%(prog)s <src_dataset>'
	parser = argparse.ArgumentParser(usage = usage, description = __doc__, add_help = True)
	parser.add_argument('src', metavar = 'src_dataset', type = str, nargs = 1, help = 'the source dataset file name')

	args_dict = vars(parser.parse_args())
	src_file = args_dict['src'][0]

	if not os.path.isfile(src_file): 
		parser.exit(status = 2, message = 'Error: {} does not exist.\n'.format(src_file))
		
	elif get_ext(src_file) == 'shp':
		prj_file = prj_ext(src_file)
		if os.path.isfile(prj_file):
			get_shp_prj(prj_file)
		else:
			parser.exit(status = 2, message = 'Error: .prj file for {} does not exist.\n'.format(os.path.basename(src_file)))
		
	elif get_ext(src_file) == 'tif':
		get_ras_prj(src_file)
		
	else:
		parser.exit(status = 2, message = 'Error: src_dataset must be a Shapefile or GeoTIFF.\n')

if __name__ == '__main__':
	main()
