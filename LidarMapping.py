import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def get_lidar_data(fileName):
    lidarData = {'x': [], 'y': [], 'z': [], 'intensity': [], 'laserId': [], 'azimuth': [], 'distance': [],
                 'timestamp': [], 'vertical_angle': []}

    with open(fileName, 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:  # skip first line
        line = line.split(',')

        lidarData['x'].append(line[3])
        lidarData['y'].append(line[4])
        lidarData['z'].append(line[5])
        lidarData['intensity'].append(line[6])
        lidarData['laserId'].append(line[7])
        lidarData['azimuth'].append(line[8])
        lidarData['distance'].append(line[9])
        lidarData['timestamp'].append(line[11])
        lidarData['vertical_angle'].append(line[12])

    return lidarData

def get_imu_data(fileName):
    imuData = {'year': [], 'month': [], 'day': [], 'hour': [], 'minute': [], 'second': [], 'roll': [],
                 'pitch': [], 'yaw': [], 'lat': [], 'long': [], 'alt': []}

    with open(fileName, 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:  # skip first line
        line = line.split(',')

        imuData['year'].append(line[2])
        imuData['month'].append(line[3])
        imuData['day'].append(line[4])
        imuData['hour'].append(line[5])
        imuData['minute'].append(line[6])
        imuData['second'].append(line[7])
        imuData['roll'].append(line[9])
        imuData['pitch'].append(line[10])
        imuData['yaw'].append(line[11])
        imuData['lat'].append(line[12])
        imuData['long'].append(line[13])
        imuData['alt'].append(line[14])

    return imuData

def main():

    LiDarFileName = "LidarSampleFile.txt"
    ImuFileName = "ImuSampleFile.csv"

    lidarData = get_lidar_data(LiDarFileName)
    imuData = get_imu_data(ImuFileName)

    # test
    #print(imuData['second'][45])


if __name__ == "__main__":
    main()
