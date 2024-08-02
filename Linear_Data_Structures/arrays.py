# Arrays

'''
 [X] Initializing 
 [X] Accessing elements 
 [] Searching for elements 
 [] Sorting elements 
 [] Inserting elements 
 [] Deleting elements 
 [] Updating elements 
 [] Traversing elements

'''

# Initializing Arrays
''' 
a = [] 
a = [0 for x in range(10) ]
print (a)
'''

a = [10, 20, 30, 40, 50, 60]

# Accessing elements
''' 
print(a[1])
print(a[5])
'''

# Searching for elements
# Linear Search
'''
time complexity : O(n) 
n - lenght of the array
'''
def linear_Search(x) :
    for i in range(len(a)) : 
        if x == a[i]: 
            return True
    return False

''' 
print( linear_Search(40))
print(linear_Search(20))
print(linear_Search(100))
'''

# Binary Search
'''
O(log 2 N)
n - lenght of the array
'''
# sort arrays
a.sort()

def binary_search(a, low, high, x):
    if high >= low:
        mid = low + (high-low) //2
    
        if x == a[mid]:
            return mid
        
        elif x < a[mid]:
            return binary_search(a, low, mid-1, x)
        else:
            return binary_search(a, mid+1, high, x)
    else:
        return -1

''' 
print(binary_search(a, 0, len(a)-1 ,40))
print(binary_search(a, 0, len(a)-1 ,20))
print(binary_search(a, 0, len(a)-1 ,100))
'''

# Ternary Search
'''
O(log 3 N)
n - lenght of the array
'''

# def ternary_search(x):


''' 
print(ternary_search(a, 0, len(a)-1 ,40))
print(ternary_search(a, 0, len(a)-1 ,20))
print(ternary_search(a, 0, len(a)-1 ,100))
'''