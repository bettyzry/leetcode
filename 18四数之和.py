"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        执行用时：1196 ms, 在所有 Python 提交中击败了10.39%的用户
        内存消耗：12.6 MB, 在所有 Python 提交中击败了15.17%的用户
        """
        result = []
        nums.sort()  # [0,0,0,0]
        for i, num_i in enumerate(nums[:-3]):
            if i > 0 and num_i == nums[i - 1]:
                continue
            for j, num_j in enumerate(nums[i + 1:-2]):
                if j > 0 and num_j == nums[i + j]:  # [0,1,2,3,4,5,6]
                    continue
                low = i + j + 2
                high = len(nums) - 1
                while low < high:
                    if num_i + num_j + nums[low] + nums[high] == target:
                        result.append([num_i, num_j, nums[low], nums[high]])
                        while nums[high] == nums[high - 1] and high > i + j + 2:
                            high -= 1
                        high -= 1
                        while high > low > i + j + 2 and nums[low] == nums[low + 1]:
                            low += 1
                        low += 1
                    elif num_i + num_j + nums[low] + nums[high] > target:
                        while nums[high] == nums[high - 1] and high > i + j + 2:
                            high -= 1
                        high -= 1
                    elif num_i + num_j + nums[low] + nums[high] < target:
                        while high > low > i + j + 2 and nums[low] == nums[low + 1]:
                            low += 1
                        low += 1
        return result


if __name__ == '__main__':
    a = Solution()
    nums = [-4,0,-4,2,2,2,-2,-2]
    target = 7
    b = a.fourSum(nums, target)
    print(b)
