from .abs_factory import AbsFactory
from autos.gm.spark import ChevyVolt
from autos.gm.camaro import ChevyCamaro
from autos.gm.cadillac import CadillacCTS

class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevyVolt()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
