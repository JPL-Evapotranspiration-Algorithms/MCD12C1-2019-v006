# MODIS/Terra+Aqua Land Cover Type CMG Yearly L3 Global 0.05 Deg 2019 Collection 6 Dataset Python Tool

This package generates rasters of the MODIS/Terra+Aqua Land Cover Type CMG Yearly L3 Global 0.05 Deg (MCD12C1) 2019 global composite collection 6 dataset, as used in ECOSTRESS Collection 2.

[Gregory H. Halverson](https://github.com/gregory-halverson-jpl) (they/them)<br>
[gregory.h.halverson@jpl.nasa.gov](mailto:gregory.h.halverson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 329G

## Installation

```
pip install MCD12C1-2019-v006
```

## Usage

```
from MCD12C1_2019_v006 import load_MCD12C1_raster

IGBP = load_MCD12C1_raster()
```

## References

- **NASA LP DAAC**. (2015). *MCD12C1 MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG*. NASA LP DAAC. https://doi.org/10.5067/MODIS/MCD12C1.006
- **Friedl, M., & Sulla-Menashe, D.** (2015). *MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG*. NASA LP DAAC. https://doi.org/10.5067/MODIS/MCD12C1.006
