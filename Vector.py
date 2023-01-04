class vector(list):

    def __init__(self, components):
        


    def __repr__(self):     #prints the vector as a list of components
        return("[ {0}, {1} ]".format(self.x, self.y))
    
    def __add__(self, u):
        return vector(self.x + u.x, self.y + u.y)
    
    def dot(self, u):
        return (self.x * u.x + self.y * u.y)

    def __rmul__(self, scalar):
        return vector(self.x * scalar, self.y * scalar)

    def mag(self):
        return ((self.x **2 + self.y **2)**0.5)

