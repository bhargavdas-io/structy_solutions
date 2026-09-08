def pair_sum(numbers, target_sum):
    hash_map = {}
    for i in range(len(numbers)):
        complement = target_sum - numbers[i]
        if complement in hash_map:
            return (hash_map[complement],i)
        else:
            hash_map[numbers[i]] = hash_map.get(i,0)