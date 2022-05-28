"""
File: rotten_tomato.py
Name:
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	word_d = {}
	with open(FILENAME, 'r') as f:
		for line in f:
			lst = line.split(':')
			score = int(lst[0][1:3])
			review = lst[1]
			tokens = review.split()
			for token in tokens:
				token = string_manipulation(token)
				if token in word_d:
					word_d[token] += score
				else:
					word_d[token] = score
		print(word_d)

	d = {'positive': [], 'neutral': [], 'negative': []}
	for word, score in word_d.items():
		if score > 0:
			d['positive'].append(word)
		elif score < 0:
			d['negative'].append(word)
		else:
			d['neutral'].append(word)

	for head, lst in d.items():
		print(head)
		print(lst)


def string_manipulation(word):
	s = ''
	for ch in word:
		if ch.isalpha():
			s += ch.lower()
	return s



if __name__ == '__main__':
	main()
