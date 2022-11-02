class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(n):
            addVal = ""
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                addVal = "FizzBuzz"
            elif (i + 1) % 3 == 0 == 0:
                addVal = "Fizz"
            elif (i + 1) % 5 == 0:
                addVal = "Buzz"
            else:
                addVal = str(i + 1)
            list.append(addVal)
        return list