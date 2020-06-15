class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        import numpy as np
        data = target/2
        index = np.where(np.array(nums) == data)[0]
        if len(index) == 2:
            return index
        nums_unique = np.unique(nums)
        subnums = [target-num for num in nums_unique]
        nums_subnums = np.concatenate([nums_unique, subnums])
        list = []
        for i in nums_unique:
            if np.sum(nums_subnums == i) == 2 and i!=data:
                list.append(i)
        l = np.concatenate([np.where(np.array(nums) == i)[0] for i in list])
        return np.sort(l)

if __name__ == '__main__':
    a = Solution()
    num = [0,3,-3,4,-1]
    target = -1
    t = a.twoSum(num, target)
    print(t)