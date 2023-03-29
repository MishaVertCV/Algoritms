class Solution:
    def removeDuplicates(nums):
        a = len(nums)
        l = list()
        x = 1
        y = nums[0]
        l.append(y)
        while x < a:
            if nums[x] > y:
                l.append(nums[x])
                y = nums[x]
            x += 1
        return l
    a = [1, 2, 2, 4, 4, 10, 10, 11]
    print(removeDuplicates(a))