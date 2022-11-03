class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        uniCommonStr = ""
        for i in range(len(strs) - 1):
            firstStr = strs[i]
            secondStr = strs[i + 1]
            minimum = min(len(firstStr), len(secondStr))
            commonStr = ""
            for j in range(minimum):
                if firstStr[i] == secondStr[i + 1]:
                    commonStr += firstStr[i]
                else:
                    break
            if len(uniCommonStr) > len(commonStr):
                uniCommonStr = commonStr
        return uniCommonStr