from app.models import db, Problem

# Adds a demo user, you can add other users here if you want


def seed_problems():

    # Arrays - Easy
    problem1 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Running Sum of 1d Array',
        description='Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.',
        solution='def runningSum(self, nums: List[int]) -> List[int]: for i in range(1, len(nums)): nums[i] += nums[i - 1] return nums',
        solved=False
    )

    problem2 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Shuffle the Array',
        description='Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].',
        solution='def shuffle(self, nums: List[int], n: int) -> List[int]: temp = [] for i in range(n): temp.append(nums[i]) temp.append(nums[n + i]) return temp',
        solved=False
    )

    problem3 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Number of Good Pairs',
        description='Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.',
        solution='def numIdenticalPairs(self, nums: List[int]) -> int: ans = 0 d = defaultdict(list) for i in range(len(nums)): d[nums[i]].append(i) for k,v in d.items(): n = len(v) if n > 1: ans += ((n-1) * n) // 2 return ans',
        solved=False
    )

    problem4 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='How Many Numbers Are Smaller Than the Current Number',
        description='Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j\'s such that j != i and nums[j] < nums[i]. Return the answer in an array.',
        solution='def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: lookup = {} for i, v in enumerate(sorted(nums)): if v in lookup: continue lookup[v] = i return [lookup[num] for num in nums]',
        solved=False
    )

    problem5 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find N Unique Integers Sum up to Zero',
        description='Given an integer n, return any array containing n unique integers such that they add up to 0.',
        solution='def sumZero(self, n): a = range(1, n) return a + [-sum(a)]',
        solved=False
    )

    problem6 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Fibonacci Number',
        description='The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. Given n, calculate F(n).',
        solution='def fib(N): if N == 0: return 0 memo = (0,1) for _ in range(2,N+1): memo = (memo[-1], memo[-1] + memo[-2]) return memo[-1]',
        solved=False
    )

    problem7 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Squares of a Sorted Array',
        description='Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.',
        solution='def sortedSquares(self, A: List[int]) -> List[int]: for i in range(len(A)) : A[i] = A[i]*A[i] A.sort() return A',
        solved=False
    )

    problem8 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Find Common Characters',
        description='Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer. You may return the answer in any order.',
        solution='def commonChars(self, A: List[str]) -> List[str]: ans = [] d1 = Counter(A[0]) for i in range(1,len(A)): d2 = Counter(A[i]) d1 = d1 & d2 ans = list(d1.elements()) return ans',
        solved=False
    )

    problem9 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Move Zeroes',
        description='Given an integer array nums, move all 0\'s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array',
        solution='def moveZeroes(self, nums): i = 0 for j in range(len(nums)): if nums[j] != 0: nums[i], nums[j] = nums[j], nums[i] i += 1',
        solved=False
    )

    problem10 = Problem(
        category='Arrays',
        difficulty='Easy',
        title='Missing Number',
        description='Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.',
        solution='def missingNumber(self, nums): n = len(nums) return n * (n+1) / 2 - sum(nums)',
        solved=False
    )

    # Arrays - Medium

    problem11 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find All Duplicates in an Array',
        description='Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.',
        solution='def findDuplicates(self, nums): result = [] for x in nums: if nums[abs(x)-1] < 0: result.append(abs(x)) else: nums[abs(x)-1] = -1*nums[abs(x)-1] return result',
        solved=False
    )

    problem12 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Max Area of Island',
        description='You are given an m x n binary matrix grid. An island is a group of 1\'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island, return 0',
        solution='def maxAreaOfIsland(self, grid): m, n = len(grid), len(grid[0]) def dfs(i, j): if 0 <= i < m and 0 <= j < n and grid[i][j]: grid[i][j] = 0 return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) return 0 areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]] return max(areas) if areas else 0',
        solved=False
    )

    problem13 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Rotate Image',
        description='You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.',
        solution='def rotate(self, matrix): n = len(matrix) for i in range(n): for k in xrange(0, n - 1 - i): matrix[i][k], matrix[n - 1 - k][n - 1 - i] = matrix[n - 1 - k][n - 1 - i], matrix[i][k] for j in range(n): for k in range(n/2): matrix[k][j], matrix[n - 1 - k][j] = matrix[n - 1 - k][j], matrix[k][j]',
        solved=False
    )

    problem14 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Product of Array Except Self',
        description='Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer',
        solution='def productExceptSelf(self, nums: List[int]) -> List[int]: res = [1] * len(nums) left = 1 right = 1 for i in range(1, len(nums)): left *= nums[i - 1] res[i] *= left right *= nums[~i + 1] res[~i] *= right return res',
        solved=False
    )

    problem15 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Combination Sum',
        description='Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.',
        solution='class Solution(object): def combinationSum(self, candidates, target): ret = [] self.dfs(candidates, target, [], ret) return ret def dfs(self, nums, target, path, ret): if target < 0: return if target == 0: ret.append(path) return for i in range(len(nums)): self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)',
        solved=False
    )

    problem16 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Find the Duplicate Number',
        description='Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.',
        solution='class Solution(object): def findDuplicate(self, nums): if len(nums) == 0: return 0 low = 1 high = len(nums) while low < high: mid = low + int((high-low)>>1) count = 0 for x in nums: if x <= mid: count = count + 1 if count > mid: high = mid else: low = mid+1 return low',
        solved=False
    )

    problem17 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Container With Most Water',
        description='Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water. Notice that you may not slant the container.',
        solution='class Solution: def maxArea(self, height: List[int]) -> int: l = 0 r = len(height)-1 res = 0 while l < r: area = (r - l) * min(height[l], height[r]) res = max(area,res) if height[l]<height[r]: l = l+1 else: r = r-1 return res',
        solved=False
    )

    problem18 = Problem(
        category='Arrays',
        difficulty='Medium',
        title='Subarray Sum Equals K',
        description='Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.',
        solution='def subarraySum(self, nums, k): preSums = {0: 1} s = 0 res = 0 for num in nums: s += num res += preSums.get(s - k, 0) preSums[s] = preSums.get(s, 0) + 1 return res',
        solved=False
    )

    # Array - Hard
    problem19 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Trapping Rain Water',
        description='Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.',
        solution='class Solution: def trap(self, height): water, left_highest, right_highest, j = 0, [0]*len(height), [0]*len(height), len(height)-2 for i in xrange(1, len(height)): left_highest[i] = max(left_highest[i-1], height[i-1]) right_highest[j] = max(right_highest[j+1], height[j+1]) j -= 1 for i in xrange(1, len(height)-1): water += max(min(left_highest[i], right_highest[i]) - height[i], 0) return water',
        solved=False
    )

    problem20 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='First Missing Positive',
        description='Given an unsorted integer array nums, find the smallest missing positive integer.',
        solution='class Solution(object): def firstMissingPositive(self, nums): N, i = len(nums), 0 while i < N: while 1<=nums[i]<=N: idx_expected = nums[i]-1 if nums[i] == nums[idx_expected]: break nums[i], nums[idx_expected] = nums[idx_expected], nums[i] i = i + 1 for i in range(N): if nums[i] != i+1: return i+1 return N+1',
        solved=False
    )

    problem21 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Median of Two Sorted Arrays',
        description='Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.',
        solution='class Solution: def findMedianSortedArrays(self, nums1, nums2): a, b = sorted((nums1, nums2), key=len) m, n = len(a), len(b) after = (m + n - 1) / 2 lo, hi = 0, m while lo < hi: i = (lo + hi) / 2 if after-i-1 < 0 or a[i] >= b[after-i-1]: hi = i else: lo = i + 1 i = lo nextfew = sorted(a[i:i+2] + b[after-i:after-i+2]) return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0',
        solved=False
    )

    problem22 = Problem(
        category='Arrays',
        difficulty='Hard',
        title='Max Chunks To Make Sorted II',
        description='Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array. What is the most number of chunks we could have made?',
        solution="class Solution: def maxChunksToSorted(self, arr): min_elements = [float('inf')] * len(arr) for i in range(len(arr) - 2, -1, -1): min_elements[i] = min(min_elements[i + 1], arr[i + 1]) count = 0 max_n = arr[0] for i, n in enumerate(arr): max_n = max(max_n, arr[i]) if min_elements[i] >= max_n: count += 1 return countfor a, b in zip(arr, sorted(arr)): c1[a] += 1 c2[b] += 1 res += c1 == c2 return res",
        solved=False
    )

    # Strings
    # Strings - Easy

    problem23 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Reverse String',
        description='Write a function that reverses a string. The input string is given as an array of characters s.',
        solution="class Solution(object): def reverseString(self, s): return s[::-1]",
        solved=False
    )

    problem24 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Count Binary Substrings',
        description='Give a binary string s, return the number of non-empty substrings that have the same number of 0\'s and 1\'s, and all the 0\'s and all the 1\'s in these substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.',
        solution="class Solution(object): def countBinarySubstrings(self, s): res = 0 prev = 0 tmp = 1 for i in range(1, len(s)): if s[i] != s[i-1]: res += min(prev, tmp) prev = tmp tmp = 1 else: tmp += 1 res += min(prev, tmp) return res",
        solved=False
    )

    problem25 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Parentheses',
        description='Given a string s containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.',
        solution='class Solution: def isValid(self, s: str) -> bool: if len(s)%2!=0: return False stack = list() dic = {"(":")","{":"}","[":"]"} for i, c in enumerate(s): if s[i] in dic: stack.append(s[i]) else: if len(stack)!=0 and dic[stack[-1]] == s[i]: stack.pop() else: return False if stack: return False else: return True',
        solved=False
    )

    problem26 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome',
        description='Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.',
        solution="class Solution(object): def isPalindrome(self, s): if not s: return True i, j = 0, len(s) - 1 while i < j: while i < j and not s[i].isalnum(): i += 1 while i < j and not s[j].isalnum(): j -= 1 if s[i].lower() != s[j].lower(): return False i += 1; j -= 1 return True",
        solved=False
    )

    problem27 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Binary',
        description='Given two binary strings a and b, return their sum as a binary string.',
        solution="class Solution(object): def addBinary(self, a, b): return bin(int(a,2) + int(b,2))[2:]",
        solved=False
    )

    problem28 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Add Strings',
        description='Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.',
        solution="class Solution: def addStrings(self, num1: str, num2: str) -> str: L1, L2, n1, n2 = len(num1), len(num2), [int(i) for i in num1], [int(i) for i in num2] if L1 < L2: n2, n1 = n1, n2 n1, n2, n3 = [0] + n1, [0]*(abs(L1-L2)+1) + n2, [0]*(len(n1)+1) for i in range(len(n1)-1,-1,-1): s = n1[i]+n2[i] n3[i] = s % 10 if s > 9: n1[i-1] += int(s/10) if n3[0] == 0: n3 = n3[1:] return "".join([str(i) for i in n3])",
        solved=False
    )

    problem29 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Valid Palindrome II',
        description='Given a string s, return true if the s can be palindrome after deleting at most one character from it.',
        solution="class Solution(object): def validPalindrome(self, s): left, right = 0, len(s) - 1 while left < right: if s[left] != s[right]: one, two = s[left:right], s[left + 1:right + 1] return one == one[::-1] or two == two[::-1] left, right = left + 1, right - 1 return True",
        solved=False
    )

    problem30 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Consecutive Characters',
        description='Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character. Return the power of the string.',
        solution="class Solution: def maxPower(self, s: str) -> int: cnt = ans = 1 for i in range(1, len(s)): if s[i] == s[i - 1]: cnt += 1 ans = max(cnt, ans) else: cnt = 1 return ans",
        solved=False
    )

    problem31 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Greatest Common Divisor of Strings',
        description='For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times) Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.',
        solution="class Solution: def gcdOfStrings(self, s1: str, s2: str) -> str: return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''",
        solved=False
    )

    problem32 = Problem(
        category='Strings',
        difficulty='Easy',
        title='Longest Common Prefix',
        description='Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".',
        solution='class Solution(object): def longestCommonPrefix(self, strs): result = "" for n in zip(*strs): if len(set(n)) == 1: result += n[0] else: return result return result',
        solved=False
    )

    # Strings - Medium

    problem33 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Generate Parentheses',
        description='Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.',
        solution="class Solution: def generateParenthesis(self, n: int) -> List[str]: bfs = [(0, 0, '')] for _ in range(n * 2): new = [] for l, r, s in bfs: if l + 1 <= n: new.append((l + 1, r, s + '(')) if l - r: new.append((l, r + 1, s + ')')) bfs = new return [s for l, r, s in bfs]",
        solved=False
    )

    problem34 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Palindromic Substrings',
        description='Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.',
        solution="class Solution(object): def countSubstrings(self, s): n = len(s) dp = [[0] * n for i in xrange(n)] count = 0 for end in xrange(n): dp[end][end] = 1 count += 1 for start in xrange(end): if s[start] == s[end] and (start+1 >= end-1 or dp[start+1][end-1]): count += 1 dp[start][end] = 1 return count",
        solved=False
    )

    problem35 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Group Anagrams',
        description='Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        solution="class Solution(object): def groupAnagrams(self, strs): def convert(s): res = [0]*26 for char in s: res[ord(char)-ord('a')] += 1 return tuple(res) rec = {} res = [] for s in strs: t = convert(s) if t in rec: res[rec[t]].append(s) else: res.append([s]) rec[t] = len(res)-1 return res",
        solved=False
    )

    problem36 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Reorganize String',
        description='Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same. If possible, output any possible result.  If not possible, return the empty string.',
        solution="class Solution: def reorganizeString(self, S): res, c = [], Counter(S) pq = [(-value,key) for key,value in c.items()] heapq.heapify(pq) p_a, p_b = 0, '' while pq: a, b = heapq.heappop(pq) res += [b] if p_a < 0: heapq.heappush(pq, (p_a, p_b)) a += 1 p_a, p_b = a, b res = ''.join(res) if len(res) != len(S): return "" return res",
        solved=False
    )

    problem37 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Basic Calculator II',
        description='Given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.',
        solution='class Solution: def calculate(self, s): num, stack, sign = 0, [], "+" for i in range(len(s)): if s[i].isdigit(): num = num * 10 + int(s[i]) if s[i] in "+-*/" or i == len(s) - 1: if sign == "+": stack.append(num) elif sign == "-": stack.append(-num) elif sign == "*": stack.append(stack.pop()*num) else: stack.append(int(stack.pop()/num)) num = 0 sign = s[i] return sum(stack)',
        solved=False
    )

    problem38 = Problem(
        category='Strings',
        difficulty='Medium',
        title='Multiply Strings',
        description='Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.',
        solution='class Solution: def multiply(self, num1: str, num2: str) -> str: n, m = len(num1), len(num2) if not n or not m: return "0" result = [0] * (n + m) for i in reversed(range(n)): for j in reversed(range(m)): current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j]) result[i + j + 1] = current % 10 result[i + j] += current // 10 for i, c in enumerate(result): if c != 0: return "".join(map(str, result[i:])) return "0"',
        solved=False
    )

    # Strings - Hard

    problem39 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Distinct Subsequences',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        solution='class Solution(object): def numDistinct(self, s, t): n1, n2 = len(s), len(t) dp = [1] + [0] * n2 for i in range(1, n1+1): pre = dp[0] for j in range(1, n2+1): dp[j], pre = dp[j] + pre * (s[i-1] == t[j-1]), dp[j] return dp[-1]',
        solved=False
    )

    problem40 = Problem(
        category='Strings',
        difficulty='Hard',
        title='Text Justification',
        description='Given two strings s and t, return the number of distinct subsequences of s which equals t. A string\'s subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters\' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not). It is guaranteed the answer fits on a 32-bit signed integer.',
        solution='class Solution(object): def fullJustify(self, words, maxWidth): line = [] word_count = 0 char_count = 0 res = [] for word in words: length = char_count+1+len(word) if length > maxWidth: space_left = maxWidth - char_count if word_count == 1: string = line[0]+" "*(maxWidth-len(line[0])) res.append(string) line = [word] char_count = len(word) else: q, r = divmod(space_left, word_count-1) front = (" "*(q+2)).join(line[:r+1]) end = (" "*(q+1)).join(line[r+1:]) string = front+" "*(q+1)+end if string: res.append(string) line = [word] word_count = 1 char_count = len(word) else: if line: char_count += len(word)+1 else: char_count += len(word) line.append(word) word_count += 1 if line: line = " ".join(line) line += " "*(maxWidth-len(line)) res.append(line) return res',
        solved=False
    )

    # Trees

    # Graphs

    db.session.add(demo)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_problems():
    db.session.execute('TRUNCATE problems;')
    db.session.commit()
