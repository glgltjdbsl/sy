# ROS2 Mobile Robot - Portfolio Assets

This folder contains evidence collected during ROS2 robot simulation coursework (November 2026). These are demonstrations of completed educational exercises, not claims of independently developing the entire Nav2/SLAM stack.

## Images

| File | Description |
| --- | --- |
| [01_urdf_model.jpg](images/01_urdf_model.jpg) | URDF model shown in RViz |
| [02_joint_tf.jpg](images/02_joint_tf.jpg) | Joint / TF RViz verification screenshot |
| [03_gazebo_environment.jpg](images/03_gazebo_environment.jpg) | Gazebo environment and obstacles |
| [04_gazebo_robot.jpg](images/04_gazebo_robot.jpg) | Robot spawned in Gazebo |
| [05_tf_tree.jpg](images/05_tf_tree.jpg) | Final TF tree including wheel and sensor frames |
| [06_lidar_rviz.jpg](images/06_lidar_rviz.jpg) | RViz LaserScan visualization on /scan |
| [07_camera_rviz.jpg](images/07_camera_rviz.jpg) | Camera image visualization (frame from recorded demonstration) |
| [08_slam_rviz.jpg](images/08_slam_rviz.jpg) | SLAM mapping view in RViz |
| [09_slam_map.jpg](images/09_slam_map.jpg) | Map preview; original map is stored in [robot_sim_ws/maps/](../robot_sim_ws/maps/) |
| [10_navigation_rviz.jpg](images/10_navigation_rviz.jpg) | Nav2 map and costmap |
| [11_navigation_gazebo.jpg](images/11_navigation_gazebo.jpg) | Frame from Navigation demonstration |

## Videos

MP4 files are compressed viewing copies of the WebM recordings captured during coursework.

- [01_teleoperation.mp4](videos/01_teleoperation.mp4) - Manual robot drive using `teleop_twist_keyboard`.
- [02_lidar_teleop.mp4](videos/02_lidar_teleop.mp4) - LiDAR scan while driving.
- [03_camera_teleop.mp4](videos/03_camera_teleop.mp4) - Camera image while driving.
- [04_navigation_demo.mp4](videos/04_navigation_demo.mp4) - Nav2 path visualization and robot motion; goal-arrival success has not been independently verified.

## Source files

- [URDF robot model](../robot_sim_ws/src/my_robot_description/)
- [Gazebo simulation](../robot_sim_ws/src/my_robot_gazebo/)
- [SLAM](../robot_sim_ws/src/my_robot_slam/)
- [Nav2 Navigation](../robot_sim_ws/src/my_robot_navigation/)
- [Saved map PGM/YAML](../robot_sim_ws/maps/)

The separately prepared PDF portfolio is not stored in this repository.
