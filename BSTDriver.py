from BinarySearchTree import BinarySearchTree
import turtle

positions = [(0, 0)]


def draw(x=0, y=0, d=2, a=45.0):
    """
    Draws a BST example
    :param x: the x position
    :param y: the y position
    :param d: the depth
    :param a: the angle
    :return: None
    """

    # create window and title
    window = turtle.Screen()
    window.title("Inserting values into a BST")

    # create two turtles and hide shape
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.hideturtle()
    t2.hideturtle()

    # recursive base case
    if d == 0:
        return
    elif d == 2:
        # draw root node
        t1.pencolor("green")
        t1.dot(50)
        t1.pencolor("black")

    t1.penup()
    t2.penup()
    t1.goto(x, y)
    t2.goto(x, y)
    t1.pendown()
    t2.pendown()

    # draw lines
    t1.down()
    t2.down()
    t1.left(a)
    t2.right(a)
    t1.forward(100)
    t2.forward(100)

    # draw nodes
    t1.pencolor("green")
    t2.pencolor("green")
    t1.dot(50)
    t2.dot(50)
    t1.pencolor("black")
    t2.pencolor("black")

    # get new positions after movement
    t1x, t1y = t1.pos()
    t2x, t2y = t2.pos()
    positions.append((t1x, t1y))
    positions.append((t2x, t2y))

    # recursive calls
    draw(t1x, t1y, d - 1, a / 2)
    draw(t2x, t2y, d - 1, a / 2)


def write_numbers(vals):
    """
    Write numbers for bst turtle graphic
    :param vals; list of values to write to screen
    :return: None
    """

    # declare turtle and values
    text_turtle = turtle.Turtle()

    # iterate and print values to screen
    for i in range(len(vals)):
        text_turtle.penup()
        text_turtle.goto(positions[i])
        text_turtle.pendown()

        text_turtle.write(vals[i])


def main():
    """
    Main function
    :return: None
    """

    print("Creating a new Binary Search Tree...")
    mytree = BinarySearchTree()

    print("Inserting 45 into the tree")
    mytree.insert(45)
    print()

    print(f"Tree length should be 1: {len(mytree)}")
    print(f"Tree current height should be 0: {mytree.current_height()}")
    print(f"Tree max height should be 0: {mytree.max_height()}")
    print()

    print("Printing mytree with display method...")
    mytree.root.display()
    print()

    print("Inserting eight more values...")
    mytree.insert(67)
    mytree.insert(22)
    mytree.insert(100)
    mytree.insert(75)
    mytree.insert(13)
    mytree.insert(11)
    mytree.insert(64)
    mytree.insert(30)

    print(f"Tree length should be 9: {len(mytree)}")
    print(f"Tree current height should be 3: {mytree.current_height()}")
    print(f"Tree max height should be 3: {mytree.max_height()}")
    print()

    print("Printing mytree with display method...")
    mytree.root.display()
    print()

    print(f"Preorder traversal of tree should be: \n"
          f"45 22 13 11 30 67 64 100 75")
    mytree.traverse_preorder()
    print('\n')

    print(f"Inorder traversal of tree should be: \n"
          f"11 13 22 30 45 64 67 75 100")
    mytree.traverse_inorder()
    print('\n')

    print(f"Postorder traversal of tree should be: \n"
          f"11 13 30 22 64 75 100 67 45")
    mytree.traverse_postorder()
    print('\n')

    print(f"45 in tree should be True: {45 in mytree}")
    print(f"110 in tree should be False: {110 in mytree}")
    print()

    print("Deleting item 11")
    mytree.delete(11)
    mytree.root.display()
    print()

    print("Deleting item 64")
    mytree.delete(64)
    mytree.root.display()
    print()

    print("Deleting item 100")
    mytree.delete(100)
    mytree.root.display()
    print()

    print("Deleting item 22")
    mytree.delete(22)
    mytree.root.display()
    print()

    print("Deleting item 45")
    mytree.delete(45)
    mytree.root.display()
    print()

    print(f"Tree length should be 4: {len(mytree)}")
    print(f"Tree current height should be 2: {mytree.current_height()}")
    print(f"Tree max height should be 3: {mytree.max_height()}")
    print()

    print("Inserting 5 more values...")
    mytree.insert(12)
    mytree.insert(100)
    mytree.insert(47)
    mytree.insert(11)
    mytree.insert(70)

    mytree.root.display()
    print(f"Tree length should be 9: {len(mytree)}")
    print(f"Tree current height should be 4: {mytree.current_height()}")
    print(f"Tree max height should be 4: {mytree.max_height()}")
    print()

    answer = input("Would you like to see an example drawing? (y/n): ").lower()

    if answer.lower() == "y":
        import time
        draw()
        write_numbers([45, 67, 22, 100, 64, 30, 13])
        time.sleep(3)


if __name__ == "__main__":
    main()
