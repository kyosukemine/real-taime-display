#================================================================
# caio.py
# module file for CONTEC Analog I/O device
#                                                CONTEC.Co., Ltd.
#================================================================
import ctypes

caio_dll = ctypes.cdll.LoadLibrary('libcaio.so')


#----------------------------------------
# Type definition
#----------------------------------------
#----------------------------------------
# Input/Output Range
#----------------------------------------
PM10 = 0                        # +/-10V
PM5 = 1                         # +/-5V
PM25 = 2                        # +/-2.5V
PM125 = 3                       # +/-1.25V
PM1 = 4                         # +/-1V
PM0625 = 5                      # +/-0.625V
PM05 = 6                        # +/-0.5V
PM03125 = 7                     # +/-0.3125V
PM025 = 8                       # +/-0.25V
PM0125 = 9                      # +/-0.125V
PM01 = 10                       # +/-0.1V
PM005 = 11                      # +/-0.05V
PM0025 = 12                     # +/-0.025V
PM00125 = 13                    # +/-0.0125V
PM001 = 14                      # +/-0.01V
P10 = 50                        # 0 ~ 10V
P5 = 51                         # 0 ~ 5V
P4095 = 52                      # 0 ~ 4.095V
P25 = 53                        # 0 ~ 2.5V
P125 = 54                       # 0 ~ 1.25V
P1 = 55                         # 0 ~ 1V
P05 = 56                        # 0 ~ 0.5V
P025 = 57                       # 0 ~ 0.25V
P01 = 58                        # 0 ~ 0.1V
P005 = 59                       # 0 ~ 0.05V
P0025 = 60                      # 0 ~ 0.025V
P00125 = 61                     # 0 ~ 0.0125V
P001 = 62                       # 0 ~ 0.01V
P20MA = 100                     # 0 ~ 20mA
P4TO20MA = 101                  # 4 ~ 20mA
PM20MA = 102                    # +/-20mA
P1TO5 = 150                     # 1 ~ 5V
#----------------------------------------
# Analog Input Event
#----------------------------------------
AIE_START = 0x00000002          # Event that AD converting start conditions are satisfied
AIE_RPTEND = 0x00000010         # Event of repeat end
AIE_END = 0x00000020            # Event of device operation end
AIE_DATA_NUM = 0x00000080       # Event that data of the specified sampling times are stored
AIE_OFERR = 0x00010000          # Event of Overflow
AIE_SCERR = 0x00020000          # Event of sampling clock error
AIE_ADERR = 0x00040000          # Event of AD converting error
#----------------------------------------
# Analog Output Event
#----------------------------------------
AOE_START = 0x00000002          # Event that DA converting start conditions are satisfied
AOE_RPTEND = 0x00000010         # Event of repeat end
AOE_END = 0x00000020            # Event of device operation end
AOE_DATA_NUM = 0x00000080       # Event that data of the specified sampling times are output
AOE_SCERR = 0x00020000          # Event of sampling clock error
AOE_DAERR = 0x00040000          # Event of DA converting error
#----------------------------------------
# Counter Event
#----------------------------------------
CNTE_DATA_NUM = 0x00000010      # Event of count comparison match
CNTE_ORERR = 0x00010000         # Event of count overrun
CNTE_ERR = 0x00020000           # Counter operating error
#----------------------------------------
# Analog Input Status
#----------------------------------------
AIS_BUSY = 0x00000001           # Device is working
AIS_START_TRG = 0x00000002      # Wait the start trigger
AIS_DATA_NUM = 0x00000010       # Store the data of the specified number of samplings
AIS_OFERR = 0x00010000          # Overflow
AIS_SCERR = 0x00020000          # Sampling clock error
AIS_AIERR = 0x00040000          # AD converting error
AIS_DRVERR = 0x00080000         # Driver spec error
#----------------------------------------
# Analog Output Status
#----------------------------------------
AOS_BUSY = 0x00000001           # Device is working
AOS_START_TRG = 0x00000002      # Wait the start trigger
AOS_DATA_NUM = 0x00000010       # Output the data of the specified number of samplings
AOS_SCERR = 0x00020000          # Sampling clock error
AOS_AOERR = 0x00040000          # DA converting error
AOS_DRVERR = 0x00080000         # Driver spec error
#----------------------------------------
# Counter Status 
#----------------------------------------
CNTS_BUSY = 0x00000001          # Counter is working
CNTS_DATA_NUM = 0x00000010      # Count comparison match
CNTS_ORERR = 0x00010000         # Overrun
CNTS_ERR = 0x00020000           # Count operating error
#----------------------------------------
# Analog Input Message
#----------------------------------------
AIOM_AIE_START = 0x1000         # Event that AD converting start condition are satisfied
AIOM_AIE_RPTEND = 0x1001        # Event of repeat end
AIOM_AIE_END = 0x1002           # Event of device operation end
AIOM_AIE_DATA_NUM = 0x1003      # Event that data of the specified sampling times are stored
AIOM_AIE_DATA_TSF = 0x1007      # Event that data of the specified number are transferred
AIOM_AIE_OFERR = 0x1004         # Event of Overflow
AIOM_AIE_SCERR = 0x1005         # Event of sampling clock error
AIOM_AIE_ADERR = 0x1006         # Event of AD converting error
#----------------------------------------
# Analog Output Message
#----------------------------------------
AIOM_AOE_START = 0x1020         # Event that DA converting start conditions are satisfied
AIOM_AOE_RPTEND = 0x1021        # Event of repeat end
AIOM_AOE_END = 0x1022           # Event of device operation end
AIOM_AOE_DATA_NUM = 0x1023      # Event that data of the specified sampling times are output
AIOM_AOE_DATA_TSF = 0x1027      # Event that data of the specified number are transferred
AIOM_AOE_SCERR = 0x1025         # Event of sampling clock error
AIOM_AOE_DAERR = 0x1026         # Event of DA converting error
#----------------------------------------
# Counter Message
#----------------------------------------
AIOM_CNTE_DATA_NUM = 0x1042     # Event of count comparison match
AIOM_CNTE_ORERR = 0x1043        # Event of count overrun
AIOM_CNTE_ERR = 0x1044          # Event of counter operating error
#----------------------------------------
# Counter Action Mode
#----------------------------------------
CNT_LOADPRESET = 0x0000001      # Load the preset count value
CNT_LOADCOMP = 0x0000002        # Load the count comparison value
#----------------------------------------
# Event Controller Destination Signal
#----------------------------------------
AIOECU_DEST_AI_CLK = 4          # Analog input sampling clock
AIOECU_DEST_AI_START = 0        # Analog input converting start signal
AIOECU_DEST_AI_STOP = 2         # Analog input converting stop signal
AIOECU_DEST_AO_CLK = 36         # Analog output sampling clock
AIOECU_DEST_AO_START = 32       # Analog output converting start signal
AIOECU_DEST_AO_STOP = 34        # Analog output converting stop signal
AIOECU_DEST_CNT0_UPCLK = 134    # Up clock signal of counter 0
AIOECU_DEST_CNT1_UPCLK = 135    # Up clock signal of counter 1
AIOECU_DEST_CNT0_START = 128    # Start signal of counter 0
AIOECU_DEST_CNT1_START = 129    # Start signal of counter 1
AIOECU_DEST_CNT0_STOP = 130     # Stop signal of counter 0
AIOECU_DEST_CNT1_STOP = 131     # Stop signal of counter 1
AIOECU_DEST_MASTER1 = 104       # Synchronization bus master signal 1
AIOECU_DEST_MASTER2 = 105       # Synchronization bus master signal 2
AIOECU_DEST_MASTER3 = 106       # Synchronization bus master signal 3
#----------------------------------------
# Event Controller Source Signal
#----------------------------------------
AIOECU_SRC_OPEN = -1            # Not connect
AIOECU_SRC_AI_CLK = 4           # Analog input internal clock signal
AIOECU_SRC_AI_EXTCLK = 146      # Analog input external clock signal
AIOECU_SRC_AI_TRGSTART = 144    # Analog input external trigger start signal
AIOECU_SRC_AI_LVSTART = 28      # Analog input level trigger start signal
AIOECU_SRC_AI_STOP = 17         # Analog input signal that data of the specified sampling times have been converted (No delay)
AIOECU_SRC_AI_STOP_DELAY = 18   # Analog input signal that data of the specified sampling times have been converted (delay)
AIOECU_SRC_AI_LVSTOP = 29       # Analog input level trigger stop signal
AIOECU_SRC_AI_TRGSTOP = 145     # Analog input external trigger stop signal
AIOECU_SRC_AO_CLK = 66          # Analog output internal clock signal
AIOECU_SRC_AO_EXTCLK = 149      # Analog output external clock signal
AIOECU_SRC_AO_TRGSTART = 147    # Analog output external trigger start signal
AIOECU_SRC_AO_STOP_FIFO = 352   # Analog output signal that data of the specified sampling times have been output (FIFO)
AIOECU_SRC_AO_STOP_RING = 80    # Analog output signal that data of the specified sampling times have been output (RING)
AIOECU_SRC_AO_TRGSTOP = 148     # Analog output external trigger stop signal
AIOECU_SRC_CNT0_UPCLK = 150     # Up clock signal of counter 0
AIOECU_SRC_CNT1_UPCLK = 152     # Up clock signal of counter 1
AIOECU_SRC_CNT0_CMP = 288       # Count comparison match of counter 0
AIOECU_SRC_CNT1_CMP = 289       # Count comparison match of counter 1
AIOECU_SRC_SLAVE1 = 136         # Synchronization bus master signal 1
AIOECU_SRC_SLAVE2 = 137         # Synchronization bus master signal 2
AIOECU_SRC_SLAVE3 = 138         # Synchronization bus master signal 3
AIOECU_SRC_START = 384          # Ai, Ao, Cnt software start signal
AIOECU_SRC_STOP = 385           # Ai, Ao, Cnt software stop signal


