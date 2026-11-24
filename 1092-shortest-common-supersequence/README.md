# [1092. Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/submissions/2202697732/)

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)
![Language: python](https://img.shields.io/badge/Language-python-blue?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-N%2FA-success?style=flat-square)
![Memory](https://img.shields.io/badge/Memory-N%2FA-informational?style=flat-square)


### Topics
`String` `Dynamic Programming` `Longest Common Subsequence`

---

### Description

Given two strings `str1` and `str2`, return *the shortest string that has both*`str1`*and*`str2`*as **subsequences***. If there are multiple valid strings, return **any** of them.

A string `s` is a **subsequence** of string `t` if deleting some number of characters from `t` (possibly `0`) results in the string `s`.

**Example 1:**

```
**Input:** str1 = "abac", str2 = "cab"
**Output:** "cabac"
**Explanation:** 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
```

**Example 2:**

```
**Input:** str1 = "aaaaaaaa", str2 = "aaaaaaaa"
**Output:** "aaaaaaaa"
```

**Constraints:**

- `1 <= str1.length, str2.length <= 1000`
	
- `str1` and `str2` consist of lowercase English letters.

---

*Solved on Nov 24, 2026 using **LeetCommit**.*
