"""Exact checks of the explicit constants in the paper; standard library only.

1. The moments E rho^(2s) of the inner product of two independent uniform unit vectors in R^d,
   by a second route (Beta integral), and the closed form and bound for mu_4 = E (rho^2 - 1/d)^4.
2. The Marchenko-Pastur edge function f_0(u) = -1/u + r v/(1 + v u): f_0'(u_0) = 0, f_0(u_0) = E_0,
   f_0''(u_0) = 2 v^3 (1 + sqrt r)^4 / sqrt r and gamma_0^3 = 2 / f_0''(u_0), for r with rational square root.
3. The change of normalization from H_P = (N/m) K_P to the statement of the theorem.
"""

from fractions import Fraction as R
from math import comb


def moment_rho(d, s):
    """E rho^(2s), rho = u^T w, product formula (paper equation for the spherical moments)."""
    num = 1
    den = 1
    for i in range(s):
        num *= 2 * i + 1
        den *= d + 2 * i
    return R(num, den)


def moment_rho_beta(d, s):
    """Same moment from rho^2 ~ Beta(1/2, (d-1)/2): E X^s = prod_{i<s} (1/2 + i) / (d/2 + i)."""
    out = R(1)
    for i in range(s):
        out *= (R(1, 2) + i) / (R(d, 2) + i)
    return out


for d in range(2, 60):
    for s in range(0, 6):
        assert moment_rho(d, s) == moment_rho_beta(d, s)
    mu4 = sum(comb(4, j) * moment_rho(d, j) * R(-1, d) ** (4 - j) for j in range(5))
    closed = R(12 * (d - 1) * (5 * d * d - 13 * d + 12), d ** 4 * (d + 2) * (d + 4) * (d + 6))
    assert mu4 == closed, d
    assert mu4 <= R(60, d ** 4)
    c = 1 - R(1, d)
    tau = R(2, d * (d + 2))
    assert tau <= R(2, d * d) and c <= 1
for d in range(60, 5000, 7):
    closed = R(12 * (d - 1) * (5 * d * d - 13 * d + 12), d ** 4 * (d + 2) * (d + 4) * (d + 6))
    assert closed <= R(60, d ** 4)
print("spherical moments: two routes agree; mu_4 closed form and mu_4 <= 60/d^4 for 2 <= d < 5000")

# Edge of the Marchenko-Pastur law with population v I and ratio r = M/m.
for sr in (R(1, 3), R(1, 2), R(2, 3), R(3, 2), R(2), R(5, 2)):
    r = sr * sr
    for v in (R(1), R(2, 5), R(7, 3)):
        u0 = -1 / (v * (1 + sr))
        f0 = -1 / u0 + r * v / (1 + v * u0)
        f1 = 1 / u0 ** 2 - r * v * v / (1 + v * u0) ** 2
        f2 = -2 / u0 ** 3 + 2 * r * v ** 3 / (1 + v * u0) ** 3
        f3 = 6 / u0 ** 4 - 6 * r * v ** 4 / (1 + v * u0) ** 4
        assert f1 == 0
        assert f0 == v * (1 + sr) ** 2
        assert f2 == 2 * v ** 3 * (1 + sr) ** 4 / sr
        # gamma_0 = r^(1/6) / (v (1 + sqrt r)^(4/3)), so gamma_0^3 = sqrt(r) / (v^3 (1 + sqrt r)^4) = 2 / f2.
        assert sr / (v ** 3 * (1 + sr) ** 4) == 2 / f2
        assert 1 + v * u0 == sr / (1 + sr) and 1 + v * u0 > 0
        # gamma_0^(-1) equals Johnstone's scale (1 + sqrt r)(1 + 1/sqrt r)^(1/3) at v = 1: compare cubes.
        if v == 1:
            assert (1 + sr) ** 4 / sr == ((1 + sr) ** 3) * (1 + 1 / sr)
print("edge function: f0'(u0) = 0, f0(u0) = v(1+sqrt r)^2, f0''(u0) and gamma_0 as stated")

# Normalization: lambda(H_P) = (N/m) lambda(K_P), M = N - 1, r = M/m = c/b with c = M/N, b = m/N.
# Centre: (m/N) v (1 + sqrt(c/b))^2 = v (sqrt b + sqrt c)^2.
# Scale: gamma_0(r) m^(2/3) (N/m) = [c^(1/6) b^(1/6) / (v (sqrt b + sqrt c)^(4/3))] N^(2/3).
# Checked on cubes, with sb = sqrt b, sc = sqrt c rational, and m = b N.
for sb in (R(1, 2), R(3, 4), R(3, 2), R(2)):
    for sc in (R(9, 10), R(99, 100), R(1)):
        b, c = sb * sb, sc * sc
        for v in (R(1), R(3, 7)):
            r = c / b
            sr = sc / sb
            assert b * v * (1 + sr) ** 2 == v * (sb + sc) ** 2
            # cube of gamma_0(r) * (N/m) * m^(2/3) / N^(2/3) = gamma_0^3 / b
            lhs = (sr / (v ** 3 * (1 + sr) ** 4)) / b
            rhs = sc * sb / (v ** 3 * (sb + sc) ** 4)
            assert lhs == rhs
print("normalization: centre v(sqrt b + sqrt c)^2 and scale c^(1/6) b^(1/6) / (v (sqrt b + sqrt c)^(4/3)) confirmed")
print("PASS")