#----------------------------------------
# Types for callback function.
#----------------------------------------
PAIO_AI_CALLBACK = ctypes.CFUNCTYPE(None,
                                       ctypes.c_short, ctypes.c_short, ctypes.c_short,
                                       ctypes.c_long, ctypes.c_void_p)
PAIO_AO_CALLBACK = ctypes.CFUNCTYPE(None,
                                       ctypes.c_short, ctypes.c_short, ctypes.c_short,
                                       ctypes.c_long, ctypes.c_void_p)
PAIO_CNT_CALLBACK = ctypes.CFUNCTYPE(None,
                                       ctypes.c_short, ctypes.c_short, ctypes.c_short,
                                       ctypes.c_long, ctypes.c_void_p)


#----------------------------------------
# Prototype definition
#----------------------------------------
#----------------------------------------
# Common function
#----------------------------------------
# C Prototype: long AioInit(char * DeviceName, short * Id);
AioInit = caio_dll.AioInit
AioInit.restype = ctypes.c_long
AioInit.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioExit(short Id);
AioExit = caio_dll.AioExit
AioExit.restype = ctypes.c_long
AioExit.argtypes = [ctypes.c_short]

# C Prototype: long AioResetDevice(short Id);
AioResetDevice = caio_dll.AioResetDevice
AioResetDevice.restype = ctypes.c_long
AioResetDevice.argtypes = [ctypes.c_short]

# C Prototype: long AioGetErrorString(long ErrorCode, char * ErrorString);
AioGetErrorString = caio_dll.AioGetErrorString
AioGetErrorString.restype = ctypes.c_long
AioGetErrorString.argtypes = [ctypes.c_long, ctypes.c_char_p]

# C Prototype: long AioQueryDeviceName(short Index, char * DeviceName, char * Device);
AioQueryDeviceName = caio_dll.AioQueryDeviceName
AioQueryDeviceName.restype = ctypes.c_long
AioQueryDeviceName.argtypes = [ctypes.c_short, ctypes.c_char_p, ctypes.c_char_p]

