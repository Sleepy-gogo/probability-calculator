import copy
import random
# Consider using the modules imported above.

def reshape_balls(balls):
	contents = []
	for key, val in balls.items():
			for i in range(val):
				contents.append(key)
	return contents

class Hat:

	def __init__(self, **balls):
		self.contents = reshape_balls(balls)

	def draw(self, ammount):
		if not ammount or ammount < 0:
			return []

		if ammount > len(self.contents):
			drawed = self.contents
			self.contents = []
			return drawed

		drawed = []
		for i in range(ammount):

			random_idx = random.randint(0, len(self.contents)-1)

			ball = self.contents.pop(random_idx)

			drawed.append(ball)

		return drawed


def lists_are_equal(expected, drawed):
	for item in expected:
		if item not in drawed:
			return False
		idx = drawed.index(item)
		drawed.pop(idx)
	return True



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

	expected = reshape_balls(expected_balls)

	count = 0

	for i in range(num_experiments):
		test_hat = copy.deepcopy(hat)
		balls = test_hat.draw(num_balls_drawn)

		if lists_are_equal(expected, balls):
			count += 1

	return count / num_experiments
