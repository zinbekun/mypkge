# mypkge
千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に、課題で作成したファイルを追加したものです。

[![Test](https://github.com/zinbekun/mypkge/actions/workflows/test.yml/badge.svg)](https://github.com/zinbekun/mypkge/actions/workflows/test.yml)

[README](https://github.com/zinbekun/mypkge/blob/main/README.md?plain=1#L2)は[akajaika](https://github.com/akajaika/robosys2024/blob/main/README.md?plain=1)（© 2024 Kai Nonaka）を参考に作られています。

## テスト済みの環境
・Ubuntu 24.04.5 LTS

・Python: 3.12

## mypkge 機能説明
本パッケージ mypkg には、
ROS 2 のサービス通信を用いた以下の 2 つのノードが含まれています。

### talkerノード：サービスサーバー

役割：サービス要求を受信し、内容に応じた応答を返します。

使用するサービス：person_msgs/srv/Query

サービス名：query

### 動作内容

サービス要求の request.time を確認する

request.time == "now" の場合
→ 現在の日時を文字列で取得し、レスポンスに格納する

それ以外の場合
→ "unknown" を返す


### listenerノード：サービスクライアント

役割：
サービスサーバに要求を送り、応答を受信・表示する

使用するサービス：person_msgs/srv/Query

サービス名：query

### 動作内容

query サービスが利用可能になるまで待機

time = "now" を設定したリクエストを送信

サービス応答を受信

返却された現在時刻をログとして表示
person_msgs/srv/Query サービスを用いて、
クライアントから送られた要求に対し、現在時刻を返します。


## talker.py ・listener.py 使い方
talker.pyを起動後、別の端末で"now"と入力し、サービスを呼び出すと入力した瞬間の時間が表示されます。しかし、now以外を入力しサービスを呼び出すと、"unknown"と表示されます。また、launchファイル経由で実行することもできます。


```shell
$ ros2 run mypkg talker


$ ros2 service call /query person_msgs/srv/Query "time: now"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(time='now')

response:
person_msgs.srv.Query_Response(now='2025-12-27 23:33:35')

$ ros2 service call /query person_msgs/srv/Query "time: y"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(time='y')

response:
person_msgs.srv.Query_Response(now='unknown')


$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/nbalu/.ros/log/2025-12-27-23-59-25-473375-itto-1747
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [1750]
[INFO] [listener-2]: process started with pid [1751]
[listener-2] [INFO] [1766847566.030323328] [listener]: now:2025-12-27 23:59:26
[INFO] [listener-2]: process has finished cleanly [pid 1751]
```

## ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Itto Hase
