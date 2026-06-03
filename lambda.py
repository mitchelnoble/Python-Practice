#small one-line nameless/unnamed functions are called lambda

square = lambda x: x ** 2
print(square(5)) #Output: 25

#Using lambda in a map function
numbers = [1,2,3,4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared)) #Output: [1,4,9,16]