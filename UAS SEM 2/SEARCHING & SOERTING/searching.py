# searching.py
import math

class Searching:
    def binary_search(self, arr, x):
        print("==============")
        print("Proses Binary Search:")
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                print(f"Data ditemukan padaaa indeks {mid}")
                print("==============")
                return
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        print("Data tidak ditemukan")
        print("==============")

    def linear_search(self, arr, x):
        print("==============")
        print("Proses Linear Search:")
        for i in range(len(arr)):
            if arr[i] == x:
                print(f"Data ditemukan di indeks {i}")
                print("==============")
                return
        print("Data tidak ditemukan")
        print("==============")

    def jump_search(self, arr, x):
        print("==============")
        print("Proses Jump Search:")
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n) - 1] < x:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("Data tidak ditemukan")
                print("==============")
                return
        for i in range(prev, min(step, n)):
            if arr[i] == x:
                print(f"Data ditemukan di indeks {i}")
                print("==============")
                return
        print("Data tidak ditemukan")
        print("==============")

    def rekursive_search(self, arr, l, r, x):
        if r >= l:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.rekursive_search(arr, l, mid - 1, x)
            else:
                return self.rekursive_search(arr, mid + 1, r, x)
        else:
            return -1
