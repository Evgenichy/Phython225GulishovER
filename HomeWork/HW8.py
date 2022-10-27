a = [1, 2, 3]
b = [9, 12, 33, 54, 105]
c = ['с', 'л', 'о', 'н']

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(['с', 'л', 'о', 'н']))