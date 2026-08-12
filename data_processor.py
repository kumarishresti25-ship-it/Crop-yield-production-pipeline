import numpy as np

def calculate_indices(red, nir, blue):
    """Calculates NDVI and EVI indices."""
    # NDVI = (NIR - Red) / (NIR + Red)
    ndvi = (nir - red) / (nir + red + 1e-8)
    
    # EVI = 2.5 * ((NIR - Red) / (NIR + 6 * Red - 7.5 * Blue + 1))
    evi = 2.5 * ((nir - red) / (nir + 6 * red - 7.5 * blue + 1))
    
    return ndvi, evi

def mock_satellite_data(size=64):
    """Generates mock multi-spectral data for 1000 regions."""
    # Simulating 4 bands: Blue, Green, Red, NIR
    return np.random.rand(size, size, 4)