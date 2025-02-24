from Controller.SelectFolderController import SelectFolderController
from Service.DataLoad import DataLoad
from Service.DataSave import DataSave
from View.View import View
from Model.Data import (
    AcceDataList, AudioDataList, GyroDataList, GyroUDataList,
    MagnDataList, MagnUDataList, PositionDataList, RotaDataList, VideoDataList,
)
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

def main() -> None:
    view = View(2200, 1200)

    # 数据载入服务
    dataLoader = DataLoad(MODEL_DICT)
    # 数据保存服务
    dataSaver = DataSave()

    selectFolderController = SelectFolderController(dataLoader, dataSaver, view)
    selectFolderController.setSlot()

    view.run()

if __name__ == "__main__":
    main()
