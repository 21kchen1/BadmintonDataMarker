from Controller.DataLoadController import DataLoadController
from Controller.DataShowController import DataShowController
from Controller.DataTagController import DataTagController
from Service.DataLoad import DataLoad
from Service.DataSave import DataSave
from Service.DataShow import DataShow
from Service.DataTag import DataTag
from View.View import View
from Model.Data import (
    AcceDataList, AudioDataList, GyroDataList, GyroUDataList,
    MagnDataList, MagnUDataList, PositionDataList, RotaDataList, VideoDataList,
)
from Model.Note import Note
import logging

# 日志设置
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(funcName)s . %(message)s',
                    level=logging.INFO)

"""
    类型与模型实例的映射
"""
MODEL_DICT = {
    AcceDataList.AcceDataList.TYPE: AcceDataList.AcceDataList(),
    AudioDataList.AudioDataList.TYPE: AudioDataList.AudioDataList(),
    GyroDataList.GyroDataList.TYPE: GyroDataList.GyroDataList(),
    GyroUDataList.GyroUDataList.TYPE: GyroUDataList.GyroUDataList(),
    MagnDataList.MagnDataList.TYPE: MagnDataList.MagnDataList(),
    MagnUDataList.MagnUDataList.TYPE: MagnUDataList.MagnUDataList(),
    PositionDataList.PositionDataList.TYPE: PositionDataList.PositionDataList(),
    RotaDataList.RotaDataList.TYPE: RotaDataList.RotaDataList(),
    VideoDataList.VideoDataList.TYPE: VideoDataList.VideoDataList(),
}

"""
    数据 Note 信息
"""
DATA_NOTE = Note.Note()

"""
    保存的数据类型
"""
SAVEDATA_LIST = [
    AcceDataList.AcceDataList.TYPE,
    AudioDataList.AudioDataList.TYPE,
    GyroDataList.GyroDataList.TYPE,
    GyroUDataList.GyroUDataList.TYPE,
    MagnDataList.MagnDataList.TYPE,
    MagnUDataList.MagnUDataList.TYPE,
    RotaDataList.RotaDataList.TYPE,
]

def main() -> None:
    view = View(2200, 1200)

    # 数据载入服务
    dataLoader = DataLoad(MODEL_DICT, DATA_NOTE)
    # 数据显示服务
    dataShower = DataShow(MODEL_DICT)
    # 数据保存服务
    dataSaver = DataSave()
    # 数据标签服务
    dataTager = DataTag(MODEL_DICT, DATA_NOTE, SAVEDATA_LIST)

    # 数据载入控制器
    dataLoadController = DataLoadController(dataLoader, dataSaver, view)
    dataLoadController.setSlot()
    # 数据显示控制器
    dataShowController = DataShowController(dataShower, view)
    dataShowController.setSlot()
    # 数据标签控制器
    dataTagController = DataTagController(dataTager, dataSaver, view)
    dataTagController.setSlot()

    view.run()

if __name__ == "__main__":
    main()
