def printBoolArray(arr):
  uniqueFiles = sorted(list({el[0] for el in arr}), key=lambda x:x[1])
  uniqueFiles = [el[0] for el in uniqueFiles]
  for file in uniqueFiles:
    returnList = []
    lista = [m[1] for m in arr if m[0][0] == file]
    returnList = [str(int(any(n in elem for elem in lista))) for n in objects]
    print(file, ' '.join(returnList))



T, N = map(int, input().split())
objects = ["bison", "elephant", "horse", "ibis", "sky", "mountain", "building", "flower", "sand", "tree", "field", "road", "tower", "ocean", "cliff", "waterfall"]


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
    readObjects.append([(nome_arquivo, j), atributo_objeto,x1, y1, x2, y2])
  printBoolArray(readObjects)

if T == 2:
  frequencia_objetos = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    frequencia_objetos.append(atributo_objeto)
  # printPercentages(frequencia_objetos,objetos)

if T == 3:
  coordenadas = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    coordenadas.append([x1, y1, x2, y2])
  # calculaMedias(coordenadas)

if T == 4:
  coordenadas = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    coordenadas.append(dict(fileName = nome_arquivo, objectAttribute=atributo_objeto,coord = [x1, y1, x2, y2]))
  # prinPositions(coordenadas)
