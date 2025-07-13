# sorting.py
class Sorting:
    def bubble_sort(self, arr):
        print("==============")
        print("Proses Bubble Sort:")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Hasil sorting:", arr)
        print("==============")

    def insertion_sort(self, arr):
        print("==============")
        print("Proses Insertion Sort:")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        print("Hasil sorting:", arr)
        print("==============")

    def selection_sort(self, arr):
        print("==============")
        print("Proses Selection Sort:")
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Hasil sorting:", arr)
        print("==============")

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            kiri = arr[:mid]
            kanan = arr[mid:]

            self.merge_sort(kiri)
            self.merge_sort(kanan)

            i = j = k = 0

            while i < len(kiri) and j < len(kanan):
                if kiri[i] < kanan[j]:
                    arr[k] = kiri[i]
                    i += 1
                else:
                    arr[k] = kanan[j]
                    j += 1
                k += 1

            while i < len(kiri):
                arr[k] = kiri[i]
                i += 1
                k += 1

            while j < len(kanan):
                arr[k] = kanan[j]
                j += 1
                k += 1
