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

from src import AIO_160802GY_USB

AIO = AIO_160802GY_USB.AIO_160802GY_USB("AIO000",6)
V = [np.empty(0) for i in range(AIO.AiChannels)]

AIO.AioStartAi()

cnt = 0
try:
    while True:
        AiSamplingCount = AIO.AioGetAiSamplingCount()
        print(AiSamplingCount)
        print(AIO.AiSamplingTimes)
        print("\033[3A")
        if AiSamplingCount >= AIO.AiSamplingTimes:
            cnt += AIO.AiSamplingTimes
            AiData = AIO.AioGetAiSamplingDataEx()

            for i in range(AIO.AiChannels):
                npAiData = np.array(AiData)
                V[i] = np.append(V[i], npAiData[i::AIO.AiChannels])
                # curves[i].setData(V[i][max(0, cnt - TIMERANGE):])
                # curves[i].setData(V[i])

        # cnt += 1
        # if cnt % 10 ==threading.Thread 0:
        #     print(cnt)
        # print(len(V[0]))
        # P[0].setTitle((now-old)*1000)
        # caio.AioExit(aio_id)
        # sys.exit()
        # old = now
except KeyboardInterrupt:
    V = np.array(V).T
    V = np.vstack([[i for i in range(1,AIO.AiChannels+1)], V])
    np.savetxt('./np_savetxt.csv', V, delimiter=',', fmt='%f')

    # ----------------------------------------
    # デバイスの終了
    # ----------------------------------------
    AIO.AioStopAi()
    AIO.AioExit()
    sys.exit()
