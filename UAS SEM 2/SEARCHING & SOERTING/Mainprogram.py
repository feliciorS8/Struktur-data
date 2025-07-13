# main.py dija
from sorting import Sorting
from searching import Searching

def main():
    print("==============")
    print("PROGRAM SORTING DAN SEARCHING KELOMPOK 1")
    print("==============")

    # Input data manual pisah pakai koma
    data_input = input("Masukkan data (pisahkan dengan koma): ")
    data = list(map(int, data_input.split(',')))

    # Tampilkan data hasil input
    print("==============")
    print("Data yang kamu masukkan:")
    print(data)
    print("==============")

    sorter = Sorting()
    searcher = Searching()

    while True:
        print("\nPILIH MENU UTAMA")
        print("1. Sorting")
        print("2. Searching")
        print("3. Keluar")
        menu_utama = input("Pilih menu (1/2/3): ")

        if menu_utama == '1':
            # Menu Sorting
            print("\nMenu Sorting:")
            print("a. Bubble Sort")
            print("b. Insertion Sort")
            print("c. Selection Sort")
            print("d. Merge Sort")
            pilih_sort = input("Pilih metode sorting (a/b/c/d): ")

            data_copy = data.copy()

            if pilih_sort == 'a':
                sorter.bubble_sort(data_copy)
            elif pilih_sort == 'b':
                sorter.insertion_sort(data_copy)
            elif pilih_sort == 'c':
                sorter.selection_sort(data_copy)
            elif pilih_sort == 'd':
                print("==============")
                print("Proses Merge Sort:")
                sorter.merge_sort(data_copy)
                print("Hasil sorting:", data_copy)
                print("==============")
            else:
                print("Pilihan tidak valid")

        elif menu_utama == '2':
            # Menu Searching
            print("\nMenu Searching:")
            print("a. Binary Search")
            print("b. Linear Search")
            print("c. Jump Search")
            print("d. Recursive Search")
            pilih_search = input("Pilih metode searching (a/b/c/d): ")

            cari = int(input("Masukkan data yang ingin dicari: "))

            data_copy = data.copy()

            # Pastikan data urut kalau metode yang butuh data terurut
            if pilih_search in ['a', 'c', 'd']:
                data_copy.sort()

            if pilih_search == 'a':
                searcher.binary_search(data_copy, cari)
            elif pilih_search == 'b':
                searcher.linear_search(data_copy, cari)
            elif pilih_search == 'c':
                searcher.jump_search(data_copy, cari)
            elif pilih_search == 'd':
                print("==============")
                print("Proses Recursive Search:")
                result = searcher.recursive_search(data_copy, 0, len(data_copy)-1, cari)
                if result != -1:
                    print(f"Data ditemukan di indeks {result}")
                else:
                    print("Data tidak ditemukan")
                print("==============")
            else:
                print("Pilihan tidak valid")

        elif menu_utama == '3':
            print("==============")
            print("Program Selesai")
            print("==============")
            break

        else:
            print("Pilihan tidak valid, silakan ulangi.")

if __name__ == "__main__":
    main()
