class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        pointer = 0
        while pointer < len(s):
            if s[pointer] == '[':
                pointer += 1
                continue
            elif s[pointer] == ']':
                pointer += 1
                text = ''
                while stack[-1].isalpha():
                    text = stack.pop() + text

                stack.append(text * int(stack.pop()))
            else:
                text = ''
                while pointer < len(s) and s[pointer].isalpha():
                    text += s[pointer]
                    pointer += 1
                if text:
                    stack.append(text)

                number = ''
                while pointer < len(s) and s[pointer].isdigit():
                    number += s[pointer]
                    pointer += 1
                if number:
                    stack.append(number)
            print(stack)

        return "".join(stack)


