class Solution(object):
    def isValid(self, s):
        answer = ''
        brackets = ['()', '[]', '{}']
        for i in s:
            answer += i
            if answer[-2:] in brackets:
                answer = answer[:-2]
        if len(answer) == 0:
            return True
        else:
            return False
        