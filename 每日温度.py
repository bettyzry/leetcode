def dailyTemperatures( T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    import numpy as np
    times = np.zeros(len(T), dtype=int)
    for i in range(len(T) - 2, -1, -1):
        for j in range(i + 1, len(T)):
            if T[i] < T[j]:
                times[i] = j - i
                break
    return times


if __name__ == '__main__':
    T = [73,74,75,71,69,72,76,73]
    t = dailyTemperatures(T)
    print(t)