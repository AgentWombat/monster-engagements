# Improve this function
def predict(strength: int, num_zombies: int, num_spirits: int,
	num_spiders: int, num_ghouls: int) -> int:
	'''
	Predicts the outcome of a battle engagement.
	:param strength: The strength of the human fighting the monsters.
	:param num_zumbies: The number of zombies attacking the human.
	:param num_spirits: The number of spirits attacking the human.
	:param num_spiders: The number of spiders attacking the human.
	:param num_ghouls: The number of ghouls attacking the human.
	:returns: Either '1' indicating that the human should win or '0' indicating
		the monsters should win.
	'''


	if strength > 20:
		return 1

	else:
		return 0