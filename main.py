import statistics

def printBoolArray(arr):
  uniqueFiles = [el[0] for el in sorted(list({el[0] for el in arr}), key=lambda x:x[1])]
  returns = []
  for file in uniqueFiles:
    returnList = []
    lista = [m[1] for m in arr if m[0][0] == file]
    returnList = [str(int(any(n in elem for elem in lista))) for n in objects]
    returns.append((file, tuple(returnList)))
  return returns

def printStatistics(arr):
  uniqueFiles = [el[0] for el in sorted(list({el[0] for el in arr}), key=lambda x:x[1])]
  returns = []
  for file in uniqueFiles:
    s1 = [1 for n in arr if n[0][0] == file]
    s2 = [(n[2]+n[4])/2 for n in arr if n[0][0] == file]
    s3 = [(n[3]+n[5])/2 for n in arr if n[0][0] == file]
    s4 = [n[4]-n[2] for n in arr if n[0][0] == file]
    s5 = [n[5]-n[3] for n in arr if n[0][0] == file]
    s6 = [(n[4]-n[2])*(n[5]-n[3]) for n in arr if n[0][0] == file]
    s7 = statistics.pstdev(s2)
    s8 = statistics.pstdev(s3)
    s9 = statistics.pstdev(s4)
    s10 = statistics.pstdev(s5)
    returns.append((file,(
      sum(s1)/2, (sum(s2)/len(s2))/128, (sum(s3)/len(s3))/128, (sum(s4)/len(s4))/128, (sum(s5)/len(s5))/128, (sum(s6)/len(s6))/128**2, s7/32, s8/32, s9/32, s10/32)))
  return returns

def printMediumArray(arr1, arr2):
  def setAverage(arr):
    arr = list(map(float, arr))
    return sum(arr)/len(arr)  
  return list(map(setAverage, zip(*[i[1] + j[1] for i, j in zip(arr1, arr2)])))

def printMedoid(arr1, arr2):
  def setDifsL1(num1, num2):
    return abs(num1 - num2)
  arr1 = [list(n) for n in arr1]
  arr2 = [list(n) for n in arr2]
  for i, n in enumerate(arr1):
    arr1[i][1] = list(map(float, arr1[i][1]))
    arr2[i][1] = list(map(float, arr2[i][1]))
  arr = [(i[0],i[1] + j[1]) for i, j in zip(arr1, arr2)]
  results = []
  for n in arr:
    for m in arr:
      result = sum([abs(l - k) for l, k in zip(n[1],m[1])])
      results.append((n[0], result))
  returns = []
  for n in arr:
    returns.append((n[0], sum([m[1] for m in results if m[0]==n[0]])))
  returns.sort(key=lambda x: x[1])
  return returns[0][0]
objects = ["bison", "elephant", "horse", "ibis", "sky", "mountain", "building", "flower", "sand", "tree", "field", "road", "tower", "ocean", "cliff", "waterfall"]

T, N = map(int, input().split())

if T == 1:
  readObjects = []
  j = 0
  last_object = ""
  for i in range(N):
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    if last_object != nome_arquivo:
      last_object = nome_arquivo
      j += 1
    readObjects.append([(nome_arquivo, j), atributo_objeto])
  listBool = printBoolArray(readObjects)
  [print(n[0], ' '.join(n[1])) for n in listBool]

if T == 2:
  readObjects = []
  j = 0
  last_object = ""
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    if last_object != nome_arquivo:
      last_object = nome_arquivo
      j += 1
    readObjects.append([(nome_arquivo, j), atributo_objeto, x1, y1, x2, y2])
  listStatics = printStatistics(readObjects)
  for i, t in listStatics:print(i, " ".join(map("{:.1f}".format, t)))

if T == 3:
  readObjects = []
  j = 0
  last_object = ""
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    if last_object != nome_arquivo:
      last_object = nome_arquivo
      j += 1
    readObjects.append([(nome_arquivo, j), atributo_objeto, x1, y1, x2, y2])
  listBool = printBoolArray(readObjects)
  listStatics = printStatistics(readObjects)
  print(" ".join([f'{n:.1f}' for n in printMediumArray(listBool, listStatics)]))

if T == 4:
  readObjects = []
  j = 0
  last_object = ""
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    if last_object != nome_arquivo:
      last_object = nome_arquivo
      j += 1
    readObjects.append([(nome_arquivo, j), atributo_objeto, x1, y1, x2, y2])
  listBool = printBoolArray(readObjects)
  listStatics = printStatistics(readObjects)
  print(printMedoid(listBool, listStatics))
