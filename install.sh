#!/bin/bash

echo "Installing dependencies for auto_nav..."

# ROS 2 basics
sudo apt update
sudo apt install -y \
  ros-humble-turtlebot3* \
  ros-humble-slam-toolbox \
  ros-humble-nav2-bringup \
  ros-humble-navigation2 \
  ros-humble-nav2-simple-commander

# Python packages
pip3 install -U \
  speechrecognition \
  sounddevice \
  numpy

echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc

echo "✅ Done setting up auto_nav!"
