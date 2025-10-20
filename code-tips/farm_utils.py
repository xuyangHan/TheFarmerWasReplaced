def farm_column(crop):
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(crop)
		move(North)

def plant_column(n, crop):
	# Till n columns 
	for _ in range(n):
		for i in range(get_world_size()):
			if (crop == Entities.Carrot):
				till()
			plant(crop)
			move(North)
		move(East)
	for _ in range(n):
		move(West)