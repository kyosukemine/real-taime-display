# ================================================================
# ================================================================
# API-AIO(WDM)
# MultiAiサンプル
#                                                CONTEC Co., Ltd.
# ================================================================
# ================================================================
import matplotlib.pyplot as plt
import ctypes
import ctypes.wintypes
import sys
import caio
import keyboard
import numpy as np
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore
from time import time
import faulthandler
faulthandler.enable()
# ================================================================
# 文字列を数値に変換できるかどうか確認する関数
# ================================================================


def isnum(str, base):
    try:
        if 10 == base:
            int(str, 10)
        else:
            float(str)
    except:
        return False
    return True


# ----------------------------------------
#               変数宣言
# ----------------------------------------
err_str = ctypes.create_string_buffer(256)      # エラー文字列
lret = ctypes.c_long()                          # 関数の戻り値
aio_id = ctypes.c_short()                       # ID
device_name = ctypes.create_string_buffer(50)   # デバイス名
device_name = "AIO001"
AiSamplingCount = ctypes.c_long(0)
MaxAiChannels = ctypes.c_short()                # 最大チャネル数
AiSamplingTimes = 100
AiChannels = int()
P = []
curves = []
T = np.empty(0)
V = []
cnt = int()


# ----------------------------------------
#               デバイスの初期化
# ----------------------------------------
# ----------------------------------------
# 初期化処理
# ----------------------------------------
lret.value = caio.AioInit(device_name.encode(), ctypes.byref(aio_id))
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioInit = {lret.value} : {err_str.value.decode('sjis')}")
    sys.exit()
# ----------------------------------------
# デバイスのリセット
# ----------------------------------------
lret.value = caio.AioResetDevice(aio_id)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioResetDevice = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()
# ----------------------------------------
# メモリのリセット
# ----------------------------------------
lret.value = caio.AioResetAiMemory(aio_id)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioResetAiMemory = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()


# print("\nアナログ入力レンジを以下の範囲から選択してください")
# print("±10V\t\t : 0\t0～10V\t\t : 50")
# print("±5V\t\t : 1\t0～5V\t\t : 51")
# print("±2.5V\t\t : 2\t0～4.095V\t : 52")
# print("±1.25V\t\t : 3\t0～2.5V\t\t : 53")
# print("±1V\t\t : 4\t0～1.25V\t : 54")
# print("±0.625V\t : 5\t0～1V\t\t : 55")
# print("±0.5V\t\t : 6\t0～0.5V\t\t : 56\t")
# print("±0.3125V\t : 7\t0～0.25V\t : 57")
# print("±0.25V\t\t : 8\t0～0.1V\t\t : 58")
# print("±0.125V\t : 9\t0～0.05V\t : 59")
# print("±0.1V\t\t : 10\t0～0.025V\t : 60")
# print("±0.05V\t\t : 11\t0～0.0125V\t : 61")
# print("±0.025V\t : 12\t0～0.01V\t : 62")
# print("±0.0125V\t : 13\t0～20mA\t\t : 100")
# print("±0.01V\t\t : 14\t4～20mA\t\t : 101")
# print("±20mA\t\t : 102\t1～5V\t\t : 150")
# buf = input()

AiRange = 0

# print("")
# ----------------------------------------
# 入力レンジの設定
# ----------------------------------------
lret.value = caio.AioSetAiRangeAll(aio_id, AiRange)
# lret.value = caio.AioSetAiRange(aio_id,AiRange) 個別で設定可能
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioSetAiRangeAll = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()

# ----------------------------------------
# アナログ入力チャネルの設定
# ----------------------------------------
# ----------------------------------------
# 最大チャネル数の取得
# ----------------------------------------
lret.value = caio.AioGetAiMaxChannels(aio_id, ctypes.byref(MaxAiChannels))
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioGetAiMaxChannels = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()
# ----------------------------------------
# 指定チャネル数の設定
# ----------------------------------------
while True:
    print(f"\nアナログ入力を行うチャネル数を入力してください 1～{(MaxAiChannels.value)} : ", end='')
    buf = input()
    if not isnum(buf, 10):
        continue
    AiChannels = int(buf)
    break
# AiChannels = 4
if (AiChannels < 1) or (AiChannels > MaxAiChannels.value):
    print("\nチャネル数が設定可能範囲外です\n")
    caio.AioExit(aio_id)
    sys.exit()

lret.value = caio.AioSetAiChannels(aio_id, AiChannels)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioSetAiChannels = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()

# ----------------------------------------
# クロックの設定
# ----------------------------------------
lret.value = caio.AioSetAiClockType(aio_id, 0)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioSetAiClockType = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()
lret.value = caio.AioSetAiSamplingClock(aio_id, 1000)  # μsec
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioSetAiSamplingClock = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()


P = []
curves = []
T = np.empty(0)
V = []
cnt = int()


