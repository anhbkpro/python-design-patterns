from autos.abs_auto import AbsAuto

class ChevyCamaro(AbsAuto):
    def start(self):
        print('Chevy Camaro running fast!')

    def stop(self):
        print('Chevy Camaro shutting down.')
