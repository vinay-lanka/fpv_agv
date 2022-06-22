#!/bin/bash

#Entry point to start FPV AGV video, LiDAR & command streaming
echo "[INFO]: FPV Started"
source /home/tony/fpv_agv_ws/devel/setup.bash

cd ../../
python3 video_stream/client.py &
#Replace with the start script
roslaunch ydlidar_ros_driver X4.launch
# roslaunch fpv_agv_ws start.launch