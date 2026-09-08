def pair_product(numbers, target_product):
  hash = {}
  for num in range(len(numbers)):
    complement = target_product % numbers[num]
    if complement not in hash:
      hash[numbers[num]] = num
    else:
      return (hash[complement], num)