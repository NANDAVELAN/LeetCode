class Solution:
  def maxFreqSum(self, s: str) -> int:
    vowels = {}
    consonants = {}
    for i in s:
      if i in 'aeiou':
        vowels[i] = vowels.get(i,0) + 1    #get returns the value and then incremt
      else:
        consonants[i] = consonants.get(i,0) + 1
    return max(vowels.values(), default=0) + max(consonants.values(), default=0)
