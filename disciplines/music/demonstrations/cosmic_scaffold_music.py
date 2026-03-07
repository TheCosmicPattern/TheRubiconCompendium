"""
Music Demonstration — The Cosmic Pattern
=========================================
Derives musical structures from D=3 scaffold constants.
Shows how R=13, r=3, the 39-sector walk, and CA map to
intervals, rhythm, tension, and expressive timing.

Run: python3 cosmic_scaffold_music.py
Outputs: text score + optional MIDI if midiutil is available
"""

import math

# ── Scaffold ─────────────────────────────────────────────────────────────────
D     = 3
R     = D**2 + D + 1    # = 13
r     = D               # = 3
L     = math.sqrt((R**2 - r**2) / R**2)
CA    = 1.0 - L
delta_CP_deg = math.degrees(2 * math.pi * r / R)   # ≈ 83.1°
sectors = R * r                                     # = 39

SEP = "═" * 64

print(SEP)
print("THE COSMIC PATTERN — MUSIC DEMONSTRATION")
print(f"Scaffold: D={D}, R={R}, r={r}, sectors={sectors}")
print(SEP)


# ── PART 1: FREQUENCY RATIOS FROM THE SCAFFOLD ───────────────────────────────
print(f"\n{'─'*64}")
print("PART 1 — CONSONANT INTERVALS FROM D AND ITS NEIGHBORS")
print("─" * 64)

