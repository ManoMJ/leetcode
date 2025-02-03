class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        cnt = 1
        for i in range(len(chars)):
            if i > 0 and chars[i-1] == chars[i]:
                cnt += 1
            elif i > 0 and chars[i-1] != chars[i]:
                result.append(chars[i-1])
                if cnt > 1:
                    if len(str(cnt)) > 1:
                        for n in str(cnt):
                            result.append(n)
                    else:
                        result.append(str(cnt))
                cnt = 1
        if cnt == 1:
            result.append(chars[i])
        if cnt > 1:
            result.append(chars[i])
            if len(str(cnt)) > 1:
                for n in str(cnt):
                    result.append(n)
            else:
                result.append(str(cnt))
        
        chars[:len(result)] = result
        return len(result)