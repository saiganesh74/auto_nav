from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    gazebo_pkg = get_package_share_directory('gazebo_ros')
    tb3_description_pkg = get_package_share_directory('turtlebot3_description')
    world_file = os.path.join(get_package_share_directory('auto_nav_gazebo'), 'worlds', 'my_world.world')

    return LaunchDescription([
        # Launch Gazebo with your world
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_pkg, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'world': world_file}.items()
        ),

        # Spawn TurtleBot3
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'turtlebot3',
                '-file', os.path.join(
                    tb3_description_pkg, 'urdf', 'turtlebot3_burger.urdf'
                ),
                '-x', '0.0', '-y', '0.0', '-z', '0.1'
            ],
            output='screen'
        )
    ])
