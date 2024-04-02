import numpy as np  # Importing the numpy library
from typing import Tuple  # Importing the Tuple type from the typing module

def _pad_1d(inp: np.ndarray, num: int) -> np.ndarray:
    z = np.zeros(num)  # Creating an array of zeros with length 'num'
    return np.concatenate([z, inp, z])  # Concatenating the zero array, 'inp', and another zero array

def conv_1d(inp: np.ndarray, param: np.ndarray) -> np.ndarray:
    def assert_dim(arr: np.ndarray, dim: int) -> None:
        assert arr.ndim == dim, f"Expected array with dimension {dim}, but got array with dimension {arr.ndim}."

    def assert_same_shape(arr1: np.ndarray, arr2: np.ndarray) -> None:
        assert arr1.shape == arr2.shape, f"Expected arrays with same shape, but got arrays with shapes {arr1.shape} and {arr2.shape}."

    assert_dim(inp, 1)  # Asserting that 'inp' has dimension 1
    assert_dim(param, 1)  # Asserting that 'param' has dimension 1

    param_len = param.shape[0]  # Getting the length of 'param'
    param_mid = param_len // 2  # Calculating the midpoint of 'param_len'
    input_pad = _pad_1d(inp, param_mid)  # Padding 'inp' with zeros using '_pad_1d' function

    out = np.zeros(inp.shape)  # Creating an array of zeros with the same shape as 'inp'

    for o in range(out.shape[0]):  # Looping over the elements of 'out'
        for p in range(param_len):  # Looping over the elements of 'param'
            out[o] += param[p] * input_pad[o+p]  # Performing the convolution operation

    assert_same_shape(inp, out)  # Asserting that 'inp' and 'out' have the same shape
    return out  # Returning the convolution result

def conv_1d_sum(inp: np.ndarray, param: np.ndarray) -> np.ndarray:
    out = conv_1d(inp, param)  # Performing the 1D convolution
    return np.sum(out)  # Returning the sum of the convolution result

input_1d = np.array([1, 2, 3, 4, 5])  # Creating a 1D input array
input_1d_2 = np.array([1, 2, 3, 4, 6])  # Creating another 1D input array
param_1d = np.array([1, 1, 1])  # Creating a 1D parameter array

print(conv_1d_sum(input_1d, param_1d))  # Printing the sum of the convolution result for 'input_1d' and 'param_1d'
print(conv_1d_sum(input_1d_2, param_1d))  # Printing the sum of the convolution result for 'input_1d_2' and 'param_1d'
