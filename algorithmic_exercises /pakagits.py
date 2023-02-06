# Check the parentheses. You have 3 types of parentheses () [] {}, for example! ({{}} {] []}})!
# Check that each open parenthesis has a closing parenthesis.
class Solution(object):
    def isValid(self, s):

        # s = '(([{()}]))'
        # s = input('please input parentheses string: ')
        if len(s) % 2 > 0:
            return False
        else:
            for i in range(len(s) // 2):
                h = len(s) // 2
                x = s[(h - 1):(h + 1)]
                if x == '()' or x == '[]' or x == '{}':
                    s = s.replace(x, "")
                else:
                    break
            return s == ''


s = '(([{()}]))()'
mm = Solution()
print(mm.isValid(s))
