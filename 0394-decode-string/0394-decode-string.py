class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_ch = ''
        current_num = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                current_num = current_num*10 + int(ch)
            elif ch=='[':
                stack.append( (current_ch, current_num) )
                current_ch = ''
                current_num = 0
            elif ch==']':
                prev_ch, rp_cnt = stack.pop()
                current_ch = prev_ch + (current_ch * rp_cnt)
            else:
                current_ch += ch
        
        return current_ch