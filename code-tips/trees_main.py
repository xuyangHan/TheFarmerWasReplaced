import farm_utils

clear()

farm_utils.till_columns(get_world_size() - 2)

while True:
    x = get_pos_x()
    
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        
        if x < get_world_size() - 2:
            y = get_pos_y()
            if (x + y) % 2 == 0:
                plant(Entities.Tree)
            else:
                plant(Entities.Carrot)
        move(North)
    move(East)