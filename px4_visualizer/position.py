import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, PoseStamped

class PositionVisualizer(Node):
    def __init__(self):
        super().__init__('position_visualizer')

        self.declare_parameter('position_topic_name', '/locate/px4_1/position')
        self.position_topic_name = self.get_parameter('position_topic_name').value
        self.get_logger().info('position_topic_name: %s' % self.position_topic_name)

        self.subscription = self.create_subscription(
            Point,
            self.position_topic_name,
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(PoseStamped, self.position_topic_name+'/PoseStamped', 10)


    def listener_callback(self, msg):
        # self.get_logger().info('msg: [%s, %s, %s]' % (msg.x, msg.y, msg.z))
        pose = PoseStamped()
        pose.header.frame_id = "map"
        pose.pose.position.x = msg.x
        pose.pose.position.y = msg.y
        pose.pose.position.z = msg.z
        self.publisher.publish(pose)


def main(args=None):
    rclpy.init(args=args)
    node = PositionVisualizer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()