#-*- coding: utf-8 -*-
# ================================================================
# ================================================================
# API-AIO(WDM)
# MultiAiサンプル
#                                                CONTEC Co., Ltd.
# ================================================================
# ================================================================
import sys
import numpy as np
from time import time
import faulthandler
faulthandler.enable()
import threading
from src import AIO_160802GY_USB


class main():
    def __init__(self):
        self.AIO = AIO_160802GY_USB.AIO_160802GY_USB("AIO000",6)
        self.V = [np.empty(0) for i in range(self.AIO.AiChannels)]

        self.AIO.AioStartAi()
        self.cnt = 0
        self.frg = True
        # update_thread = threading.Thread(target=self.update, name='update')
        fft_thread = threading.Thread(target=self.fft, name='fft')
        # update_thread.start()
        fft_thread.start()
        try:
            while True:
                AiSamplingCount = self.AIO.AioGetAiSamplingCount()
                # print(AiSamplingCount)
                # print(self.AIO.MaxAiSamplingTimes)
                # print("\033[3A")
                if AiSamplingCount >= self.AIO.MaxAiSamplingTimes//10:
                    AiData, _AiSamplingTimes = self.AIO.AioGetAiSamplingDataEx(AiSamplingCount)
                    self.cnt += _AiSamplingTimes

                    for i in range(self.AIO.AiChannels):
                        npAiData = np.array(AiData)
                        self.V[i] = np.append(self.V[i], npAiData[i:_AiSamplingTimes*self.AIO.AiChannels:self.AIO.AiChannels])
                        # curves[i].setData(self.V[i][max(0, self.cnt - TIMERANGE):])
                        # curves[i].setData(self.V[i])

                # self.cnt += 1
                # if self.cnt % 10 ==threading.Thread 0:
                #     print(self.cnt)
                # print(len(self.V[0]))
                # P[0].setTitle((now-old)*1000)
                # caio.AioExit(aio_id)
                # sys.exit()
                # old = now
        except KeyboardInterrupt:
            self.frg = False
            self.V = np.array(self.V).T
            self.V = np.vstack([[i for i in range(1,self.AIO.AiChannels+1)], self.V])
            np.savetxt('./np_savetxt.csv', self.V, delimiter=',', fmt='%f')

            # ----------------------------------------
            # デバイスの終了
            # ----------------------------------------
            self.AIO.AioStopAi()
            self.AIO.AioExit()
            sys.exit()
    def fft(self):
        while self.frg:
            try:
                
                # print(11111111111111)
                print("-")
                # np.fft.fft(self.V[0][0:1024])
                pass
            except:
                break
        #     print("-", end='')
        pass

if __name__ == '__main__':
    m = main()
