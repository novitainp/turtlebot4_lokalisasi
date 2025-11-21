#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from irobot_create_msgs.msg import AudioNote, AudioNoteVector

from turtlebot4_navigation.turtlebot4_navigator import (
    TurtleBot4Directions,
    TurtleBot4Navigator
)

class DeliveryNotifier(Node):
    def __init__(self):
        super().__init__("delivery_notifier")
        self.buzzer_pub = self.create_publisher(AudioNoteVector, "/cmd_audio", 10)

    def beep_once(self):
        msg = AudioNoteVector()
        note = AudioNote()
        note.frequency = 1000
        note.max_runtime.sec = 1
        msg.notes = [note]
        self.buzzer_pub.publish(msg)
        self.get_logger().info("Beep 1x - PICK Finished")

    def beep_twice(self):
        msg = AudioNoteVector()
        note1 = AudioNote()
        note1.frequency = 1000
        note1.max_runtime.sec = 1

        note2 = AudioNote()
        note2.frequency = 1000
        note2.max_runtime.sec = 1

        msg.notes = [note1, note2]
        self.buzzer_pub.publish(msg)
        self.get_logger().info("Beep 2x - PLACE Finished")


def main():
    rclpy.init()

    notif = DeliveryNotifier()
    navigator = TurtleBot4Navigator()

    # ===== 1. DOCK CHECK =====
    if not navigator.getDockedStatus():
        navigator.info("Robot tidak sedang di dock, sekarang docking...")
        navigator.dock()

    # ===== 2. SET INITIAL POSE =====
    initial_pose = navigator.getPoseStamped([0.0, 0.0], TurtleBot4Directions.NORTH)
    navigator.setInitialPose(initial_pose)
    navigator.waitUntilNav2Active()

    # ===== 3. UNDOCK =====
    navigator.info("Undocking...")
    navigator.undock()

    # ===== 4. WAYPOINTS =====
    wp_pick = navigator.getPoseStamped([-12.9, -14.9], TurtleBot4Directions.NORTH)  # Ruang 203
    wp_place = navigator.getPoseStamped([-3.7, -5.2], TurtleBot4Directions.EAST)    # Lobby BRAIL

    goals = [wp_pick, wp_place]

    navigator.info("Menuju waypoint...")
    result = navigator.followWaypoints(goals)

    # ===== 5. BEEP SESUAI WAYPOINT =====
    for i, success in enumerate(result):
        if success:
            if i == 0:
                notif.beep_once()   # PICK
            elif i == 1:
                notif.beep_twice()  # PLACE

    # ===== 6. DOCK ULANG =====
    navigator.info("Kembali ke docking...")
    navigator.dock()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
