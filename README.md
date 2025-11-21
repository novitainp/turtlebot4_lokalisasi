# 🐢TurtleBot4 Navigation — Point A to Point B

Proyek ini merupakan tugas UTS Matakuliah RE702 — Lokalisasi dan Pemetaan.
Tujuan dari proyek ini adalah membuat TurtleBot4 bergerak secara otonom dari Point A di area GU Lantai 2 menuju Point B di Lab BRAIL menggunakan navigation stack (Nav2).

📍 Aksi robot:

Sampai Point A → buzzer bunyi 1x
Sampai Point B → buzzer bunyi 2x

Proyek ini menggunakan ROS2 (Humble/Jazzy), Nav2, SLAM, dan RViz sebagai visualisasi.

📂 Fitur Utama

Navigasi otomatis Point A → Point B

Buzzer notifikasi berdasarkan titik tujuan

SLAM untuk pemetaan lingkungan

Localization + Nav2

Teleop sebagai mode manual

Mendukung ROS2 Humble & Jazzy

🛠️ 1. Cara Build Workspace
Buat Folder Workspace
mkdir -p turtlebot4_ws/src
cd turtlebot4_ws/src

Clone Repository
git clone https://github.com/AdriandPratama/turtlebot4.git

Install Dependency
cd ..
rosdep install --from-paths src --ignore-src -r -y

Build Package
colcon build

🌐 2. Cara Terhubung ke TurtleBot4
Via Ethernet
ssh ubuntu@192.168.185.3

Via WiFi
ssh ubuntu@your_robot_ip

🗺️ 3. Mode Mapping (SLAM)
Jalankan SLAM
ros2 launch turtlebot4_navigation slam.launch.py

Jalankan RViz
ROS2 Jazzy
ros2 launch turtlebot4_viz view_navigation.launch.py

ROS2 Humble
ros2 launch turtlebot4_viz view_robot.launch.py

Teleop Keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true

🧭 4. Menjalankan Nav2
Localization
source install/setup.bash
ros2 launch turtlebot4_pick_place localization.launch.py

Navigation
source install/setup.bash
ros2 launch turtlebot4_pick_place uts_nav.launch.py

Jalankan RViz
ROS2 Jazzy
ros2 launch turtlebot4_viz view_navigation.launch.py

ROS2 Humble
ros2 launch turtlebot4_viz view_robot.launch.py

🎯 5. Menjalankan Script Pengiriman Goal (Point A & B)
source install/setup.bash
ros2 run turtlebot4_pick_place turtlebot4_pick_place_node

📝 Catatan

Pastikan IP robot telah di-export sebagai ROS_DOMAIN_ID atau ROS_LOCALHOST_ONLY=0.

Pastikan maps telah disimpan sebelum menjalankan Nav2.

Semua script berada di dalam package turtlebot4_pick_place.
