import random

class A_Tree():
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi
        self.child_count = random.randint(self.mini, self.maxi)
        
def makeTree(mini, maxi, child_count, treeobj):
    terminal_min, terminal_max = 1, 100
    tree = [random.randint(terminal_min, terminal_max)]
    if maxi <= 5 or mini <= 1:
        return tree
    for child in range(child_count):
        cluster_size = random.randint(1, 4)
        cluster = []
        for terminal in range(cluster_size):
            num = random.randint(1, 100)
            if num < 25:
                cluster += [makeTree(mini=mini - random.randint(1, 5),
                                     maxi=maxi - random.randint(1, 5),
                                     child_count=child_count, treeobj=treeobj)]
            else:
                cluster += [random.randint(terminal_min, terminal_max)]
        tree += [cluster]
    return tree

def depthcount(node):
    counter_list = []
    count = 1
    for child in node:
        if type(child) == int:
            count = 1
            counter_list.append(count)
        elif type(child) == list:
            count += depthcount(child)
            counter_list.append(count)
            count = 1
    return max(counter_list)

        
def findMin(node):
    if type(node) == int:
        num = node
        return num
    lowestnum = 1000
    for child in node:
        num = findMin(child)
        if num < lowestnum:
            lowestnum = num
    return lowestnum

def findMax(node):
    if type(node) == int:
        num = node
        return num
    highestnum = 0
    for child in node:
        num = findMax(child)
        if num > highestnum:
            highestnum = num
    return highestnum

def minimax(node, turn='max'):
    if turn == 'max':
        return getmax(node)
    else:
        return getmin(node)

def getmax(node):
    bestvalue = 0
    for child in node:
        if type(child) == int:
            terminal = child
        elif type(child) == list:
            terminal = getmin(child)
        if terminal > bestvalue:
            bestvalue = terminal
    return bestvalue

def getmin(node):
    bestvalue = 100
    for child in node:
        if type(child) == int:
            terminal = child
        elif type(child) == list:
            terminal = getmax(child)
        if terminal < bestvalue:
            bestvalue = terminal
    return bestvalue



#create tree object
tree = A_Tree(6, 7)

#generate data set
treenode = makeTree(tree.mini, tree.maxi, tree.child_count, tree)

#turn tree object into list to be iterable
treenode_list = [treenode]
treenode_list = treenode_list[0]
print(treenode_list)

#add depth to tree object
tree.depth = depthcount(treenode_list)

#tree minimax info:
print('')
print('Depth count: {}'.format(tree.depth))
print('Min num: {}'.format(findMin(treenode_list)))
print('Max num: {}'.format(findMax(treenode_list)))
print('')
print("On max's turn, given that the player has " + str(tree.child_count + 1) + " paths to choose from, he should choose to play " + str(minimax(treenode_list, turn='max')) + " either on the 1st or 2nd level to maximize returns.")
print("On min's turn, given that the player has " + str(tree.child_count + 1) + " paths to choose from, he should choose to play " + str(minimax(treenode_list, turn='min')) + " either on the 1st or 2nd level to minimize damages.")

