#================================================================
#================================================================
# API-AIO(WDM)
# MultiAiサンプル
#                                                CONTEC Co., Ltd.
#================================================================
#================================================================
import ctypes
import ctypes.wintypes
import sys
import caio
import keyboard

#================================================================
# 文字列を数値に変換できるかどうか確認する関数
#================================================================
def isnum(str, base):
    try:
        if 10 == base:
            int(str, 10)
        else:
            float(str)
    except:
        return False
    return True

import matplotlib.pyplot as plt

#================================================================
# メイン関数
#================================================================
def main():
    #----------------------------------------
    # 変数宣言
    #----------------------------------------
    err_str = ctypes.create_string_buffer(256)      # エラー文字列
    lret = ctypes.c_long()                          # 関数の戻り値
    aio_id = ctypes.c_short()                       # ID
    device_name = ctypes.create_string_buffer(50)   # デバイス名
    AiDataType = ctypes.c_float * 256               # 配列タイプを作成(変換データ)
    AiData = AiDataType()                           # 変換データ
    MaxAiChannels = ctypes.c_short()                # 最大チャネル数

    #----------------------------------------
    # デバイス名の入力確認
    #----------------------------------------
    # device_name = input("デバイス名を入力してください : ")
    device_name = "AIO000"
    #----------------------------------------
    # デバイスの初期化
    #----------------------------------------
    #----------------------------------------
    # 初期化処理
    #----------------------------------------
    lret.value = caio.AioInit(device_name.encode(), ctypes.byref(aio_id))
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioInit = {lret.value} : {err_str.value.decode('sjis')}")
        sys.exit()
    #----------------------------------------
    # デバイスのリセット
    #----------------------------------------
    lret.value = caio.AioResetDevice(aio_id)
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioResetDevice = {lret.value} : {err_str.value.decode('sjis')}")
        caio.AioExit(aio_id)
        sys.exit()
    #----------------------------------------
    # アナログ入力レンジの設定
    #----------------------------------------
    while True:
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
        buf = "0"
        if False == isnum(buf, 10):
            continue
        AiRange = int(buf)
        break
    print("")
    #----------------------------------------
    # 入力レンジの設定
    #----------------------------------------
    lret.value = caio.AioSetAiRangeAll(aio_id, AiRange)
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioSetAiRangeAll = {lret.value} : {err_str.value.decode('sjis')}")
        caio.AioExit(aio_id)
        sys.exit()
    #----------------------------------------
    # アナログ入力チャネルの設定
    #----------------------------------------
    #----------------------------------------
    # 最大チャネル数の取得
    #----------------------------------------
    lret.value = caio.AioGetAiMaxChannels(aio_id, ctypes.byref(MaxAiChannels))
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioGetAiMaxChannels = {lret.value} : {err_str.value.decode('sjis')}")
        caio.AioExit(aio_id)
        sys.exit()
    #----------------------------------------
    # 指定チャネル数の設定
    #----------------------------------------
    while True:
        print(f"\nアナログ入力を行うチャネル数を入力してください 1～{(MaxAiChannels.value)} : ", end='')
        buf = input()
        if False == isnum(buf, 10):
            continue
        AiChannels = int(buf)
        break
    if (AiChannels < 1) or (AiChannels > MaxAiChannels.value):
        print("\nチャネル数が設定可能範囲外です\n")
        caio.AioExit(aio_id)
        sys.exit()
    #----------------------------------------
    # 複数チャネルを1回アナログ入力
    #----------------------------------------
    # fig, ax = plt.subplots(1, 1)
    # l, = ax.plot([0,10], [0,10])
    # T = []
    # v = []
    cnt = 0
    print("start")
    while True:
        # if keyboard.read_key() == "q":
        #     break
        # T.append(t)
        lret.value = caio.AioMultiAiEx(aio_id, AiChannels, AiData)
        cnt += 1
        if cnt %10 == 0:
            print(cnt)
        # if lret.value != 0:
        #     caio.AioGetErrorString(lret, err_str)
        #     print(f"AioMultiAiEx = {lret.value} : {err_str.value.decode('sjis')}")
        #     caio.AioExit(aio_id)
        #     sys.exit()
        # if (AiRange == caio.P20MA) or (AiRange == caio.P4TO20MA) or (AiRange == caio.PM20MA):
        #     print("チャネル\t電流")
        #     for i in range(0, AiChannels):
        #         # if i == 2:
        #         #     v.append(float(AiData[i]))
        #         print("{0:d}\t\t{1:f}mA".format(i, AiData[i]))
        # else:
        #     print("チャネル\t電圧")
        #     for i in range(0, AiChannels):
        #         print("{0:d}\t\t{1:f}V".format(i, AiData[i]))
        # l.set_data(v, T)
        # plt.pause(.01)
    #----------------------------------------
    # デバイスの終了
    #----------------------------------------
    lret.value = caio.AioExit(aio_id)
    if lret.value != 0:
        caio.AioGetErrorString(lret, err_str)
        print(f"AioExit = {lret.value} : {err_str.value.decode('sjis')}")
        sys.exit()
    sys.exit()


#----------------------------------------
# main関数呼び出し
#----------------------------------------
if __name__ == "__main__":
    main()
