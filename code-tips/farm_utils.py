def till_column(n):
    # Till n columns 
    for _ in range(n):
        for i in range(get_world_size()):
            till()
            move(North)
        move(East)
    for _ in range(n):
        move(West)


def plant_crop_column(crop_type):
    """Plant one full column of a specific crop"""
    for _ in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(crop_type)
        move(North)