TurtleBot4 Navigation -- Point A to Point B
Projek ini merupakan projek UTS dari matakuliah RE702 Lokalisasi dan Pemetaan. Tujuannya adalah menggerakkan TurtleBot4 menuju titik A pada GU lantai 2, kemudian buzzer akan menyala satu kali ketika sudah sampai, lalu melanjutkan ke titik B didalam lab BRAIL dan buzzer akan menyala dua kali.

🔧 Cara Build Workspace
1. Buat Folder Workspace
mkdir -p turtlebot4_ws/src
cd turtlebot4_ws/src
2. Clone Repository
git clone https://github.com/AdriandPratama/turtlebot4.git
3. Install Dependency
cd ..
rosdep install --from-paths src --ignore-src -r -y
4. Build Package
colcon build
🌐 Cara Terhubung ke TurtleBot4
Via Ethernet
ssh ubuntu@192.168.185.3
Via WiFi
ssh ubuntu@your_robot_ip
🗺️ Mode Mapping
1. Jalankan SLAM
ros2 launch turtlebot4_navigation slam.launch.py
2. Jalankan RViz
Untuk ROS2 Jazzy:

ros2 launch turtlebot4_viz view_navigation.launch.py
Untuk ROS2 Humble:

ros2 launch turtlebot4_viz view_robot.launch.py
3. Kendalikan Robot via Teleop Keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true
🧭 Cara Menjalankan Nav2
1. Localization
source install/setup.bash
ros2 launch turtlebot4_pick_place localization.launch.py
2. Navigation
source install/setup.bash
ros2 launch turtlebot4_pick_place uts_nav.launch.py
3. Jalankan RViz
Untuk ROS2 Jazzy:

ros2 launch turtlebot4_viz view_navigation.launch.py
Untuk ROS2 Humble:

ros2 launch turtlebot4_viz view_robot.launch.py
🎯 Menjalankan Script Pengiriman Goal (Point A & B)
source install/setup.bash
ros2 run turtlebot4_pick_place turtlebot4_pick_place_node