# C Prototype: long AioGetDeviceType(char * Device, short * DeviceType);
AioGetDeviceType = caio_dll.AioGetDeviceType
AioGetDeviceType.restype = ctypes.c_long
AioGetDeviceType.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetControlFilter(short Id, short Signal, float Value);
AioSetControlFilter = caio_dll.AioSetControlFilter
AioSetControlFilter.restype = ctypes.c_long
AioSetControlFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetControlFilter(short Id, short Signal, float *Value);
AioGetControlFilter = caio_dll.AioGetControlFilter
AioGetControlFilter.restype = ctypes.c_long
AioGetControlFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioResetProcess(short Id);
AioResetProcess = caio_dll.AioResetProcess
AioResetProcess.restype = ctypes.c_long
AioResetProcess.argtypes = [ctypes.c_short]

#----------------------------------------
# Analog input function
#----------------------------------------
# C Prototype: long AioSingleAi(short Id, short AiChannel, long * AiData);
AioSingleAi = caio_dll.AioSingleAi
AioSingleAi.restype = ctypes.c_long
AioSingleAi.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSingleAiEx(short Id, short AiChannel, float * AiData);
AioSingleAiEx = caio_dll.AioSingleAiEx
AioSingleAiEx.restype = ctypes.c_long
AioSingleAiEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioMultiAi(short Id, short AiChannels, long * AiData);
AioMultiAi = caio_dll.AioMultiAi
AioMultiAi.restype = ctypes.c_long
AioMultiAi.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioMultiAiEx(short Id, short AiChannels, float * AiData);
AioMultiAiEx = caio_dll.AioMultiAiEx
AioMultiAiEx.restype = ctypes.c_long
AioMultiAiEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioSingleAiSR(short Id, short AiChannel, long * AiData, unsigned short * Timestamp, unsigned char Mode);
AioSingleAiSR = caio_dll.AioSingleAiSR
AioSingleAiSR.restype = ctypes.c_long
AioSingleAiSR.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_ushort), ctypes.c_ubyte]

# C Prototype: long AioSingleAiExSR(short Id, short AiChannel, float * AiData, unsigned short * Timestamp, unsigned char Mode);
AioSingleAiExSR = caio_dll.AioSingleAiExSR
AioSingleAiExSR.restype = ctypes.c_long
AioSingleAiExSR.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_ushort), ctypes.c_ubyte]

# C Prototype: long AioMultiAiSR(short Id, short AiChannels, long * AiData, unsigned short * Timestamp, unsigned char Mode);
AioMultiAiSR = caio_dll.AioMultiAiSR
AioMultiAiSR.restype = ctypes.c_long
AioMultiAiSR.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_ushort), ctypes.c_ubyte]

# C Prototype: long AioMultiAiExSR(short Id, short AiChannels, float * AiData, unsigned short * Timestamp, unsigned char Mode);
AioMultiAiExSR = caio_dll.AioMultiAiExSR
AioMultiAiExSR.restype = ctypes.c_long
AioMultiAiExSR.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_ushort), ctypes.c_ubyte]

