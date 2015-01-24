
class Station(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        
        # Put/duplicate Airship from airship.blend at (unX, unY, un_pos_z + 4/3) * City.UNIT_VALUE