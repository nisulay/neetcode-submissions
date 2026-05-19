class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #if key doesn't exist it just creates a empty list []
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
            # print(groups)

        # print(list(groups.values()))
        return list(groups.values())

