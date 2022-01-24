class Rectangle:
    '''
    When a Rectangle object is created, 
    it should be initialized with width and height attributes. 
    '''       
    
    def __init__(self, width, height):        
        self.width = width
        self.heigth = height
        
    
    def __str__(self):
        '''
        if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
        '''
        
        re_str = "Rectangle(width=" + str(self.width) + ", height=" + str(self.heigth) + ")"
        
        return  re_str
        
    def set_width(self, width):        
        self.width = width
        return self.width
        
        
    def set_height(self, heigth):        
        self.heigth = heigth
        return self.heigth
        
        
    def get_area(self):
        '''
        Returns area (width * height)
        '''
        
        return (self.width*self.heigth)
    
    
    def get_perimeter(self):
        '''
        Returns perimeter (2 * width + 2 * height)
        '''                
        
        return ((2 * self.width) + (2 *self.heigth))
    
    
    def get_diagonal(self):
        '''
        Returns diagonal ((width ** 2 + height ** 2) ** .5)
        '''
        
        return (((self.width ** 2) + (self.heigth ** 2)) ** .5)
    
    
    def get_picture(self):
        '''
        Returns a string that represents the shape using lines of "*". 
        The number of lines should be equal to the height and the number of "*" 
        in each line should be equal to the width. 
        There should be a new line (\n) at the end of each line. 
        If the width or height is larger than 50, this should return the string: "Too big for picture.".
        '''
        
        if self.heigth > 50 or self.width > 50:
            return "Too big for picture."
        
        picture = (("*" * self.width) + "\n") * self.heigth
        
        return picture
        
    
    def get_amount_inside(self, shape):
        '''
        Takes another shape (square or rectangle) as an argument. 
        Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        '''  
   
        result = int(self.get_area() / shape.get_area())
        
        return result
       
    
class Square(Rectangle):
    
    def __init__(self, side): 
        '''
        The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
        '''       
        self.width = side
        self.heigth = side
        
    
    def __str__(self):
        '''
        If an instance of a Square is represented as a string, it should look like: Square(side=9)
        '''
        
        re_str = "Square(side=" + str(self.width) + ")"
        
        return  re_str
    
    def set_side(self, side):        
        self.width = side
        self.heigth = side
        
        return None