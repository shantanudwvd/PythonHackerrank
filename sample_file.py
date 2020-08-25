class Solution:
    def isPalindrome(string: str, low: int, high: int):
        while low < high:
            if string[low].lower() != string[high].lower():
                return False
            low += 1
            high -= 1
        return True

    def allPalPartUtil(allPart: list, currPart: list, start: int, n: int,
                       string: str):
        if start >= n:
            x = currPart.copy()
            allPart.append(x)
            return
        for i in range(start, n):
            if isPalindrome(string, start, i):
                currPart.append(string[start:i + 1])
                allPalPartUtil(allPart, currPart, i + 1, n, string)
                currPart.pop()

    def pallindromePartitions(string: str):
        n = len(string)
        allPart = []
        currPart = []
        allPalPartUtil(allPart, currPart, 0, n, string)
        return allPart
        # for i in range(len(allPart)):
        #     for j in range(len(allPart[i])):
        #         print(allPart[i][j], end=" ")
        #     print()

    def partition(self, s: str) -> List[List[str]]:
        pallindromePartitions(str)
