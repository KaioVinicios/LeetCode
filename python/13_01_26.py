"""
2114- Maximum Number of Words Found in Sentences

https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""

# First solution
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        highest_number = 0
        for sentence in sentences: 
          words_in_sentence = len(sentence.split(" "))
          if words_in_sentence > highest_number: highest_number = words_in_sentence
        return highest_number
    

# Second solution
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        highest_count = 0
        for sentence in sentences: 
          words_in_sentence = len(sentence.split(" "))
          highest_count = max(highest_count, words_in_sentence)
        return highest_count