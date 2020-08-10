# python-ping-gui

**ルートユーザ**でのみ実行可能．[pings](https://github.com/satoshi03/pings)の制約条件のため．

![サンプル画像](./sample.gif)

## Usage

```
usage: python-ping-gui.py [-h] [--tmax TMAX] [--dmax DMAX] [--top TOP]
                          [--destination [DESTINATION [DESTINATION ...]]]

Ping結果を可視化するツール

optional arguments:
  -h, --help            show this help message and exit
  --tmax TMAX           表示時間[s]
  --dmax DMAX           表示最大遅延時間[ms]
  --top TOP             ping回数
  --destination [DESTINATION [DESTINATION ...]]
                        pingの宛先

```
