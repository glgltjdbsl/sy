import math

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped


class WaypointNavigationNode(Node):

    def __init__(self):
        super().__init__('waypoint_navigation')

        # 웨이포인트를 [x1, y1, yaw1, x2, y2, yaw2, ...] 형태의 배열로 선언
        self.declare_parameter('waypoints', [
            2.0, 1.0, 0.0,
            2.0, -1.0, -1.57,
            0.0, 0.0, 0.0,
        ])

        self._client = ActionClient(
            self, FollowWaypoints, 'follow_waypoints')

        self.get_logger().info('Nav2 액션 서버 대기 중...')
        self._client.wait_for_server()
        self.get_logger().info('액션 서버 연결 완료')

        self._send_goal()

    def _send_goal(self):
        raw = self.get_parameter('waypoints').value

        if len(raw) % 3 != 0:
            self.get_logger().error(
                'waypoints 파라미터는 [x, y, yaw] 단위로 3의 배수여야 합니다')
            rclpy.shutdown()
            return

        poses = []
        for i in range(0, len(raw), 3):
            x, y, yaw = raw[i], raw[i + 1], raw[i + 2]
            poses.append(self._make_pose(x, y, yaw))
            self.get_logger().info(
                f'웨이포인트 {i // 3 + 1}: x={x:.2f}, y={y:.2f}, yaw={yaw:.2f}')

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses

        self.get_logger().info(f'총 {len(poses)}개 웨이포인트 전송')

        send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self._feedback_callback,
        )
        send_goal_future.add_done_callback(self._goal_response_callback)

    def _make_pose(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        pose.pose.orientation.z = math.sin(yaw / 2.0)
        pose.pose.orientation.w = math.cos(yaw / 2.0)
        return pose

    def _goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('목표가 거부되었습니다')
            rclpy.shutdown()
            return

        self.get_logger().info('목표 수락 - 웨이포인트 주행 시작')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_callback)

    def _feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(
            f'현재 이동 중인 웨이포인트: {fb.current_waypoint + 1}번')

    def _result_callback(self, future):
        status = future.result().status

        # STATUS_SUCCEEDED = 4
        if status == 4:
            self.get_logger().info('모든 웨이포인트 도달 완료!')
        else:
            self.get_logger().warn(f'주행 종료 (status={status})')

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = WaypointNavigationNode()
    rclpy.spin(node)


if __name__ == '__main__':
    main()