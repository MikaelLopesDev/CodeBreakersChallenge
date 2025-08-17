class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        list_output_anagrams = []

        list_word_aux = strs

        for word_anagram in strs:

            list_aux_anagrams = [word for word in list_word_aux if sorted(word) == sorted(word_anagram)]
            list_word_aux.remove(word_anagram)
            if not list_aux_anagrams in list_output_anagrams:
                    list_output_anagrams.append(list_aux_anagrams)


        return list_output_anagrams


if __name__ == '__main__':
    anagram =  Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(anagram)

