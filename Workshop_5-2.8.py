def reverse(r):
  rev=""
  for char in r:
    rev = char+rev
  return rev
print(reverse("Jenish"))