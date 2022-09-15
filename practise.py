def EXPECTED_BAKE_TIME():
   return int(40)
   """This function will tell the expected bake time for the recipe"""

def bake_time_remaining(self,elapsed_bake_time):
    """This function will return the remaining bake time"""
    return 40-elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """This function will tell the preparation time"""
    return number_of_layers*2

def elapsed_time_in_minute(number_of_layers,elapsed_bake_time):

    time=int(number_of_layers*2)
    return elapsed_bake_time+time
"""
Return elapsed cooking time.
This function takes two numbers representing the number of layers & the time already spent 
baking and calculates the total elapsed minutes spent cooking the lasagna.
"""