from animator_base import AnimatorBase

# This class can be used as a starting point for new animations

class BareMinimum(AnimatorBase):

    def __init__(self, np):
        # Add any initialization and variables you need here
        # You can also pass a different period to the Animator Base if you need to
        super().__init__(np)

    def update(self, timer):
        # This update function is called at regular intervals by the Animator Base
        self.np.write()
