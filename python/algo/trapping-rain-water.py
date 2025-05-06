# https://leetcode.cn/problems/trapping-rain-water


class Solution_two_pointer:
    def trap(self, height: list[int]) -> int:
        ans = 0
        _len = len(height)
        l = 0
        r = _len - 1
        l_max = 0
        r_max = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max < r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1

        return ans
