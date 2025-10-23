import navigation

clear()

n = get_world_size()

def check_and_water():
	while num_items(Items.Water) > 0 and get_water() <= 0.75:
		use_item(Items.Water)

# plant this line until all mature
def plant_line():
	to_plant_positions = []
	for i in range(n):
		to_plant_positions.append((get_pos_x(), i))
	while len(to_plant_positions):
		next_round = []
		for pos in to_plant_positions:
			navigation.goto_naive(pos[0], pos[1])
			if get_ground_type() == Grounds.Grassland:
				till()
			if get_entity_type() != Entities.Pumpkin:
				harvest()
			if not can_harvest():
				next_round.append(pos)
				check_and_water()
				plant(Entities.Pumpkin)
		to_plant_positions = next_round
	

def drone_exec():
	x = get_pos_x()
	while True:
		plant_line()
		
		navigation.goto_naive(x, 0) # wait here until Pumpkin gets harvest
		while get_entity_type() == Entities.Pumpkin:
			pass

# spawn drones 
for i in range(n):
	spawn_drone(drone_exec)
	move(East)
	
while True:
	# main drone to do the last line
	navigation.goto_naive(n - 1, 0)
	plant_line()

	# keep checking if giant pumpkin is already formed by id at (0, 0) and (n-1, n-1)
	while True:
		navigation.goto_naive(0, 0)
		if get_entity_type() == Entities.Pumpkin:
			id = measure()
			navigation.goto_naive(n - 1, n - 1)
			if id == measure():
				harvest()
				break