from collections import Counter 

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        set1 = set()
        set2 = set()

        for c in word1:
            set1.add(c)
        for c in word2:
            set2.add(c)

        if set1 != set2:
            return False
        dict1 = {}
        dict2 = {}
        for v in counter1.values():
            if v in dict1:
                dict1[v] += 1
            else:
                dict1[v] = 1
        for v in counter2.values():
            if v in dict2:
                dict2[v] += 1
            else:
                dict2[v] = 1

        

        for k in dict1.keys():
            if k not in dict2 or dict1[k] != dict2[k]:
                return False


        return True        