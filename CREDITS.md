# Credits: Tracy–Widom fluctuations for the row-centered conjugate kernel of a random network with polynomial activation

Who proved what this paper rests on, with the cite key, the result, and how the paper uses it.
Labels: known (cited, as published), adapted (cited, changed as stated), new.

| Key | People | Result | Use here |
|---|---|---|---|
| PW | Pennington, Worah | limiting spectrum of the conjugate kernel for Gaussian weights and data; it depends on σ through two constants | context in the introduction (known) |
| LLC | Louart, Liao, Couillet | deterministic equivalents for the resolvent of random-feature matrices | context (known) |
| BP21 | Benigni, Péché | the limiting spectrum for general entry distributions | context (known) |
| FW | Fan, Wang | spectra of conjugate and neural tangent kernels for networks of fixed depth | context (known) |
| BP22 | Benigni, Péché | the largest eigenvalue of the conjugate kernel converges in probability, with a phase transition | the first-order location of the edge; Theorem 1.1 gives its fluctuations (known) |
| WWF | Wang, Wu, Fan | how spiked structure in the input data passes through the layers to outlying eigenvalues and eigenvectors of the conjugate kernel | context for the outlier of the uncentered kernel (known) |
| BBP | Baik, Ben Arous, Péché | phase transition for the largest eigenvalue of a sample covariance matrix with one large population eigenvalue | the threshold in Corollary 1.2, below which the uncentered kernel K is covered (known) |
| EK10, FM | El Karoui; Fan, Montanari | the spectrum of inner-product kernel random matrices, and the operator norm of their higher-degree parts | the splitting (4.2) of the feature covariance Σ, which is such a matrix; Lemma 4.1 proves the bounds needed here with explicit constants (known) |
| TW, Johnstone, ElKaroui, BPZ, LS | Tracy, Widom; Johnstone; El Karoui; Bao, Pan, Zhou; Lee, Schnelli | Tracy–Widom law at the edge of sample covariance matrices with independent entries | the limit law and the edge scale (known) |
| FMPW | Fan, Ma, Paquette, Wang | the quadratic form bound for the random features model sigma(Xw) with deterministic X of bounded norm, weights with independent entries and polynomial activations (Proposition 2.17), and the anisotropic local law under it | the quadratic form bound for the rows of Y given the data; Proposition 3.1 is a short proof for Gaussian weights with an explicit constant (adapted) |
| MM | Ma, Misiakiewicz | the anisotropic local law for sample covariance matrices under quadratic-form concentration alone | context in the introduction (known) |
| CL | Chen, Lyu | edge universality and the Tracy–Widom law for sample covariance matrices whose sample vectors satisfy quadratic form concentration (Corollary 1.4) | applied conditionally on the data; the complex-A case of their Assumption 1.1(iii) follows from the real case with constant sqrt(2) C_p (adapted at the point of use) |
| MP, SC | Marchenko, Pastur; Silverstein, Choi | the Marchenko–Pastur law and its edge function | the edge E_0, the scale γ_0, and the edge displacement in Lemma 5.1 (known) |
| Nelson, Hariya | Nelson; Hariya | hypercontractivity of the Ornstein–Uhlenbeck semigroup, in the form of Hariya's equation (1.1) | Lemma 2.1, moments of Gaussian polynomials (known) |
| Chernoff | Chernoff | the Gaussian Poincaré inequality | Lemma 2.2 (known) |
| ODonnell | O'Donnell | correlation of Hermite polynomials of correlated Gaussians (Section 11.2) | the conditional covariance of the features (known) |
| Vershynin | Vershynin | covering numbers of the sphere (Corollary 4.2.13) | the net argument for the operator-norm bound on the event G_N (known) |

Adapted: the quadratic form bound for polynomial features (Proposition 3.1), due to Fan, Ma, Paquette and Wang, with a
short proof and an explicit constant for Gaussian weights.

New in this paper: the projected feature covariance T = vI + small terms, with bounded trace and Frobenius defects
(Lemmas 4.1 and 4.2); the O(N^-1) displacement of the right edge and of the Tracy–Widom scale (Lemma 5.1); the Tracy–Widom law
for the largest eigenvalue of the row-centered conjugate kernel K_P (Theorem 1.1); the same law for the kernel K
itself when its large covariance eigenvalue stays below the Baik–Ben Arous–Péché threshold (Corollary 1.2).

Codex (OpenAI, GPT-6.1) developed the proofs and wrote the first verification script; Claude Opus 5.5 (Anthropic)
checked the proofs and the hypotheses of the Chen–Lyu corollary, wrote the second script and wrote the paper. The
introduction and the AI declaration name the people above with these citations.
