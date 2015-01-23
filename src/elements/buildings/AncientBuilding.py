
class AncientBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        # First the side walls:
        # MULTIPLIER TOUTES LES COORDONNÉES PAR City.UNIT_VALUE
        for z in range(0, un_height - 1):
            for x in range(un_size_x):
                # TODO Place Wall Element 1 at (un_pos_x + x, un_pos_y, un_pos_z)
                # TODO Place Wall Element 1 at (un_pos_x + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate it 180 degrees z
                pass # TODO Remove this
                
            for y in range(un_size_y):
                # TODO Place Wall Element 1 at (un_pos_x, un_pos_y + y, un_pos_z) AND rotate it 270 degrees z
                # TODO Place Wall Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + y, un_pos_z) AND rotate it 90 degrees z
                pass # TODO Remove this
            
        # Then the roof:
        # 4 corners:
        # TODO Place Roof Element 1 at (un_pos_x, un_pos_y, un_height - 1)
        # TODO Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y, un_height - 1) AND rotate it 90 degrees z
        # TODO Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 180 degrees z
        # TODO Place Roof Element 1 at (un_pos_x, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 270 degrees z
        
        # The roof sides:
        for x in range(un_size_x - 1):
            # TODO Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y, un_pos_z)
            # TODO Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate 180 degrees z
            pass # TODO Remove this
            
        for y in range(un_size_y - 1):
            # TODO Place Roof Element 2 at (un_pos_x, un_pos_y + 0.5 + y, un_pos_z) AND rotate 270 degrees z
            # TODO Place Roof Element 2 at (un_pos_x + un_size_x - 1, un_pos_y + 0.5 + y, un_pos_z) AND rotate 90 degrees z
            pass # TODO Remove this

        # The roof centre:
        for x in range(un_size_x - 1):
            for y in range(un_size_y - 1):
                # TODO Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y + 0.5 + y, un_pos_z)
                pass # TODO Remove this
            
        # TODO Joindre les objets
        # TODO Prendre une aspirine