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
        example="Input: nums = [1,2,3,4].\n Output: [1,3,6,10].\n Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].",
        solution='def runningSum(self, nums: List[int]) -> List[int]:\n     for i in range(1, len(nums)):\n         nums[i] += nums[i - 1]\n    return nums',
    )

    problem2 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Shuffle the Array',
        description='Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].',
        language="Python",
        example="Input: nums = [1,2,3,4,4,3,2,1], n = 4\n Output: [1,4,2,3,3,2,4,1]",
        solution='class Solution:\n    def shuffle(self, nums: List[int], n: int) -> List[int]:\n        temp = []\n        for i in range(n):\n            temp.append(nums[i])\n            temp.append(nums[n + i])\n        return temp',
    )

    problem3 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Number of Good Pairs',
        description='Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.',
        language="Python",
        example="Input: nums = [1,2,3,1,1,3]\n Output: 4\n Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.",
        solution='class Solution:\n    def numIdenticalPairs(self, nums: List[int]) -> int:\n        diction = dict()\n        pairs = 0\n        for num in nums:\n            if num in diction:\n                pairs += diction[num]\n                diction[num] += 1\n            else:\n                diction[num] = 1\n        return pairs',
    )

    problem4 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='How Many Numbers Are Smaller Than the Current Number',
        description='Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j\'s such that j != i and nums[j] < nums[i]. Return the answer in an array.',
        language="Python",
        example="Input: nums = [6,5,4,8]\n Output: [2,1,0,3]",
        solution='class Solution:\n    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:\n        sorted_nums = sorted(nums)\n        return [sorted_nums.index(num) for num in nums]',
    )

    problem5 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find N Unique Integers Sum up to Zero',
        description='Given an integer n, return any array containing n unique integers such that they add up to 0.',
        language="Python",
        example="Input: n = 5\n Output: [-7,-1,1,3,4]\n Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].",
        solution='class Solution:\n    def sumZero(self, n):\n        return range(1 - n, n, 2)',
    )

    problem6 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Fibonacci Number',
        description='The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. Given n, calculate F(n).',
        language="Python",
        example="Input: n = 2\n Output: 1\n Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.",
        solution='class Solution:\n    def fib(self, N):\n	    if N <= 1: return N\n	    a, b = 0, 1\n	    for i in range(2, N+1):\n		    c = a + b\n		    a, b = b, c\n	    return c',
    )

    problem7 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Squares of a Sorted Array',
        description='Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.',
        language="Python",
        example="Input: nums = [-4,-1,0,3,10]\n Output: [0,1,9,16,100]\n Explanation: After squaring, the array becomes [16,1,0,9,100].\n After sorting, it becomes [0,1,9,16,100].",
        solution='class Solution:\n    def sortedSquares(self, A: List[int]) -> List[int]:\n        result = [None for _ in A]\n        left, right = 0, len(A) - 1\n        for index in range(len(A)-1, -1, -1):\n            if abs(A[left]) > abs(A[right]):\n                result[index] = A[left] ** 2\n                left += 1\n            else:\n                result[index] = A[right] ** 2\n                right -= 1\n        return result',
    )

    problem8 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find Common Characters',
        description='Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer. You may return the answer in any order.',
        language="Python",
        example='Input: ["bella","label","roller"]\n Output: ["e","l","l"]',
        solution='class Solution:\n    def commonChars(self, A: List[str]) -> List[str]:\n        ans = []\n        d1 = Counter(A[0])\n        for i in range(1,len(A)):\n            d2 = Counter(A[i])\n            d1 = d1 & d2\n            ans = list(d1.elements())\n        return ans',
    )

    problem9 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Move Zeroes',
        description='Given an integer array nums, move all 0\'s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array',
        language="Python",
        example="Input: nums = [0,1,0,3,12]\n Output: [1,3,12,0,0]",
        solution='class Solution:\n    def moveZeroes(self, nums):\n        i = 0\n        for j in range(len(nums)):\n            if nums[j] != 0:\n                nums[i], nums[j] = nums[j], nums[i]\n                i += 1',
    )

    problem10 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Missing Number',
        description='Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.',
        language="Python",
        example="Input: nums = [3,0,1]\n Output: 2\n Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.",
        solution='class Solution:\n    def missingNumber(self, nums):\n    n = len(nums)\n        return n * (n+1) // 2 - sum(nums)',
    )

    # Arrays - Medium

    problem11 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find All Duplicates in an Array',
        description='Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.',
        language="Python",
        example="Input: nums = [4,3,2,7,8,2,3,1]\n Output: [2,3]",
        solution='class Solution(object):\n    def findDuplicates(self, nums):\n        result = []\n        for x in nums:\n            if nums[abs(x)-1] < 0:\n                result.append(abs(x))\n            else:\n                nums[abs(x)-1] = -1*nums[abs(x)-1]\n        return result',
    )

    problem12 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Max Area of Island',
        description='You are given an m x n binary matrix grid. An island is a group of 1\'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0',
        language="Python",
        example="Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],\n [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],\n [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],\n [0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],\n [0,0,0,0,0,0,0,1,1,0,0,0,0]]\n Output: 6\n Explanation: The answer is not 11, because the island must be connected 4-directionally.",
        solution='class Solution:\n    def maxAreaOfIsland(self, grid):\n        return max([self.dfs(r, c, grid) for r in range(len(grid)) for c in range(len(grid[0]))])\n    def dfs(self, r, c, grid):\n        if not (0 <= r < len(grid) and (0 <= c < len(grid[0])) and grid[r][c]):\n            return 0\n        grid[r][c] = 0\n        return 1 + sum([self.dfs(r + x[0], c + x[1], grid) for x in [(0, 1), (0, -1), (1, 0), (-1, 0)]])',
    )

    problem13 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Rotate Image',
        description='You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.',
        language="Python",
        example="Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]\n Output: [[7,4,1],[8,5,2],[9,6,3]]",
        solution='class Solution(object):\n    def transpose(self, matrix):\n        M,N = len(matrix), len(matrix[0])\n        cols = 1\n        for i in range(M):\n            for j in range(cols):\n                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n            cols += 1\n        return\n\n    def rotate(self, matrix):\n        if matrix == []:\n            return matrix\n        self.transpose(matrix)\n        for r in matrix:\n            r.reverse()\n        return',
    )

    problem14 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Product of Array Except Self',
        description='Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer',
        language="Python",
        example="Input: nums = [1,2,3,4]\n Output: [24,12,8,6]",
        solution='class Solution:\n    def productExceptSelf(self, nums):\n        res = [1]*len(nums)\n        lprod = 1\n        rprod = 1\n        for i in range(len(nums)):\n            res[i] *= lprod\n            lprod *= nums[i]\n            res[~i] *= rprod\n            rprod *= nums[~i]\n        return res',
    )

    problem15 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Combination Sum',
        description='Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.',
        language="Python",
        example="Input: candidates = [2,3,5], target = 8\n Output: [[2,2,2,2],[2,3,3],[3,5]]",
        solution='class Solution(object):\n    def combinationSum(self, candidates, target):\n        ret = []\n        self.dfs(candidates, target, [], ret)\n        return ret\n\n    def dfs(self, nums, target, path, ret):\n        if target < 0:\n            return\n        if target == 0:\n            ret.append(path)\n            return\n        for i in range(len(nums)):\n            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)',
    )

    problem16 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find the Duplicate Number',
        description='Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.',
        language="Python",
        example="Input: nums = [1,3,4,2,2]\n Output: 2",
        solution='class Solution(object):\n    def findDuplicate(self, nums):\n        if len(nums) == 0:\n            return 0\n        low = 1\n        high = len(nums)\n        while low < high:\n            mid = low + int((high-low)>>1)\n            count = 0\n            for x in nums:\n                if x <= mid:\n                    count = count + 1\n            if count > mid:\n                high = mid\n            else:\n                low = mid+1\n        return low',
    )

    problem17 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Container With Most Water',
        description='Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water. Notice that you may not slant the container.',
        language="Python",
        example="Input: height = [1,8,6,2,5,4,8,3,7]\n Output: 49\n Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.",
        solution='class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        l = 0\n        r = len(height)-1\n        res = 0\n        while l < r:\n            area = (r - l) * min(height[l], height[r])\n            res = max(area,res)\n            if height[l]<height[r]:\n                l = l+1\n            else:\n                r = r-1\n        return res',
    )

    problem18 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Subarray Sum Equals K',
        description='Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.',
        language="Python",
        example="Input: nums = [1,1,1], k = 2\n Output: 2",
        solution='class Solution:\n    def subarraySum(self, nums, k):\n        preSums = {0: 1}\n        s = 0\n        res = 0\n        for num in nums:\n            s += num\n            res += preSums.get(s - k, 0)\n            preSums[s] = preSums.get(s, 0) + 1\n        return res',
    )

    # Array - Hard
    problem19 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Trapping Rain Water',
        description='Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.',
        language="Python",
        example="Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]\n Output: 6\n Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.",
        solution='class Solution:\n    def trap(self, height: List[int]) -> int:\n        stack =[]\n        area = 0\n        for i in range(len(height)):\n            offset = 0\n            while(stack and height[i] >= height[stack[-1]]):\n                pre_i = stack.pop()\n                area += (height[pre_i]-offset) * (i-pre_i-1)\n                offset = height[pre_i]\n            if stack:\n                area += (height[i]-offset) * (i-stack[-1]-1)\n            stack.append(i)\        return area',
    )

    problem20 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='First Missing Positive',
        description='Given an unsorted integer array nums, find the smallest missing positive integer.',
        language="Python",
        example="Input: nums = [1,2,0]\n Output: 3",
        solution='class Solution(object)\n:    def firstMissingPositive(self, nums):\n        N, i = len(nums), 0\n        while i < N:\n        while 1<=nums[i]<=N:\n            idx_expected = nums[i]-1\n                if nums[i] == nums[idx_expected]:\n                    break\n                nums[i], nums[idx_expected] = nums[idx_expected], nums[i]\n            i = i + 1\n        for i in range(N):\n            if nums[i] != i+1:\n                return i+1\n        return N+1',
    )

    problem21 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Median of Two Sorted Arrays',
        description='Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.',
        language="Python",
        example="Input: nums1 = [1,3], nums2 = [2]\n Output: 2.00000\n Explanation: merged array = [1,2,3] and median is 2.",
        solution='class Solution:\n    def findMedianSortedArrays(self, nums1, nums2):\n        a, b = sorted((nums1, nums2), key=len)\n        m, n = len(a), len(b)\n        after = (m + n - 1) / 2\n        lo, hi = 0, m\n        while lo < hi: \n            i = (lo + hi) / 2\n            if after-i-1 < 0 or a[i] >= b[after-i-1]:\n                hi = i\n            else:\n                lo = i + 1\n        i = lo\n        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])\n        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0',
    )

    problem22 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Max Chunks To Make Sorted II',
        description='Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array. What is the most number of chunks we could have made?',
        language="Python",
        example="Input: arr = [5,4,3,2,1]\n Output: 1\n Explanation:\n Splitting into two or more chunks will not return the required result. For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.",
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
        example='Input: s = ["h","e","l","l","o"]\n Output: ["o","l","l","e","h"]',
        solution="class Solution(object):\n        def reverseString(self, s):\n            return s[::-1]",
    )

    problem24 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Count Binary Substrings',
        description='Give a binary string s, return the number of non-empty substrings that have the same number of 0\'s and 1\'s, and all the 0\'s and all the 1\'s in these substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.',
        language="Python",
        example='Input: s = "10101"\n Output: 4\n Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1\'s and 0\'s.',
        solution="class Solution(object):\n    def countBinarySubstrings(self, s):\n        res = 0\n        prev = 0\n        tmp = 1\n    for i in range(1, len(s)):\n        if s[i] != s[i-1]:\n            res += min(prev, tmp)\n                prev = tmp\n                tmp = 1\n            else:\n                tmp += 1\n        res += min(prev, tmp)\n        return res",
    )

    problem25 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Parentheses',
        description='Given a string s containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.',
        language="Python",
        example='Input: s = "()[]{}"\n Output: true',
        solution="class Solution:\n    def isValid(self, s: str) -> bool:\n        stack = []\n        for x in s:\n            if x in {'(', '[', '{'}:\n                stack.append(x)\n            else:\n                if not stack or stack.pop() + x not in {'()', '[]', '{}'}:\n                    return False\n        return not stack",
    )

    problem26 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome',
        description='Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.',
        language="Python",
        example='Input: s = "A man, a plan, a canal: Panama"\n Output: true\n Explanation: "amanaplanacanalpanama" is a palindrome.',
        solution="class Solution(object):\n    def isPalindrome(self, s):\n        s = s.lower()\n        s_stripped = ''.join(list(filter(lambda x: x.isalnum() == True, s)))\n        return s_stripped == s_stripped[::-1]",
    )

    problem27 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Binary',
        description='Given two binary strings a and b, return their sum as a binary string.',
        language="Python",
        example='Input: a = "11", b = "1"\n Output: "100"',
        solution="class Solution(object):\n    def addBinary(self, a, b):\n        return bin(int(a,2) + int(b,2))[2:]",
    )

    problem28 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Strings',
        description='Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.',
        language="Python",
        example='Input: num1 = "11", num2 = "123"\n Output: "134"',
        solution='def addString(num1, num2):\n    i, j, carrier, res = len(num1)-1, len(num2)-1, 0, ""\n    while i >= 0 or j >=0 or carrier:\n        if i >= 0:\n            carrier += int(num1[i])\n            i -= 1\n        if j >= 0:\n            carrier += int(num2[j])\n            j -= 1\n        res += str(carrier % 10)\n        carrier //= 10\n    return "".join(res[::-1])',
    )

    problem29 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome II',
        description='Given a string s, return true if the s can be palindrome after deleting at most one character from it.',
        language="Python",
        example='Input: s = "aba"\n Output: true',
        solution="class Solution:\n    def validPalindrome(self, s):\n        left, right = 0, len(s)-1\n        while left < right:\n            if s[left] == s[right]:\n                left += 1\n                right -= 1\n            else:\n                tmp1 = s[:left]+s[left+1:]\n                tmp2 = s[:right]+s[right+1:]\n                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]\n        return True",
    )

    problem30 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Consecutive Characters',
        description='Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character. Return the power of the string.',
        language="Python",
        example='Input: s = "leetcode"\n Output: 2\n Explanation: The substring "ee" is of length 2 with the character "e" only.',
        solution="class Solution:\n    def maxPower(self, s: str) -> int:\n        cnt = ans = 1\n        for i in range(1, len(s)):\n            if s[i] == s[i - 1]:\n                cnt += 1\n                ans = max(cnt, ans)\n            else:\n                cnt = 1\n        return ans",
    )

    problem31 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Greatest Common Divisor of Strings',
        description='For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times) Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.',
        language="Python",
        example='Input: str1 = "ABCABC", str2 = "ABC"\n Output: "ABC"',
        solution="class Solution:\n    def gcdOfStrings(self, s1: str, s2: str) -> str:\n        return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''",
    )

    problem32 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Longest Common Prefix',
        description='Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".',
        language="Python",
        example='Input: strs = ["flower","flow","flight"]\n Output: "fl"',
        solution='class Solution(object):\n    def longestCommonPrefix(self, strs):\n        result = ""\n        for n in zip(*strs):\n            if len(set(n)) == 1:\n                result += n[0]\n            else:\n                return result\n        return result',
    )

    # Strings - Medium

    problem33 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Generate Parentheses',
        description='Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.',
        language="Python",
        example='Input: n = 3\n Output: ["((()))","(()())","(())()","()(())","()()()"]',
        solution="class Solution:\n    def generateParenthesis(self, n: int) -> List[str]:\n        bfs = [(0, 0, '')]\n        for _ in range(n * 2):\n            new = []\n            for l, r, s in bfs:\n                if l + 1 <= n:\n                    new.append((l + 1, r, s + '('))\n                if l - r:\n                    new.append((l, r + 1, s + ')'))\n            bfs = new\n        return [s for l, r, s in bfs]",
    )

    problem34 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Palindromic Substrings',
        description='Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.',
        language="Python",
        example='Input: s = "abc"\n Output: 3\n Explanation: Three palindromic strings: "a", "b", "c".',
        solution="class Solution:\n    def countSubstrings(self, s: str) -> int:\n        self.res = 0\n        def helper(s, l, r):\n            while l >= 0 and r < len(s) and s[l] == s[r]:\n                l -= 1\n                r += 1\n                self.res += 1\n		for i in range(len(s)):\n			helper(s, i, i)\n			helper(s, i, i + 1)\n		return self.res",
    )

    problem35 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Group Anagrams',
        description='Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        language="Python",
        example='Input: strs = ["eat","tea","tan","ate","nat","bat"]\n Output: [["bat"],["nat","tan"],["ate","eat","tea"]]',
        solution="class Solution(object):\n    def groupAnagrams(self, strs):\n        def convert(s):\n            res = [0]*26\n            for char in s:\n                res[ord(char)-ord('a')] += 1\n            return tuple(res)\n        rec = {}\n        res = []\n        for s in strs:\n            t = convert(s)\n            if t in rec:\n                res[rec[t]].append(s)\n            else:\n                res.append([s])\n                rec[t] = len(res)-1\n        return res",
    )

    problem36 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Reorganize String',
        description='Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same. If possible, output any possible result.  If not possible, return the empty string.',
        language="Python",
        example='Input: s = "aab"\n Output: "aba"',
        solution="class Solution:\n    def reorganizeString(self, S):\n        res, c = [], Counter(S)\n        pq = [(-value,key) for key,value in c.items()]\n        heapq.heapify(pq)\n        p_a, p_b = 0, ''\n        while pq:\n            a, b = heapq.heappop(pq)\n            res += [b]\n            if p_a < 0:\n                heapq.heappush(pq, (p_a, p_b))\n            a += 1\n            p_a, p_b = a, b\n        res = ''.join(res)\n        if len(res) != len(S): return ''\n        return res",
    )

    problem37 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Basic Calculator II',
        description='Given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.',
        language="Python",
        example='Input: s = "3+2*2"\n Output: 7',
        solution="class Solution:\n    def calculate(self, s: str) -> int:\n        num, presign, stack=0, '+', []\n        for i in s+'+':\n            if i.isdigit():\n                num = num*10 +int(i)\n            elif i in '+-*/':\n                if presign =='+':\n                    stack.append(num)\n                if presign =='-':\n                    stack.append(-num)\n                if presign =='*':\n                    stack.append(stack.pop()*num)\n                if presign == '/':\n                    stack.append(math.trunc(stack.pop()/num))\n                presign = i\n                num = 0\n        return sum(stack)",
    )

    problem38 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Multiply Strings',
        description='Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.',
        language="Python",
        example='Input: num1 = "2", num2 = "3"\n Output: "6"',
        solution='class Solution:\n    def multiply(self, num1: str, num2: str) -> str:\n        n, m = len(num1), len(num2)\n        if not n or not m:\n            return "0"\n        result = [0] * (n + m)\n        for i in reversed(range(n)):\n            for j in reversed(range(m)):\n                current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j])\n                result[i + j + 1] = current % 10\n                result[i + j] += current // 10\n        for i, c in enumerate(result):\n            if c != 0:\n                return "".join(map(str, result[i:]))\n        return "0"',
    )

    # Strings - Hard

    problem39 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Distinct Subsequences',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        language="Python",
        example='Input: s = "rabbbit", t = "rabbit"\n Output: 3\n Explanation:\n As shown below, there are 3 ways you can generate "rabbit" from S.',
        solution='class Solution(object):\n    def numDistinct(self, s, t):\n        n1, n2 = len(s), len(t)\n        dp = [1] + [0] * n2\n        for i in range(1, n1+1):\n            pre = dp[0]\n            for j in range(1, n2+1):\n                dp[j], pre = dp[j] + pre * (s[i-1] == t[j-1]), dp[j]\n        return dp[-1]',
    )

    problem40 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Text Justification',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        language="Python",
        example='Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16\n Output:\n [\n "This    is    an",\n "example  of text",\n "justification.  "\n ]',
        solution='class Solution(object):\n    def fullJustify(self, words, maxWidth):\n        line = []\n        word_count = 0\n        char_count = 0\n        res = []\n        for word in words:\n            length = char_count+1+len(word)\n            if length > maxWidth:\n                space_left = maxWidth - char_count\n                if word_count == 1:\n                    string = line[0]+" "*(maxWidth-len(line[0]))\n                    res.append(string)\n                    line = [word]\n                    char_count = len(word)\n                else:\n                    q, r = divmod(space_left, word_count-1)\n                    front = (" "*(q+2)).join(line[:r+1])\n                    end = (" "*(q+1)).join(line[r+1:])\n                    string = front+" "*(q+1)+end\n                    if string:\n                        res.append(string)\n                    line = [word]\n                    word_count = 1\n                    char_count = len(word)\n            else:\n                if line:\n                    char_count += len(word)+1\n                else:\n                    char_count += len(word)\n                line.append(word)\n                word_count += 1\n        if line:\n            line = " ".join(line)\n            line += " "*(maxWidth-len(line))\n            res.append(line)\n        return res',
    )

    # Trees

    # Trees - Easy

    problem40 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Range Sum of BST',
        description='Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].',
        language="Python",
        example="Input: root = [10,5,15,3,7,null,18], low = 7, high = 15\n Output: 32\n Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.",
        solution='class Solution:\n    def rangeSumBST(self, root, L, R):\n        def dfs(root):\n            if not root:\n                return\n            if L <= root.val <= R:\n                self.res += root.val\n            if L <= root.val:\n                dfs(root.left)\n            if R >= root.val:\n                dfs(root.right)\n        self.res = 0\n        dfs(root)\n        return self.res',
    )

    problem41 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Maximum Depth of Binary Tree',
        description='Given the root of a binary tree, return its maximum depth. A binary tree\'s maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.',
        language="Python",
        example="Input: root = [3,9,20,null,null,15,7]\n Output: 3",
        solution='class Solution(object):\n    def maxDepth(self, root):\n        if root == None:\n            return 0\n        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))',
    )

    problem42 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Invert Binary Tree',
        description='Given the root of a binary tree, invert the tree, and return its root.',
        language="Python",
        example="Input: root = [4,2,7,1,3,6,9]\n Output: [4,7,2,9,6,3,1]",
        solution='class Solution:\n    def invertTree(self, root):\n        if root:\n            invert = self.invertTree\n            root.left, root.right = invert(root.right), invert(root.left)\n            return root',
    )

    problem43 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Binary Tree Postorder Traversal',
        description='Given the root of a binary tree, return the postorder traversal of its nodes\' values.',
        language="Python",
        example="Input: root = [1,null,2,3]\n Output: [3,2,1]",
        solution='class Solution(object):\n    def postorderTraversal(self, root):\n        def dfs(root):\n            if not root:\n                return\n            dfs(root.left)\n            dfs(root.right)\n            res.append(root.val)\n        res = []\n        dfs(root)\n        return res',
    )

    problem44 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Binary Tree Preorder Traversal',
        description='Given the root of a binary tree, return the preorder traversal of its nodes\' values.',
        language="Python",
        example="Input: root = [1,null,2,3]\n Output: [1,2,3]",
        solution='class Solution(object):\n    def preorderTraversal(self, root):\n        if not root:\n           return []\n        elif not root.left and not root.right:\n            return [root.val]\n        l = self.preorderTraversal(root.left)\n        r = self.preorderTraversal(root.right)\n        return [root.val]+l+r',
    )

    problem45 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Diameter of Binary Tree',
        description='Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.',
        language="Python",
        example="Input: root = [1,2,3,4,5]\n Output: 3\n Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].",
        solution='class Solution(object):\n    def diameterOfBinaryTree(self, root):\n        self.ans = 0\n        def depth(p):\n            if not p:\n                return 0\n            left, right = depth(p.left), depth(p.right)\n            self.ans = max(self.ans, left+right)\n            return 1 + max(left, right)\n        depth(root)\n        return self.ans',
    )

    problem46 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Symmetric Tree',
        description='Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).',
        language="Python",
        example="Input: root = [1,2,2,3,4,4,3]\n Output: true",
        solution='class Solution(object):\n    def isSymmetric(self, root):\n        def isSym(root1, root2):\n            if root1 == None and root2 == None:\n                return True\n            elif root1 == None and root2 != None:\n                return False\n            elif root1 != None and root2 == None:\n                return False\n            else:\n                if root1.val != root2.val:\n                    return False\n                else:\n                    return isSym(root1.left, root2.right) and isSym(root1.right,root2.left)\n        return root == None or isSym(root.left,root.right)',
    )

    problem47 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Same Tree',
        description='Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.',
        language="Python",
        example="",
        solution='class Solution(object): def isSameTree(self, p, q): if p == None and q == None: return True elif p == None and q != None: return False elif p != None and q == None: return False else: if p.val != q.val: return False else: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)',
    )

    problem48 = Problem(
        category='Trees',
        difficulty='Easy',
        title='Subtree of Another Tree',
        description='Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise. A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node\'s descendants. The tree tree could also be considered as a subtree of itself.',
        language="Python",
        example="Input: p = [1,2,3], q = [1,2,3]\n Output: true",
        solution='class Solution(object):\n    def isSameTree(self, p, q):\n        queue = collections.deque([p,q])\n        while queue:\n            u1 = queue.popleft()\n            u2 = queue.popleft()\n            if u1 == None and u2 != None:\n                return False\n            if u1 != None and u2 == None:\n                return False\n            if u1 != None and u2 != None:\n                if u1.val != u2.val:\n                    return False\n                else:\n                    queue.append(u1.left)\n                    queue.append(u2.left)\n                    queue.append(u1.right)\n                    queue.append(u2.right)\n        return True',
    )

    # Trees - Medium

    problem48 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Insert into a Binary Search Tree',
        description='You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST. Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.',
        language="Python",
        example="Input: root = [4,2,7,1,3], val = 5\n Output: [4,2,7,1,3,5]",
        solution='class Solution:\n    def insertIntoBST(self, root, val):\n        if val < root.val:\n            if not root.left:\n                root.left = TreeNode(val)\n            else:\n                self.insertIntoBST(root.left, val)\n        else:\n            if not root.right:\n                root.right = TreeNode(val)\n            else:\n                self.insertIntoBST(root.right, val)\n        return root',
    )

    problem49 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Count Good Nodes in Binary Tree',
        description='Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.',
        language="Python",
        example="Input: root = [3,1,4,3,null,1,5]\n Output: 4",
        solution="class Solution:\n    def goodNodes(self, root: TreeNode):\n        maxSoFar = -1*float('inf')\n        def postorder(cur,maxSoFar):\n            count = 0\n            if cur is None:\n                return count\n            if cur.val >= maxSoFar:\n                count += 1\n            maxSoFar = max(maxSoFar, cur.val)\n            left_count = postorder(cur.left,maxSoFar)\n            right_count = postorder(cur.right,maxSoFar)\n            count += left_count + right_count\n            return count\n        res = postorder(root,maxSoFar)\n        return res",
    )

    problem50 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Construct Binary Tree from Preorder and Postorder Traversal',
        description='Return any binary tree that matches the given preorder and postorder traversals. Values in the traversals pre and post are distinct positive integers.',
        language="Python",
        example="Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]\n Output: [1,2,3,4,5,6,7]",
        solution='class Solution:\n    def constructFromPrePost(self, pre, post):\n        if pre:\n            root = TreeNode(pre.pop(0))\n            post.pop()\n            if pre:\n                if pre[0] == post[-1]:\n                    root.left = self.constructFromPrePost(pre, post)\n                else:\n                    l, r = post.index(pre[0]), pre.index(post[-1])\n                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])\n                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:])\n                    return root',
    )

    problem51 = Problem(
        category='Trees',
        difficulty='Medium',
        title='Binary Tree Right Side View',
        description='Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.',
        language="Python",
        example="Input: root = [1,2,3,null,5,null,4]\n Output: [1,3,4]",
        solution='class Solution(object):\n    def rightSideView(self, root):\n        if root == None:\n            return[]\n        ans = [root.val]\n        left = ans + self.rightSideView(root.left)\n        right = ans + self.rightSideView(root.right)\n        if len(right) >= len(left):\n            return right\n        return right + left[len(right):]',
    )

    # Trees - Hard

    problem52 = Problem(
        category='Trees',
        difficulty='Hard',
        title='Binary Tree Maximum Path Sum',
        description='A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node\'s values in the path. Given the root of a binary tree, return the maximum path sum of any path.',
        language="Python",
        example="Input: root = [1,2,3]\n Output: 6\n Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.",
        solution="class Solution:\n    def maxPathSum(self, root):\n        def maxSum(root):\n            if not root:\n                return 0\n            l_sum = maxSum(root.left)\n            r_sum = maxSum(root.right)\n            l = max(0, l_sum)\n            r = max(0, r_sum)\n            res[0] = max(res[0], root.val + l + r)\n            return root.val + max(l, r)\n        res = [-float('inf')]\n        maxSum(root)\n        return res[0]",
    )

    problem53 = Problem(
        category='Trees',
        difficulty='Hard',
        title='Vertical Order Traversal of a Binary Tree',
        description='Given the root of a binary tree, calculate the vertical order traversal of the binary tree. For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0). The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the vertical order traversal of the binary tree.',
        language="Python",
        example="Input: root = [3,9,20,null,null,15,7]\n Output: [[9],[3,15],[20],[7]]",
        solution="class Solution(object):\n    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:\n        hash = defaultdict(list)\n        def walk(root,row,col):\n            if root is None:\n                return\n            hash[col].append((row,root.val))\n            walk(root.left,row+1,col-1)\n            walk(root.right,row+1,col+1)\n        walk(root,0,0)\n        res = []\n        for key in sorted(hash.keys()):\n            hash[key].sort(key = lambda x: (x[0],x[1]))\n            res.append([x[1] for x in hash[key]])\n        return res",
    )

    # Hash Table
    # Hash Table - Easy
    problem54 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Number of Good Pairs',
        description='Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.',
        language="Python",
        example="Input: nums = [1,2,3,1,1,3]\n Output: 4\n Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.",
        solution="class Solution:\n    def numIdenticalPairs(self, nums: List[int]) -> int:\n        ans = 0\n        d = defaultdict(list)\n        for i in range(len(nums)):\n            d[nums[i]].append(i)\n        for k,v in d.items():\n            n = len(v)\n            if n > 1:\n                ans += ((n-1) * n) // 2\n        return ans",
    )

    problem55 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Jewels and Stones',
        description='You\'re given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels. Letters are case sensitive, so "a" is considered a different type of stone from "A".',
        language="Python",
        example='Input: jewels = "aA", stones = "aAAbbbb"\n Output: 3',
        solution="class Solution:\n    def numJewelsInStones(self, J: str, S: str) -> int:\n        jewels = set(J)\n        count_of_jewel = 0\n        for item in S:\n            if item in jewels:\n                count_of_jewel += 1\n        return count_of_jewel",
    )

    problem56 = Problem(
        category='Hash',
        difficulty='Easy',
        title='How Many Numbers Are Smaller Than the Current Number',
        description='Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j\'s such that j != i and nums[j] < nums[i]. Return the answer in an array.',
        language="Python",
        example="Input: nums = [8,1,2,2,3]\n Output: [4,0,1,1,3]",
        solution="class Solution:\n    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:\n        counts = [0]*101\n        for nn in nums:\n            counts[nn] += 1\n        return_counts = list()\n        for nn in nums:\n            if nn ==0:\n                return_counts.append(0)\n            else:\n                return_counts.append(sum(counts[:nn]))\n        return return_counts",
    )

    problem57 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Design HashMap',
        description='Design a HashMap without using any built-in hash table libraries.',
        language="Python",
        example='Input ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]\n [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]\n Output\n [null, null, null, 1, -1, null, 1, null, -1]',
        solution="cclass MyHashMap:\n    def __init__(self):\n        self.golden_ratio = 1.618\n        self.table_size = 65536\n        self.table = [[] for _ in range(self.table_size)]\n        self.hash = lambda i: i*math.ceil(self.golden_ratio*self.table_size) % self.table_size\n    def put(self, key, value):\n        self.remove(key)\n        hkey = self.hash(key)\n        self.table[hkey].append((key, value))\n    def get(self, key):\n        hkey = self.hash(key)\n        ix = -1\n        for i, x in enumerate(self.table[hkey]):\n            if x[0] == key:\n                ix = i\n        return -1 if ix==-1 else self.table[hkey][ix][1]\n    def remove(self, key):\n        hkey = self.hash(key)\n        ix = -1\n        for i, x in enumerate(self.table[hkey]):\n            if x[0] == key:\n                ix = i\n        if ix >= 0:\n            del self.table[hkey][ix]",
    )

    problem58 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Single Number',
        description='Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.',
        language="Python",
        example="Input: nums = [2,2,1]\n Output: 1",
        solution="class Solution:\n    def singleNumber(self, nums):\n        res = nums[0]\n        for i in range(1, len(nums)):\n            res ^= nums[i]\n        return res",
    )

    problem59 = Problem(
        category='Hash',
        difficulty='Easy',
        title='Verifying an Alien Dictionary',
        description='In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.',
        language="Python",
        example='Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"\n Output: true\n Explanation: As "h" comes before "l" in this language, then the sequence is sorted.',
        solution='class Solution:\n    def isAlienSorted(self, words: List[str], order: str) -> bool:\n        mapping = {char: i for i, char in enumerate(order)}\n        alien_char_codes = [[mapping[char] for char in word] for word in words]\n        for curr_word, next_word in zip(alien_char_codes, alien_char_codes[1:]):\n            if curr_word > next_word:\n                return False\n        return True',
    )

    # Hash Table - Medium

    problem60 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Top K Frequent Words',
        description='Given a non-empty list of words, return the k most frequent elements. Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.',
        language="Python",
        example="",
        solution="class Solution:\n    def topKFrequent(self, words, k):\n        d = {}\n        for word in words:\n            d[word] = d.get(word, 0) + 1\n        ret = sorted(d, key=lambda word: (-d[word], word))\n        return ret[:k]",
    )

    problem61 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Daily Temperatures',
        description='Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.',
        language="Python",
        example="",
        solution="class Solution(object): def dailyTemperatures(self, temperatures): res = [0]*len(temperatures) T = [-1]*71 for i in range(len(temperatures)-1, -1, -1): t = temperatures[i] for j in range(t-1, 29, -1): T[j-30] = i if T[t-30] != -1: res[i] = T[t-30]-i return res",
    )

    problem62 = Problem(
        category='Hash',
        difficulty='Medium',
        title='Subarray Sum Equals K',
        description='Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.',
        language="Python",
        example="",
        solution="class Solution: def subarraySum(self, nums, k): preSums = {0: 1} s = 0 res = 0 for num in nums: s += num res += preSums.get(s - k, 0) preSums[s] = preSums.get(s, 0) + 1 return res",
    )

    # Hash Tables - Hard

    problem63 = Problem(
        category='Hash',
        difficulty='Hard',
        title='Group Anagrams',
        description='Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        language="Python",
        example="",
        solution="class Solution(object): def groupAnagrams(self, strs): def convert(s): res = [0]*26 for char in s: res[ord(char)-ord('a')] += 1 return tuple(res) rec = {} res = [] for s in strs: t = convert(s) if t in rec: res[rec[t]].append(s) else: res.append([s]) rec[t] = len(res)-1 return res",
    )

    problem64 = Problem(
        category='Hash',
        difficulty='Hard',
        title='Minimum Window Substring',
        description='Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.',
        language="Python",
        example="",
        solution="class Solution: def minWindow(self, s, t): dicT = collections.Counter(t) dicS = {} rec = set() j = 0 res = float('inf') for i, c in enumerate(s): if c not in dicS: dicS[c] = 1 else: dicS[c] += 1 if c in dicT and dicT[c] <= dicS[c]: rec.add(c) while len(rec) == len(dicT): dicS[s[j]] -= 1 if s[j] in dicT and dicT[s[j]] > dicS[s[j]]: rec.remove(s[j]) if res > i-j+1: start = j end = i res = i-j+1 j += 1 if res == float('inf'): return "" return s[start:end+1]",
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

    db.session.commit()


def undo_problems():
    db.session.execute('TRUNCATE problems;')
    db.session.commit()
