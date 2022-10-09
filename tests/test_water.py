from unittest import TestCase

from scp.water import Water


class TestWater(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.p = Water()

    def test_viscosity(self):
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(1.0), 1.731e-03, delta=1.731e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(5.0), 1.518e-03, delta=1.518e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(10.0), 1.306e-03, delta=1.306e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(25.0), 8.900e-04, delta=8.900e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(50.0), 5.465e-04, delta=5.465e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(75.0), 3.774e-04, delta=3.774e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(90.0), 3.142e-04, delta=3.142e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(95.0), 2.971e-04, delta=2.971e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(99.0), 2.846e-04, delta=2.846e-06)

    def test_specific_heat(self):
        # PropsSI('C', 'P', 101325, 'T', 273.15 + 1, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(1.0), 4.216e+03, delta=4.216e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 5, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(5.0), 4.205e+03, delta=4.205e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 10, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(10.0), 4.195e+03, delta=4.195e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 25, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(25.0), 4.181e+03, delta=4.181e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 50, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(50.0), 4.181e+03, delta=4.181e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 75, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(75.0), 4.193e+03, delta=4.193e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 90, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(90.0), 4.205e+03, delta=4.205e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 95, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(95.0), 4.210e+03, delta=4.210e+01)

        # PropsSI('C', 'P', 101325, 'T', 273.15 + 99, 'WATER')
        self.assertAlmostEqual(self.p.specific_heat(99.0), 4.215e+03, delta=4.215e+01)

    def test_density(self):
        # PropsSI('D', 'P', 101325, 'T', 273.15 + 1, 'WATER')
        self.assertAlmostEqual(self.p.density(1.0), 9.999e+02, delta=9.999e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 5, 'WATER')
        self.assertAlmostEqual(self.p.density(5.0), 1.000e+03, delta=1.000e+01)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 10, 'WATER')
        self.assertAlmostEqual(self.p.density(10.0), 9.997e+02, delta=9.997e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 25, 'WATER')
        self.assertAlmostEqual(self.p.density(25.0), 9.970e+02, delta=9.970e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 50, 'WATER')
        self.assertAlmostEqual(self.p.density(50.0), 9.880e+02, delta=9.880e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 75, 'WATER')
        self.assertAlmostEqual(self.p.density(75.0), 9.748e+02, delta=9.748e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 90, 'WATER')
        self.assertAlmostEqual(self.p.density(90.0), 9.653e+02, delta=9.653e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 95, 'WATER')
        self.assertAlmostEqual(self.p.density(95.0), 9.619e+02, delta=9.619e+00)

        # PropsSI('D', 'P', 101325, 'T', 273.15 + 99, 'WATER')
        self.assertAlmostEqual(self.p.density(99.0), 9.591e+02, delta=9.591e+00)

    def test_conductivity(self):
        # PropsSI('L', 'P', 101325, 'T', 273.15 + 1, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(1.0), 5.582e-01, delta=5.582e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 5, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(5.0), 5.678e-01, delta=5.678e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 10, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(10.0), 5.788e-01, delta=5.788e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 25, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(25.0), 6.065e-01, delta=6.065e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 50, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(50.0), 6.406e-01, delta=6.406e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 75, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(75.0), 6.636e-01, delta=6.636e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 90, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(90.0), 6.728e-01, delta=6.728e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 95, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(95.0), 6.752e-01, delta=6.752e-03)

        # PropsSI('L', 'P', 101325, 'T', 273.15 + 99, 'WATER')
        self.assertAlmostEqual(self.p.conductivity(99.0), 6.768e-01, delta=6.768e-03)