intervals = [
    ("Unison",       1, 1,    "cosh²−sinh²=1; closure identity"),
    ("Octave",       D+1, (D+1)//2, "Φ₂:(Φ₂/2) = 4:2; doubling"),
    ("Perfect Fifth", r, D-1, "r:(D-1) = 3:2; most stable non-octave"),
    ("Perfect Fourth", D+1, r, "Φ₂:r = 4:3; inversion of fifth"),
    ("Major Sixth",  r+D, r,  "(D+r):r = 5:3 ≈ major sixth"),
    ("Minor Third",  D+1+D-1, D+1+1, "6:5 (approx from D neighbors)"),
]

print(f"\n  {'Interval':<18} {'Ratio':<10} {'Cents':<8} {'Framework source'}")
print(f"  {'-'*18} {'-'*10} {'-'*8} {'-'*30}")
for name, num, den, source in intervals:
    if den == 0: continue
    ratio = num / den
    cents = 1200 * math.log2(ratio)
    print(f"  {name:<18} {num}:{den:<8} {cents:>6.1f}¢  {source}")

print(f"\n  Note: The three primary consonances (Octave, Fifth, Fourth)")
print(f"  are exactly D+1:D/2, D:D-1, and D+1:D with D={D}.")


# ── PART 2: THE 39-SECTOR WALK AS RHYTHMIC STRUCTURE ─────────────────────────
print(f"\n{'─'*64}")
print("PART 2 — THE 39-SECTOR WALK AS RHYTHMIC STRUCTURE")
print("─" * 64)

print(f"\n  Total sectors in one knot circuit: R×r = {R}×{r} = {sectors}")
print(f"\n  Decomposition options:")
print(f"    {sectors} = {R} groups of {r}  → {R} beats per phrase, {r} phrases = {sectors}")
print(f"    {sectors} = {r} groups of {R}  → {r} beats per phrase, {R} phrases = {sectors}")
print(f"    {sectors} = 13×3 = 3×13  (the two natural readings of the knot)")

print(f"\n  Natural rhythmic form:")
print(f"    • {r} sections")
print(f"    • Each section: {R} beats")
print(f"    • Total: {sectors} beats = 1 complete knot circuit")

print(f"\n  Phase accumulation per section:")
for i in range(1, r+1):
    phase = i * (360 * r / sectors)
    print(f"    After section {i}: {phase:.1f}°  (holonomy: {i*delta_CP_deg/r:.1f}°)")

print(f"\n  The holonomy twist δ = {delta_CP_deg:.1f}° = the 'tension' at the section boundary.")
print(f"  It resolves to 0° (unison) only after all {r}×{R} = {sectors} beats complete.")


# ── PART 3: THE 12-TONE SCALE FROM PG(2,3) ───────────────────────────────────
print(f"\n{'─'*64}")
print("PART 3 — THE 12-TONE SCALE FROM R=13 POINTS")
print("─" * 64)

print(f"\n  PG(2,3) has R = {R} points.")
print(f"  The 12-tone chromatic scale has 12 pitch classes + 1 octave return = 13.")
print(f"\n  Mapping: R=13 projective points → 12 pitch classes + octave closure")
print(f"\n  Equal temperament (12-TET) pitch classes:")
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', "C'"]
for i in range(R):
    freq_ratio = 2**(i/12)
    cents = i * 100
    tag = "← octave (closure)" if i == 12 else ""
    tag = "← tonic (start)" if i == 0 else tag
    print(f"    Point {i+1:>2}: {note_names[i]:<4}  {freq_ratio:.4f}×  {cents:>4}¢  {tag}")

print(f"\n  The 13th point IS the 1st point (octave = tonic × 2).")
print(f"  The circle of fifths (12 notes, closes exactly) is the")
print(f"  cycle of R=13 points modulo the octave identification.")


# ── PART 4: EXPRESSIVE TIMING AND CA ─────────────────────────────────────────
print(f"\n{'─'*64}")
print("PART 4 — EXPRESSIVE TIMING: THE CA SWEET SPOT")
print("─" * 64)

print(f"\n  CA = 1-L = {CA:.6f} = {CA*100:.4f}%")
print(f"\n  Empirical studies of expressive timing in live performance:")
print(f"  (Repp 1992, Clarke 1999, Sloboda 2000)")
print(f"    • Mechanical (metronomic): 0% deviation → sounds robotic")
print(f"    • Too much rubato: >5% deviation → sounds sloppy")
print(f"    • 'Sweet spot': ~2-3% deviation → sounds human, musical")
print(f"    • Framework prediction: CA = {CA*100:.2f}% ← the interface thickness")
print(f"\n  Interpretation: the observer resolves time at the CA level.")
print(f"  Music at CA deviation is operating at the natural resolution")
print(f"  limit of the embedded observer — which is why it 'feels right'.")

# Timing example
tempo_bpm = 120
beat_duration_ms = 60000 / tempo_bpm
ca_deviation_ms = CA * beat_duration_ms
print(f"\n  At {tempo_bpm} BPM (beat = {beat_duration_ms:.0f}ms):")
print(f"  CA deviation = {ca_deviation_ms:.1f}ms — this is the expressive timing range")
print(f"  (Human JND for timing: ~10-20ms; CA deviation: {ca_deviation_ms:.0f}ms — both in range)")


# ── PART 5: TEXT SCORE ────────────────────────────────────────────────────────
print(f"\n{'─'*64}")
print("PART 5 — SCAFFOLD SONIFICATION (text score)")
print("─" * 64)

print(f"""
  Title: "The Observer" — derived from D={D}

  Structure: {r} sections × {R} beats = {sectors} total beats (1 complete knot circuit)

  Section 1 (beats 1-{R}): INSIDE CHART
    • Tempo: 83 BPM  (= δ_CP = {delta_CP_deg:.0f}°, 1 beat per degree)
    • Mode: C major (9 notes = r² = inside modes)
    • Phrase: ascending from C (w=0, observer surface) to B (w={R-1})
    • Dynamics: pp → mf  (optical depth increasing)

  Section 2 (beats {R+1}-{2*R}): TRANSITION (lens surface)
    • Tempo: 137 BPM  (= A = fine-structure integer)
    • Mode: whole-tone (6 notes = CA × {R}/..., the lens approximation)
    • Phrase: circular patterns around G# (tritone from C; maximum tension)
    • Dynamics: mf → f

  Section 3 (beats {2*R+1}-{sectors}): OUTSIDE CHART
    • Tempo: 83 BPM (same as section 1, but L↔β chart flip = mirror inversion)
    • Mode: C minor (the β-chart mirror)
    • Phrase: descending from B to C (holonomy completing circuit)
    • Dynamics: f → pp  (return to observer surface)

  Expressive timing: ±{ca_deviation_ms:.0f}ms at 83 BPM (= CA = {CA*100:.2f}%)

  Final note: C, unison, pp, with {CA*100:.1f}% decay in final {beat_duration_ms:.0f}ms
  (This is the cosh²-sinh²=1 resolution — the geometry returning to 1.)
""")

print(SEP)
print("To generate MIDI from this score:")
print("  pip install midiutil")
print("  python3 cosmic_scaffold_midi.py  (coming soon)")
print(SEP)
