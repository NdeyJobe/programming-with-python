class Parent () :
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color


billy_cyrus = Parent ("Cyrus", "blue")

print (billy_cyrus.last_name)

class Child (Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

mileycyrus =  Child ("Cyrus", "Blue", 5)

print (mileycyrus.last_name)
print (mileycyrus.number_of_toys)