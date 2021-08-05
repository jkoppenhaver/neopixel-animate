from animator_base import AnimatorBase

# This class can be used as a starting point for new animations

class Chase(AnimatorBase):

    def __init__(self, np, color, width=1, period=0.1):
        # Add any initialization and variables you need here
        self.index = 0
        self.width = width
        self.n = np.n
        self.color = color
        self.off = tuple([0] * len(color))
        # You can also pass a different period to the Animator Base if you need to
        super().__init__(np, int(period*1000))

    def update(self, timer):
        # This update function is called at regular intervals by the Animator Base
        # Replace 'pass' with your pattern updates and np.write()
        self.np[self.index-self.width] = self.off
        self.np[self.index] = self.color
        if(self.index == self.n-1):
            self.index = 0
        else:
            self.index = self.index + 1
        self.np.write()
