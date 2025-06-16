cmake_minimum_required(VERSION 3.5)
project(auto_nav_gazebo)

# Required for ROS 2 packages
find_package(ament_cmake REQUIRED)

install(DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
