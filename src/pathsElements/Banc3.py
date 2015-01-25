
class Banc3(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_orientation):
        
        if un_orientation == 0:
            # Put banc3 at (un_pos_x, un_pos_y + 1/3, un_pos_z)
        elif un_orientation == 1:
            # Put banc3 at (un_pos_x - 1/3, un_pos_y, un_pos_z)
            # Rotate it 90 z
        elif un_orientation == 2:
            # Put banc3 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
        else:
            # Put banc3 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z