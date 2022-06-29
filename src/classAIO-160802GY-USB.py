# -*- coding: utf-8 -*-
import ctypes
import os
if os.name == 'nt':
    import ctypes.wintypes 
    import src.caio_win as caio
else:
    import src.caio_lnx as caio
import sys
import numpy as np

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


class AIO_160802GY_USB():
    def __init__(self, devicename="AIO000", AiChannels=1):
        # ----------------------------------------
        #               変数宣言
        # ----------------------------------------
        self.err_str = ctypes.create_string_buffer(256)      # エラー文字列
        self.lret = ctypes.c_long()                          # 関数の戻り値
        self.aio_id = ctypes.c_short()                       # ID
        self.device_name = ctypes.create_string_buffer(50)   # デバイス名
        self.device_name = devicename
        self.AiSamplingCount = ctypes.c_long(0)
        self.MaxAiChannels = ctypes.c_short()                # 最大チャネル数
        self.AiSamplingClock = 1000  # μsec
        self.AiSamplingTimes = 100
        self.AiChannels = AiChannels
        self.P = []
        self.curves = []
        self.T = np.empty(0)
        self.V = []
        self.cnt = int()
        AiDataType = ctypes.c_float * (self.AiSamplingTimes*self.AiChannels)               # 配列タイプを作成(変換データ)
        self.AiData = AiDataType()                            # 変換データ
        # ----------------------------------------
        #               デバイスの初期化
        # ----------------------------------------
        # ----------------------------------------
        # 初期化処理
        # ----------------------------------------
        self.lret.value = caio.AioInit(self.device_name.encode(), ctypes.byref(self.aio_id))
        self._validateLret("AioInit")
        # ----------------------------------------
        # デバイスのリセット
        # ----------------------------------------
        self.lret.value = caio.AioResetDevice(self.aio_id)
        self._validateLret("AioResetDevice")
        # ----------------------------------------
        # メモリのリセット
        # ----------------------------------------
        self.lret.value = caio.AioResetAiMemory(self.aio_id)
        self._validateLret("AioResetAiMemory")

        # print("")
        # ----------------------------------------
        # 入力レンジの設定
        # ----------------------------------------
        # AIO-160802GY-USBは±10V固定固定
        AiRange = 0
        self.lret.value = caio.AioSetAiRangeAll(self.aio_id, AiRange)
        # lret.value = caio.AioSetAiRange(self.aio_id,AiRange) 個別で設定可能
        self._validateLret("AioSetAiRangeAll")
        # ----------------------------------------
        # アナログ入力チャネルの設定
        # ----------------------------------------
        # ----------------------------------------
        # 最大チャネル数の取得
        # ----------------------------------------
        self.lret.value = caio.AioGetAiMaxChannels(self.aio_id, ctypes.byref(self.MaxAiChannels))
        self._validateLret("AioGetAiMaxChannels")
        # ----------------------------------------
        # 指定チャネル数の設定
        # ----------------------------------------
        self.lret.value = caio.AioSetAiChannels(self.aio_id, ctypes.c_short(self.AiChannels))
        self._validateLret("AioSetAiChannels")
        # ----------------------------------------
        # クロックの設定
        # ----------------------------------------
        self.lret.value = caio.AioSetAiClockType(self.aio_id, 0)
        self._validateLret("AioSetAiClockType")
        self.lret.value = caio.AioSetAiSamplingClock(self.aio_id, self.AiSamplingClock)  # μsec
        self._validateLret("AioGetAiSamplingCount")
        # ----------------------------------------
        # Trigger
        # ----------------------------------------

        self.lret.value = caio.AioSetAiStartTrigger(self.aio_id, 0)
        self._validateLret("AioSetAiStartTrigger")
        self.lret.value = caio.AioSetAiStopTrigger(self.aio_id, 4)
        self._validateLret("AioSetAiStopTrigger")

    def AioGetAiSamplingCount(self):
        self.lret.value = caio.AioGetAiSamplingCount(self.aio_id, self.AiSamplingCount)
        self._validateLret("AioGetAiSamplingCount")
        _AiSamplingCount = self.AiSamplingCount.value
        return _AiSamplingCount

    def AioGetAiSamplingDataEx(self):
        caio.AioGetAiSamplingDataEx(self.aio_id, ctypes.c_long(self.AiSamplingTimes), self.AiData)
        _AiData = self.AiData
        return _AiData

    def AioStartAi(self):
        # ----------------------------------------
        # サンプリングスタート
        # ----------------------------------------
        self.lret.value = caio.AioStartAi(self.aio_id)
        self._validateLret("AioStartAi")

    def AioStopAi(self):
        self.lret.value = caio.AioStopAi(self.aio_id)
        self._validateLret("AioStopAi")

    def AioExit(self):
        self.lret.value = caio.AioExit(self.aio_id)
        self._validateLret("AioExit")

    def _validateLret(self, funcname=""):
        if self.lret.value != 0:
            caio.AioGetErrorString(self.lret, self.err_str)
            print(f"{funcname} = {self.lret.value} : {self.err_str.value.decode('sjis')}")
            sys.exit()

