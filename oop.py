# class User:
#     name = ''
#     address =''
#     email_id =''
#     username = ''
#     password = ''

#     def login():
#         pass
#     def logout():
#         pass

# class student(User):
#     course =''
#     fee = ''

#     def enroll():
#         pass

#     def attend():
#         pass
#     def upgrade():
#         pass
#     def leave():
#         pass




class shape:
    no_of_side = ''
    length = ''
    name = ''

    def _init_(self, n, l)
        self.no_of_side = n
        self.length = l


    def get_perimeter(self):
        return (self. no_of_side * self.length)

    def get_area(self):
        return 0

    def get_angle(self)
        return(((self.no_of_side-2)*180)/self.no_of_side)

class triangle(shape):
    base = 0
    height = 0


    def _init_(self,b,h,n,name)
        self.base = b
        self.height = h
        super()._init_(n,name)

    def get_area(self):
        return(1/2*self.base*self.height)   



class rectangle(shape)
    length = 0
    breadth =0

    def _init_(self, l, b):
        self.length = l
        self.breadth = b

    def get_area (self):
        return(self._length*self._breadth)