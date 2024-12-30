


#make sure its 0(n) at MOST ---> 1 for loop at any given time
#make the first --> ROOT NODE
#if next is bigger then ROOT NODE then place after
    #if not then place before  (assuming its not the value itself)
# for each in list create object
# in a controller class we store the list in generate_list()


class Node(object):
    def __init__(self, value,before=None, after=None):
        self.value = value
        self.before = before
        self.after = after


class List(object):
    def __init__(self, root):
        self.list = []
        self.root = root
        self.list.append(root.value)

    def insert(self, value):
        newNode = Node(value)
        #if value is the same as root forget it
        #if root node has a next node -> RECURSION
        if self.root.after:
            self.root.after.before = self.root
            self.root = self.root.after
            del(newNode)
            self.insert(value)
        else:


            if value == self.root.value:
                print('same')
                return
            elif value < self.root.value:
                print('less')
                newNode.after = self.root
                self.root.before = newNode
            elif value > self.root.value:
                print("greater")
                newNode.before = self.root
                self.root.after = newNode

            #at end call print from root to before values
            #if not place in if greater

        #if value is less then put it before
        #if its greater put it after   <----------INTRODUCE BEFORE AND AFTER ATTRIBUTES

    def generate_list(self, root):
        liist = []
        if root.before:
            self.generate_list(root.before)
        else:
            liist.append(root.value)
        print(liist)


arr = [1, 2, 7, 1, 3, 4, 1, 2]
root = Node(arr[0])     #grabbing root node
myList = List(root)     #creating List object with Root node set

for num in arr:
    myList.insert(num)

for num in range(0,len(arr)):
    myList.generate_list(root)