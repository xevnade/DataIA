DATA = ['apple', 'banana', 'cherry', 'banana', 'apple']
QUERIES = ['apple', 'banana', 'grape']

def HitungKata(Array1,Array2):
  list_total = []
  for kata in Array1:
    total_kata = 0
    for buah in Array2:
      if kata == buah:
        total_kata += 1
      else:
        total_kata = total_kata
    list_total.append(total_kata)
  print(list_total)

HitungKata(QUERIES,DATA)
