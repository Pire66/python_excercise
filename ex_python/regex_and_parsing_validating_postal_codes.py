# Regex and Parsing Validating Postal Codes
#  A valid postal code  P have to fullfil both below requirements:
# 1. P must be a number in the range from 100000 to 999999 inclusive.
# 2. P must not contain more than one alternating repetitive digit pair.

import re

regex_integer_in_range = r'^[1-9]([0-9]){5}$'	# condition 1
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'	# condition 2

t=input()

print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
