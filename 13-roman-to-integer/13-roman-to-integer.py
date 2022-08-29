class Solution(object):
    def romanToInt(self, s):
        two_roman_alpha = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        roman_alpha = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        answer = 0
        while len(s) != 0:
            if s[:2] in two_roman_alpha:
                answer += two_roman_alpha[s[:2]]
                s = s[2:]
            else:
                answer += roman_alpha[s[:1]]
                s = s[1:]
        return answer
        