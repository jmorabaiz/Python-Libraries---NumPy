import numpy as np

a = np.arange(12, 30, 3)
b = np.reshape(a, (2, 3))  # TODO

if __name__ == "__main__":
    print(a)
    print('shape : ', a.shape)
    print('\nAfter reshaping : ')
    print(b)
    print('shape : ', b.shape)
