from sense_hat import SenseHat
from time import sleep
#from libsvm.svmutil import *

sense = SenseHat()

file_path = "output_open.txt"

def write_file(file_path, Gx, Gy, Gz, Ax, Ay, Az):
    with open(file_path, "a", newline="") as f:
        out = "+1"+" Gx:"+str(Gx)+" Gy:"+str(Gy)+" Gz:"+str(Gz)+" Ax:"+str(Ax)+" Ay:"+str(Ay)+" Az:"+str(Az)+"\n"
        #out = "-1"+" 1:"+str(Gx)+" 2:"+str(Gy)+" 3:"+str(Gz)+" 4:"+str(Ax)+" 5:"+str(Ay)+" 6:"+str(Az)+"\n"
        #out = "1:"+str(Gx)+" 2:"+str(Gy)+" 3:"+str(Gz)+" 4:"+str(Ax)+" 5:"+str(Ay)+" 6:"+str(Az)+"\n"
        f.write(out)

count = 0

#while True:
while count < 500:
    count += 1
    if(count%20 ==0):
        print("pause")
        sleep(5)
    print('read')
    
    #Read Accelerometer raw value
    accel = sense.get_accelerometer_raw()
    Ax = accel['x']
    Ay = accel['y']
    Az = accel['z']
    
    #Read Gyroscope raw value
    gyro = sense.get_gyroscope_raw()
    Gx = gyro['x']
    Gy = gyro['y']
    Gz = gyro['z']    
	
    write_file(file_path, Gx, Gy, Gz, Ax, Ay, Az)

    sleep(0.1)
