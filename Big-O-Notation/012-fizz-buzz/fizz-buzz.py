def fizz_buzz(n):
  nums_list = []
  for i in range(1,n+1):
    nums_list.append(i)
  fz = [
        "fizzbuzz" if num % 15 == 0 else
        "buzz" if num % 5 == 0 else
        "fizz" if num % 3 == 0 else
        num
        for num in nums_list
    ]
  return fz