from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share = FindPackageShare(package='auto_nav_gazebo').find('auto_nav_gazebo')
    world_path = os.path.join(pkg_share, 'worlds', 'my_college_world.world')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('gazebo_ros'), '/launch/gazebo.launch.py'
            ]),
            launch_arguments={'world': world_path}.items()
        )
    ])
