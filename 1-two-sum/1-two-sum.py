class Solution(object):
    def twoSum(self, nums, target):
        I = []
        R = 0
        for i in range(R, len(nums) - 1):
            for j in range(R + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    I.append(i)
                    I.append(j)
                    break
            R += 1
        return I
        