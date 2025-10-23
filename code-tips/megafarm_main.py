clear()

def plant_column(x, crop):
	need_till_list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]
	for i in range(get_world_size()):
		if (crop in need_till_list):
			till()
		use_item(Items.Water)
		if(crop == Entities.Tree):
			y = get_pos_y()
			if ((x+y) % 2 == 0):
				plant(Entities.Tree)
			else:
				plant(Entities.Sunflower)
		else:
			plant(crop)
		move(North)

def farm_column(x, crop):
	can_plant_list = [None, Entities.Dead_Pumpkin, Entities.Grass]
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if(get_water() < 0.5):
				use_item(Items.Water)
		if get_entity_type() in can_plant_list:
			if(crop == Entities.Tree):
				y = get_pos_y()
				if ((x+y) % 2 == 0):
					plant(Entities.Tree)
				else:
					plant(Entities.Sunflower)
			else:
				plant(crop)
		move(North)

def task():
	x = get_pos_x()
	crop = crops[x]
	plant_column(x, crop)
	while True:
		farm_column(x, crop)
	
crops = [
		Entities.Tree,
		Entities.Tree,
		Entities.Tree,
		Entities.Tree,
		Entities.Carrot,
		Entities.Carrot,
		Entities.Carrot,
		Entities.Carrot,
		Entities.Pumpkin,
		Entities.Pumpkin,
		Entities.Pumpkin,
		Entities.Pumpkin,
		Entities.Cactus,
		Entities.Cactus,
		Entities.Cactus,
		Entities.Cactus,
		Entities.Sunflower,
		Entities.Sunflower,
		Entities.Sunflower,
		Entities.Sunflower,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass,
		Entities.Grass
		]
		
for i in range(get_world_size()):
	if spawn_drone(task):
		move(East) 
task()