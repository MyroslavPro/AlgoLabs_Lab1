import time


class QuickSort:
    def __init__(self):
        self.swaps_count = 0
        self.comparisons_count = 0

    def quick_sort(self, array_not_sorted, start_position, end_position, order):
        if start_position >= end_position:
            self.comparisons_count += 1
            return

        # take a pivot
        pivot = self.finding_position(array_not_sorted, start_position, end_position, order)

        # recursion
        self.quick_sort(array_not_sorted, start_position, pivot - 1, order)
        self.quick_sort(array_not_sorted, pivot + 1, end_position, order)
        return array_not_sorted

    def finding_position(self, array, start_pos, end_pos, order):
        i = start_pos
        j = end_pos

        # ascending order
        if order == "asc":
            while i <= j:
                while array[i] < array[start_pos]:
                    i += 1

                while array[j] > array[start_pos]:
                    j -= 1

                if i <= j:
                    swap_var = array[i]
                    array[i] = array[j]
                    array[j] = swap_var
                    self.swaps_count += 1
                    self.comparisons_count += 1
                    i += 1
                    j -= 1
        # descending order
        elif order == "desc":
            while i <= j:
                while array[i] > array[start_pos]:
                    i += 1

                while array[j] < array[start_pos]:
                    j -= 1

                if i <= j:
                    swap_var = array[i]
                    array[i] = array[j]
                    array[j] = swap_var
                    self.swaps_count += 1
                    self.comparisons_count += 1
                    i += 1
                    j -= 1
        i -= 1
        # swap of first element and pivot
        swap = array[i]
        array[i] = array[start_pos]
        array[start_pos] = swap
        self.swaps_count += 1
        return i


if __name__ == '__main__':
    order_of_sort = input("Way of sorting -> asc/desc: ")
    if order_of_sort not in ("asc", "desc"):
        raise Exception("Incorrect name of way of sorting")

    number = int(input("Введіть кілкість елементів: "))
    array_input = []
    for i in range(number):
        new_elem = int(input())
        array_input.append(new_elem)
    print("Input array:", array_input)

    start_time = time.time()
    A = QuickSort()
    array_sorted = A.quick_sort(array_input, 0, len(array_input) - 1, order_of_sort)
    end_time = time.time()

    # output
    print("QuickSort")
    print("Execution time:", end_time - start_time, "s")
    print("Total swaps:", A.swaps_count)
    print("Total comparisons:", A.comparisons_count)
    print("Final array", array_sorted)
