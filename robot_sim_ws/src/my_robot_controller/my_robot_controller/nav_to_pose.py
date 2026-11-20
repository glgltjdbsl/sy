import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.duration import Duration

from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped


class NavToPoseNode(Node):

    def __init__(self):
        super().__init__('nav_to_pose')

        # 파라미터 선언 (launch 파일 또는 CLI로 전달)
        self.declare_parameter('goal_x', 0.0)
        self.declare_parameter('goal_y', 0.0)
        self.declare_parameter('goal_yaw', 0.0)

        self._client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        self.get_logger().info('Nav2 액션 서버 대기 중...')
        self._client.wait_for_server()
        self.get_logger().info('액션 서버 연결 완료')

        self._send_goal()

    def _send_goal(self):
        x = self.get_parameter('goal_x').value
        y = self.get_parameter('goal_y').value
        yaw = self.get_parameter('goal_yaw').value

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = self._make_pose(x, y, yaw)

        self.get_logger().info(
            f'목표 전송: x={x:.2f}, y={y:.2f}, yaw={yaw:.2f}')

        send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self._feedback_callback,
        )
        send_goal_future.add_done_callback(self._goal_response_callback)

    def _make_pose(self, x, y, yaw):
        import math
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0

        # yaw → quaternion
        pose.pose.orientation.z = math.sin(yaw / 2.0)
        pose.pose.orientation.w = math.cos(yaw / 2.0)

        return pose

    def _goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error('목표가 거부되었습니다')
            return

        self.get_logger().info('목표 수락 - 주행 시작')

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_callback)

    def _feedback_callback(self, feedback_msg):
        distance = feedback_msg.feedback.distance_remaining
        self.get_logger().info(f'남은 거리: {distance:.2f} m')

    def _result_callback(self, future):
        result = future.result()
        status = result.status

        # action_msgs/msg/GoalStatus
        # STATUS_SUCCEEDED = 4
        if status == 4:
            self.get_logger().info('목표 도달 완료!')
        else:
            self.get_logger().warn(f'주행 종료 (status={status})')

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = NavToPoseNode()
    rclpy.spin(node)


if __name__ == '__main__':
    main()