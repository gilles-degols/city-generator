
class Platform1(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        fX = un_pos_x + (un_size_x - 1)/2
        fY = un_pos_y + (un_size_y - 1)/2
        
        # Put/duplicate mountain1 at (fX, fY, un_pos_z)*City...
        # Scale it (un_size_x, un_size_y, min(un_size_x, un_size_y))