# C Prototype: long AioGetAiResolution(short Id, short * AiResolution);
AioGetAiResolution = caio_dll.AioGetAiResolution
AioGetAiResolution.restype = ctypes.c_long
AioGetAiResolution.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiInputMethod(short Id, short AiInputMethod);
AioSetAiInputMethod = caio_dll.AioSetAiInputMethod
AioSetAiInputMethod.restype = ctypes.c_long
AioSetAiInputMethod.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiInputMethod(short Id, short * AiInputMethod);
AioGetAiInputMethod = caio_dll.AioGetAiInputMethod
AioGetAiInputMethod.restype = ctypes.c_long
AioGetAiInputMethod.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioGetAiMaxChannels(short Id, short * AiMaxChannels);
AioGetAiMaxChannels = caio_dll.AioGetAiMaxChannels
AioGetAiMaxChannels.restype = ctypes.c_long
AioGetAiMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiChannels(short Id, short AiChannels);
AioSetAiChannels = caio_dll.AioSetAiChannels
AioSetAiChannels.restype = ctypes.c_long
AioSetAiChannels.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiChannels(short Id, short * AiChannels);
AioGetAiChannels = caio_dll.AioGetAiChannels
AioGetAiChannels.restype = ctypes.c_long
AioGetAiChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiChannelSequence(short Id, short AiSequence, short AiChannel);
AioSetAiChannelSequence = caio_dll.AioSetAiChannelSequence
AioSetAiChannelSequence.restype = ctypes.c_long
AioSetAiChannelSequence.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiChannelSequence(short Id, short AiSequence, short * AiChannel);
AioGetAiChannelSequence = caio_dll.AioGetAiChannelSequence
AioGetAiChannelSequence.restype = ctypes.c_long
AioGetAiChannelSequence.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiRange(short Id, short AiChannel, short AiRange);
AioSetAiRange = caio_dll.AioSetAiRange
AioSetAiRange.restype = ctypes.c_long
AioSetAiRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioSetAiRangeAll(short Id, short AiRange);
AioSetAiRangeAll = caio_dll.AioSetAiRangeAll
AioSetAiRangeAll.restype = ctypes.c_long
AioSetAiRangeAll.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiRange(short Id, short AiChannel, short * AiRange);
AioGetAiRange = caio_dll.AioGetAiRange
AioGetAiRange.restype = ctypes.c_long
AioGetAiRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioGetAiMemorySize(short Id, long *AiMemorySize);
AioGetAiMemorySize = caio_dll.AioGetAiMemorySize
AioGetAiMemorySize.restype = ctypes.c_long
AioGetAiMemorySize.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiMemoryType(short Id, short AiMemoryType);
AioSetAiMemoryType = caio_dll.AioSetAiMemoryType
AioSetAiMemoryType.restype = ctypes.c_long
AioSetAiMemoryType.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiMemoryType(short Id, short * AiMemoryType);
AioGetAiMemoryType = caio_dll.AioGetAiMemoryType
AioGetAiMemoryType.restype = ctypes.c_long
AioGetAiMemoryType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiRepeatTimes(short Id, long AiRepeatTimes);
AioSetAiRepeatTimes = caio_dll.AioSetAiRepeatTimes
AioSetAiRepeatTimes.restype = ctypes.c_long
AioSetAiRepeatTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAiRepeatTimes(short Id, long * AiRepeatTimes);
AioGetAiRepeatTimes = caio_dll.AioGetAiRepeatTimes
AioGetAiRepeatTimes.restype = ctypes.c_long
AioGetAiRepeatTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiClockType(short Id, short AiClockType);
AioSetAiClockType = caio_dll.AioSetAiClockType
AioSetAiClockType.restype = ctypes.c_long
AioSetAiClockType.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiClockType(short Id, short * AiClockType);
AioGetAiClockType = caio_dll.AioGetAiClockType
AioGetAiClockType.restype = ctypes.c_long
AioGetAiClockType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiSamplingClock(short Id, float AiSamplingClock);
AioSetAiSamplingClock = caio_dll.AioSetAiSamplingClock
AioSetAiSamplingClock.restype = ctypes.c_long
AioSetAiSamplingClock.argtypes = [ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetAiSamplingClock(short Id, float * AiSamplingClock);
AioGetAiSamplingClock = caio_dll.AioGetAiSamplingClock
AioGetAiSamplingClock.restype = ctypes.c_long
AioGetAiSamplingClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioSetAiScanClock(short Id, float AiScanClock);
AioSetAiScanClock = caio_dll.AioSetAiScanClock
AioSetAiScanClock.restype = ctypes.c_long
AioSetAiScanClock.argtypes = [ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetAiScanClock(short Id, float * AiScanClock);
AioGetAiScanClock = caio_dll.AioGetAiScanClock
AioGetAiScanClock.restype = ctypes.c_long
AioGetAiScanClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioSetAiClockEdge(short Id, short AoClockEdge);
AioSetAiClockEdge = caio_dll.AioSetAiClockEdge
AioSetAiClockEdge.restype = ctypes.c_long
AioSetAiClockEdge.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiClockEdge(short Id, short * AoClockEdge);
AioGetAiClockEdge = caio_dll.AioGetAiClockEdge
AioGetAiClockEdge.restype = ctypes.c_long
AioGetAiClockEdge.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiStartTrigger(short Id, short AiStartTrigger);
AioSetAiStartTrigger = caio_dll.AioSetAiStartTrigger
AioSetAiStartTrigger.restype = ctypes.c_long
AioSetAiStartTrigger.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiStartTrigger(short Id, short * AiStartTrigger);
AioGetAiStartTrigger = caio_dll.AioGetAiStartTrigger
AioGetAiStartTrigger.restype = ctypes.c_long
AioGetAiStartTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiStartLevel(short Id, short AiChannel, long AiStartLevel, short AiDirection);
AioSetAiStartLevel = caio_dll.AioSetAiStartLevel
AioSetAiStartLevel.restype = ctypes.c_long
AioSetAiStartLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_short]

# C Prototype: long AioSetAiStartLevelEx(short Id, short AiChannel, float AiStartLevel, short AiDirection);
AioSetAiStartLevelEx = caio_dll.AioSetAiStartLevelEx
AioSetAiStartLevelEx.restype = ctypes.c_long
AioSetAiStartLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_short]

# C Prototype: long AioGetAiStartLevel(short Id, short AiChannel, long * AiStartLevel, short * AiDirection);
AioGetAiStartLevel = caio_dll.AioGetAiStartLevel
AioGetAiStartLevel.restype = ctypes.c_long
AioGetAiStartLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioGetAiStartLevelEx(short Id, short AiChannel, float * AiStartLevel, short * AiDirection);
AioGetAiStartLevelEx = caio_dll.AioGetAiStartLevelEx
AioGetAiStartLevelEx.restype = ctypes.c_long
AioGetAiStartLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiStartInRange(short Id, short AiChannel, long Level1, long Level2, long StateTimes);
AioSetAiStartInRange = caio_dll.AioSetAiStartInRange
AioSetAiStartInRange.restype = ctypes.c_long
AioSetAiStartInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]

# C Prototype: long AioSetAiStartInRangeEx(short Id, short AiChannel, float Level1, float Level2, long StateTimes);
AioSetAiStartInRangeEx = caio_dll.AioSetAiStartInRangeEx
AioSetAiStartInRangeEx.restype = ctypes.c_long
AioSetAiStartInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]

# C Prototype: long AioGetAiStartInRange(short Id, short AiChannel, long *Level1, long *Level2, long *StateTimes);
AioGetAiStartInRange = caio_dll.AioGetAiStartInRange
AioGetAiStartInRange.restype = ctypes.c_long
AioGetAiStartInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiStartInRangeEx(short Id, short AiChannel, float *Level1, float *Level2, long *StateTimes);
AioGetAiStartInRangeEx = caio_dll.AioGetAiStartInRangeEx
AioGetAiStartInRangeEx.restype = ctypes.c_long
AioGetAiStartInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiStartOutRange(short Id, short AiChannel, long Level1, long Level2, long StateTimes);
AioSetAiStartOutRange = caio_dll.AioSetAiStartOutRange
AioSetAiStartOutRange.restype = ctypes.c_long
AioSetAiStartOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]

# C Prototype: long AioSetAiStartOutRangeEx(short Id, short AiChannel, float Level1, float Level2, long StateTimes);
AioSetAiStartOutRangeEx = caio_dll.AioSetAiStartOutRangeEx
AioSetAiStartOutRangeEx.restype = ctypes.c_long
AioSetAiStartOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]

