from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        letter_set1 = set()
        letter_set2 = set()
        dict1 = {}
        dict2 = {}

        for n in count1:
            if count1[n] in dict1:
                dict1[count1[n]] += 1
            else:
                dict1[count1[n]] = 1
            letter_set1.add(n)

        for n in count2:
            if count2[n] in dict2:
                dict2[count2[n]] += 1
            else:
                dict2[count2[n]] = 1
            letter_set2.add(n)

        if letter_set1==letter_set2 and dict1==dict2:
            return True
        else:
            return False
        