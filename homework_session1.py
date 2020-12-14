from faker import Faker  # Before running this script, run `pip install faker`
from numpy.random import normal
import numpy as np

# First, let me generate some fake data for you...
fake = Faker()
students = []
for i in range(100):
    students.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'maths': np.clip(normal(3, .5), 0, 4),
        'linguistics': np.clip(normal(3, .5), 0, 4),
        'psychology': np.clip(normal(3, .5), 0, 4)
    })

#for i in range(10):
    #print(fake.name())
# The students variable now contains a list of dictionaries, where each dictionary contains 6 key-value pairs.
# Now, let's try out some things!
first_names = []
last_names = []
addresses = []
maths_grades = []
linguistics_grades = []
psychology_grades = []

# Can you write a loop that fills the above lists with the corresponding values from the list of dictionaries (students)?

for i in students:
    first_names[first_name[i]]

    
# Now, can you turn this dataset into a pandas dataframe?
#   hint: use the list of dictionaries to initialize your dataframe

# What if you wanted to create a 3x100 numpy array of all the grades? (excluding the other information)
#   hint: use the separate lists to create a list of lists to initialize your array

# Now, try to do the following for all four data structures: list of dictionaries, separate lists, dataframe, array.
# Don't spend more than 20 minutes on any of these!
# Thinking about a solution is more important than actually programming it.
# 1. Get all the information belonging to the 20th student
# 2. Find the student with the highest linguistics grade
# 3. Calculate the average grade per student; (maths + linguistics + psychology) / 3
# What operations do you find easier to do in each of these four structures? And what operations harder?