# C Prototype: long AioGetAiStartOutRange(short Id, short AiChannel, long *Level1, long *Level2, long *StateTimes);
AioGetAiStartOutRange = caio_dll.AioGetAiStartOutRange
AioGetAiStartOutRange.restype = ctypes.c_long
AioGetAiStartOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiStartOutRangeEx(short Id, short AiChannel, float *Level1, float *Level2, long *StateTimes);
AioGetAiStartOutRangeEx = caio_dll.AioGetAiStartOutRangeEx
AioGetAiStartOutRangeEx.restype = ctypes.c_long
AioGetAiStartOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiStopTrigger(short Id, short AiStopTrigger);
AioSetAiStopTrigger = caio_dll.AioSetAiStopTrigger
AioSetAiStopTrigger.restype = ctypes.c_long
AioSetAiStopTrigger.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAiStopTrigger(short Id, short * AiStopTrigger);
AioGetAiStopTrigger = caio_dll.AioGetAiStopTrigger
AioGetAiStopTrigger.restype = ctypes.c_long
AioGetAiStopTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiStopTimes(short Id, long AiStopTimes);
AioSetAiStopTimes = caio_dll.AioSetAiStopTimes
AioSetAiStopTimes.restype = ctypes.c_long
AioSetAiStopTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAiStopTimes(short Id, long * AiStopTimes);
AioGetAiStopTimes = caio_dll.AioGetAiStopTimes
AioGetAiStopTimes.restype = ctypes.c_long
AioGetAiStopTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiStopLevel(short Id, short AiChannel, long AiStopLevel, short AiDirection);
AioSetAiStopLevel = caio_dll.AioSetAiStopLevel
AioSetAiStopLevel.restype = ctypes.c_long
AioSetAiStopLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_short]

# C Prototype: long AioSetAiStopLevelEx(short Id, short AiChannel, float AiStopLevel, short AiDirection);
AioSetAiStopLevelEx = caio_dll.AioSetAiStopLevelEx
AioSetAiStopLevelEx.restype = ctypes.c_long
AioSetAiStopLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_short]

# C Prototype: long AioGetAiStopLevel(short Id, short AiChannel, long * AiStopLevel, short * AiDirection);
AioGetAiStopLevel = caio_dll.AioGetAiStopLevel
AioGetAiStopLevel.restype = ctypes.c_long
AioGetAiStopLevel.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioGetAiStopLevelEx(short Id, short AiChannel, float * AiStopLevel, short * AiDirection);
AioGetAiStopLevelEx = caio_dll.AioGetAiStopLevelEx
AioGetAiStopLevelEx.restype = ctypes.c_long
AioGetAiStopLevelEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAiStopInRange(short Id, short AiChannel, long Level1, long Level2, long StateTimes);
AioSetAiStopInRange = caio_dll.AioSetAiStopInRange
AioSetAiStopInRange.restype = ctypes.c_long
AioSetAiStopInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]

# C Prototype: long AioSetAiStopInRangeEx(short Id, short AiChannel, float Level1, float Level2, long StateTimes);
AioSetAiStopInRangeEx = caio_dll.AioSetAiStopInRangeEx
AioSetAiStopInRangeEx.restype = ctypes.c_long
AioSetAiStopInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]

# C Prototype: long AioGetAiStopInRange(short Id, short AiChannel, long *Level1, long *Level2, long *StateTimes);
AioGetAiStopInRange = caio_dll.AioGetAiStopInRange
AioGetAiStopInRange.restype = ctypes.c_long
AioGetAiStopInRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiStopInRangeEx(short Id, short AiChannel, float *Level1, float *Level2, long *StateTimes);
AioGetAiStopInRangeEx = caio_dll.AioGetAiStopInRangeEx
AioGetAiStopInRangeEx.restype = ctypes.c_long
AioGetAiStopInRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiStopOutRange(short Id, short AiChannel, long Level1, long Level2, long StateTimes);
AioSetAiStopOutRange = caio_dll.AioSetAiStopOutRange
AioSetAiStopOutRange.restype = ctypes.c_long
AioSetAiStopOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long]

# C Prototype: long AioSetAiStopOutRangeEx(short Id, short AiChannel, float Level1, float Level2, long StateTimes);
AioSetAiStopOutRangeEx = caio_dll.AioSetAiStopOutRangeEx
AioSetAiStopOutRangeEx.restype = ctypes.c_long
AioSetAiStopOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float, ctypes.c_float, ctypes.c_long]

