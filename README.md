This project as Mid-semester exam in course RE 702 Localization and Mapping using Turtlebot4 Robot.
___________  
# **Turtlebot4 Pick and Place Item and Activate Buzzer**
Study Case :

The robot is tasked with delivering goods from Room 203 to the BRAIL Lobby on the 2nd floor of the	of the Batam State Polytechnic. The robot must be able to perform localization, mapping, and autonomous navigation using ROS. To simulate the process of delivering goods, use a buzzer indicator with the following conditions:

• When the robot reaches the pick location (Room 203) and “picks up the item,” the buzzer indicator will sound once or a sound will come from the speaker.	and “picks up the goods,” the buzzer indicator sounds once or a sound is emitted from the speaker.

• When the robot reaches the place location (BRAIL Lobby) and “delivers the item,” the buzzer sounds twice or a sound is emitted from the speaker.
________  
## A. Build Workspace 
1. Create Ros WorkSpace ROS to manage all ROS packages, code, dependencies, and build results.
```
mkdir -p kelompok1/src
cd kelompok1
```
2. Clone this Repository
```
git clone https://github.com/novitainp/turtlebot4_lokalisasi.git
```
3. Install Package and Dependencies
```
cd ../ && rosdep install --from-paths src --ignore-src -r -y
```
4. Then, Build the Package
```
colcon build
```
____________________________  
## B. Connect PC to Turtlebot4
### Via Ethernet Cable
```
ssh ubuntu@192.168.185.3
```
### Via WiFi
```
ssh ubuntu@robot_ip
```
___________  
## C. Generate a Map for the Robot's Route
### Mapping Launch
```
ros2 launch turtlebot4_navigation slam.launch.py
```
### Rviz2 Run
```
ros2 launch turtlebot4_viz view_navigation.launch.py  # for Jazzy
```
then, drive the robot use Teleop Keyboard
### Control Robot using Teleop Keyboard
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true
```
Keep watch of RVIZ as when drive the robot around the area to make sure that the map gets filled out properly.
### Save the Map
```
ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap "name:
  data: 'map_name'"
```
______________________  
## D. Run Mission
### Localization Launch
Load map and activate AMCL
```
ros2 launch turtlebot4_navigation localization.launch.py map:=Mapping_Kelompok1APagiUTS.yaml params:=localization.yaml
```
### Nav2/Navigation Lauch
Enable Navigation2
```
ros2 launch turtlebot4_pick_place uts_nav.launch.py
```
wait until it ```Nav2 is active``` appears on the terminal 
### Rviz Navigation Visualization
```
ros2 launch turtlebot4_viz view_navigation.launch.py  # for Jazzy
```
### Run the Program Pick Item and Place the Item (Room 203 - Lobby BRAIL)
```
cd kelompok1
source install/setup.bash
```
for source the environment
```
ros2 run uts uts
```
_________________________  
### Note:
1. Ensure that the maps (office.yaml and .pgm) correspond to the actual location.
2. Use time.sleep() wisely so that the robot has time to stabilize before the next waypoint.
3. Adjust the waypoint coordinates if using a different map.
4. Ensure that the robot is in the correct starting position before beginning navigation.
_______________________  
Link Video Demonstration Robot : https://youtu.be/SL129U_dq9o
