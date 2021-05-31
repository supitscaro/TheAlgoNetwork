from app.models import db, Problem

# Adds problems for the users to look over


def seed_problems():

    # Arrays - Easy
    problem1 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Running Sum of 1d Array',
        description='Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.',
        language="Python",
        solution='def runningSum(self, nums: List[int]) -> List[int]:\n     for i in range(1, len(nums)):\n         nums[i] += nums[i - 1]\n    return nums',
    )

    problem2 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Shuffle the Array',
        description='Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].',
        language="Python",
        solution='class Solution:\n    def shuffle(self, nums: List[int], n: int) -> List[int]:\n        temp = []\n        for i in range(n):\n            temp.append(nums[i])\n            temp.append(nums[n + i])\n        return temp',
    )

    problem3 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Number of Good Pairs',
        description='Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.',
        language="Python",
        solution='class Solution:\n    def numIdenticalPairs(self, nums: List[int]) -> int:\n        diction = dict()\n        pairs = 0\n        for num in nums:\n            if num in diction:\n                pairs += diction[num]\n                diction[num] += 1\n            else:\n                diction[num] = 1\n        return pairs',
    )

    problem4 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='How Many Numbers Are Smaller Than the Current Number',
        description='Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j\'s such that j != i and nums[j] < nums[i]. Return the answer in an array.',
        language="Python",
        solution='class Solution:\n    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:\n        sorted_nums = sorted(nums)\n        return [sorted_nums.index(num) for num in nums]',
    )

    problem5 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find N Unique Integers Sum up to Zero',
        description='Given an integer n, return any array containing n unique integers such that they add up to 0.',
        language="Python",
        solution='class Solution:\n    def sumZero(self, n):\n        return range(1 - n, n, 2)',
    )

    problem6 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Fibonacci Number',
        description='The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. Given n, calculate F(n).',
        language="Python",
        solution='class Solution:\n    def fib(self, N):\n	    if N <= 1: return N\n	    a, b = 0, 1\n	    for i in range(2, N+1):\n		    c = a + b\n		    a, b = b, c\n	    return c',
    )

    problem7 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Squares of a Sorted Array',
        description='Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.',
        language="Python",
        solution='class Solution:\n    def sortedSquares(self, A: List[int]) -> List[int]:\n        result = [None for _ in A]\n        left, right = 0, len(A) - 1\n        for index in range(len(A)-1, -1, -1):\n            if abs(A[left]) > abs(A[right]):\n                result[index] = A[left] ** 2\n                left += 1\n            else:\n                result[index] = A[right] ** 2\n                right -= 1\n        return result',
    )

    problem8 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find Common Characters',
        description='Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer. You may return the answer in any order.',
        language="Python",
        solution='class Solution:\n    def commonChars(self, A: List[str]) -> List[str]:\n        ans = []\n        d1 = Counter(A[0])\n        for i in range(1,len(A)):\n            d2 = Counter(A[i])\n            d1 = d1 & d2\n            ans = list(d1.elements())\n        return ans',
    )

    problem9 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Move Zeroes',
        description='Given an integer array nums, move all 0\'s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array',
        language="Python",
        solution='class Solution:\n    def moveZeroes(self, nums):\n        i = 0\n        for j in range(len(nums)):\n            if nums[j] != 0:\n                nums[i], nums[j] = nums[j], nums[i]\n                i += 1',
    )

    problem10 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Missing Number',
        description='Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.',
        language="Python",
        solution='class Solution:\n    def missingNumber(self, nums):\n    n = len(nums)\n        return n * (n+1) // 2 - sum(nums)',
    )

    # Arrays - Medium

    problem11 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find All Duplicates in an Array',
        description='Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.',
        language="Python",
        solution='class Solution(object):\n    def findDuplicates(self, nums):\n        result = []\n        for x in nums:\n            if nums[abs(x)-1] < 0:\n                result.append(abs(x))\n            else:\n                nums[abs(x)-1] = -1*nums[abs(x)-1]\n        return result',
    )

    problem12 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Max Area of Island',
        description='You are given an m x n binary matrix grid. An island is a group of 1\'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0',
        language="Python",
        solution='class Solution:\n    def maxAreaOfIsland(self, grid):\n        return max([self.dfs(r, c, grid) for r in range(len(grid)) for c in range(len(grid[0]))])\n    def dfs(self, r, c, grid):\n        if not (0 <= r < len(grid) and (0 <= c < len(grid[0])) and grid[r][c]):\n            return 0\n        grid[r][c] = 0\n        return 1 + sum([self.dfs(r + x[0], c + x[1], grid) for x in [(0, 1), (0, -1), (1, 0), (-1, 0)]])',
    )

    problem13 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Rotate Image',
        description='You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.',
        language="Python",
        solution='class Solution(object):\n    def transpose(self, matrix):\n        M,N = len(matrix), len(matrix[0])\n        cols = 1\n        for i in range(M):\n            for j in range(cols):\n                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n            cols += 1\n        return\n\n    def rotate(self, matrix):\n        if matrix == []:\n            return matrix\n        self.transpose(matrix)\n        for r in matrix:\n            r.reverse()\n        return',
    )

    problem14 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Product of Array Except Self',
        description='Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer',
        language="Python",
        solution='class Solution:\n    def productExceptSelf(self, nums):\n        res = [1]*len(nums)\n        lprod = 1\n        rprod = 1\n        for i in range(len(nums)):\n            res[i] *= lprod\n            lprod *= nums[i]\n            res[~i] *= rprod\n            rprod *= nums[~i]\n        return res',
    )

    problem15 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Combination Sum',
        description='Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.',
        language="Python",
        solution='class Solution(object):\n    def combinationSum(self, candidates, target):\n        ret = []\n        self.dfs(candidates, target, [], ret)\n        return ret\n\n    def dfs(self, nums, target, path, ret):\n        if target < 0:\n            return\n        if target == 0:\n            ret.append(path)\n            return\n        for i in range(len(nums)):\n            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)',
    )

    problem16 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find the Duplicate Number',
        description='Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.',
        language="Python",
        solution='class Solution(object):\n    def findDuplicate(self, nums):\n        if len(nums) == 0:\n            return 0\n        low = 1\n        high = len(nums)\n        while low < high:\n            mid = low + int((high-low)>>1)\n            count = 0\n            for x in nums:\n                if x <= mid:\n                    count = count + 1\n            if count > mid:\n                high = mid\n            else:\n                low = mid+1\n        return low',
    )

    problem17 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Container With Most Water',
        description='Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water. Notice that you may not slant the container.',
        language="Python",
        solution='class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        l = 0\n        r = len(height)-1\n        res = 0\n        while l < r:\n            area = (r - l) * min(height[l], height[r])\n            res = max(area,res)\n            if height[l]<height[r]:\n                l = l+1\n            else:\n                r = r-1\n        return res',
    )

    problem18 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Subarray Sum Equals K',
        description='Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.',
        language="Python",
        solution='class Solution:\n    def subarraySum(self, nums, k):\n        preSums = {0: 1}\n        s = 0\n        res = 0\n        for num in nums:\n            s += num\n            res += preSums.get(s - k, 0)\n            preSums[s] = preSums.get(s, 0) + 1\n        return res',
    )

    # Array - Hard
    problem19 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Trapping Rain Water',
        description='Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.',
        language="Python",
        solution='class Solution:\n    def trap(self, height: List[int]) -> int:\n        stack =[]\n        area = 0\n        for i in range(len(height)):\n            offset = 0\n            while(stack and height[i] >= height[stack[-1]]):\n                pre_i = stack.pop()\n                area += (height[pre_i]-offset) * (i-pre_i-1)\n                offset = height[pre_i]\n            if stack:\n                area += (height[i]-offset) * (i-stack[-1]-1)\n            stack.append(i)\        return area',
    )

    problem20 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='First Missing Positive',
        description='Given an unsorted integer array nums, find the smallest missing positive integer.',
        language="Python",
        solution='class Solution(object)\n:    def firstMissingPositive(self, nums):\n        N, i = len(nums), 0\n        while i < N:\n        while 1<=nums[i]<=N:\n            idx_expected = nums[i]-1\n                if nums[i] == nums[idx_expected]:\n                    break\n                nums[i], nums[idx_expected] = nums[idx_expected], nums[i]\n            i = i + 1\n        for i in range(N):\n            if nums[i] != i+1:\n                return i+1\n        return N+1',
    )

    problem21 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Median of Two Sorted Arrays',
        description='Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.',
        language="Python",
        solution='class Solution:\n    def findMedianSortedArrays(self, nums1, nums2):\n        a, b = sorted((nums1, nums2), key=len)\n        m, n = len(a), len(b)\n        after = (m + n - 1) / 2\n        lo, hi = 0, m\n        while lo < hi: \n            i = (lo + hi) / 2\n            if after-i-1 < 0 or a[i] >= b[after-i-1]:\n                hi = i\n            else:\n                lo = i + 1\n        i = lo\n        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])\n        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0',
    )

    problem22 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Max Chunks To Make Sorted II',
        description='Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array. What is the most number of chunks we could have made?',
        language="Python",
        solution="class Solution(object):\n    def maxChunksToSorted(self, arr):\n        n = len(arr)\n        min_right = [0]*n\n        max_left = [0]*n\n        for i in range(n):\n            if i == 0:\n                max_left[i] = arr[i]\n            else:\n                max_left[i] = max(arr[i], max_left[i-1])\n        for i in range(n-1, -1, -1):\n            if i == n-1:\n                min_right[i] = arr[i]\n            else:\n                min_right[i] = min(arr[i], min_right[i+1])\n        res = 1\n        for i in range(n-1):\n            if max_left[i] <= min_right[i+1]:\n                res += 1\n        return res",
    )

    # Strings
    # Strings - Easy

    problem23 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Reverse String',
        description='Write a function that reverses a string. The input string is given as an array of characters s.',
        language="Python",
        solution="class Solution(object): def reverseString(self, s): return s[::-1]",
    )

    problem24 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Count Binary Substrings',
        description='Give a binary string s, return the number of non-empty substrings that have the same number of 0\'s and 1\'s, and all the 0\'s and all the 1\'s in these substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.',
        language="Python",
        solution="class Solution(object): def countBinarySubstrings(self, s): res = 0 prev = 0 tmp = 1 for i in range(1, len(s)): if s[i] != s[i-1]: res += min(prev, tmp) prev = tmp tmp = 1 else: tmp += 1 res += min(prev, tmp) return res",
    )

    problem25 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Parentheses',
        description='Given a string s containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.',
        language="Python",
        solution='class Solution: def isValid(self, s: str) -> bool: if len(s)%2!=0: return False stack = list() dic = {"(":")","{":"}","[":"]"} for i, c in enumerate(s): if s[i] in dic: stack.append(s[i]) else: if len(stack)!=0 and dic[stack[-1]] == s[i]: stack.pop() else: return False if stack: return False else: return True',
    )

    problem26 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome',
        description='Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.',
        language="Python",
        solution="class Solution(object): def isPalindrome(self, s): if not s: return True i, j = 0, len(s) - 1 while i < j: while i < j and not s[i].isalnum(): i += 1 while i < j and not s[j].isalnum(): j -= 1 if s[i].lower() != s[j].lower(): return False i += 1; j -= 1 return True",
    )

    problem27 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Binary',
        description='Given two binary strings a and b, return their sum as a binary string.',
        language="Python",
        solution="class Solution(object): def addBinary(self, a, b): return bin(int(a,2) + int(b,2))[2:]",
    )

    problem28 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Strings',
        description='Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.',
        language="Python",
        solution="class Solution: def addStrings(self, num1: str, num2: str) -> str: L1, L2, n1, n2 = len(num1), len(num2), [int(i) for i in num1], [int(i) for i in num2] if L1 < L2: n2, n1 = n1, n2 n1, n2, n3 = [0] + n1, [0]*(abs(L1-L2)+1) + n2, [0]*(len(n1)+1) for i in range(len(n1)-1,-1,-1): s = n1[i]+n2[i] n3[i] = s % 10 if s > 9: n1[i-1] += int(s/10) if n3[0] == 0: n3 = n3[1:] return "".join([str(i) for i in n3])",
    )

    problem29 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome II',
        description='Given a string s, return true if the s can be palindrome after deleting at most one character from it.',
        language="Python",
        solution="class Solution(object): def validPalindrome(self, s): left, right = 0, len(s) - 1 while left < right: if s[left] != s[right]: one, two = s[left:right], s[left + 1:right + 1] return one == one[::-1] or two == two[::-1] left, right = left + 1, right - 1 return True",
    )

    problem30 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Consecutive Characters',
        description='Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character. Return the power of the string.',
        language="Python",
        solution="class Solution: def maxPower(self, s: str) -> int: cnt = ans = 1 for i in range(1, len(s)): if s[i] == s[i - 1]: cnt += 1 ans = max(cnt, ans) else: cnt = 1 return ans",
    )

    problem31 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Greatest Common Divisor of Strings',
        description='For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times) Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.',
        language="Python",
        solution="class Solution: def gcdOfStrings(self, s1: str, s2: str) -> str: return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''",
    )

    problem32 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Longest Common Prefix',
        description='Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".',
        language="Python",
        solution='class Solution(object): def longestCommonPrefix(self, strs): result = "" for n in zip(*strs): if len(set(n)) == 1: result += n[0] else: return result return result',
    )

    # Strings - Medium

    problem33 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Generate Parentheses',
        description='Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.',
        language="Python",
        solution="class Solution: def generateParenthesis(self, n: int) -> List[str]: bfs = [(0, 0, '')] for _ in range(n * 2): new = [] for l, r, s in bfs: if l + 1 <= n: new.append((l + 1, r, s + '(')) if l - r: new.append((l, r + 1, s + ')')) bfs = new return [s for l, r, s in bfs]",
    )

    problem34 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Palindromic Substrings',
        description='Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.',
        language="Python",
        solution="class Solution(object): def countSubstrings(self, s): n = len(s) dp = [[0] * n for i in xrange(n)] count = 0 for end in xrange(n): dp[end][end] = 1 count += 1 for start in xrange(end): if s[start] == s[end] and (start+1 >= end-1 or dp[start+1][end-1]): count += 1 dp[start][end] = 1 return count",
    )

    problem35 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Group Anagrams',
        description='Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        language="Python",
        solution="class Solution(object): def groupAnagrams(self, strs): def convert(s): res = [0]*26 for char in s: res[ord(char)-ord('a')] += 1 return tuple(res) rec = {} res = [] for s in strs: t = convert(s) if t in rec: res[rec[t]].append(s) else: res.append([s]) rec[t] = len(res)-1 return res",
    )

    problem36 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Reorganize String',
        description='Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same. If possible, output any possible result.  If not possible, return the empty string.',
        language="Python",
        solution="class Solution: def reorganizeString(self, S): res, c = [], Counter(S) pq = [(-value,key) for key,value in c.items()] heapq.heapify(pq) p_a, p_b = 0, '' while pq: a, b = heapq.heappop(pq) res += [b] if p_a < 0: heapq.heappush(pq, (p_a, p_b)) a += 1 p_a, p_b = a, b res = ''.join(res) if len(res) != len(S): return "" return res",
    )

    problem37 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Basic Calculator II',
        description='Given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.',
        language="Python",
        solution='class Solution: def calculate(self, s): num, stack, sign = 0, [], "+" for i in range(len(s)): if s[i].isdigit(): num = num * 10 + int(s[i]) if s[i] in "+-*/" or i == len(s) - 1: if sign == "+": stack.append(num) elif sign == "-": stack.append(-num) elif sign == "*": stack.append(stack.pop()*num) else: stack.append(int(stack.pop()/num)) num = 0 sign = s[i] return sum(stack)',
    )

    problem38 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Multiply Strings',
        description='Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.',
        language="Python",
        solution='class Solution: def multiply(self, num1: str, num2: str) -> str: n, m = len(num1), len(num2) if not n or not m: return "0" result = [0] * (n + m) for i in reversed(range(n)): for j in reversed(range(m)): current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j]) result[i + j + 1] = current % 10 result[i + j] += current // 10 for i, c in enumerate(result): if c != 0: return "".join(map(str, result[i:])) return "0"',
    )

    # Strings - Hard

    problem39 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Distinct Subsequences',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        language="Python",
        solution='class Solution(object): def numDistinct(self, s, t): n1, n2 = len(s), len(t) dp = [1] + [0] * n2 for i in range(1, n1+1): pre = dp[0] for j in range(1, n2+1): dp[j], pre = dp[j] + pre * (s[i-1] == t[j-1]), dp[j] return dp[-1]',
    )

    problem40 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Text Justification',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        language="Python",
        solution='class Solution(object): def fullJustify(self, words, maxWidth): line = [] word_count = 0 char_count = 0 res = [] for word in words: length = char_count+1+len(word) if length > maxWidth: space_left = maxWidth - char_count if word_count == 1: string = line[0]+" "*(maxWidth-len(line[0])) res.append(string) line = [word] char_count = len(word) else: q, r = divmod(space_left, word_count-1) front = (" "*(q+2)).join(line[:r+1]) end = (" "*(q+1)).join(line[r+1:]) string = front+" "*(q+1)+end if string: res.append(string) line = [word] word_count = 1 char_count = len(word) else: if line: char_count += len(word)+1 else: char_count += len(word) line.append(word) word_count += 1 if line: line = " ".join(line) line += " "*(maxWidth-len(line)) res.append(line) return res',
    )

    # Trees

    # Trees - Easy

    problem40 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Range Sum of BST',
        description='Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].',
        language="Python",
        solution='class Solution: def rangeSumBST(self, root, L, R): def dfs(root): if not root: return if L <= root.val <= R: self.res += root.val if L <= root.val: dfs(root.left) if R >= root.val: dfs(root.right) self.res = 0 dfs(root) return self.res',
    )

    problem41 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Maximum Depth of Binary Tree',
        description='Given the root of a binary tree, return its maximum depth. A binary tree\'s maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.',
        language="Python",
        solution='class Solution(object): def maxDepth(self, root): if root == None: return 0 return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))',
    )

    problem42 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Invert Binary Tree',
        description='Given the root of a binary tree, invert the tree, and return its root.',
        language="Python",
        solution='class Solution: def invertTree(self, root): if root: invert = self.invertTree root.left, root.right = invert(root.right), invert(root.left) return root',
    )

    problem43 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Binary Tree Postorder Traversal',
        description='Given the root of a binary tree, return the postorder traversal of its nodes\' values.',
        language="Python",
        solution='class Solution(object): def postorderTraversal(self, root): def dfs(root): if not root: return dfs(root.left) dfs(root.right) res.append(root.val) res = [] dfs(root) return res',
    )

    problem44 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Binary Tree Preorder Traversal',
        description='Given the root of a binary tree, return the preorder traversal of its nodes\' values.',
        language="Python",
        solution='class Solution(object): def preorderTraversal(self, root): if not root: return [] elif not root.left and not root.right: return [root.val] l = self.preorderTraversal(root.left) r = self.preorderTraversal(root.right) return [root.val]+l+r',
    )

    problem45 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Diameter of Binary Tree',
        description='Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.',
        language="Python",
        solution='class Solution(object): def diameterOfBinaryTree(self, root): self.ans = 0 def depth(p): if not p: return 0 left, right = depth(p.left), depth(p.right) self.ans = max(self.ans, left+right) return 1 + max(left, right) depth(root) return self.ans',
    )

    problem46 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Symmetric Tree',
        description='Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).',
        language="Python",
        solution='class Solution(object): def isSymmetric(self, root): def isSym(root1, root2): if root1 == None and root2 == None: return True elif root1 == None and root2 != None: return False elif root1 != None and root2 == None: return False else: if root1.val != root2.val: return False else: return isSym(root1.left, root2.right) and isSym(root1.right,root2.left) return root == None or isSym(root.left,root.right)',
    )

    problem47 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Same Tree',
        description='Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.',
        language="Python",
        solution='class Solution(object): def isSameTree(self, p, q): if p == None and q == None: return True elif p == None and q != None: return False elif p != None and q == None: return False else: if p.val != q.val: return False else: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)',
    )

    problem48 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Subtree of Another Tree',
        description='Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise. A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node\'s descendants. The tree tree could also be considered as a subtree of itself.',
        language="Python",
        solution='class Solution: def isSubtree(self, s, t): def isSame(s,t): if not s and not t: return True elif not s or not t: return False return s.val == t.val and isSame(s.left,t.left) and isSame(s.right,t.right) def traverse(s,t): if not s and not t: return True elif not s and t: return False elif s and not t: return False else: if s.val != t.val: return traverse(s.left,t) or traverse(s.right,t) else: if traverse(s.left,t) or traverse(s.right,t): return True else: return isSame(s,t) return traverse(s,t)',
    )

    # Trees - Medium

    problem48 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Insert into a Binary Search Tree',
        description='You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST. Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.',
        language="Python",
        solution='class Solution: def insertIntoBST(self, root, val): if val < root.val: if not root.left: root.left = TreeNode(val) else: self.insertIntoBST(root.left, val) else: if not root.right: root.right = TreeNode(val) else: self.insertIntoBST(root.right, val) return root',
    )

    problem49 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Count Good Nodes in Binary Tree',
        description='Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.',
        language="Python",
        solution="class Solution: def goodNodes(self, root: TreeNode) -> int: self.cnt = 0 def dfs(node, v): if not node: return if node.val >= v: self.cnt += 1 v = max(v, node.val) dfs(node.left, v) dfs(node.right, v) dfs(root,-float('inf')) return self.cnt",
    )

    problem50 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Construct Binary Tree from Preorder and Postorder Traversal',
        description='Return any binary tree that matches the given preorder and postorder traversals. Values in the traversals pre and post are distinct positive integers.',
        language="Python",
        solution='class Solution: def constructFromPrePost(self, pre, post): if pre: root = TreeNode(pre.pop(0)) post.pop() if pre: if pre[0] == post[-1]: root.left = self.constructFromPrePost(pre, post) else: l, r = post.index(pre[0]), pre.index(post[-1]) root.left = self.constructFromPrePost(pre[:r], post[:l + 1]) root.right = self.constructFromPrePost(pre[r:], post[l + 1:]) return root',
    )

    problem51 = Problem(
        category='Trees',
        difficulty='Medium',
        title='All Nodes Distance K in Binary Tree',
        description='We are given a binary tree (with root node root), a target node, and an integer value k. Return a list of the values of all nodes that have a distance k from the target node.  The answer can be returned in any order.',
        language="Python",
        solution='class Solution: def distanceK(self, root, target, K): def dfs(root, d): if not root: return  if d == 0: res.append(root.val) return  if root.left: dfs(root.left, d-1) if root.right: dfs(root.right, d-1) parent = {} q = collections.deque([root]) while q: u = q.popleft() if u == target: break if u.left: parent[u.left] = u q.append(u.left) if u.right: parent[u.right] = u q.append(u.right) res = [] trav = target d = K while trav != root and d > 0: tmp = parent[trav] d -= 1 if d == 0: res.append(tmp.val) break if tmp.left == trav: dfs(tmp.right, d-1) else: dfs(tmp.left, d-1) trav = tmp dfs(target, K) return res',
    )

    problem52 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Binary Tree Right Side View',
        description='Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.',
        language="Python",
        solution='class Solution(object): def rightSideView(self, root): if root == None: return [] ans = [root.val] left = ans + self.rightSideView(root.left) right = ans + self.rightSideView(root.right) if len(right) >= len(left): return right return right + left[len(right):]',
    )

    # Trees - Hard

    problem53 = Problem(
        category='Trees',
        difficulty='Hard',
        title='Serialize and Deserialize Binary Tree',
        description='Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.',
        language="Python",
        solution='class Codec: def serialize(self, root): def dfs(root): if not root: res.append("None,") return  res.append(str(root.val)+",") dfs(root.left) dfs(root.right) res = [] dfs(root) return "".join(res) def deserialize(self, data): def helper(q): if q[0] == "None": q.popleft() return root = TreeNode(q.popleft()) l = helper(q) r = helper(q) root.left = l root.right = r return root lst = data.split(",") q = collections.deque(lst) return helper(q)',
    )

    problem54 = Problem(
        category='Trees',
        difficulty='Hard',
        title='Binary Tree Maximum Path Sum',
        description='A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node\'s values in the path. Given the root of a binary tree, return the maximum path sum of any path.',
        language="Python",
        solution="class Solution: def maxPathSum(self, root): def maxSum(root): if not root: return 0 l_sum = maxSum(root.left) r_sum = maxSum(root.right) l = max(0, l_sum) r = max(0, r_sum) res[0] = max(res[0], root.val + l + r) return root.val + max(l, r) res = [-float('inf')] maxSum(root) return res[0]",
    )

    problem55 = Problem(
        category='Trees',
        difficulty='Hard',
        title='Vertical Order Traversal of a Binary Tree',
        description='Given the root of a binary tree, calculate the vertical order traversal of the binary tree. For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0). The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the vertical order traversal of the binary tree.',
        language="Python",
        solution="class Solution(object): def verticalTraversal(self, root): res = [] frontier = [(root, 0)] h = collections.defaultdict(list) while frontier: next = [] for u, x in frontier: h[x].append(u.val) if u.left: next.append((u.left, x-1))  if u.right: next.append((u.right, x+1)) next.sort(key = lambda x: (x[1], x[0].val)) frontier = next for k in sorted(h): res.append(h[k]) return res",
    )

    # Hash Table
    # Hash Table - Easy
    problem56 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Number of Good Pairs',
        description='Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.',
        language="Python",
        solution="class Solution: def numIdenticalPairs(self, nums: List[int]) -> int: ans = 0 d = defaultdict(list) for i in range(len(nums)): d[nums[i]].append(i) for k,v in d.items(): n = len(v) if n > 1: ans += ((n-1) * n) // 2 return ans",
    )

    problem57 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Jewels and Stones',
        description='You\'re given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels. Letters are case sensitive, so "a" is considered a different type of stone from "A".',
        language="Python",
        solution="class Solution: def numJewelsInStones(self, J: str, S: str) -> int: jewels = set(J) count_of_jewel = 0 for item in S: if item in jewels: count_of_jewel += 1 return count_of_jewel",
    )

    problem58 = Problem(
        category='Hash',
        difficulty='Easy',
        title='How Many Numbers Are Smaller Than the Current Number',
        description='Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j\'s such that j != i and nums[j] < nums[i]. Return the answer in an array.',
        language="Python",
        solution="class Solution: def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: indexes = {} for idx,val in enumerate(nums): if val in indexes: indexes[val].append(idx) else: indexes[val] = [idx] lst = sorted(list(set(nums))) ans = [None for x in nums] count_smaller = 0 for x in lst: for idx in indexes[x]: ans[idx] = count_smaller count_smaller += len(indexes[x]) return ans",
    )

    problem59 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Subdomain Visit Count',
        description='A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly. Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com". We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.',
        language="Python",
        solution='class Solution(object): def subdomainVisits(self, cpdomains): res = [] dic = {} for item in cpdomains: count, domain = item.split() dlst = domain.split(".") summ = dlst[-1] if summ in dic: dic[summ] += int(count) else: dic[summ] = int(count) for i in range(len(dlst)-2, -1, -1): summ = dlst[i] + "." + summ if summ in dic: dic[summ] += int(count) else: dic[summ] = int(count) for key, val in dic.items(): res.append(str(val) + " " + key) return res',
    )

    problem60 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Design HashMap',
        description='Design a HashMap without using any built-in hash table libraries.',
        language="Python",
        solution="class MyHashMap(object): def __init__(self): self.map = [[] for i in xrange(1024)] def put(self, key, value): self.remove(key) self.map[key & 1023].append((key, value)) def get(self, key): values = [x[1] for x in self.map[key & 1023] if x[0] == key] return -1 if len(values) == 0 else values[0] def remove(self, key): self.map[key & 1023] = [x for x in self.map[key & 1023] if x[0] != key]",
    )

    problem61 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Single Number',
        description='Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.',
        language="Python",
        solution="class Solution: def singleNumber(self, nums): res = nums[0] for i in range(1, len(nums)): res ^= nums[i] return res",
    )

    problem62 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Verifying an Alien Dictionary',
        description='In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.',
        language="Python",
        solution='class Solution: def isAlienSorted(self, words, order): dic = {} for i, c in enumerate(order): dic[c] = i for i in range(len(words)-1): cur = words[i] nex = words[i+1] for i in range(min(len(cur), len(nex))): if cur[i] != nex[i]: if dic[cur[i]] > dic[nex[i]]: return False break else: if len(cur) > len(nex): return False return True',
    )

    # Hash Table - Medium

    problem63 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Top K Frequent Words',
        description='Given a non-empty list of words, return the k most frequent elements. Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.',
        language="Python",
        solution="import heapq import collections class Solution: def topKFrequent(self, words: List[str], k: int) -> List[str]: word_count = self.calc_count(words) word_count_pairs = [] for word, count in word_count.items(): word_count_pairs.append((-count, word)) heapq.heapify(word_count_pairs) result = [] for _ in range(k): result.append(heapq.heappop(word_count_pairs)[1]) return result def calc_count(self, words): result = collections.defaultdict(int) for word in words: result[word] += 1 return result",
    )

    problem64 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Daily Temperatures',
        description='Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.',
        language="Python",
        solution="class Solution(object): def dailyTemperatures(self, temperatures): res = [0]*len(temperatures) T = [-1]*71 for i in range(len(temperatures)-1, -1, -1): t = temperatures[i] for j in range(t-1, 29, -1): T[j-30] = i if T[t-30] != -1: res[i] = T[t-30]-i return res",
    )

    problem65 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Subarray Sum Equals K',
        description='Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.',
        language="Python",
        solution="class Solution: def subarraySum(self, nums, k): preSums = {0: 1} s = 0 res = 0 for num in nums: s += num res += preSums.get(s - k, 0) preSums[s] = preSums.get(s, 0) + 1 return res",
    )

    # Hash Tables - Hard

    problem66 = Problem(
        category='Hash',
        difficulty='Hard',
        title='Group Anagrams',
        description='Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        language="Python",
        solution="class Solution(object): def groupAnagrams(self, strs): def convert(s): res = [0]*26 for char in s: res[ord(char)-ord('a')] += 1 return tuple(res) rec = {} res = [] for s in strs: t = convert(s) if t in rec: res[rec[t]].append(s) else: res.append([s]) rec[t] = len(res)-1 return res",
    )

    problem67 = Problem(
        category='Hash',
        difficulty='Hard',
        title='Minimum Window Substring',
        description='Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.',
        language="Python",
        solution="class Solution: def minWindow(self, s, t): dicT = collections.Counter(t) dicS = {} rec = set() j = 0 res = float('inf') for i, c in enumerate(s): if c not in dicS: dicS[c] = 1 else: dicS[c] += 1 if c in dicT and dicT[c] <= dicS[c]: rec.add(c) while len(rec) == len(dicT): dicS[s[j]] -= 1 if s[j] in dicT and dicT[s[j]] > dicS[s[j]]: rec.remove(s[j]) if res > i-j+1: start = j end = i res = i-j+1 j += 1 if res == float('inf'): return "" return s[start:end+1]",
    )

    problem68 = Problem(
        category='Hash',
        difficulty='Hard',
        title='Palindrome Pairs',
        description='Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.',
        language="Python",
        solution='class Solution: def palindromePairs(self, words: List[str]) -> List[List[int]]: if len(words) == 0: return [] res = [] mapping = {word: i for i, word in enumerate(words)} for i, word in enumerate(words): for j in range(len(word)+1): s1, s2 = word[:j], word[j:] if self.valid(s1): tmp = s2[::-1] if tmp in mapping and mapping[tmp] != i: res.append([mapping[tmp], i]) if len(s2) > 0 and self.valid(s2): tmp = s1[::-1] if tmp in mapping and mapping[tmp] != i: res.append([i, mapping[tmp]]) return res def valid(self, s): start, end = 0, len(s)-1 while start < end: if s[start] != s[end]: return False start += 1 end -= 1 return True',
    )

    db.session.add(problem1)
    db.session.add(problem2)
    db.session.add(problem3)
    db.session.add(problem4)
    db.session.add(problem5)
    db.session.add(problem6)
    db.session.add(problem7)
    db.session.add(problem8)
    db.session.add(problem9)
    db.session.add(problem10)
    db.session.add(problem11)
    db.session.add(problem12)
    db.session.add(problem13)
    db.session.add(problem14)
    db.session.add(problem15)
    db.session.add(problem16)
    db.session.add(problem17)
    db.session.add(problem18)
    db.session.add(problem19)
    db.session.add(problem20)
    db.session.add(problem21)
    db.session.add(problem22)
    db.session.add(problem23)
    db.session.add(problem24)
    db.session.add(problem25)
    db.session.add(problem26)
    db.session.add(problem27)
    db.session.add(problem28)
    db.session.add(problem29)
    db.session.add(problem30)
    db.session.add(problem31)
    db.session.add(problem32)
    db.session.add(problem33)
    db.session.add(problem34)
    db.session.add(problem35)
    db.session.add(problem36)
    db.session.add(problem37)
    db.session.add(problem38)
    db.session.add(problem39)
    db.session.add(problem40)
    db.session.add(problem41)
    db.session.add(problem42)
    db.session.add(problem43)
    db.session.add(problem44)
    db.session.add(problem45)
    db.session.add(problem46)
    db.session.add(problem47)
    db.session.add(problem48)
    db.session.add(problem49)
    db.session.add(problem50)
    db.session.add(problem51)
    db.session.add(problem52)
    db.session.add(problem53)
    db.session.add(problem54)
    db.session.add(problem55)
    db.session.add(problem56)
    db.session.add(problem57)
    db.session.add(problem58)
    db.session.add(problem59)
    db.session.add(problem60)
    db.session.add(problem61)
    db.session.add(problem62)
    db.session.add(problem63)
    db.session.add(problem64)
    db.session.add(problem65)
    db.session.add(problem66)
    db.session.add(problem67)
    db.session.add(problem68)

    db.session.commit()


def undo_problems():
    db.session.execute('TRUNCATE problems;')
    db.session.commit()
