def anagrams(s1, s2):
  if len(s1) != len(s2):
    return False
  hashmap_s1 = {}
  hashmap_s2 = {}
  for i in range(len(s1)):
    hashmap_s1[s1[i]] = 1 + hashmap_s1.get(s1[i], 0)
    hashmap_s2[s2[i]] = 1 + hashmap_s2.get(s2[i], 0)
  for j in hashmap_s1:
    if hashmap_s1[j] != hashmap_s2.get(j,0):
      return False
  return True