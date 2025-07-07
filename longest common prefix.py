class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

param_1 = ["flower", "flow", "flight"]
ret = Solution().longestCommonPrefix(param_1)
print(ret)  
