import random
from app.sort import Sort

class Search:
    def __init__(self):
        self.count_ops = 0

    # Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a
    # target value within a sorted array.
    # The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm
    # and executes in logarithmic time. O log(n)
    def binary_search(self, sorted_list, find_me, test=False):

        start = 0
        end = len(sorted_list)
        found = False

        while start<=end and not found:
            mid = (start + end) // 2

            if sorted_list[mid] == find_me:
                found = True

            else:
                if find_me < sorted_list[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return found


class TestSearch:
    def __init__(self):
        self.list_size = 100
        self.search_list = [random.randrange(-1*self.list_size*50, self.list_size*50, 1) for i in range(self.list_size)]
        self.len_list = len(self.search_list)
        self.sorted_list = []
        self.s = Search()

    def get_unsorted(self):
        return self.search_list

    def do_test(self, search_this, test=False):
        self.s.count_ops = 0

        print(f'Size = {len(search_this)}, Ops = {self.s.count_ops}')
        return search_this
