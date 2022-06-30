# ================================================================
# ================================================================
# API-AIO(WDM)
# MultiAiサンプル
#                                                CONTEC Co., Ltd.
# ================================================================
# ================================================================
# import matplotlib.pyplot as plt
import ctypes
import ctypes.wintypes
import sys
# import caio
# import keyboard
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import time 
from src import AIO_160802GY_USB
import threading

class main():
    def __init__(self):
        self.AIO = AIO_160802GY_USB.AIO_160802GY_USB("AIO000",6)
        self.V = [np.empty(0) for i in range(self.AIO.AiChannels)]
        self.cnt = 0
        P = []
        curves = []
        self.T = np.empty(0)
        # self.V = []
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
            curve.setData([i for i in range(100)])
            p.setRange(yRange=(-2, 2))
            P.append(p)
            curves.append(curve)
            win.nextRow()
        # pg.exec()
        app.processEvents()
        # time.sleep(1000)

        TIMERANGE = 10 * 1000
        cnt = 0
        V = [np.empty(0) for i in range(self.AIO.AiChannels)]

        ptr = 0

        self.AIO.AioStartAi()
        try:
            while True:
                AiSamplingCount = self.AIO.AioGetAiSamplingCount()
                print(AiSamplingCount)
                # print(self.AIO.AiSamplingTimes)
                # print("\033[3A")
                if AiSamplingCount >= self.AIO.AiSamplingTimes:
                    self.cnt += self.AIO.AiSamplingTimes
                    AiData = self.AIO.AioGetAiSamplingDataEx()

                    for i in range(self.AIO.AiChannels):
                        npAiData = np.array(AiData)
                        self.V[i] = np.append(self.V[i], npAiData[i::self.AIO.AiChannels])
                        curves[i].setData(self.V[i][max(0, self.cnt - TIMERANGE):])
                        # curves[i].setData(self.V[i])
                        app.processEvents()

                # self.cnt += 1
                # if self.cnt % 10 ==threading.Thread 0:
                #     print(self.cnt)
                # print(len(self.V[0]))
                # P[0].setTitle((now-old)*1000)
                # caio.AioExit(aio_id)
                # sys.exit()
                # old = now
        except KeyboardInterrupt:
            self.V = np.array(self.V).T
            self.V = np.vstack([[i for i in range(1,self.AIO.AiChannels+1)], self.V])
            np.savetxt('./np_savetxt.csv', self.V, delimiter=',', fmt='%f')

            # ----------------------------------------
            # デバイスの終了
            # ----------------------------------------
            self.AIO.AioStopAi()
            self.AIO.AioExit()
            sys.exit()

main()