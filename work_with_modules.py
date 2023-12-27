"""Import our own math file and random library to encrypt numbers in the set range"""

from test_files import math
import random

# r_result = random.randrange(math.sum(31, 1))
# sum_math = math.sum(10, 5) + r_result
#
# print('Encrypted result based on random numbers is: ' + str(sum_math))

"""Create a random login for user using random function of the range library"""
ran = random.randrange(0, 1000)


create_user_login = "user" + str(ran)
print(create_user_login)

