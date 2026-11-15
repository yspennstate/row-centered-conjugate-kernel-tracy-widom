# Tracy–Widom fluctuations for the row-centered conjugate kernel of a random network with polynomial activation

Yitzchak Shmalo

Let Y = σ(WX/√d), where W is an m×d matrix with independent standard Gaussian entries, the N columns of X are
independent and uniform on the sphere of radius √d, and σ is a fixed polynomial with E σ(Z) = E[Z σ(Z)] = 0 for a
standard Gaussian Z. Let m, d, N grow proportionally with m ≠ N asymptotically, and let K_P = Y P Yᵀ / N, where P
removes the mean of each row of Y over the N data points. The largest eigenvalue of K_P has Tracy–Widom fluctuations
of order N^(-2/3) around v(1 + √(m/N))², where v = E σ(Z)². The same holds for the largest eigenvalue of YYᵀ/N
when a₂²N/d stays below v√(N/m), where a₂ is the second Hermite coefficient of σ (the Baik–Ben Arous–Péché
threshold for the one large eigenvalue of the feature covariance). The proof applies, conditionally on the data, the edge
universality theorem of Chen and Lyu for sample covariance matrices under quadratic form concentration. The
concentration bound for polynomial features follows from Gaussian Poincaré and hypercontractivity inequalities, with
constants independent of the dimension.

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_quadratic_forms.py`: exact rational-arithmetic checks of the Gaussian polynomial identities behind the
  quadratic form bound (Proposition 4.1) in dimension at most four and degree at most five.
- `code/check_constants.py`: exact checks of the spherical moments, the closed form and bound for μ₄, the
  Marchenko–Pastur edge constants and the change of normalization in Theorem 2.1.

- `code/edge_weight_side.py`: the weight-side edge E_W of Remark 7.1 for σ = h₂, in Tracy–Widom units, at the sizes
  quoted there (`python3 code/edge_weight_side.py 6`; needs NumPy).

The first two scripts use the Python standard library only; run them with `python3 code/<script>.py`. The proofs do
not depend on any of them. Credits for the results the paper rests on are in `CREDITS.md`.
