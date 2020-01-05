import random

class Sort:
    def __init__(self):
        self.count_ops = 0

    def selection_sort(self, len_original, sort_this, start, test=False):
        if start > len_original-1:
            return sort_this
        if test:
            print(f'{start}')
        minimum_i = start
        for i in range(start+1, len_original, 1):   # From 0 to len_list-2
            self.count_ops += 1
            if sort_this[i] < sort_this[minimum_i]:
                minimum_i = i
                if test:
                    print(f'{i}: {sort_this[i]} < {sort_this[start]}')
        if minimum_i != start:
            sort_this[start], sort_this[minimum_i] = sort_this[minimum_i], sort_this[start]
            if test:
                print(f'{sort_this}')
        else:
            if test:
                print(f'No swaps!')
        self.selection_sort(len_original, sort_this, start+1, test)

    # This is the fewest LOC I have gotten to for selection sort
    def selection_sort_2(self, sort_list, test=False):
        for outer_i in range(0, len(sort_list)):

            min_idx = outer_i
            for i in range(outer_i+1, len(sort_list)):

                if sort_list[i]<sort_list[min_idx]:
                    min_idx = i

            if min_idx != outer_i:
                sort_list[min_idx], sort_list[outer_i] = sort_list[outer_i], sort_list[min_idx]

        return sort_list

    def selection_sort_iter(self, sort_this, test=False):
        for outer_i in range(len(sort_this)):
            inner_list = sort_this
            len_list = len(sort_this)-outer_i
            min_idx = outer_i
            min_idx_save = min_idx
            for i in range(outer_i, len(sort_this)):
                if sort_this[i] < sort_this[min_idx]:
                    min_idx = i
            if min_idx != min_idx_save:
                if test:
                    print(f'Swapped {i}: {sort_this[min_idx_save]} and {sort_this[min_idx]}')
                sort_this[min_idx_save], sort_this[min_idx] = sort_this[min_idx], sort_this[min_idx_save]
        return sort_this

    def bubble_sort(self, sort_this, test=False):
        for passnum in range(len(sort_this) - 1, 0, -1):
            if test:
                print(f'passnum: {passnum}')
            exchanges = False
            for i in range(passnum):
                if test:
                    print(f'i: {i}')
                if i - 1 >= 0:
                    if sort_this[i] < sort_this[i - 1]:
                        sort_this[i], sort_this[i - 1] = sort_this[i - 1], sort_this[i]
                        exchanges = True
            if not exchanges:
                print("Stopped early due to no exchanges this pass")
                break
        return sort_this

    def insertion_sort(self, sort_this):
        if sort_this is not None:
            # import pdb
            # pdb.set_trace()
            # Loop from the 2nd character to the end
            for j in range(1, len(sort_this), 1):
                # grab that element
                key = sort_this[j]
                # If any elements to the left of this one
                # are bigger than this one, overlay them
                i = j - 1
                while i >= 0 and sort_this[i] > key:
                    sort_this[i + 1] = sort_this[i]
                    i = i - 1
                # Put the number where it belongs
                sort_this[i + 1] = key
        return sort_this

    def insertion_sort2(self, sort_this):
        return sort_this

def get_random_digits(list_size, range_list):
    return [random.randrange(-1 * list_size * 10, range_list * 10, 1) for i in range(list_size)]

def get_random_in_range(start, stop):
    return random.randrange(start, stop, 1)

class TestSort:
    def __init__(self):
        self.list_size = 100
        self.unsorted_list = [random.randrange(-1 * self.list_size * 10, self.list_size * 10, 1) for i in range(self.list_size)]
        self.len_list = len(self.unsorted_list)
        self.sorted_list = []
        self.s = Sort()

    def get_unsorted(self):
        return self.unsorted_list

    def do_test(self, sort_this, test=False):
        self.s.count_ops = 0
        # sorted_list = self.s.bubble_sort(sort_this)
        sorted_this = self.s.selection_sort_2(sort_this, test)
        # sorted_this = self.s.selection_sort(len(sort_this), sort_this, 0, test)
        print(f'Size = {len(sort_this)}, Ops = {self.s.count_ops}')
        return sort_this
