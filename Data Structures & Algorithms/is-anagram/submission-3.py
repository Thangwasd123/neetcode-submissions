class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for val in s:
            if dict_s.get(val) is None:
                dict_s[val] = 1
            elif dict_s[val] >= 1:
                dict_s[val] += 1
        for val in t:
            if dict_t.get(val) is None:
                dict_t[val] = 1
            elif dict_t[val] >= 1:
                dict_t[val] += 1
        if dict_s == dict_t:
            return True
        else:
            return False