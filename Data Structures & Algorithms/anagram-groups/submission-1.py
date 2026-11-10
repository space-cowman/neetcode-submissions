class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_value_dict = defaultdict(list)
        for each_word in strs:
            sorted_each_word = ''.join(sorted(each_word))
            key_value_dict[sorted_each_word].append(each_word)
        return list(key_value_dict.values()) #oout of key value just extract each seperate values which is in form of list already