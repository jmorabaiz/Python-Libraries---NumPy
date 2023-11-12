import numpy as np

rng = np.random.default_rng()

arr = np.arange(100).reshape(5, 20)
rng.shuffle(arr)  # TODO: shuffle rows of `arr` in place
permuted_2d = rng.permuted(arr)  # TODO: now permute the elements within rows of `arr`
fully_random = rng.permuted(np.reshape(permuted_2d, 100)).reshape(5, 20)  # TODO: fully randomize the array


if __name__ == '__main__':
    print(arr)
    for i in arr:
        print(i[0], min(i))
        print(i[-1], max(i))
    print(permuted_2d)
    print(fully_random)
