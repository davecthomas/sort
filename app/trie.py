

class Trie(object):

    def __init__(self, word_list):
        self.root = Node("")

        for word in word_list:
            parent = self.root
            for char in word:
                # print(f"New char {char}")
                node = self.find_or_new(char, parent)
                parent = node

    def print_it(self, node, parent=None):
        if node.children is not None and len(node.children) > 0:
            for child in node.children:
                if parent is None:
                    parent_char = "<root>"
                else:
                    parent_char = parent.char
                print(f'{parent_char}->{child.char}->{len(child.children)}')
                self.print_it(child, node)
        else:
            print(node.char)

    def find_or_new(self, char, parent=None):
        return_node = None
        if parent is None:
            parent = self.root

        for node in parent.children:
            if node.char == char:
                return_node = node

        if return_node is None:
            return_node = Node(char, parent)

        return return_node



class Node(object):

    def __init__(self, char_, parent_=None):
        self.children = []
        self.char = char_
        self.parent = parent_
        if parent_ is not None:
            parent_.children.append(self)


def main():
    trie = Trie(word_list=["monkey","moose","maggot","magoo","money","dave","day","dan"])
    print(f'Len root={len(trie.root.children)}')
    trie.print_it(trie.root)


if __name__ == "__main__":
    main()