# C Prototype: long AioGetAiStopOutRange(short Id, short AiChannel, long *Level1, long *Level2, long *StateTimes);
AioGetAiStopOutRange = caio_dll.AioGetAiStopOutRange
AioGetAiStopOutRange.restype = ctypes.c_long
AioGetAiStopOutRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiStopOutRangeEx(short Id, short AiChannel, float *Level1, float *Level2, long *StateTimes);
AioGetAiStopOutRangeEx = caio_dll.AioGetAiStopOutRangeEx
AioGetAiStopOutRangeEx.restype = ctypes.c_long
AioGetAiStopOutRangeEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiStopDelayTimes(short Id, long AiStopDelayTimes);
AioSetAiStopDelayTimes = caio_dll.AioSetAiStopDelayTimes
AioSetAiStopDelayTimes.restype = ctypes.c_long
AioSetAiStopDelayTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAiStopDelayTimes(short Id, long * AiStopDelayTimes);
AioGetAiStopDelayTimes = caio_dll.AioGetAiStopDelayTimes
AioGetAiStopDelayTimes.restype = ctypes.c_long
AioGetAiStopDelayTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAiCallBackProc(short Id,
#                                               long (_stdcall *pProc)(short Id, short AiEvent, WPARAM wParam, LPARAM lParam, void *Param), long AiEvent, void *Param);
AioSetAiCallBackProc = caio_dll.AioSetAiCallBackProc
AioSetAiCallBackProc.restype = ctypes.c_long
AioSetAiCallBackProc.argtypes = [ctypes.c_short, PAIO_AI_CALLBACK, ctypes.c_long, ctypes.c_void_p]

# C Prototype: long AioSetAiEventSamplingTimes(short Id, long AiSamplingTimes);
AioSetAiEventSamplingTimes = caio_dll.AioSetAiEventSamplingTimes
AioSetAiEventSamplingTimes.restype = ctypes.c_long
AioSetAiEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAiEventSamplingTimes(short Id, long * AiSamplingTimes);
AioGetAiEventSamplingTimes = caio_dll.AioGetAiEventSamplingTimes
AioGetAiEventSamplingTimes.restype = ctypes.c_long
AioGetAiEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioStartAi(short Id);
AioStartAi = caio_dll.AioStartAi
AioStartAi.restype = ctypes.c_long
AioStartAi.argtypes = [ctypes.c_short]

# C Prototype: long AioStartAiSync(short Id, long TimeOut);
AioStartAiSync = caio_dll.AioStartAiSync
AioStartAiSync.restype = ctypes.c_long
AioStartAiSync.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioStopAi(short Id);
AioStopAi = caio_dll.AioStopAi
AioStopAi.restype = ctypes.c_long
AioStopAi.argtypes = [ctypes.c_short]

# C Prototype: long AioGetAiStatus(short Id, long * AiStatus);
AioGetAiStatus = caio_dll.AioGetAiStatus
AioGetAiStatus.restype = ctypes.c_long
AioGetAiStatus.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiSamplingCount(short Id, long * AiSamplingCount);
AioGetAiSamplingCount = caio_dll.AioGetAiSamplingCount
AioGetAiSamplingCount.restype = ctypes.c_long
AioGetAiSamplingCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiStopTriggerCount(short Id, long * AiStopTriggerCount);
AioGetAiStopTriggerCount = caio_dll.AioGetAiStopTriggerCount
AioGetAiStopTriggerCount.restype = ctypes.c_long
AioGetAiStopTriggerCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiRepeatCount(short Id, long * AiRepeatCount);
AioGetAiRepeatCount = caio_dll.AioGetAiRepeatCount
AioGetAiRepeatCount.restype = ctypes.c_long
AioGetAiRepeatCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiSamplingData(short Id, long * AiSamplingTimes, long * AiData);
AioGetAiSamplingData = caio_dll.AioGetAiSamplingData
AioGetAiSamplingData.restype = ctypes.c_long
AioGetAiSamplingData.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAiSamplingDataEx(short Id, long * AiSamplingTimes, float * AiData);
AioGetAiSamplingDataEx = caio_dll.AioGetAiSamplingDataEx
AioGetAiSamplingDataEx.restype = ctypes.c_long
AioGetAiSamplingDataEx.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioResetAiStatus(short Id);
AioResetAiStatus = caio_dll.AioResetAiStatus
AioResetAiStatus.restype = ctypes.c_long
AioResetAiStatus.argtypes = [ctypes.c_short]

# C Prototype: long AioResetAiMemory(short Id);
AioResetAiMemory = caio_dll.AioResetAiMemory
AioResetAiMemory.restype = ctypes.c_long
AioResetAiMemory.argtypes = [ctypes.c_short]


#----------------------------------------
# Analog output function
#----------------------------------------
# C Prototype: long AioSingleAo(short Id, short AoChannel, long AoData);
AioSingleAo = caio_dll.AioSingleAo
AioSingleAo.restype = ctypes.c_long
AioSingleAo.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long AioSingleAoEx(short Id, short AoChannel, float AoData);
AioSingleAoEx = caio_dll.AioSingleAoEx
AioSingleAoEx.restype = ctypes.c_long
AioSingleAoEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]

