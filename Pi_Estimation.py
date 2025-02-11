import math

'''
The function computes an interval for the number pi based on archimedes method whereby the circumference of the 
circle is bound between an inscribed polygon and a circumscribed polygon such that the circumference of the circle
equates to pi with a radius of 0.5.

parameters:
iterations(int): The number of iterations

returns: An interval for the number pi
'''


def PI_Computation_Upper(iterations):
   i=0
   #The initial value for number of iterations
   b=0.5*1/math.sqrt(3)
   # b is half the legnth of one side of the circumscribed polygon
   a=1/math.sqrt(3)
   #a is the length of a line between the centre of the polygon to one of its vertices
   while i <= iterations:
        # Performs an iterative calculation to compute the length of the side
        # of a circumscribed polygon that has twice the number of sides
        # of the previous polygon.
        b = b / (2 * a + 1)
        # This is computed from the angle bisection theorem.
        print(f"iteration:{i}")
        print(b, ' b')
        a = math.sqrt(pow(b, 2) + 1 / 4)
        # Applies pythagoras' theorem to compute the new value for a which will
        # then generate the new value for b.
        print(a, ' a')
        i = i + 1
    # Goes to the next iteration
    return 2 * b * 6 * pow(2,iterations+1)

# Returns the perimeter of the circumscribed polygon after a number of iterations.


def PI_Computation_Lower(iterations):
    # Computes the lower bound for pi.
    i = 0
    # The initial value for our iteration.
    c = 0.5
    # c is the length of the one side of the polygon whereby we
    # start with a value of 0.5 which corresponds to an inscribed hexagon.
    while i <= iterations:
        a = c / 2
        b = math.sqrt(0.25 - pow(a, 2))
        # Computes the distance from the centre of the polygon
        # to the midpoint of one of its sides.
        print(f"iteration:{i}")
        print(b, ' b')
        c = math.sqrt(((pow(a, 2)) + pow((1 / 2 - b), 2)))
        # Computes the distance from the centre of the polygon
        #       to the midpoint of one of its sides.
        print(c, ' c')
        i = i + 1
    # Goes to the next iteration.
    return c * 6 * pow(2,iterations + 1)


# Returns the perimeter of the inscribed polygon after x iterations.


def PI_Estimation(iterations):
    # Computes an interval for the value pi.
    print("The value of pi for x =",iterations, " iterations is between ", PI_Computation_Lower(iterations), " and ",
          PI_Computation_Upper(iterations))



iterations=100
# The number of iterations.
PI_Estimation(iterations)
