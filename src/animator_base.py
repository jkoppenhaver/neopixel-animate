from machine import Timer

class AnimatorBase:

    def __init__(self, np, period=10):
        self.np = np
        self.tim = Timer(-1)
        self.period = period

    def start(self):
        self.tim.init(mode=Timer.PERIODIC, period=self.period, callback=self.update)

    def stop(self, clear=True):
        self.tim.deinit()
        if(clear):
            self.np.fill(tuple([0] * self.np.bpp))
            self.np.write()

    def update(self, timer):
        # This method should be overridden by each animation.
        # This method will be called automatiacally at a defined interval to
        # allow each animation to do display updates.
        pass
