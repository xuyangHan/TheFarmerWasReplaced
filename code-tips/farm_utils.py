def farm_column(crop):
	can_plant_list = [None, Entities.Dead_Pumpkin, Entities.Grass]
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_entity_type() in can_plant_list:
			plant(crop)
		move(North)

def plant_column(crop):
	need_till_list = [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
	for i in range(get_world_size()):
		if (crop in need_till_list):
			till()
		plant(crop)
		move(North)

def plant_columns(crops):
	for i in range(len(crops)):
		crop = crops[i]
		plant_column(crop)
		move(East)

def plant_all(crop):
	need_till_list = [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if (crop in need_till_list and get_ground_type() != Grounds.Soil):
				till()
			plant(crop)
			move(North)
		move(East)
		
def till_columns(n):
	for i in range(n):
		for j in range(get_world_size()):
			till()
			move(North)
		move(East)
	for i in range(n):
		move(West)

def till_grids(n, m):
	for i in range(n):
		for j in range(get_world_size()):
			if j < m:
				till()
			move(North)
		move(East)
	for i in range(n):
		move(West)
		
def till_all():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			move(North)
		move(East)