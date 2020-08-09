import matplotlib.pyplot as plt
import numpy as np
import pings
import datetime
import seaborn as sns
import argparse
sns.set()
plt.rcParams["font.size"] = 12


def main():
    # 引数
    parser = argparse.ArgumentParser(description='Ping結果を可視化するツール')
    parser.add_argument('--tmax', type=int, default=20, help='表示時間[s]')
    parser.add_argument('--dmax', type=int, default=200, help='表示最大遅延時間[ms]')
    parser.add_argument('--top', type=int, default=1, help='ping回数')
    parser.add_argument('--destination', nargs='*', type=str,
                        default=['google.com', 'yahoo.com', 'amazon.com'],
                        help='pingの宛先')
    args = parser.parse_args()

    # パラメータ
    tmax = args.tmax
    dmax = args.dmax
    top = args.top
    destination = args.destination
    ax = [0] * len(destination)
    x = [0] * len(destination)
    y = [0] * len(destination)
    line = [0] * len(destination)
    res = [0] * len(destination)

    # Pingによる遅延値取得
    p = pings.Ping()

    # グラフの概要を作成
    fig = plt.figure()
    fig.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.95)

    # 初期グラフ作成
    for dest in range(len(destination)):
        ax[dest] = fig.add_subplot(1, len(destination), (dest + 1),
                                   xlabel="time", ylabel="network delay[ms]")
        ax[dest].set_title(destination[dest])
        ax[dest].set_xticks([])
        ax[dest].set_ylim(0, dmax)
        x[dest] = [str(0) for i in range(0, tmax)]
        y[dest] = [0 for i in range(0, tmax)]
        line[dest], = ax[dest].plot(x[dest], y[dest], marker='o')

    while True:
        # 最新の遅延値取得
        for dest in range(len(destination)):
            del x[dest][0]
            x[dest].append(
                datetime.datetime.today().time().strftime("%H:%M:%S"))
            del y[dest][0]
            res[dest] = p.ping(destination[dest], top)
            y[dest].append(res[dest].avg_rtt)
            # 描画
            line[dest].set_data(x[dest], y[dest])
            ax[dest].set_xlim(min(x[dest]), max(x[dest]))

        plt.pause(.05)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        print("Key borad interrupt.")
