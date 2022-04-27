# Python thing
class nameOfClass:

    # Initiate Self
    def __init__(self, a, b, c):
        # This code will be run for the class passed with the variable 'self' allowing creation of variables.
        # Declares data belonging to this class and sets the initial values.
        # ** Notice all prefaced with 'self'
        self.var_a = a
        self.var_b = b+c

    def __str__(self):
        # Return data in this class as a string
        return 'This classes data as a string'

    def some_function(self, thing):
        # Custom functions should include a self argument
        print("Do things with self")
        return self.var_a, thing

# Start a class

x = nameOfClass('the', 'parameters', 'needed') # Calls __init__

x.some_function('do suff')


############################################################################################################################

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def __str__(self):
        return ("Circle with center at (%d, %d) and radius at %d" % (self.x, self.y, self.radius)) # !! REMEMBER TO USE SELF !! #


a_circle = Circle(5,10,7)
print(a_circle) # Calls the __str__ function