# ----------------------------------------
# グラフウィンドウ作成
# ----------------------------------------
# pg.setConfigOption('background', 'w')
# pg.setConfigOption('foreground', 'k')

# app = pg.mkQApp("Plotting Example")
# # mw = QtWidgets.QMainWindow()
# # mw.resize(800,800)

# win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
# win.resize(1000, 600)
# win.setWindowTitle('pyqtgraph example: Plotting')

# # Enable antialiasing for prettier plots
# pg.setConfigOptions(antialias=True)

# for i in range(AiChannels):
#     p = win.addPlot(title=f"[{i}]real-time plot")
#     curve = p.plot(pen='black')
#     P.append(p)
#     curves.append(curve)


#     win.nextRow()


# TIMERANGE = 1 * 1000
# cnt = 0
# V = [np.empty(0) for i in range(AiChannels)]

AiDataType = ctypes.c_float * (AiSamplingTimes*AiChannels*10)               # 配列タイプを作成(変換データ)
AiData = AiDataType()                           # 変換データ
# AiData = ctypes.c_long()
# ----------------------------------------
# サンプリングスタート
# ----------------------------------------
lret.value = caio.AioSetAiStopTrigger(aio_id, 4)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioSetAiStopTrigger = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()
lret.value = caio.AioStartAi(aio_id)
if lret.value != 0:
    caio.AioGetErrorString(lret, err_str)
    print(f"AioStartAi = {lret.value} : {err_str.value.decode('sjis')}")
    caio.AioExit(aio_id)
    sys.exit()

# def update():
#     global curves, T, V, cnt, AiChannels, now, old, start, AiSamplingCount
#     # now = time()
try:
    while True:
            lret.value = caio.AioGetAiSamplingCount(aio_id, AiSamplingCount)
            if lret.value != 0:
                caio.AioGetErrorString(lret, err_str)
                print(f"AioGetAiSamplingCount = {lret.value} : {err_str.value.decode('sjis')}")
                caio.AioExit(aio_id)
                sys.exit()

            print(AiSamplingCount.value)
            if AiSamplingCount.value >= AiSamplingTimes:
                cnt += AiSamplingTimes
                lret.value = caio.AioGetAiSamplingDataEx(aio_id, ctypes.c_long(AiSamplingTimes), AiData)
                if lret.value != 0:
                    caio.AioGetErrorString(lret, err_str)
                    print(f"AioMultiAiEx = {lret.value} : {err_str.value.decode('sjis')}")
                    caio.AioExit(aio_id)
                    sys.exit()
                # for i in range(AiChannels):
                    # print(AiData[i::AiChannels])
                    # print(len(V[i]))
                    # npAiData = np.array(AiData)
                    # V[i] = np.append(V[i], npAiData[i::AiChannels])
                    # curves[i].setData(V[i][max(0, cnt - TIMERANGE):])
                    # curves[i].setData(V[i])

        # cnt += 1
        # if cnt % 10 == 0:
        #     print(cnt)
        # print(len(V[0]))
        # P[0].setTitle((now-old)*1000)
        # caio.AioExit(aio_id)
        # sys.exit()
        # old = now
except KeyboardInterrupt:

    # ----------------------------------------
    # デバイスの終了
    # ----------------------------------------
    lret.value = caio.AioStopAi(aio_id)
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
        sys.exit()

    lret.value = caio.AioExit(aio_id)
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
        sys.exit()
    sys.exit()



# try:
#     start = time()
#     old = time()
#     now = time()

#     timer = QtCore.QTimer()
#     timer.timeout.connect(update)
#     timer.start(10)
#     pg.exec()
#     print(V)
#     # ----------------------------------------
#     # デバイスの終了
#     # ----------------------------------------
#     lret.value = caio.AioStopAi(aio_id)
#     if lret.value != 0:
#         caio.AioGetErrorString(lret, err_str)
#         print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
#         sys.exit()

#     lret.value = caio.AioExit(aio_id)
#     if lret.value != 0:
#         caio.AioGetErrorString(lret, err_str)
#         print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
#         sys.exit()
#     sys.exit()
# except KeyboardInterrupt:

#     # ----------------------------------------
#     # デバイスの終了
#     # ----------------------------------------
#     lret.value = caio.AioStopAi(aio_id)
#     if lret.value != 0:
#         caio.AioGetErrorString(lret, err_str)
#         print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
#         sys.exit()

#     lret.value = caio.AioExit(aio_id)
#     if lret.value != 0:
#         caio.AioGetErrorString(lret, err_str)
#         print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
#         sys.exit()
#     sys.exit()

# print("if keyboard.read_key() == q:break")
# while True:
#     if keyboard.read_key() == "q":
#         break

# l.set_data(v, T)
# plt.pause(.01)


# ----------------------------------------
# main関数呼び出し
# ----------------------------------------
# if __name__ == "__main__":
#     main()
