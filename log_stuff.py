#!/usr/bin/python

import jfitbit
import sys
import getopt


def usage():
        print("\n\nUsage: %s < -w (--weight) | -b (--bike) > \n" % sys.argv[0])
        print("\t-w:\tlog weight")
        print("\t-b:\tlog bike ride [NOT DONE YET!] \n\n")
        quit()

if len(sys.argv) < 2:
	usage()
else:
	client = jfitbit.Jfitbit()

try:
        opts,args = getopt.getopt(sys.argv[1:], "w:b", ["weight=", "bike"])
except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
for o, a in opts:
        if o in ["-w", "--weight"]:
		weight = a
		client.log_weight(weight)
	if o in ["-b", "--bike"]:
		time = raw_input("Enter start time (24-hour format): ")
		mins = int(raw_input("Enter duration in minutes: "))
		distance = int(raw_input("Enter distance in miles: "))
		calories = int(raw_input("Enter approx. calories burned (don't ask how the hell you're supposed to know this): "))
		client.log_bike_ride(time, mins, distance, calories)
        else:
                usage()
                sys.exit(2)


