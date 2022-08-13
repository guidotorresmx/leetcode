class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2let = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        output = []
        lenD = len(digits)


        def combine(treedepth, branch):
            """"""
            if len(digits) <= 0:
                 return []

            firstDigit = digits[0]

            if (treedepth==lenD):
                output.append(branch)
            else:
                for letter in num2let[digits[treedepth]]:
                    combine(treedepth+1, branch+letter)

        combine(0, "")
        return output
