class Solution:
    def romanToInt(self, s: str) -> int:
        romanList = ["I", "V", "X", "L", "C", "D", "M"]
        numList = [1, 5, 10, 50, 100, 500, 1000]
        retNum = 0
        couldMinus = True
        for i in range(len(s)):
            if i < len(s) - 1 and couldMinus:
                if romanList.index(s[i]) < romanList.index(s[i + 1]):
                    retNum -= numList[romanList.index(s[i])]
                    couldMinus = False
                else:
                    retNum += numList[romanList.index(s[i])]
                    couldMinus = True
            else:
                retNum += numList[romanList.index(s[i])]
                couldMinus = True

        return retNum