# C Prototype: long AioMultiAo(short Id, short AoChannels, long * AoData);
AioMultiAo = caio_dll.AioMultiAo
AioMultiAo.restype = ctypes.c_long
AioMultiAo.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioMultiAoEx(short Id, short AoChannels, float * AoData);
AioMultiAoEx = caio_dll.AioMultiAoEx
AioMultiAoEx.restype = ctypes.c_long
AioMultiAoEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioGetAoResolution(short Id, short * AoResolution);
AioGetAoResolution = caio_dll.AioGetAoResolution
AioGetAoResolution.restype = ctypes.c_long
AioGetAoResolution.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoChannels(short Id, short AoChannels);
AioSetAoChannels = caio_dll.AioSetAoChannels
AioSetAoChannels.restype = ctypes.c_long
AioSetAoChannels.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoChannels(short Id, short * AoChannels);
AioGetAoChannels = caio_dll.AioGetAoChannels
AioGetAoChannels.restype = ctypes.c_long
AioGetAoChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioGetAoMaxChannels(short Id, short * AoMaxChannels);
AioGetAoMaxChannels = caio_dll.AioGetAoMaxChannels
AioGetAoMaxChannels.restype = ctypes.c_long
AioGetAoMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoRange(short Id, short AoChannel, short AoRange);
AioSetAoRange = caio_dll.AioSetAoRange
AioSetAoRange.restype = ctypes.c_long
AioSetAoRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioSetAoRangeAll(short Id, short AoRange);
AioSetAoRangeAll = caio_dll.AioSetAoRangeAll
AioSetAoRangeAll.restype = ctypes.c_long
AioSetAoRangeAll.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoRange(short Id, short AoChannel, short * AoRange);
AioGetAoRange = caio_dll.AioGetAoRange
AioGetAoRange.restype = ctypes.c_long
AioGetAoRange.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoMemoryType(short Id, short AoMemoryType);
AioSetAoMemoryType = caio_dll.AioSetAoMemoryType
AioSetAoMemoryType.restype = ctypes.c_long
AioSetAoMemoryType.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoMemoryType(short Id, short * AoMemoryType);
AioGetAoMemoryType = caio_dll.AioGetAoMemoryType
AioGetAoMemoryType.restype = ctypes.c_long
AioGetAoMemoryType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoRepeatTimes(short Id, long AoRepeatTimes);
AioSetAoRepeatTimes = caio_dll.AioSetAoRepeatTimes
AioSetAoRepeatTimes.restype = ctypes.c_long
AioSetAoRepeatTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAoRepeatTimes(short Id, long * AoRepeatTimes);
AioGetAoRepeatTimes = caio_dll.AioGetAoRepeatTimes
AioGetAoRepeatTimes.restype = ctypes.c_long
AioGetAoRepeatTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAoClockType(short Id, short AoClockType);
AioSetAoClockType = caio_dll.AioSetAoClockType
AioSetAoClockType.restype = ctypes.c_long
AioSetAoClockType.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoClockType(short Id, short * AoClockType);
AioGetAoClockType = caio_dll.AioGetAoClockType
AioGetAoClockType.restype = ctypes.c_long
AioGetAoClockType.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoSamplingClock(short Id, float AoSamplingClock);
AioSetAoSamplingClock = caio_dll.AioSetAoSamplingClock
AioSetAoSamplingClock.restype = ctypes.c_long
AioSetAoSamplingClock.argtypes = [ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetAoSamplingClock(short Id, float * AoSamplingClock);
AioGetAoSamplingClock = caio_dll.AioGetAoSamplingClock
AioGetAoSamplingClock.restype = ctypes.c_long
AioGetAoSamplingClock.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioSetAoClockEdge(short Id, short AoClockEdge);
AioSetAoClockEdge = caio_dll.AioSetAoClockEdge
AioSetAoClockEdge.restype = ctypes.c_long
AioSetAoClockEdge.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoClockEdge(short Id, short * AoClockEdge);
AioGetAoClockEdge = caio_dll.AioGetAoClockEdge
AioGetAoClockEdge.restype = ctypes.c_long
AioGetAoClockEdge.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoSamplingData(short Id, long AoSamplingTimes, long * AoData);
AioSetAoSamplingData = caio_dll.AioSetAoSamplingData
AioSetAoSamplingData.restype = ctypes.c_long
AioSetAoSamplingData.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAoSamplingDataEx(short Id, long AoSamplingTimes, float * AoData);
AioSetAoSamplingDataEx = caio_dll.AioSetAoSamplingDataEx
AioSetAoSamplingDataEx.restype = ctypes.c_long
AioSetAoSamplingDataEx.argtypes = [ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioGetAoSamplingTimes(short Id, long * AoSamplingTimes);
AioGetAoSamplingTimes = caio_dll.AioGetAoSamplingTimes
AioGetAoSamplingTimes.restype = ctypes.c_long
AioGetAoSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioSetAoStartTrigger(short Id, short AoStartTrigger);
AioSetAoStartTrigger = caio_dll.AioSetAoStartTrigger
AioSetAoStartTrigger.restype = ctypes.c_long
AioSetAoStartTrigger.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoStartTrigger(short Id, short * AoStartTrigger);
AioGetAoStartTrigger = caio_dll.AioGetAoStartTrigger
AioGetAoStartTrigger.restype = ctypes.c_long
AioGetAoStartTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoStopTrigger(short Id, short AoStopTrigger);
AioSetAoStopTrigger = caio_dll.AioSetAoStopTrigger
AioSetAoStopTrigger.restype = ctypes.c_long
AioSetAoStopTrigger.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoStopTrigger(short Id, short * AoStopTrigger);
AioGetAoStopTrigger = caio_dll.AioGetAoStopTrigger
AioGetAoStopTrigger.restype = ctypes.c_long
AioGetAoStopTrigger.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetAoCallBackProc(short Id,
#                                               long (_stdcall *pProc)(short Id, short AiEvent, WPARAM wParam, LPARAM lParam, void *Param), long AoEvent, void *Param);
AioSetAoCallBackProc = caio_dll.AioSetAoCallBackProc
AioSetAoCallBackProc.restype = ctypes.c_long
AioSetAoCallBackProc.argtypes = [ctypes.c_short, PAIO_AO_CALLBACK, ctypes.c_long, ctypes.c_void_p]

# C Prototype: long AioSetAoEventSamplingTimes(short Id, long AoSamplingTimes);
AioSetAoEventSamplingTimes = caio_dll.AioSetAoEventSamplingTimes
AioSetAoEventSamplingTimes.restype = ctypes.c_long
AioSetAoEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetAoEventSamplingTimes(short Id, long * AoSamplingTimes);
AioGetAoEventSamplingTimes = caio_dll.AioGetAoEventSamplingTimes
AioGetAoEventSamplingTimes.restype = ctypes.c_long
AioGetAoEventSamplingTimes.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioStartAo(short Id);
AioStartAo = caio_dll.AioStartAo
AioStartAo.restype = ctypes.c_long
AioStartAo.argtypes = [ctypes.c_short]

# C Prototype: long AioStopAo(short Id);
AioStopAo = caio_dll.AioStopAo
AioStopAo.restype = ctypes.c_long
AioStopAo.argtypes = [ctypes.c_short]

# C Prototype: long AioEnableAo(short Id, short AoChannel);
AioEnableAo = caio_dll.AioEnableAo
AioEnableAo.restype = ctypes.c_long
AioEnableAo.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioDisableAo(short Id, short AoChannel);
AioDisableAo = caio_dll.AioDisableAo
AioDisableAo.restype = ctypes.c_long
AioDisableAo.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetAoStatus(short Id, long * AoStatus);
AioGetAoStatus = caio_dll.AioGetAoStatus
AioGetAoStatus.restype = ctypes.c_long
AioGetAoStatus.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAoSamplingCount(short Id, long * AoSamplingCount);
AioGetAoSamplingCount = caio_dll.AioGetAoSamplingCount
AioGetAoSamplingCount.restype = ctypes.c_long
AioGetAoSamplingCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetAoRepeatCount(short Id, long * AoRepeatCount);
AioGetAoRepeatCount = caio_dll.AioGetAoRepeatCount
AioGetAoRepeatCount.restype = ctypes.c_long
AioGetAoRepeatCount.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioResetAoStatus(short Id);
AioResetAoStatus = caio_dll.AioResetAoStatus
AioResetAoStatus.restype = ctypes.c_long
AioResetAoStatus.argtypes = [ctypes.c_short]

# C Prototype: long AioResetAoMemory(short Id);
AioResetAoMemory = caio_dll.AioResetAoMemory
AioResetAoMemory.restype = ctypes.c_long
AioResetAoMemory.argtypes = [ctypes.c_short]


#----------------------------------------
# Digital input and output function
#----------------------------------------
# C Prototype: long AioSetDiFilter(short Id, short Bit, float Value);
AioSetDiFilter = caio_dll.AioSetDiFilter
AioSetDiFilter.restype = ctypes.c_long
AioSetDiFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetDiFilter(short Id, short Bit, float *Value);
AioGetDiFilter = caio_dll.AioGetDiFilter
AioGetDiFilter.restype = ctypes.c_long
AioGetDiFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioInputDiBit(short Id, short DiBit, short * DiData);
AioInputDiBit = caio_dll.AioInputDiBit
AioInputDiBit.restype = ctypes.c_long
AioInputDiBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioOutputDoBit(short Id, short DoBit, short DoData);
AioOutputDoBit = caio_dll.AioOutputDoBit
AioOutputDoBit.restype = ctypes.c_long
AioOutputDoBit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioInputDiByte(short Id, short DiPort, short * DiData);
AioInputDiByte = caio_dll.AioInputDiByte
AioInputDiByte.restype = ctypes.c_long
AioInputDiByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioOutputDoByte(short Id, short DoPort, short DoData);
AioOutputDoByte = caio_dll.AioOutputDoByte
AioOutputDoByte.restype = ctypes.c_long
AioOutputDoByte.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]


#----------------------------------------
# Counter function
#----------------------------------------
# C Prototype: long AioGetCntMaxChannels(short Id, short * CntMaxChannels);
AioGetCntMaxChannels = caio_dll.AioGetCntMaxChannels
AioGetCntMaxChannels.restype = ctypes.c_long
AioGetCntMaxChannels.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetCntComparisonMode(short Id, short CntChannel, short CntMode);
AioSetCntComparisonMode = caio_dll.AioSetCntComparisonMode
AioSetCntComparisonMode.restype = ctypes.c_long
AioSetCntComparisonMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetCntComparisonMode(short Id, short CntChannel, short *CntMode);
AioGetCntComparisonMode = caio_dll.AioGetCntComparisonMode
AioGetCntComparisonMode.restype = ctypes.c_long
AioGetCntComparisonMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetCntPresetReg(short Id, short CntChannel, long PresetNumber, long *PresetData, short Flag);
AioSetCntPresetReg = caio_dll.AioSetCntPresetReg
AioSetCntPresetReg.restype = ctypes.c_long
AioSetCntPresetReg.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.c_short]

# C Prototype: long AioSetCntComparisonReg(short Id, short CntChannel, long ComparisonNumber, long *ComparisonData, short Flag);
AioSetCntComparisonReg = caio_dll.AioSetCntComparisonReg
AioSetCntComparisonReg.restype = ctypes.c_long
AioSetCntComparisonReg.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.c_short]

