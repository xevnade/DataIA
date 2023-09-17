Matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]

def SumDiagonal(Matrix):
  Diagonal1 = 0
  Diagonal2 = 0
  panjang = len(Matrix[1])
  for a in range(len(Matrix)):
    for b in range(len(Matrix[a])):
      if a == b:
        Diagonal1 = Diagonal1 + Matrix[a][b]
  for a in range(len(Matrix)):
    for b in range(len(Matrix[a])):
      if a == (panjang-b-1):
        Diagonal2 = Diagonal2 + Matrix[a][b]
  print(Diagonal1-Diagonal2)

SumDiagonal(Matrix)
