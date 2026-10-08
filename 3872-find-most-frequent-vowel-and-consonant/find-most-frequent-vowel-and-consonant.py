class Solution:
  def maxFreqSum(self, s: str) -> int:
    vowels = {v: 0 for v in s if v in "aeiou"}
    consonants = {c: 0 for c in s if c not in "aeiou"}
    for i in s:
      if i in vowels:
        vowels[i] += 1
      else:
        consonants[i] += 1
    return max(vowels.values(), default=0) + max(consonants.values(), default=0)
