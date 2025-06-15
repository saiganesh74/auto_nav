import rclpy
from rclpy.node import Node
from geometry_msgs.msg import *
from nav2_simple_commander.robot_navigator import *
class NavClient(Node):
    def __init__(self):
        super().__init__('nav_client')
        self.navigator = BasicNavigator()
        self.locations = {
            'library': (2.0, -1.0),
            'lab': (3.5, 0.0),
            'canteen': (1.0, 2.5)
        }
    def create_pose(self,x,y):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y 
        pose.pose.orientation.w = 1.0
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        return pose
    
    def run(self):
        self.get_logger().warn('Waiting for the Nav2 to become active')
        self.navigator.waitUntilNav2Active()
        while rclpy.ok():
            cmd = int(input("Where to go ? \n1. Library \n2. Laboratory \n3. Canteen \n4. Exit"))
            if cmd == '1':
                location = 'library'
            elif cmd== '2':
                location = 'lab'
            elif cmd == '3' :
                location = 'canteen'
            else :
                print("Exiting Nav2")
                break
            
            x ,y = self.locations[location]
            goal_pose = self.create_pose(x,y)
            print(f"Navigating to {location} ")
            
            while not self.navigator.isTaskComplete():
                feedback = self.navigator.feedback()
                if feedback and feedback.distance_remaining :
                    print(f'Distance remaining : {feedback.distance_remaining :.2f}m')
                    
            result = self.navigator.getResult()
            if result == TaskResult.SUCCEEDED:
                print(f"{location.capitalize()} reached sucessfully ")
            elif result == TaskResult.CANCELED :
                print("Cancelled by the user")
            elif result == TaskResult.FAILED:
                print(" Navigation Failed")

def main(args = None):
    rclpy.init(args = args)
    node = NavClient()
    node.run()
    rclpy.shutdown()
    
if __name__== '__main__':
    main()
        