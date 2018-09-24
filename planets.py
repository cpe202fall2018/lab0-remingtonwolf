MARS_WEIGHT_MULTIPLIER = 0.38
JUPITER_WEIGHT_MULTIPLIER = 2.34 # used to calculate weights on other planets

def weight_on_planets():
	weightOnEarth = float(input("What do you weigh on earth? ")) # get user input then convert to float before calculations
	weightOnMars = weightOnEarth * MARS_WEIGHT_MULTIPLIER
	weightOnJupiter = weightOnEarth * JUPITER_WEIGHT_MULTIPLIER # get weight on Jupiter and Mars
	print("\n" +
		"On Mars you would weigh", weightOnMars, "pounds.\n" +
		"On Jupiter you would weigh", weightOnJupiter, "pounds.") # print results using \n for new line
	
if __name__ == '__main__':
   weight_on_planets()