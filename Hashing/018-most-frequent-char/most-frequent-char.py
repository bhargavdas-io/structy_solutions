def most_frequent_char(s):
  char_map = {}
  for i in range(len(s)):
    char_map[s[i]] = 1 + char_map.get(s[i], 0)
  val = max(char_map, key = char_map.get)
  