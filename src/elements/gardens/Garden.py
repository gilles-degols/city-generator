from random import random, uniform

class Garden(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        
        for x in range(un_pos_x, un_pos_x + un_size_x):
            for y in range(un_pos_y, un_pos_y + un_size_y):
                if random() < 0.33:
                    # Put (duplicate) "banana palm tree (low poly leaves) joined" at (x, y, un_pos_z)
                    fScale = uniform(0.2, 1)
                    # Scale it at fScale
                    pass # Remove this
                
        # Tout joindre et remove doubles.