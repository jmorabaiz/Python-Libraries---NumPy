import numpy as np

data = 'somedata.csv'
arr = np.genfromtxt(data, delimiter=',', skip_header=3)

if __name__ == '__main__':
    print(arr.shape)
    print(arr.dtype)
    np.set_printoptions(precision=10, suppress=True)
    print(arr[:10])
    np.savetxt('test.out', arr[:10], delimiter=',')  # Saves the first 10 lines to a new file
