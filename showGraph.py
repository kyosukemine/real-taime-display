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
# import caio
import keyboard
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from time import time
from src import AIO_160802GY_USB
import threading
# ================================================================
# 文字列を数値に変換できるかどうか確認する関数
# ================================================================


class main():
    def __init__(self):
        self.AIO = AIO_160802GY_USB.AIO_160802GY_USB("AIO001", 6)
        self.V = [np.empty(0) for i in range(self.AIO.AiChannels)]
        self.P = []
        self.urves = []
        self.T = np.empty(0)
        self.V = []
        self.cnt = int()

        # ----------------------------------------
        # グラフウィンドウ作成
        # ----------------------------------------
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        app = pg.mkQApp("Plotting Example")
        # mw = QtWidgets.QMainWindow()
        # mw.resize(800,800)

        win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        win.resize(1000, 600)
        win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        for i in range(self.AIO.AiChannels):
            p = win.addPlot(title=f"[{i}]real-time plot")
            curve = p.plot(pen='black')
            p.setRange(yRange=(-2, 2))
            self.P.append(p)
            self.curves.append(curve)

            win.nextRow()

        self.TIMERANGE = 10 * 1000
        self.cnt = 0
        self.V = [np.empty(0) for i in range(self.AIO.AiChannels)]

        self.ptr = 0
        # ----------------------------------------
        # サンプリングスタート
        # ----------------------------------------
        self.AIO.AioStartAi()
        try:
            update_thread = threading.Thread(target=self.update, name='update')
            fft_thread = threading.Thread(target=self.fft, name='fft')
            update_thread.start()
            fft_thread.start()

            while self.win.isVisible():
                pass
            # ----------------------------------------
            # デバイスの終了
            # ----------------------------------------
            V = np.array(self.V).T
            V = np.vstack([[i for i in range(1, self.AIO.AiChannels+1)], V])
            np.savetxt('./np_savetxt.csv', V, delimiter=',', fmt='%f')

            # ----------------------------------------
            # デバイスの終了
            # ----------------------------------------
            self.AIO.AioStopAi()
            self.AIO.AioExit()
            sys.exit()
        except KeyboardInterrupt:
            V = np.array(V).T
            V = np.vstack([[i for i in range(1, self.AIO.AiChannels+1)], V])
            np.savetxt('./np_savetxt.csv', V, delimiter=',', fmt='%f')
            # ----------------------------------------
            # デバイスの終了
            # ----------------------------------------
            self.AIO.AioStopAi()
            self.AIO.AioExit()
            sys.exit()

    def update(self):
        while self.win.isVisible():
            # now = time()
            AiSamplingCount = self.AIO.AioGetAiSamplingCount()

            # print(AiSamplingCount)
            if AiSamplingCount >= self.AIO.AiSamplingTimes:
                self.cnt += self.AiSamplingTimes
                # print(AiSamplingTimes*AiChannels)
                # print(len(AiData))
                # print(len(V[0]))
                AiData = self.AIO.AioGetAiSamplingDataEx()
                # lret.value = caio.AioGetAiSamplingDataEx(aio_id, ctypes.c_long(400), AiData)
                # pg.plot(np.array(AiData))
                for i in range(self.AIO.AiChannels):
                    # print(AiData[i::AiChannels])
                    # print(len(V[i]))
                    npAiData = np.array(AiData)
                    self.V[i] = np.append(self.V[i], npAiData[i::self.AIO.AiChannels])  # AiSamplingTimes*AiChannels+i+1
                    self.curves[i].setData(self.V[i][max(0, self.cnt - self.TIMERANGE):])
                    # curves[i].setData(V[i])
                self.ptr += 1

    def fft(self):
        while self.win.isVisible():
            print("-", end='')
        pass


if __name__ == '__main__':
    m = main()
