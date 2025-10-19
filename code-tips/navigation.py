def goto_naive(x, y):
    """
    Move the drone to the target (x, y) on a wrap-around grid.

    Positive delta_x: drone is east of target
    Positive delta_y: drone is north of target
    """
    half_world_size = get_world_size() / 2

    def choose_direction(delta, positive_dir, negative_dir):
        # Determine shortest wrap-around direction
        if delta >= half_world_size or (-half_world_size <= delta < 0):
            return positive_dir
        else:
            return negative_dir

    # Move in Y first
    while get_pos_y() != y:
        dy = get_pos_y() - y
        move(choose_direction(dy, North, South))

    # Move in X
    while get_pos_x() != x:
        dx = get_pos_x() - x
        move(choose_direction(dx, East, West))
