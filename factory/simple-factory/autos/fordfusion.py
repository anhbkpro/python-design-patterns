from .abs_auto import AbsAuto

class FordFusion(AbsAuto):
    def start(self):
        print('Ford Fusion running with family power!')

    def stop(self):
        print('Ford Fusion shutting down.')
