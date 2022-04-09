# Code adapted from 
# https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi

import smbus
import csv
from time import sleep
import keyboard
from libsvm.svmutil import *

# some MPU6050 Registers and their Address
# https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address (sudo i2cdetect -y 1)

#file_path = "output.csv"
file_path = "output_closed_4.txt"

def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    #concatenate higher and lower value
    value = ((high << 8) | low)
    
    # to get signed value from mpu6050
    if value > 32768:
        value = value - 65536
    return value

def write_file(file_path, Gx, Gy, Gz, Ax, Ay, Az):
    with open(file_path, "a", newline="") as f:
        #w = csv.writer(f)
        #w.writerow([Gx, Gy, Gz, Ax, Ay, Az])
        #out = "+1"+" Gx:"+str(Gx)+" Gy:"+str(Gy)+" Gz:"+str(Gz)+" Ax:"+str(Ax)+" Ay:"+str(Ay)+" Az:"+str(Az)+"\n"
        out = "-1"+" 1:"+str(Gx)+" 2:"+str(Gy)+" 3:"+str(Gz)+" 4:"+str(Ax)+" 5:"+str(Ay)+" 6:"+str(Az)+"\n"
        #out = "1:"+str(Gx)+" 2:"+str(Gy)+" 3:"+str(Gz)+" 4:"+str(Ax)+" 5:"+str(Ay)+" 6:"+str(Az)+"\n"
        f.write(out)

MPU_Init()

print("Reading Data of Gyroscope and Accelerometer")

count = 0

#while True:
while count < 500:
    count += 1
    
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    
    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    
    # Calibrate based on the value range
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0
    
    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0
    

    #print("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
    #write_file(file_path, Gx, Gy, Gz, Ax, Ay, Az)
    if(Gx > 5):
        print("open")
    elif(Gx < -5):
        print("close")
    sleep(0.1)
