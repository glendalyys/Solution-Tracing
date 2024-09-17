def optimal_alignment(a, b):
  n = len(a) + 1
  m = len(b) + 1
  v = [[0] * m for i in range(n)] # created the 2D array of 0s
  traceback = [['I'] * m for z in range(n)]

   # Initialize the first row and column

  for i in range(n):
        v[i][0] = i
  for j in range(m):
        v[0][j] = j

    # Fill in the rest of the array based on edit distance algorithm

  for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
               change = 0
            else:
              change = 1
            deletion = v[i - 1][j] + 1
            insertion = v[i][j - 1] + 1
            substitution = v[i - 1][j - 1] + change

            v[i][j] = min(deletion, insertion, substitution)

            if v[i][j] == deletion:
                traceback[i][j] = 'D'  # Deletion
                traceback.append('D')
            elif v[i][j] == insertion:
                traceback[i][j] = 'I'  # Insertion
                traceback.append('I')

            else:
                traceback[i][j] = 'S' if change == 1 else 'M'  # Substitution or Match
                traceback.append('S') if change == 1 else traceback.append('M')

# Traceback to reconstruct the optimal alignment
  i, j = n - 1, m - 1
  align = []


  while i > 0 or j > 0:
      if traceback[i][j] == 'D':
          align.append(a[i - 1] + '-')
          i -= 1
      elif traceback[i][j] == 'I':
          align.append('-' +b[j - 1])
          j -= 1
      else:
          align.append(a[i - 1] + b[j - 1])
          i -= 1
          j -= 1

  align.reverse()
  return align



