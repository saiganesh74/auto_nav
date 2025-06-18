import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher = self.create_publisher(
            Twist ,
            '/cmd_vel',
            10
        )
        timer_period = 0.5 
        self.timer = self.create_timer(
            timer_period,
            self.timer_callback
        )
        self.get_logger().info('Moving robot')
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.1
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing linear {msg.linear.x} and angular {msg.angular.z}')
def main():
    rclpy.init()
    node = MoveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()