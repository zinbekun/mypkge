import rclpy
from rclpy.node import Node
from person_msgs.srv import Query
from datetime import datetime, timedelta

rclpy.init()
node = Node("talker")

def cb(request, response):
    if request.time == "now":
        response.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        response.time = "unknown"

    return response



def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
