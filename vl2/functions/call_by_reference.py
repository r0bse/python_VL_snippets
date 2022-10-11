# When Mutable objects such as list, dict, set, etc
# are passed as arguments to the function call,
# then it can be considered as Call by reference in Python.
# This is because when the values are modified within the function
# then the change also gets reflected outside the function.

def call_by_reference(myList):
    print("\t List received: ",myList)
    myList.append(3)
    myList.extend([7,1])
    myList.remove(7)
    print("\t List within called function:", myList)
    return


if __name__ == "__main__":
    list=[1]
    print("List before function call :",list)
    call_by_reference(list)
    print("\t List after function call: ",list)