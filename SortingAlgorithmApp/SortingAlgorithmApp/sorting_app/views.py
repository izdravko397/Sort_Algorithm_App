from django.shortcuts import render
from django.http import JsonResponse
import numpy as np

def quick_sort_animation(arr, low, high, steps):
    if low < high:
        pivot_index = partition_animation(arr, low, high, steps)
        quick_sort_animation(arr, low, pivot_index - 1, steps)
        quick_sort_animation(arr, pivot_index + 1, high, steps)

def partition_animation(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps.append(arr.copy())
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append(arr.copy())
    return i + 1

def index(request):
    return render(request, 'index.html')

def sort_array(request):
    if request.method == 'POST':
        print("Received POST request")
        size = int(request.POST.get('size', 50))
        print("Requested size:", size)
        arr = np.random.randint(1, size + 1, size).tolist()
        steps = [arr.copy()]
        quick_sort_animation(arr, 0, len(arr) - 1, steps)
        return JsonResponse(steps, safe=False)
    else:
        print("Invalid request method")
        return JsonResponse({'error': 'Invalid request method'}, status=400)