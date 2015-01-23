from random import random

class StairsBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        unScaleX = un_size_x
        unScaleY = un_size_y
        
        # TODO Duplicate Element from Modern 1 building.
        
        fRand = random()
        
        if fRand < 0.25:
            # TODO Put it at (un_pos_x - 0.5, un_pos_y - 0.5) * City.UNIT_VALUE
            pass # TODO Remove this
        elif 0.25 <= fRand < 0.5:
            # TODO Put it at (un_pos_x + un_size_x - 0.5, un_pos_y - 0.5) * City.UNIT_VALUE AND rotate 90 degrees z
            pass # TODO Remove this
        elif 0.5 <= fRand < 0.75:
            # TODO Put it at (un_pos_x + un_size_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 180 degrees z
            pass # TODO Remove this
        else:
            # TODO Put it at (un_pos_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 270 degrees z
            pass # TODO Remove this
        
        # TODO Scale Element (unScaleX, unScaleY)
        --unScaleX
        --unScaleY
        
        while unScaleX > 0 and unScaleY > 0:
            # Duplicate last placed element AND move it upwards (City.UNIT_VALUE)
            # TODO Scale Element (unScaleX, unScaleY, 1)
            --unScaleX
            --unScaleY
            