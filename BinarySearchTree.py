#
# Christian Offenheiser
#
# Assignment 3 BST CSC 231
#
# 11/28/023
#
# Purpose: To create and implement a Binary Search Tree
#
# Algorithm:
#
# Sources: Andrew Davison in class
#          Also based deletion code off of the textbooks code

class BinarySearchTree:
    def __init__(self):
        """
        Initializes Binary Search Tree
        """

        self.root = None
        self._size = 0
        self._height = 0
        self._max_height = 0
        # index number corresponds to level, value at index corresponds to the number of nodes at that level
        self._nodes_at_level = [0]

    def insert(self, item):
        """
        Inserts a new node into the BST
        :param item: Item to be added
        :return: None
        """

        # insert at root if no root
        if not self.root:
            # add root
            self.root = BinaryNode(item)
            self.root.depth = 0
            self._nodes_at_level[0] = 1

            # increase size
            self._size += 1
        else:
            # call helper function
            self._insert(item, self.root)

    def _insert(self, item, cur, depth=1):
        """
        Recursive helper function of insert method
        :param item: Item to be added
        :param cur: Current node
        :return: None
        """

        # make sure item not already in Tree
        if item == cur.data:
            raise ValueError(f"{item} already in Tree")

        if item < cur.data:
            # go to the left
            if cur.has_left():
                depth += 1
                self._insert(item, cur.left, depth)
            else:
                cur.left = BinaryNode(item, cur)
                # add depth to node
                cur.left.depth = depth

                # set nodes at level
                if depth > len(self._nodes_at_level) - 1:
                    self._nodes_at_level.append(1)
                else:
                    self._nodes_at_level[depth] += 1

                # increment size
                self._size += 1

                # change height if node depth is greater
                if depth > self._height:
                    self._height = depth

                # change max height if height is greater
                if self._height > self._max_height:
                    self._max_height = self._height
        else:
            # go to the right
            if cur.has_right():
                depth += 1
                self._insert(item, cur.right, depth)
            else:
                cur.right = BinaryNode(item, cur)
                # add depth to node
                cur.right.depth = depth

                # set nodes at level
                if depth > len(self._nodes_at_level)-1:
                    self._nodes_at_level.append(1)
                else:
                    self._nodes_at_level[depth] += 1

                # increment size
                self._size += 1

                # change height if node depth is greater
                if depth > self._height:
                    self._height = depth

                # change max height if height is greater/ we only need to worry abt max height when adding nodes
                if self._height > self._max_height:
                    self._max_height = self._height

    def traverse_inorder(self, node=None):
        """
        Inorder traversal of BST that prints nodes
        :return: None
        """

        # check if node not given
        if not node:
            cur = self.root
        else:
            cur = self._get(node, self.root)
        self._inorder(cur)

    def _inorder(self, cur):
        """
        Postorder helper function
        :param cur: Current pointer
        :return: None
        """

        # check if current then print and do recursive calls
        if cur:
            self._inorder(cur.left)
            print(cur.data, end=" ")
            self._inorder(cur.right)
        return

    def traverse_preorder(self, node=None):
        """
        Preorder traversal of BST that prints nodes
        :return: None
        """

        # check if node not given
        if not node:
            cur = self.root
        else:
            cur = self._get(node, self.root)
        self._preorder(cur)

    def _preorder(self, cur):
        """
        Preorder helper function
        :param cur: Current pointer
        :return: None
        """

        # check if current then print and do recursive calls
        if cur:
            print(cur.data, end=" ")
            self._preorder(cur.left)
            self._preorder(cur.right)
        return

    def traverse_postorder(self, node=None):
        """
        Postorder traversal of BST that prints nodes
        :return: None
        """

        # check if node not given
        if not node:
            cur = self.root
        else:
            cur = self._get(node, self.root)
        self._postorder(cur)

    def _postorder(self, cur):
        """
        Postorder helper function
        :param cur: Current pointer
        :return: None
        """

        # check if current then print and do recursive calls
        if cur:
            self._postorder(cur.left)
            self._postorder(cur.right)
            print(cur.data, end=" ")
        return

    def _get(self, item, cur):
        """
        Searches for a node in BST
        :param item: Item to find
        :param cur:  The current node
        :return: The node with the correct item
        """

        # check if the item exist and return if not
        if not cur:
            return

        # compare
        if cur.data == item:
            return cur

        # recursive call
        if item < cur.data:
            self._get(item, cur.left)
        else:
            self._get(item, cur.right)

    def __len__(self):
        """
        Returns length of BST
        :return: Current length as integer
        """

        return self._size

    def __contains__(self, item):
        """
        Checks if a value exists in BST
        :param item: Item to search for
        :return: A boolean value True or False
        """

        # if the BST is empty return False
        if not self.root:
            return False

        # call helper function
        cur = self._find(item)

        # if it returns anything then return true else false
        if cur:
            return True
        return False

    def _find(self, item):
        """
        Finds item in BST and returns it
        :param item: Item to be found
        :return: The found item
        """

        # set current
        cur = self.root

        # iterate through bst
        while cur:
            # if you get item return True
            if item == cur.data:
                return cur
            # go right or left
            elif item > cur.data:
                cur = cur.right
            else:
                cur = cur.left
        return None

    def current_height(self):
        """
        Returns BST current height
        :return: The height value
        """

        return self._height

    def max_height(self):
        """
        Returns BST max height
        :return: The max height value
        """

        return self._max_height

    def delete(self, item):
        """
        Deletes an item from BST
        :param item: item to be removed
        :return: None
        """

        # only delete if size > 1
        if self._size > 1:
            # find node to remove using helper function
            node_to_remove = self._find(item)

            # make sure it's found
            if node_to_remove:

                self._delete(node_to_remove)
                self._size -= 1

                # set current height if nodes no longer at lowest level
                if self._nodes_at_level[self._height] == 0:
                    self._height -= 1

            else:
                raise ValueError("fError, item {item} not in tree")
        elif self._size == 1 and self.root.data == item:  # delete root if no other nodes
            self.root = None
            self._size -= 1
            self._nodes_at_level[0] = 0
        else:
            raise ValueError(f"Error, item {item} not in tree")

    def _delete(self, current_node):
        """
        Helper method for deletion
        :param current_node: The current node to be removed
        :return: None
        """

        if not current_node.left and not current_node.right:  # if it has zero children
            self._nodes_at_level[current_node.depth] -= 1

            # check if the node is a left or right child and set it to none
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.right and current_node.right:  # if it has two children
            # get the successor
            successor = current_node.find_successor()
            self._nodes_at_level[successor.depth] -= 1
            # remove it
            successor.splice_out()
            # set data to successor
            current_node.data = successor.data
        else:  # if it has one child
            lowest_leaf_depth = self._find_lowest_depth(current_node)
            self._nodes_at_level[lowest_leaf_depth] -= 1
            # make sure it has a left child
            if current_node.left:
                # check if it is a left or right child or the root
                if current_node == current_node.parent.left:  # left child
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node == current_node.parent.right:  # right child
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:  # root value
                    # replace the values of node
                    current_node.replace_value(
                        current_node.left_child.data,
                        current_node.left_child.left,
                        current_node.left_child.right,
                    )

    def _find_lowest_depth(self, current_node):
        """
        Finds lowest depth of subtree
        :param current_node: the current node
        :return: lowest node in subtree
        """

        # return if leaf
        if not current_node.left and not current_node.right:
            return current_node
        else:
            left = self._find_lowest_depth(current_node.left).depth if current_node.left else 0
            right = self._find_lowest_depth(current_node.right).depth if current_node.right else 0

            if right > left:
                return right
            else:
                return left


