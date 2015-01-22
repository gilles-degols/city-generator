from src.Bloc import Bloc

class MyClass(Bloc):


    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)

        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        