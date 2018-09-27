#https://open.kattis.com/problems/fallingapart
pieces = int(input())
numbers = [int(x) for x in input().split()]

B = int(0)
A = int(0)
for i in range(len(numbers)):
  if numbers:
    A += max(numbers)
    numbers.remove(max(numbers))
  if numbers:
    B += max(numbers)
    numbers.remove(max(numbers))
print(A,B)