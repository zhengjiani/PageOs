class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size = len(nums)
        if size < 2:
            return size

        tail = []
        for num in nums:
            # 找到大于等于 target 的第 1 个数
            l = 0
            r = len(tail)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= num:
                    r = mid
                else:
                    l = mid + 1
            if l == len(tail):
                tail.append(num)
            else:
                tail[l] = num
        return len(tail)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    result = solution.lengthOfLIS(nums)
    print(result)