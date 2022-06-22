# fpv_agv
Development of the FPV AGV Project (Neoflux Internal Projects)

### 1. Install YDLiDAR SDK and Package into the workspace <br>

`$ git clone https://github.com/YDLIDAR/YDLidar-SDK.git` <br>
`$ cd YDLidar-SDK/build` <br>
`$ cmake ..` <br>
`$ make` <br>
`$ sudo make install` <br>
<br>
`$ git clone https://github.com/YDLIDAR/ydlidar_ros_driver.git` <br>
`$ catkin_make` <br>
`$ chmod 0777 src/ydlidar_ros_driver/startup/*` <br>
`$ sudo sh src/ydlidar_ros_driver/startup/initenv.sh` <br>
<br>
Reinsert the LiDAR

### 2. Video_Stream <br>
Contains the client and server script to stream video.<br>

### 3. rosserial_arduino <br>
Follow [this](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup). <br>

### 4. nav_bot hardware <br>
Clone from [here](https://github.com/vinay-lanka/navbot_hardware)

### 5. fpv_bringup <br>
The highest abstraction package for the vehicle. Includes launch files and bash scripts.

