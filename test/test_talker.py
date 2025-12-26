import pytest
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query
import subprocess
import time
import signal
import sys
from unittest.mock import MagicMock

# person_msgs がなくてもエラーにならないようにモック
sys.modules['person_msgs'] = MagicMock()
sys.modules['person_msgs.srv'] = MagicMock()

@pytest.fixture(scope="module")
def talker():
    # talker.py を裏で起動
    proc = subprocess.Popen(["python3", "mypkg/talker.py"])
    time.sleep(2)  # 起動待ち
    yield
    proc.send_signal(signal.SIGINT)
    proc.wait()

def test_query_service(talker):
    rclpy.init()
    node = Node("test_node")
    client = node.create_client(Query, "query")
    while not client.wait_for_service(timeout_sec=1.0):
        pass

    req = Query.Request()
    req.name = "now"
    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    result = future.result()
    assert result.age == 123
    node.destroy_node()
    rclpy.shutdown()

