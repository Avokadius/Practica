arr=[3,5,1,77,35,11]
array1 = [7, 8, 9, 10, 11]
array2 = [1, 2, 3, 4, 5, 6]
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        def selection_sort(arr):
            n = len(arr)
            for i in range(n - 1, 0, -1):
                max_idx = 0
                for j in range(1, i + 1):
                    if arr[j] < arr[max_idx]:
                        max_idx = j
                arr[i], arr[max_idx] = arr[max_idx], arr[i]
            return arr
        print(selection_sort(arr))
    elif choice == "2":
        def merge_sorted_arrays(arr1, arr2):
            result = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] >= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
            while i < len(arr1):
                result.append(arr1[i])
                i += 1
            while j < len(arr2):
                result.append(arr2[j])
                j += 1
            return result[::-1]

    elif choice == "3":
        def sort_descending(arr):
            n = len(arr)
            keys = [(i, arr[i]) for i in range(n)]
            keys.sort(key=lambda x: x[1])

            sorted_arr = [0] * n
            for i, key in enumerate(keys):
                sorted_arr[n - 1 - i] = arr[key[0]]
            return sorted_arr
        print(sort_descending(arr))
    elif choice == "4":
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        print(bubble_sort(arr))
    elif choice == "5":
        def selection_insertion_sort(arr):
            n = len(arr)
            for i in range(n - 1, -1, -1):
                max_idx = i
                for j in range(i - 1, -1, -1):
                    if arr[j] > arr[max_idx]:
                        max_idx = j
                if max_idx != i:
                    arr[max_idx], arr[i] = arr[i], arr[max_idx]
                j = i
                while j < n - 1 and arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
            return arr
        print(selection_insertion_sort(arr))
    elif choice == "6":
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - 1, i, -1):
                    if arr[j] < arr[j - 1]:
                        arr[j], arr[j - 1] = arr[j - 1], arr[j]
            return arr
        print(bubble_sort(arr))
    elif choice == "7":
        def bubble_sortplus(arr):
            n = len(arr)
            swapped = True
            while swapped:
                swapped = False
                for i in range(n - 1):
                    if arr[i] < arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                n -= 1
            return arr
        print(bubble_sortplus(arr))
    elif choice == "8":
        print("Exiting menu")
        break
    else:
        print("Invalid choice. Please try again.")



