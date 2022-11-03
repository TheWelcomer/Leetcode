class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs
        uniCommonStr = ""
        for i in range(len(strs) - 1):
            firstStr = strs[i]
            secondStr = strs[i + 1]
            minimum = min(len(firstStr), len(secondStr))
            commonStr = ""
            for j in range(minimum):
                if firstStr[j] == secondStr[j]:
                    commonStr += firstStr[j]
                else:
                    break
            if i == 0:
                uniCommonStr = commonStr
            elif len(uniCommonStr) > len(commonStr):
                uniCommonStr = commonStr
        return uniCommonStr

lister = ["a"]
print(Solution.longestCommonPrefix(lister, lister))