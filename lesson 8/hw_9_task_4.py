# 4
# Find all the numbers from 1-1000 that have a 3 in them

numbers = (num for num in range(1, 1001) if '3' in str(num))

if __name__ == '__main__':
    for num in numbers:
        print(num)
