def isValidSubsequence(array, sequence):
	sequence_index = 0
	for i in array:
		if i == sequence[sequence_index]:
			sequence_index += 1
			if sequence_index == len(sequence):
				return True
	return False
