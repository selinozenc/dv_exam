import json

# PRIMARILY & ONE LINE SOLUTION:

def vehiclesList():

        vehicles = input("Please enter your vehicles: ")

        # as if given input a list format like (in exam sheet) ** [num1,num2,..] **
        vehiclesList = json.loads(vehicles)

        # as if given input a string format like ** num1, num2,.. **
        # vehiclesList = vehicles.split()
        # OR
        # vehiclesList = vehicles.strip('][').split(', ')

        return vehiclesList


def lineCorrector(vehicles):
    # vehicles = [1, 2, 3, 4, 5, 6]
    return list(sum([(vehicles[i + 1], vehicles[i]) for i in range(0, len(vehicles), 2)], ()))

# In comparison with "map" & "itertools", this("list comprehension") is the FASTEST solution. (as far as I know:) )

######################################### NOTES: ####################################################

# - I seperated functions for modularity (also, for one line code rule for lineCorrector func.)
# - I did not add any additional control in the way of given guaranteed constraints. (2 ≤ vehicles.length ≤ 20 & 1 ≤ vehicles[i] ≤ 100)
# - Execution time is satisfactory for desired program performance (for range: 2 ≤ vehicles.length ≤ 20 & 1 ≤ vehicles[i] ≤ 100)


                                        # ... THANKS FOR YOUR TIME ... #
#####################################################################################################

# ------------------------------------------ alternative ------------------------------------------ #

# PAINFUL WAY :)(:
def lineCorrector2():
    vehicles = [1, 2, 3, 4, 5, 6]

    # MULTIPLE LINES:
    t = [(vehicles[i], vehicles[i + 1]) for i in range(0, len(vehicles), 2)]
    z = [(b, a) for a, b in t]

    # ONE LINE: (but NOT exactly!:) )

    return [item for t in z for item in t]


