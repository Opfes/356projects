from unorderedLists_Lindsay import UnorderedList
# add import statement here and run this program to get the output

myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.append(93)
myList.append(26)
myList.append(54)
myList.printList()
print()
print(myList.size())
print(myList.search(17))
myList.remove(93)
myList.remove(22)
myList.printList()