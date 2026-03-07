# The Cosmic Pattern — Cosmology

*For observational and theoretical cosmologists: those who study dark energy, the CMB, large-scale structure, and the fate of the universe.*

---

## What This Framework Offers Cosmology

Three longstanding cosmological puzzles have no accepted theoretical explanation:

1. **Why is Ω_Λ ≈ 0.69?** (Why is dark energy roughly 69% of the universe?)
2. **The Hubble tension** — why does H₀ measured from CMB (~67 km/s/Mpc) differ from local measurements (~73)?
3. **The flatness and horizon problems** — why is the universe so homogeneous and geometrically flat?

This framework gives geometric answers to all three from a single scaffold.

---

## Dark Energy: Ω_Λ = 20/29

The projective plane PG(2,3) — the geometry of a 3-dimensional space over the field F₃ — contains exactly 29 geometric elements:

```
13 points  +  13 lines  +  3 directions at infinity  =  29 total
```

An observer **inside** the geometry can directly access only r² = 3² = **9 modes** (the inner winding cross-section of the torus T²(13,3)).

The remaining **20 modes** are "outside the cone" — present in the full geometry, but refracted away from the embedded observer by the 2.5D lens. These 20 modes are dark energy.

```
Ω_Λ = 20/29 ≈ 0.6897
```

Measured (Planck 2018): 0.6847 (Δ = +0.72%)

This is not a fit. The numbers 20 and 29 are determined entirely by D = 3 and the projective geometry of 3-dimensional space. Dark energy is not a mysterious substance — it is the geometry that doesn't fit through the observer's lens.

---

## Visible Matter + Dark Matter: 9/29

The 9 inside modes further divide:

- **Visible matter (baryons)** ≈ 3 modes → Ω_b ≈ 3/29 ≈ 0.103 (measured: 0.049 — this needs CT-3 refinement)
- **Dark matter** ≈ 6 modes → Ω_DM ≈ 6/29 ≈ 0.207 (measured: 0.265)

The exact assignment of the 9 inside modes to visible vs. dark matter is an open computation target (CT-3). The total matter fraction Ω_m ≈ 9/29 = 0.310, which compares favorably to the measured 0.315.

---

## The Hubble Tension: A Depth-Chart Artifact

The Hubble tension is not a sign of new physics. It is a depth-chart artifact.

The CMB probes the universe at high redshift — deep optical depth, d >> 1. Local distance-ladder measurements probe the universe at low redshift — near the observer surface, d ≈ 1.

In the framework, the Hubble parameter is:

```
H(d) = H₀ · L^w(d)
```

where w(d) is the optical depth of the measurement. Different depths give different apparent H₀ values. The expected tension for measurements at d~1 vs. d~1000 is of order CA = 2.7% — consistent with the observed 8% tension when propagated through the distance ladder chain.

No new dark energy equation of state. No new particles. Just the observer measuring the geometry from two different depths.

---

## The Big Bang: The Optical Focus

In conventional cosmology, the Big Bang is a singularity — a point of infinite density where general relativity breaks down.

In the framework, it is the **optical focus of the reverse lens**.

The observer stands on the 2.5D interface. The horizon is the back of the lens. Looking toward the Big Bang is looking in the direction of decreasing optical depth — toward the apex of the inside cone. At the apex (w = 0), you reach the top quark — the particle that sits at the exact interface between the observer and the full geometry.

There is no singularity. The "Big Bang" is where the inside-cone geometry closes: the point at which the 39-sector walk would complete its first circuit if run backward. It is a topological feature of the knot, not a catastrophe of physics.

---

## The Horizon Problem: Dissolved

Why is the CMB so uniform across regions that couldn't have been in causal contact?

The framework's answer: the CA-surface (the 2.5D interface) is itself a horizon. The Big Bang is a feature on this surface — the optical focus of the lens. Two points on opposite sides of the CMB sky are not causally disconnected; they are connected through the inside of the lens. Their uniformity is a consequence of both being on the same CA-surface, which is a single geometric object.

No inflation required.

---

## The Flatness Problem: The Lens Is Flat by Construction

The universe appears flat (Ω_total ≈ 1) to extraordinary precision. Why?

Because the embedding of the T²(13,3) knot in ℝ³ requires the observation surface to be flat. The 2.5D interface is the surface on which the observer is embedded — and by the projective duality of the construction, this surface is flat. The flatness of the universe is the flatness of the observer's lens. It is an identity, not a fine-tuning.

---

## The Observer Resolution Limit and the CMB

The CMB power spectrum has a finite angular resolution. Physics below a certain angular scale cannot be observed. In standard cosmology, this is attributed to Silk damping and instrumental limits.

The framework adds a deeper constraint:

```
ΔCA = CA = 1 − L ≈ 2.7063%
```

Structure at angular scales below CA of the total geometry refracts into the CA-noise floor of the observer surface. The CMB acoustic peaks cannot be resolved indefinitely as you go to smaller scales — not because the physics doesn't exist, but because the embedded observer cannot resolve below the interface thickness.

---

## Predictions That Can Be Checked Now

1. **Ω_Λ = 20/29 = 0.6897** — current measurement is 0.6847; a precision improvement in Euclid/DESI data should converge toward this value, not away from it.
2. **Ω_m ≈ 9/29 = 0.310** — measured 0.315; within CA.
3. **Hubble tension = depth-chart artifact** — the measured tension should scale with the depth difference between methods, proportional to CA = 2.7%.
4. **No evidence of dark energy equation of state evolution** — w(z) = −1 exactly, because dark energy is a mode count (topological), not a dynamical field.

---

## Run It

```bash
python3 demonstrations/cosmological_constants.py
```

Shows Ω_Λ, Ω_m, and the Hubble tension estimate from first principles.

---

## Timestamped Predictions (Filed 2026-03-06)

Five specific, falsifiable predictions are on record before the data arrives.
See [`PREDICTIONS.md`](../../PREDICTIONS.md) for the full derivations and
falsification conditions. The headline:

- DESI DR3: Ω_Λ = 20/29 = 0.6897; w = −1; no evolving dark energy at 5σ
- Euclid/Rubin: Ω_m = 9/29 = 0.3103; Hubble tension is a systematic
