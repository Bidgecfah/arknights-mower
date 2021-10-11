from .utils.adb import ADBConnector
from .utils.recognize import Recognizer
from .solvers import *


class Solver():

    def __init__(self, adb=None, recog=None):
        self.adb = adb if adb is not None else ADBConnector()
        self.recog = recog if recog is not None else Recognizer(self.adb)

    def base(self):
        BaseConstructSolver(self.adb, self.recog).run()

    def credit(self):
        CreditSolver(self.adb, self.recog).run()

    def mission(self):
        MissionSolver(self.adb, self.recog).run()

    def recruit(self, priority=None):
        """
        :param priority: list[str], 公招干员优先级，默认为火神和因陀罗
        """
        RecruitSolver(self.adb, self.recog).run(priority)

    def ope(self, times=-1, potion=0, originite=0, level=None, eliminate=False):
        """
        :param times: int, 作战的次数上限，-1 为无限制，默认为 -1
        :param potion: int, 使用药剂恢复体力的次数上限，-1 为无限制，默认为 0
        :param originite: int, 使用源石恢复体力的次数上限，-1 为无限制，默认为 0
        :param level: str, 指定关卡，默认为前往上一次作战
        :param eliminate: bool, 是否优先处理未完成的每周剿灭，默认为 False
        """
        OpeSolver(self.adb, self.recog).run(times, potion, originite, level, eliminate)

    def shop(self, priority=None):
        """
        :param priority: list[str], 使用信用点购买东西的优先级, 若无指定则默认购买第一件可购买的物品
        """
        ShopSolver(self.adb, self.recog).run(priority)
