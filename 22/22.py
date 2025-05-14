import string

with open('names.txt', 'r') as file:
	names = file.read().strip('"').split('","')

names.sort(key=str.upper)

def calc_name_worth(name: str) -> int:
	score: int = 0
	for char in name:
		score += string.ascii_uppercase.index(char)+1

	return score


scores = []
for i, name in enumerate(names, 1):
	scores.append(i * calc_name_worth(name))


print(sum(scores))