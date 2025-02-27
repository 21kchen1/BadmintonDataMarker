
"""
    数据存储单元信息
    @author chen
"""

from Model.Note.Note import Note


class Info:
    """
        @param note 数据基本信息
        @param startTimestamp 开始时间戳
        @param endTimestamp 结束时间戳
    """
    def __init__(self, note: Note, startTimestamp: int, endTimestamp: int) -> None:
        self.recordName = note.recordName
        self.gender = note.gender
        self.exp = note.exp
        self.section = note.time
        self.device = note.other
        self.startTimestamp = startTimestamp
        self.endTimestamp = endTimestamp