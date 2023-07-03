# bekmuxtorov.me
# https://leetcode.com/problems/buddy-strings/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            if len(s) - len(set(s)) >= 1:
                return True
            print('2-shartda')
            return False

        diff = list()
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True

        return False


s, goal = 'ab', 'ba'

solution = Solution()
print(solution.buddyStrings(s, goal))
