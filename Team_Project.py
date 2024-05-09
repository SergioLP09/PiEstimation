# Zachary Sargeant
# Kayla Le
# Anya Debelynska
# Sergio Prestegui
# Team Project
# May 11 2024


import random
import math
import time
import turtle
def monteCarlo():
    """
    Pi estimate using monte carlo method
    """
    pointsInside = 0 
    total = 1000000 

    for _ in range(total): 
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 <= 1: 
            pointsInside+=1 
            
    estimate = 4*pointsInside/total
    return estimate
def monteCarloDrawing():
    monte = turtle.Turtle()
    monte.speed(0)  

    #square
    monte.penup()
    monte.goto(-1, 1)
    monte.pendown()
    for _ in range(4):
        monte.forward(2)
        monte.right(90)

    #circle
    monte.penup()
    monte.goto(0, -1)
    monte.pendown()
    monte.circle(1 )

    #points
    total = 1000
    pointsInside = 0
    monte.penup()
    for _ in range(total):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = (x ** 2 + y ** 2) ** 0.5 # calculate points in circle
        if distance <= 1:
            pointsInside += 1
            monte.color("blue")
        else:
            monte.color("red")
        monte.goto(x, y)
        monte.dot(9)


def accumulator_method(iterations: int) -> float:
    """
    Approximates the value of pi using the Accumulator method.
    """
    acc = 0
    for i in range(iterations):
        acc += 1 / (i * 4 + 1) - 1 / (i * 4 + 3)
    pi = acc*4
    return pi

def archimedes_method(iterations: int) -> float:
    """
    Approximates the value of pi using the Archimedes method.
    """
    number_sides = 6
    pi = 3

    for _ in range(iterations):
        central_angle = math.radians(360 / number_sides)
        side_length = 2 * math.sin(central_angle / 2)

        pi = (number_sides * side_length) / 2
        number_sides *= 2

    return pi

def main():
    # Calculate true value of pi
    true_pi = math.pi

    # Time and compute Monte Carlo method
    start_time = time.time()
    monte_carlo_pi = monteCarlo()
    monte_carlo_difference = abs(true_pi - monte_carlo_pi)
    end_time = time.time()
    
    print("Estimated value of pi using Monte Carlo method:", monte_carlo_pi)
    print("Monte Carlo method execution time:", end_time - start_time)
    print("Difference from true value of pi:", monte_carlo_difference)
    print()

    # Time and compute Accumulator method
    start_time = time.time()
    n = 10000
    accumulator_pi = accumulator_method(n)
    accumulator_difference = abs(true_pi - accumulator_pi)
    end_time = time.time()
    
    print(f"Approximate pi value using Accumulator method with {n} iterations = {accumulator_pi}")
    print("Accumulator method execution time:", end_time - start_time)
    print("Difference from true value of pi:", accumulator_difference)
    print()

    # Time and compute Archimedes method
    start_time = time.time()
    archimedes_pi = archimedes_method(10)
    archimedes_difference = abs(true_pi - archimedes_pi)
    end_time = time.time()
    
    print(f"Approximate pi value using Archimedes method with 10 iterations = {archimedes_pi}")
    print("Archimedes method execution time:", end_time - start_time)
    print("Difference from true value of pi:", archimedes_difference)
    print()

    # Find the closest approximation to pi
    min_difference = min(monte_carlo_difference, accumulator_difference, archimedes_difference)
    if min_difference == monte_carlo_difference:
        print("Monte Carlo method is closest to pi.")
    elif min_difference == accumulator_difference:
        print("Accumulator method is closest to pi.")
    else:
        print("Archimedes method is closest to pi.")
    screen = turtle.Screen()
    screen.title("Monte Carlo Method for Pi")
    screen.setup(600, 600)
    screen.setworldcoordinates(-1, -1, 1, 1)

    #Turtle drawing
    monteCarloDrawing()
    

if __name__ == "__main__":
    main()
    
    
'''
Estimated value of pi using Monte Carlo method: 3.14098
Monte Carlo method execution time: 0.5149252414703369
Difference from true value of pi: 0.0006126535897932328

Approximate pi value using Accumulator method with 10000 iterations = 3.1415426535898203
Accumulator method execution time: 0.002000570297241211
Difference from true value of pi: 4.999999997279403e-05

Approximate pi value using Archimedes method with 10 iterations = 3.1415921059992713
Archimedes method execution time: 0.0
Difference from true value of pi: 5.475905218155219e-07

Archimedes method is closest to pi.
'''
