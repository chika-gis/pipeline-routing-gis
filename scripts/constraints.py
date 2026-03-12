# constraints.py
# Converted from Raster Calculator expressions to valid Python for ArcGIS Pro

import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# ---------------------------------------------------------
# Example 1: Con(IsNull("%CostSurf_constraint%"), 1)
# ---------------------------------------------------------

def apply_costsurf_constraint(costsurf):
    """
    Returns 1 where the input raster is NULL.
    """
    return Con(IsNull(costsurf), 1)


# ---------------------------------------------------------
# Example 2:
# Con(("%Reclass_LandSlides%" == 1) | ("%Reclass_AONB%" == 1), 1, 0)
# ---------------------------------------------------------

def landslide_aonb_constraint(landslides, aonb):
    """
    Returns 1 where either raster equals 1, else 0.
    """
    return Con((landslides == 1) | (aonb == 1), 1, 0)


# ---------------------------------------------------------
# Example 3: !Shape_Length! / 1000
# (This is normally a field calculator expression)
# ---------------------------------------------------------

def length_km(shape_length):
    """
    Converts length (meters) to kilometers.
    """
    return shape_length / 1000.0


# ---------------------------------------------------------
# Example 4: Python function from ModelBuilder
# ---------------------------------------------------------

def pop(distance):
    """
    Returns distance unless None, then returns 50.
    """
    if distance is None:
        return 50
    return distance


# ---------------------------------------------------------
# Example usage (uncomment and modify paths to run)
# ---------------------------------------------------------
# cost_raster = Raster(r"path_to_costsurf.tif")
# landslides_raster = Raster(r"path_to_landslides.tif")
# aonb_raster = Raster(r"path_to_aonb.tif")

# out1 = apply_costsurf_constraint(cost_raster)
# out1.save("cost_constraint.tif")

# out2 = landslide_aonb_constraint(landslides_raster, aonb_raster)
# out2.save("landslide_aonb_constraint.tif")
