# Raster tools for Python (RasPy)

An ongoing collection of simple yet useful routines for working with raster data in python.

### Included

+ Functions to be loaded into a python session ([raspy.py](raspy.py)), and;
+ Miscellaneous python-based command line tools ([misc_clt](misc_clt)).

### Requirements

+ Python ≥3.6.9
+ GDAL python bindings ≥2.2.3
+ NumPy ≥1.16.4 

### Installing

To install, clone repository and add the following lines to your `~/.bash_profile` (or `~/.bashrc`):
```
export PYTHONPATH=/path_to_repo/raspy:$PYTHONPATH
export PATH=/path_to_repo/raspy/misc_clt:$PATH
```
Replace `/path_to_repo/` with the location of the repository clone. Note, the first line will allow you to load the functions into your python session and the second line will allow you to call tools in the `misc_clt` subdirectory from the command line.

### Author

Seth Gorelik (2020) unless otherwise stated.
