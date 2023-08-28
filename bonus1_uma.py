
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math
import statistics as stats

# Use the math module's constant for pi
pi = math.pi

# get the user inputs
# Use \n to add a blank new line to the terminal before we ask for input
string1 = input("Please enter number 1:")
string2 = input("Please enter number 2:")
string3 = input("Please enter number 3:")
# convert the user input to a number
int1 = int(string1)
int2 = int(string2)
int3 = int(string3)

# calculate the sum of three numbers
sum = int1 + int2 +int3

# log the results
logger.info(f"The sum of numbers {int1}, {int2}, {int3} is  {sum}")


#calculate avaerage of three numbers
result2 = (int1+int2+ int3)/3
logger.info(f"The avareage of numbers {int1}, {int2}, {int3} is  {result2}")

result3 = int1 * int2 * int3
logger.info(f"The product of numbers {int1}, {int2}, {int3} is  {result3}")

result4 = min(int1, int2, int3)
logger.info(f"The minimum of numbers {int1}, {int2}, {int3} is  {result4}")

result5 = max(int1, int2,int3)
logger.info(f"The maximum of numbers {int1}, {int2}, {int3} is  {result5}")

logger.info("Much better! (After you fix it.)")
