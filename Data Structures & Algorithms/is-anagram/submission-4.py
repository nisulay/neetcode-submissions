class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #compare length first and return early
        if len(s) != len(t):
            return False

        counts_s = {}
        counts_t = {}

        for item in s:
            counts_s[item] = counts_s.get(item,0) + 1

        for item in t:
            counts_t[item] = counts_t.get(item,0) + 1

        if counts_s == counts_t:
            return True
        else:
            return False
