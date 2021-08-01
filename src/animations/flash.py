from animator_base import AnimatorBase

class Flash(AnimatorBase):
    period = 1000
    current_state = False

    def __init__(self, np, color):
        self.color = color
        super().__init__(np, period=1000)

    def update(self, timer):
        if(self.current_state):
            self.np.fill(tuple([0] * self.np.bpp))
        else:
            self.np.fill(self.color)
        self.np.write()
        self.current_state = not self.current_state
