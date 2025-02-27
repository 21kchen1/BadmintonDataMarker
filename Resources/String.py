
"""
    与数据模型相关的字符串
"""
class DataType:
    ACCE = "ACCELEROMETER"
    ACCE_U = "ACCELEROMETER_UNCALIBRATED"
    AUDIO = "AUDIO"
    GYRO = "GYROSCOPE"
    GYRO_U = "GYROSCOPE_UNCALIBRATED"
    MAGN = "MAGNETIC_FIELD"
    MAGN_U = "MAGNETIC_FIELD_UNCALIBRATED"
    POSITION = "POSITION"
    ROTA = "ROTATION_VECTOR"
    VIDEO = "VIDEO"

"""
    与文件尾相关的字符串
"""
class FileEndName:
    CSV = ".csv"
    JSON = ".json"

"""
    与错误窗口相关的字符串
"""
class ErrorInfo:
    SELECT_FOLDER = "Folder Exception."
    DATALOAD_PATH = "Data Load Path Exception."
    DATALOAD = "Data Load Exception."
    STORAGE_FILE = "Storage File Exception."

"""
    与编码相关的字符串
"""
class Encoding:
    UTF8 = "utf-8"

"""
    与图表显示相关的字符串
"""
class Graph:
    X_LABEL = "Timestamp (ms)"
    Y_LABEL = "Value"

"""
    与按钮相关的字符串
"""
class Button:
    ACCE_RADIO = "AcceRadio"
    GYRO_RADIO = "GyroRadio"
    ROTATE_RADIO = "RotateRadio"

    X_CHECK = "XCheck"
    Y_CHECK = "YCheck"
    Z_CHECK = "ZCheck"