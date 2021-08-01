from animator_base import AnimatorBase

class Sine(AnimatorBase):
    sine_values = [0.5, 0.5313952597646567, 0.5626666167821521, 0.5936906572928623, 0.6243449435824274, 0.6545084971874737, 0.684062276342339, 0.7128896457825363, 0.7408768370508576, 0.7679133974894983, 0.7938926261462366, 0.8187119948743449, 0.8422735529643444, 0.8644843137107058, 0.8852566213878946, 0.9045084971874737, 0.9221639627510075, 0.9381533400219318, 0.9524135262330098, 0.9648882429441257, 0.9755282581475768, 0.9842915805643155, 0.9911436253643443, 0.9960573506572389, 0.9990133642141358, 1.0, 0.9990133642141358, 0.996057350657239, 0.9911436253643444, 0.9842915805643155, 0.9755282581475768, 0.9648882429441257, 0.9524135262330098, 0.9381533400219317, 0.9221639627510074, 0.9045084971874737, 0.8852566213878946, 0.8644843137107057, 0.8422735529643444, 0.8187119948743449, 0.7938926261462367, 0.7679133974894985, 0.7408768370508576, 0.7128896457825364, 0.6840622763423391, 0.6545084971874737, 0.6243449435824276, 0.5936906572928623, 0.5626666167821522, 0.5313952597646567, 0.5000000000000001, 0.4686047402353433, 0.43733338321784787, 0.4063093427071376, 0.3756550564175727, 0.3454915028125264, 0.31593772365766104, 0.2871103542174639, 0.2591231629491423, 0.23208660251050178, 0.20610737385376365, 0.18128800512565518, 0.1577264470356558, 0.13551568628929422, 0.11474337861210532, 0.09549150281252633, 0.07783603724899235, 0.06184665997806821, 0.0475864737669901, 0.03511175705587427, 0.024471741852423234, 0.015708419435684406, 0.00885637463565564, 0.0039426493427611176, 0.0009866357858642205, 0.0, 0.0009866357858642205, 0.003942649342761062, 0.00885637463565564, 0.015708419435684462, 0.02447174185242318, 0.035111757055874215, 0.047586473766990045, 0.06184665997806832, 0.07783603724899252, 0.09549150281252622, 0.1147433786121052, 0.13551568628929395, 0.15772644703565553, 0.18128800512565518, 0.20610737385376332, 0.23208660251050145, 0.25912316294914195, 0.2871103542174635, 0.31593772365766104, 0.34549150281252616, 0.37565505641757235, 0.40630934270713764, 0.43733338321784765, 0.4686047402353434]

    def __init__(self, np, color, period=5):
        self.color = color
        self.bpp = len(color)
        self.index = 0
        super().__init__(np, period=period*10)

    def update(self, timer):
        self.np.fill(tuple([round(x*self.sine_values[self.index]) for x in self.color]))
        self.np.write()
        if(self.index == 99):
            self.index = 0
        else:
            self.index = self.index + 1
