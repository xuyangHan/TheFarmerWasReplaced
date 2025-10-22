# define directions in clockwise
dirs = [East, South, West, North]
dirs_index = {East: 0, South: 1, West: 2, North: 3}

def get_right_dir(dir):
	return dirs[(dirs_index[dir] + 1) % 4]

def get_left_dir(dir):
	return dirs[(dirs_index[dir] - 1) % 4]


# set_world_size(10)
clear()
n = get_world_size()

while True:
	# new maze
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	# follow the wall
	dir = North
	while True:
		# turn right whenever we can
		if can_move(get_right_dir(dir)):
			dir = get_right_dir(dir)
			move(dir)
		else:
			dir = get_left_dir(dir)
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
