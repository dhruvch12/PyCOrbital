#include <cmath>

// Expose the function to C/Python
extern "C" {
    // Calculates a 2D Gaussian: e^(-alpha * (x^2 + y^2))
    void compute_gaussian_2d(double* x, double* y, double* out, int size, double alpha) {
        for(int i = 0; i < size; i++) {
            out[i] = std::exp(-alpha * ((x[i] * x[i]) + (y[i] * y[i])));
        }
    }
}