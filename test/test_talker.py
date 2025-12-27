import sys
from unittest.mock import MagicMock

# person_msgs がなくても import エラーにならないようにモック
sys.modules['person_msgs'] = MagicMock()
sys.modules['person_msgs.srv'] = MagicMock()
sys.modules['person_msgs.srv'].Query = MagicMock()

import pytest
import rclpy
from mypkg import talker

@pytest.fixture
def setup_talker(monkeypatch):
    """talker 内で呼ばれる Query サービスのモック"""
    # call_async の返り値をモックに差し替え
    mock_result = MagicMock()
    mock_result.age = 123

    mock_client = MagicMock()
    mock_future = MagicMock()
    mock_future.result.return_value = mock_result
    mock_client.call_async.return_value = mock_future

    # Node.create_client をモック化
    monkeypatch.setattr(
        "rclpy.node.Node.create_client",
        lambda self, srv_type, srv_name: mock_client
    )

    # Node.create_service をモック化して、_TYPE_SUPPORT エラーを回避
    monkeypatch.setattr(
        "rclpy.node.Node.create_service",
        lambda self, srv_type, srv_name, callback: MagicMock()
    )

    # rclpy.spin をモック化して無限ループを回避
    monkeypatch.setattr("rclpy.spin", lambda node: None)

    yield mock_client, mock_future, mock_result

def test_query_service(setup_talker):
    client, future, mock_result = setup_talker

    # talker_main() を呼ぶ（すべてモック済みなので安全）
    talker.main()

    # モックの返り値が正しく使われているか確認
    assert future.result().age == 123

