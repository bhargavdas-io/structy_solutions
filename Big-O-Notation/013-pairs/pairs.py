def pairs(elements):
  pair_list = []
  for i in range(len(elements)):
    for j in range(i+1,len(elements)):
      pair_list.append([elements[i],elements[j]])

  return pair_list