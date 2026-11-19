import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    
    pkg_dir = get_package_share_directory('my_robot_description')
    urdf_file = os.path.join(pkg_dir, 'urdf', 'my_robot.urdf.xacro')
    rviz_config_file = os.path.join(pkg_dir, 'rviz', 'my_robot.rviz')

    robot_description = ParameterValue(Command(['xacro ', urdf_file]), value_type=str)
    
    return LaunchDescription([

        # URDF 를 파싱하고 /robot_description 토픽 + TF 발행
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        
        # 연속 조인트의 joint_states 발행
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),

        # RViz2 실행
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_file],
        ),
    ])