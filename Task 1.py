Distance = int(input("Distance between cameras? (miles)"))

time1 = input('camera1 time e.g.(17:34:15)').split(':')
time2 = input('camera2 time e.g.(17:34:15)').split(':')

Time = time2 - time1
Time /= 60
Speed = (Distance / Time)
print ("Your speed is %i mph" %(Speed))


