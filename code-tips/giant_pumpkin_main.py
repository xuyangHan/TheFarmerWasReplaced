import navigation
import farm_utils

clear()
size = 12
set_world_size(size)

farm_utils.till_all()

while True:
	pumpkin_positions = []
	
	# Initialize list of all positions in the 8x8 patch
	for x in range(size):
		for y in range(size):
			navigation.goto_naive(x, y)
			use_item(Items.Water)
			if get_entity_type() in [None, Entities.Dead_Pumpkin]:
				plant(Entities.Pumpkin)
				pumpkin_positions.append((x, y))
	
	while pumpkin_positions:
		for pos in pumpkin_positions[:]:  # iterate over a copy since we may remove items
			x, y = pos
			navigation.goto_naive(x, y)
			entity = get_entity_type()
			if entity == Entities.Dead_Pumpkin or entity == None:
				use_item(Items.Water)
				plant(Entities.Pumpkin)
			elif entity == Entities.Pumpkin and can_harvest():
				# Already mature, remove from list
				pumpkin_positions.remove(pos)
	
	# Return to starting point
	# Harvest the giant pumpkin
	navigation.goto_naive(0, 0)
	harvest()