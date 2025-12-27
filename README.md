# mypkge
千葉工業大学 未来ロボティクス学科 2025年度 ロボットシステム学内で行った内容に、課題で作成したファイルを追加したものです。

[![Test](https://github.com/zinbekun/mypkge/actions/workflows/test.yml/badge.svg)](https://github.com/zinbekun/mypkge/actions/workflows/test.yml)

[README](https://github.com/zinbekun/mypkge/blob/main/README.md?plain=1#L2)は[akajaika](https://github.com/akajaika/robosys2024/blob/main/README.md?plain=1)（© 2024 Kai Nonaka）を参考に作られています。

## テスト済みの環境
・Ubuntu 24.04.5 LTS

・Python: 3.7～3.12

## mypkge 機能説明
本パッケージ mypkg には、
ROS 2 のサービス通信を用いた以下の 2 つのノードが含まれています。

・talker　ノード：サービスサーバー
役割：
サービス要求を受信し、内容に応じた応答を返す

使用するサービス：person_msgs/srv/Query

サービス名：query

動作内容

サービス要求の request.time を確認する

request.time == "now" の場合
→ 現在の日時を文字列で取得し、レスポンスに格納する

それ以外の場合
→ "unknown" を返す


・listenerノード：サービスクライアント

person_msgs/srv/Query サービスを用いて、
クライアントから送られた要求に対し、現在時刻を返します。


## talker.py ・listener.py 使い方
talker.pyを起動後、別の端末でlistener.pyを起動すると入力した瞬間の時間が表示されます。また、先にlistener.pyを起動すると別端末でtalkr.pyを起動するまで待機中と表示されます。


```shell
$ ros2 run mypkg talker


$ ros2 service call /query person_msgs/srv/Query "time: now"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(time='now')

response:
person_msgs.srv.Query_Response(now='2025-12-27 22:58:42')
```

## ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Itto Hase
