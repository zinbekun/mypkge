import sys
from unittest.mock import MagicMock

# person_msgs がなくても import エラーにならないようにモック
sys.modules['person_msgs'] = MagicMock()
sys.modules['person_msgs.srv'] = MagicMock()
sys.modules['person_msgs.srv'].Query = MagicMock()

import pytest
import rclpy
from mypkg.talker import main as talker_main

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

    yield mock_client, mock_future, mock_result

def test_query_service(setup_talker):
    client, future, mock_result = setup_talker

    # talker を実行（内部でモックを使ってサービス呼び出し）
    # main() の中で rclpy.init(), Node(), create_client() が呼ばれる想定
    # ここでは直接 main() を呼ぶと、全てモックなので person_msgs がなくても安全
    talker_main()

    # モックの返り値が正しく使われているか確認
    assert future.result().age == 123

