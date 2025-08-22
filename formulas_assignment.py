class Formula:
    """Base class for formulas"""
    def calculate(self):
        raise NotImplementedError("Subclasses must implement this method")


# 1. Hydrostatic Pressure
class HydrostaticPressure(Formula):
    def __init__(self, mud_weight, tvd):
        self.mud_weight = mud_weight
        self.tvd = tvd

    def calculate(self):
        try:
            return 0.052 * self.mud_weight * self.tvd
        except Exception as e:
            return f"Error calculating Hydrostatic Pressure: {e}"


# 2. Gas Law (Boyle’s Law) with polymorphism
class BoyleLaw(Formula):
    def __init__(self, p1, v1, v2=None, p2=None):
        self.p1 = p1
        self.v1 = v1
        self.v2 = v2
        self.p2 = p2

    def calculate(self):
        try:
            if self.v2 is not None:  # Solve for P2
                return (self.p1 * self.v1) / self.v2
            elif self.p2 is not None:  # Solve for V2
                return (self.p1 * self.v1) / self.p2
            else:
                raise ValueError("Provide either V2 or P2 to calculate.")
        except Exception as e:
            return f"Error calculating Boyle’s Law: {e}"


# 3. Darcy’s Law
class DarcyLaw(Formula):
    def __init__(self, k, A, deltaP, mu, L):
        self.k = k
        self.A = A
        self.deltaP = deltaP
        self.mu = mu
        self.L = L

    def calculate(self):
        try:
            return (self.k * self.A * self.deltaP) / (self.mu * self.L)
        except Exception as e:
            return f"Error calculating Darcy’s Law: {e}"


# 4. Formation Volume Factor
class FormationVolumeFactor(Formula):
    def __init__(self, Vo, Vres):
        self.Vo = Vo
        self.Vres = Vres

    def calculate(self):
        try:
            if self.Vres == 0:
                raise ZeroDivisionError("Reservoir volume cannot be zero.")
            return self.Vo / self.Vres
        except Exception as e:
            return f"Error calculating Formation Volume Factor: {e}"


# 5. Drilling Hydraulic Horsepower
class HydraulicHorsepower(Formula):
    def __init__(self, deltaP, Q):
        self.deltaP = deltaP
        self.Q = Q

    def calculate(self):
        try:
            return (self.deltaP * self.Q) / 1714
        except Exception as e:
            return f"Error calculating Hydraulic Horsepower: {e}"


# 6. Reynolds Number
class ReynoldsNumber(Formula):
    def __init__(self, rho, v, D, mu):
        self.rho = rho
        self.v = v
        self.D = D
        self.mu = mu

    def calculate(self):
        try:
            return (self.rho * self.v * self.D) / self.mu
        except Exception as e:
            return f"Error calculating Reynolds Number: {e}"


# Polymorphism Example
def compute_formula(formula_obj):
    print(f"Result: {formula_obj.calculate()}")


# Example usage
if __name__ == "__main__":
    f1 = HydrostaticPressure(12, 10000)   # MW=12 ppg, TVD=10,000 ft
    f2 = BoyleLaw(3000, 2, v2=1.5)        # P1=3000 psi, V1=2 ft³, V2=1.5 ft³
    f3 = DarcyLaw(100, 50, 200, 1.1, 10)  # Arbitrary values
    f4 = FormationVolumeFactor(1.5, 1.0)  
    f5 = HydraulicHorsepower(300, 500)    # ΔP=300 psi, Q=500 gpm
    f6 = ReynoldsNumber(1000, 2, 0.1, 0.001)

    formulas = [f1, f2, f3, f4, f5, f6]

    for f in formulas:
        compute_formula(f)
