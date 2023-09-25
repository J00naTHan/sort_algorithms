def heapify(arr, N, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2
  
  if left < N and arr[largest] < arr[left]:
    largest = left  
  if right < N and arr[largest] < arr[right]:
    largest = right
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, N, largest)


def heapSort(arr):
  N = len(arr)
  
  for i in range(N // 2, -1, -1):
    heapify(arr, N, i)
  for i in range(N-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)


size, arr = int(input("Informe o tamanho do array: ")), []

for each in range(0, size):
  number = int(input(f"Insira o número a ser colocado na posição {each} do array: "))
  arr.append(number)

heapSort(arr)
print(f"\nArray ordenado: {arr}")
