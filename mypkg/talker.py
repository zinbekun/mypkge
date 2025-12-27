#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from datetime import datetime

# person_msgs が無くても動くようにモック
try:
    from person_msgs.srv import Query
except ModuleNotFoundError:
    from unittest.mock import MagicMock
    Query = MagicMock()

rclpy.init()
node = Node("talker")

def cb(request, response):
    # モックでも安全に属性チェック
    req_time = getattr(request, 'time', None)
    if req_time == "now":
        # 実際の属性があれば now に書き込み
        if hasattr(response, 'now'):
            response.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        response.now = "unknown"

    return response

def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()

