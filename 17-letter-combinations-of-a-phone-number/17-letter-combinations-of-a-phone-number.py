class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2let = {'2':"abc",'3':"def",
            '4':"ghi",'5':"jkl",'6':"mno",
            '7':"pqrs",'8':"tuv",'9':"wxyz"
        }

        lenD = len(digits)
        output = []

        def combine(treedepth, branch):
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

"""
    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, cur_subset: List):
            if len(cur_subset) == len(digits):
                res.append("".join(cur_subset))
                return

            for ch in digitToChar[digits[i]]:
                backtrack(i + 1, cur_subset + [ch])

        if digits:
            backtrack(0, [])
        return res
"""