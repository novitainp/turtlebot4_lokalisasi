#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
import time
from irobot_create_msgs.msg import AudioNote, AudioNoteVector

from turtlebot4_navigation.turtlebot4_navigator import (
    TurtleBot4Directions,
    TurtleBot4Navigator
)

class DeliveryNotifier(Node):
    def __init__(self):
        super().__init__("delivery_notifier")
        self.audio_pub = self.create_publisher(AudioNoteVector, '/cmd_audio', 10)
        
    def indicator(self, times: int = 1):
        msg = AudioNoteVector()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        msg.append = False

        notes = []
        for _ in range(times):
            notes.append(AudioNote(
                frequency=440,
                max_runtime=Duration(sec=2, nanosec=500000000)
            ))
            notes.append(AudioNote(
                frequency=0,
                max_runtime=Duration(sec=0, nanosec=300000000)
            ))

        msg.notes = notes
        self.audio_pub.publish(msg)
        self.get_logger().info(f'Beep sebanyak {times}x')


def main():
    rclpy.init()

    notif = DeliveryNotifier()
    navigator = TurtleBot4Navigator()
    
    navigator.waitUntilNav2Active()

    # ===== 4. WAYPOINTS =====
    wp_pick = navigator.getPoseStamped([-0.6, -2.0], TurtleBot4Directions.NORTH)  # Ruang 203
    wp_place = navigator.getPoseStamped([-7.8, -43.5], TurtleBot4Directions.EAST)    # Lobby BRAIL
    
    navigator.startToPose(wp_pick)
    notif.indicator(times=1)
    time.sleep(5)
    
    navigator.startToPose(wp_place)
    notif.indicator(times=2)
    time.sleep(5)

    navigator.info("Menuju waypoint...")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
