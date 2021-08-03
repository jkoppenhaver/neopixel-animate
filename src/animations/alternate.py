from animator_base import AnimatorBase

# This class can be used as a starting point for new animations

class Alternate(AnimatorBase):

    def __init__(self, np, color, period=1):
        # Add any initialization and variables you need here
        self.current_state = 0
        self.n = np.n
        self.color = color
        self.off = tuple([0] * len(color))
        # You can also pass a different period to the Animator Base if you need to
        super().__init__(np, period*1000)

    def update(self, timer):
        # This update function is called at regular intervals by the Animator Base
        # Replace 'pass' with your pattern updates and np.write()
        for i in range(self.n):
            if(i % 2 == self.current_state):
                self.np[i] = self.color
            else:
                self.np[i] = self.off
        self.current_state = 0 if self.current_state else 1
        self.np.write()
