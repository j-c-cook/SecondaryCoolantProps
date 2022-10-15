from typing import Tuple

from scp.base_melinder import BaseMelinder


class EthylAlcohol(BaseMelinder):
    """
    A derived fluid class for ethylene glycol and water mixtures
    """

    def coefficient_viscosity(self) -> Tuple:
        return (
            (1.4740e00, -4.7450e-02, 4.3140e-04, -3.0230e-06),
            (1.5650e-02, -4.1060e-05, -5.1350e-06, 7.0040e-08),
            (-8.4350e-04, 1.6400e-05, -1.0910e-07, -1.9670e-09),
            (7.5520e-06, -1.1180e-07, 1.8990e-09),
            (1.5290e-07, -9.4810e-10),
            (-4.1300e-09,),
        )

    def coefficient_specific_heat(self) -> Tuple:
        return (
            (4.2040e03, 2.3190e00, -3.0420e-02, 6.8600e-04),
            (-2.1020e01, 4.9270e-01, -3.0720e-03, -5.6900e-05),
            (-3.7140e-01, -2.3350e-03, -1.9600e-05, 7.4610e-07),
            (1.7430e-02, -2.9690e-04, 1.9010e-06),
            (-6.2920e-05, 5.3530e-06),
            (-8.2900e-06,),
        )

    def coefficient_conductivity(self) -> Tuple:
        return (
            (4.0670e-01, 6.7750e-04, 3.1050e-07, -2.0000e-08),
            (-5.0080e-03, -2.3770e-05, -3.2160e-08, 8.3620e-11),
            (2.8010e-05, 2.6690e-07, -3.6060e-09, 1.5520e-11),
            (-2.0090e-08, -6.8130e-09, 1.4290e-10),
            (-1.5060e-09, 1.1670e-10),
            (-1.6530e-11,),
        )

    def coefficient_density(self) -> Tuple:
        return (
            (9.6190e02, -5.2220e-01, -3.2810e-03, 1.5690e-05),
            (-1.4330e00, -1.9890e-02, 1.8700e-04, -9.1540e-07),
            (-2.2600e-02, 2.2810e-04, -8.5810e-08, 4.0560e-09),
            (-1.6900e-04, 8.5940e-06, -9.6070e-08),
            (1.2910e-05, -1.5900e-07),
            (-8.3180e-08,),
        )

    def __init__(self, x: float) -> None:
        """
        Constructor for an ethyl alcohol mixture instance

        @param x: Concentration fraction, from 0 to 0.6
        """

        super().__init__(0.0, 40, x, 0.0, 0.6)
        self.t_min = self.t_freeze = self.calc_freeze_point(x)

        self.x_base = 29.2361
        self.t_base = 8.1578

    def calc_freeze_point(self, x: float) -> float:
        """
        Calculate the freezing point temperature of the mixture

        Based on a curve fit of the Ethyl Alcohol freezing points
        Engineering Toolbox - https://www.engineeringtoolbox.com/ethanol-water-d_989.html

        @param x: Concentration fraction, from 0 to 0.6
        """

        # should return 0 C for low concentrations
        if x < 0.05:
            return 0

        # polynomial fit
        # t_f = a + b * conc + c * conc**2 + d * conc**3
        x = self._check_concentration(x)
        coefficient_freeze = [2.4685e00, -9.8592e-01, 1.6750e-02, -1.8251e-04]
        c_pow = [x**p for p in range(4)]
        return sum(i * j for i, j in zip(coefficient_freeze, c_pow))

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "EthylAlcohol"
        """
        return "EthylAlcohol"