# C Prototype: long AioSetCntInputSignal(short Id, short CntChannel, short CntInputSignal);
AioSetCntInputSignal = caio_dll.AioSetCntInputSignal
AioSetCntInputSignal.restype = ctypes.c_long
AioSetCntInputSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetCntInputSignal(short Id, short CntChannel, short *CntInputSignal);
AioGetCntInputSignal = caio_dll.AioGetCntInputSignal
AioGetCntInputSignal.restype = ctypes.c_long
AioGetCntInputSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long AioSetCntCallBackProc(short Id, short CntChannel,
#                                               long (_stdcall *pProc)(short Id, short CntEvent, WPARAM wParam, LPARAM lParam, void *Param), long CntEvent, void *Param);
AioSetCntCallBackProc = caio_dll.AioSetCntCallBackProc
AioSetCntCallBackProc.restype = ctypes.c_long
AioSetCntCallBackProc.argtypes = [ctypes.c_short, ctypes.c_short, PAIO_CNT_CALLBACK, ctypes.c_long, ctypes.c_void_p]

# C Prototype: long AioSetCntFilter(short Id, short CntChannel, short Signal, float Value);
AioSetCntFilter = caio_dll.AioSetCntFilter
AioSetCntFilter.restype = ctypes.c_long
AioSetCntFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_float]

# C Prototype: long AioGetCntFilter(short Id, short CntChannel, short Signal, float *Value);
AioGetCntFilter = caio_dll.AioGetCntFilter
AioGetCntFilter.restype = ctypes.c_long
AioGetCntFilter.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_float)]

# C Prototype: long AioStartCnt(short Id, short CntChannel);
AioStartCnt = caio_dll.AioStartCnt
AioStartCnt.restype = ctypes.c_long
AioStartCnt.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioStopCnt(short Id, short CntChannel);
AioStopCnt = caio_dll.AioStopCnt
AioStopCnt.restype = ctypes.c_long
AioStopCnt.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long AioPresetCnt(short Id, short CntChannel, long PresetData);
AioPresetCnt = caio_dll.AioPresetCnt
AioPresetCnt.restype = ctypes.c_long
AioPresetCnt.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long AioGetCntStatus(short Id, short CntChannel, long *CntStatus);
AioGetCntStatus = caio_dll.AioGetCntStatus
AioGetCntStatus.restype = ctypes.c_long
AioGetCntStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioGetCntCount(short Id, short CntChannel, long *Count);
AioGetCntCount = caio_dll.AioGetCntCount
AioGetCntCount.restype = ctypes.c_long
AioGetCntCount.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long AioResetCntStatus(short Id, short CntChannel, long CntStatus);
AioResetCntStatus = caio_dll.AioResetCntStatus
AioResetCntStatus.restype = ctypes.c_long
AioResetCntStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]

#----------------------------------------
# Event Controller
#----------------------------------------
# C Prototype: long AioSetEcuSignal(short Id, short Destination, short Source);
AioSetEcuSignal = caio_dll.AioSetEcuSignal
AioSetEcuSignal.restype = ctypes.c_long
AioSetEcuSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long AioGetEcuSignal(short Id, short Destination, short *Source);
AioGetEcuSignal = caio_dll.AioGetEcuSignal
AioGetEcuSignal.restype = ctypes.c_long
AioGetEcuSignal.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]


