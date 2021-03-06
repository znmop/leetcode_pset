'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
  - If S[i] == "I", then A[i] < A[i+1]
  - If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]
'''

# Time Complexity: O(n), we have to check every element of the string
# Space Complexity: O(n), we must store a list of int of len(S)

# Method: 
class Solution:
    def diStringMatch(self, S: str) -> [int]:
        N = len(S)
        low = 0
        res = []
        for i in range(len(S)):
            if i == len(S) - 1:
                if S[i] == 'I':
                    res.append(low)
                    res.append(low + 1)
                else:
                    res.append(N)
                    res.append(low)
            elif S[i] == 'I':
                res.append(low)
                low += 1
            else:
                res.append(N)
                N -= 1
        return res

# Method: create a list of integers and match corresponding indices
class Solution1:
    def diStringMatch(self, S: str) -> [int]:
        N = len(S)
        low = 0
        high = 0
        nums = [x for x in range(N+1)]
        # high = S[0]
        # end = S[N-1]
        res = []
        for c in S:
            if c == 'I':
                res.append(nums[low])
                low += 1
            else:
                res.append(N)
                N -= 1
        res.append(low)
        return res


s1 = Solution()
print(s1.diStringMatch("IDID"))