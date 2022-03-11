# Regex and Parsing Validating Credit Card Numbers
# 1. It must start with a 4,5 or 6. It must contain exactly 16 digits (0-9)
# 2. It may have digits in groups of 4, separated by one hyphen "-".
# 3. It must NOT use any other separator like ' ' , '_', etc.
# 4. It must NOT have 4 or more consecutive repeated digits.

import re

regex_patterns = [r"^[456]([\d]{15}|[\d]{3}(-([\d]){4}){3})$", # 1-3 conditions
                  r".*(\d).*\1\1\1\1"] # 4 condition c ''.join(s.split('-'))
t=int(input())
credit_card_numbers = [input().strip() for _ in range(t) ]
for credit_card_number in credit_card_numbers:
    result = re.match(regex_patterns[0],credit_card_number) and not re.search(regex_patterns[1],''.join(credit_card_number.split('-')))
    print(credit_card_number,'Valid' if result else 'Invalid')
