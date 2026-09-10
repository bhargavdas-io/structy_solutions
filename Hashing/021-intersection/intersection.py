def intersection(a,b):
    hash_a = {}
    hash_b = {}
    for i in range(len(a)):
        hash_a[a[i]] = i
    for i in range(len(b)):
        hash_b[b[i]] = i
    common_elements = hash_a.keys() & hash_b.keys()
    return list(common_elements)

print(intersection(a=[4,2,1,6], b=[4,2]))
