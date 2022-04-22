from stack_implement import Stack
from binaryTreeNodes import BinaryTree
import operator

def buildParseTree(exp):
    expList = exp.split()
    expStack = Stack()
    expTree = BinaryTree('')
    expStack.push(expTree)
    currentTree = expTree

    for i in expList:
        if i == '(':
            currentTree.insertLeft('')  # add left child
            expStack.push(currentTree)  # push on stack
            currentTree = currentTree.getLeftChild()  # descend to left child
        elif i.isdigit():  # operands
            currentTree.setRootVal(int(i))  # set value
            parent = expStack.pop()
            currentTree = parent  # return to parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')  # add right child
            expStack.push(currentTree)  # push on stack
            currentTree = currentTree.getRightChild()  # descend to right child
        elif i == ')':
            currentTree = expStack.pop()
        else:
            print('Error, invalid symbol', i)
    return expTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC)) #recursion
    else: # leaf node
        return parseTree.getRootVal() #


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal


def prefixToInfix(prefix):
    stack = []
    prefix = prefix.split()
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:

            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return ' '.join(stack.pop())


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

infix = input('Enter a prefix expression: ')

converted = prefixToInfix(infix)

tree = buildParseTree(converted)

print(evaluate(tree))
