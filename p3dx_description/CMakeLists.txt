cmake_minimum_required(VERSION 2.8.3)
project(p3dx_description)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roslaunch
  roscpp
  sensor_msgs
  geometry_msgs
  visualization_msgs
  std_msgs
  std_srvs
  dynamic_reconfigure
  message_generation
  message_runtime
  nav_msgs
  gazebo_dev
  gazebo_plugins
  gazebo_msgs
  tf
  urdf
  xacro
  cv_bridge
  image_transport
  message_filters
  camera_info_manager
  genmsg
  hector_gazebo_plugins
)


catkin_package()

roslaunch_add_file_check(launch)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(
  DIRECTORY launch meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
