class Solution(object):
    '''
    time: 100%
    space: 100%
    '''
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        import numpy
        arr = numpy.array(arr)
        arr.sort()
        if arr[0]*len(arr) > target:
            num = int(target/len(arr))
            return num if abs(num*len(arr)-target) < abs((num+1)*len(arr)-target) else num+1

        result = arr[-1]
        value = 0
        for i in range(len(arr)):
            count = sum(arr[:i+1]) + arr[i] * (len(arr) - i - 1)
            if count > target:
                for j in range(arr[i-1]+1, arr[i]+1):
                    count = sum(arr[:i]) + j * (len(arr) - i )
                    if count > target:
                        print(abs(count-target), abs(sum(arr[:i]) + (j-1) * (len(arr) - i)-target))
                        if abs(count-target) < abs(sum(arr[:i]) + (j-1) * (len(arr) - i)-target):
                            result = j
                            value = abs(count-target)
                        else:
                            result = j-1
                            value = abs(sum(arr[:i]) + (j-1) * (len(arr) - i)-target)
                        break
                result = result if value < abs(sum(arr[:i+1]) + arr[i] * (len(arr) - i - 1) - target) else arr[i-1]
                break
        return result

if __name__ == '__main__':
    a = Solution()
    arr = [40091, 2502, 74024, 53101, 60555, 33732, 23467, 40560, 32693, 13013]
    target = 78666
    b = a.findBestValue(arr, target)
    print(b)