# 2.
# Using the created file in task 1, read the file and perform mathematical operations on each element.
# Output the result of the operation to the console. You cannot use imports to import from the first task module.

if __name__ == '__main__':

    with open('test/data/test_data.txt') as file:
        for row in file:
            l, r, o = row[1:-2].split(' ')
            left = int(l)
            right = int(r)
            operator = int(o)

            if operator == 1:
                print('Result of addition is:', left + right)
            elif operator == 2:
                print('Result of subtraction is:', left - right)
            else:
                print('Result of multiplication is:', left * right)
