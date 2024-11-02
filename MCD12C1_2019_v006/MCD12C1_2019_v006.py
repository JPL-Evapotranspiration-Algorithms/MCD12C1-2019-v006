from os.path import join, abspath, dirname
import numpy as np
import rasters as rt
from rasters import Raster, RasterGeometry

def load_MCD12C1_IGBP(geometry: RasterGeometry = None) -> Raster:
    filename = join(abspath(dirname(__file__)), "MCD12C1.A2019001.006.2020220162300.tif")
    image = rt.Raster.open(filename, geometry=geometry, resampling="nearest")

    return image