def work(square):
    """
    Purpose:
        Divide every value in the square by the sum of all the values in the square
    Pre-conditions:
        square: A list of lists containing positive numbers in "format" of a square (ie. NxN matrix)
    Post-conditions:
        All values in square are divided by sum of all values
    Return:
        None
    """
    sum = 0
    for row in square:
        for value in row:
            sum += value

    for row in square:
        for index in range(len(square)):
            row[index] /= sum


def fun(square):
    """
    Purpose:
        Divide every value in the row by the sum of all values in the row
    Pre-conditions:
        square: A list of lists containing positive numbers in NxN format
    Post-conditions:
        Each value in the square is divided by the sum of its row values
    Return:
        None
    """
    for row in square:
        sum = 0

        for value in row:
            sum += value

        for index in range(len(row)):
            row[index] /= sum


print("Fun")
asquare = [[1, 1], [1, 2]]
fun(asquare)
print(asquare)

print("Work")
asquare = [[1, 2], [3, 4]]
work(asquare)
print(asquare)
