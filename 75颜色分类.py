"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

"""


class Solution(object):
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return nums.sort()

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        i = 0
        while i <= high:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                tmp = nums[low]
                nums[low] = nums[i]
                nums[i] = tmp
                low += 1
                i += 1
            elif i<=high and nums[i] == 2:
                tmp = nums[high]
                nums[high] = nums[i]
                nums[i] = tmp
                high -= 1
        return nums


if __name__ == '__main__':
    a = Solution()
    nums = [2,0,1]
    # 002112
    # 001122
    b = a.sortColors(nums)
    print(b)