class BinaryNode:
    def __init__(self, data, parent=None):
        """
        Initializes BST Node class
        :param data: The data of the node
        :param parent: The parent node
        """

        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.depth = None

    def has_left(self):
        """
        Returns the left
        :return: The left Node
        """

        return self.left

    def has_right(self):
        """
        Returns the right
        :return: the right Node
        """

        return self.right

    def __str__(self):
        """
        Str override of binary node class
        :return: The string representation of a Node
        """

        return "[%s, %s, %s]" % (self.left, str(self.data), self.right)

    def display(self):
        """
        Displays lines
        :return: None
        """

        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def find_successor(self):
        """
        Finds successor of a node
        :return: The successor node
        """

        # create successor variable
        successor = None
        # if there is a right find min
        if self.right:
            successor = self.right.find_min()
        else:
            # check there is a parent
            if self.parent:
                # reset left or right
                if self == self.parent.left():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def find_min(self):
        """
        Finds leftmost point aka the min
        :return: The minimum value
        """

        # set current
        current = self

        # iterate
        while current.left:
            current = current.left

        # return current
        return current

    def splice_out(self):
        """
        Cuts out value
        :return: None
        """

        # if no children
        if not self.left and not self.right:
            # set parent left or right to none
            if self == self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None
        # if one child
        elif self.left or self.right:
            # set parent right or left to self.left
            if self.left:
                if self == self.parent.left:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:  # two children
                # set parent left or right to right
                if self == self.parent.left:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                # set right of parent to right of self
                self.right.parent = self.parent

    def replace_value(self, data, left, right):
        """
        Replaces a Nodes value
        :param data: The new data
        :param left: The left pointer
        :param right: The right pointer
        :return: None
        """

        # set new data, left, and right
        self.data = data
        self.left = left
        self.right = right

        # set parent
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
