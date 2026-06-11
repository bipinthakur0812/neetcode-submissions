class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A defaultdict automatically creates an empty list [] for any new key
        ans_dict = defaultdict(list)
        
        for word in strs:
            # 1. Sort the word to create its unique anagram signature
            #    e.g., "tea" -> ['a', 'e', 't'] -> "aet"
            signature = "".join(sorted(word))
            
            # 2. Push the original word into its signature's bucket instantly
            ans_dict[signature].append(word)
            
        # 3. Return all the grouped lists
        return list(ans_dict.values())