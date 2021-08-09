from solution import predict
import json

with open("eval_data.json", "r") as file:
	sits = json.load(file)

num_trials = len(sits)

num_correct = 0

for sit in sits:

	num_correct += 1 - abs(sit[1] - predict(*sit[0]))


acc = num_correct / num_trials


print("---------------------------")

print("Number of Trials:", num_trials)

print("Prediction Accuracy:", acc)

print("---------------------------")