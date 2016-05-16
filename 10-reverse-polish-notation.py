import operator
#define operators. Use 'x' instead of '*' for multiplication. * does weird things in command line.
ops = { '+': operator.add, '-': operator.sub, 'x': operator.mul, '/': operator.div }
import sys
print(str(sys.argv))
array = sys.argv
i = 1
my_stack = []
while i < len(array):
#    if it is a value
    if array[i] not in ops:        
#        push array[i] onto stack
        my_stack.insert(0, array[i])
    else:
#        if operand, do operation on two preceding values in stack
        answer = ops[array[i]](float(my_stack[1]),float(my_stack[0]))
#        get rid of values from stack
        my_stack.pop(1)
        my_stack.pop(0)        
#        insert answer into stack
        my_stack.insert(0, answer)
    i = i + 1

print(my_stack)
