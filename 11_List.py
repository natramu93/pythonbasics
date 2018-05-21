list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

#Accessing a list element

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#updating list
list1[2] = 2001

#deleting list element
del list1[2]

#list functions

'''
len([1, 2, 3])	                                3	                    Length
[1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]	            Concatenation
['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	                                True	                Membership
for x in [1,2,3] : print (x,end = ' ')	        1 2 3	                Iteration
'''

#indexing, slicing, matrixes
'''
L[2]	'Python'	        Offsets start at zero
L[-2]	'Java'	            Negative: count from the right
L[1:]	['Java', 'Python']	Slicing fetches sections
'''

#list functions
'''
1	cmp(list1, list2)
No longer available in Python 3.

2	len(list)
Gives the total length of the list.

3	max(list)
Returns item from the list with max value.

4	min(list)
Returns item from the list with min value.

5	list(seq)
Converts a tuple into list.
'''

#methods and descriptions
'''
1	list.append(obj)
Appends object obj to list

2	list.count(obj)
Returns count of how many times obj occurs in list

3	list.extend(seq)
Appends the contents of seq to list

4	list.index(obj)
Returns the lowest index in list that obj appears

5	list.insert(index, obj)
Inserts object obj into list at offset index

6	list.pop(obj = list[-1])
Removes and returns last object or obj from list

7	list.remove(obj)
Removes object obj from list

8	list.reverse()
Reverses objects of list in place

9	list.sort([func])
Sorts objects of list, use compare func if given
'''

