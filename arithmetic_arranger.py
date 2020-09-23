import re

# handles the ones where no sum is required, override for the sum one ?
def arithmetic_arranger(problems):

	parsed = []
	for problem in problems :
		# append a tuplet to list
		parsed.append(
			(
				int(), # first number as int
				, # symbol as string
				int(), # second number as int
				# result as int
			)
		)


	# return arranged_problems