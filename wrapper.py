import ctypes
import numpy as np
import os

# 1. Load the compiled C++ library
lib_path = os.path.join(os.path.dirname(__file__), 'core_math.dll') # Change extension based on OS
c_lib = ctypes.CDLL(lib_path)

# 2. Define the exact C++ function signature for memory safety
c_lib.compute_gaussian_2d.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # x array
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # y array
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # output array
    ctypes.c_int,     # size
    ctypes.c_double   # alpha
]

# 3. Create a clean Python API for the user
def get_gaussian_surface(x_grid, y_grid, alpha=1.0):
    size = x_grid.size
    
    # Flatten grids to 1D arrays for C++ processing
    x_flat = x_grid.flatten()
    y_flat = y_grid.flatten()
    out_flat = np.zeros(size, dtype=np.float64)
    
    # Call the C++ engine
    c_lib.compute_gaussian_2d(x_flat, y_flat, out_flat, size, alpha)
    
    # Reshape back to 2D grid for Python visualization
    return out_flat.reshape(x_grid.shape)