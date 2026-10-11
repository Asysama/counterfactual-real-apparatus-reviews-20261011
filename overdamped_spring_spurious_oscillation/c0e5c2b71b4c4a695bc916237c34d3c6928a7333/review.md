# PR 652 generator review

**Decision:** PASS
**Reviewed head:** `c0e5c2b71b4c4a695bc916237c34d3c6928a7333`
**Generator(s):** `overdamped_spring_spurious_oscillation`

**Generator correctness:** PASS

**Runtime-provenance policy scope:** NEW/REPLACEMENT

**Runtime provenance:** PASS

**Declared scaling target:** `100000 static recipes; 2 formally rendered representative cases`

**Smaller-target rationale:** `Not applicable`

**Declared-target scale readiness:** PASS

**Production readiness:** PRODUCTION READY

## Blocking findings

None in this reviewed version. These are contributor self-check results; Sara has not reviewed or approved them.

## Six-gate result

| Gate | Result | Evidence |
|---|---|---|
| Output contract | PASS | Both seeds: native 2048², 24fps,120 decoded frames,5s; [overdamped_spring_spurious_oscillation-independent.json](review-evidence/overdamped_spring_spurious_oscillation-independent.json) and per-case decoded-audit.json. |
| Violating-object-only mask | PASS | Strict native RGB 0/255; all-frame mask/red/off-mask equality plus depth-occlusion inspection. [Independent audit](review-evidence/overdamped_spring_spurious_oscillation-independent.json), [native crop index](review-evidence/native-temporal-inspection-manifest.json). |
| Real scaling | PASS | 100000 accepted static recipes,100000 effective signatures,all 5 buckets fully covered; 3 primary axes rendered low/high. [Scale audit](review-evidence/overdamped_spring_spurious_oscillation-scale.json), [rendered probes](review-evidence/overdamped_spring_spurious_oscillation-axis-probes/axis-probes.json). |
| Official unpatched environment | PASS | Official bpy 4.5.3 LTS; analytical state authority explicitly declared; successful exact-head clean runtime audit. [Witness](runtime-witness.json), [case mapping](runtime-witness-index.json). |
| Decoded matched control | PASS | All RGB frames before intervention equal exactly, with post-intervention visible divergence. [Independent all-frame audit](review-evidence/overdamped_spring_spurious_oscillation-independent.json). |
| Semantic consistency | PASS | Both True/CF prompts, source DESIGN and registered operator were checked against native and browser rendered outcomes; physical witnesses are listed below. |

## Production-quality behavioral baseline

| Check | Result | Evidence |
|---|---|---|
| True visibly completes the physically and logically correct prompt outcome | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Counterfactual visibly contains exactly one declared physical error | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| True prompt independently and exactly aligns with the True video | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Counterfactual prompt independently and exactly aligns with the Counterfactual video | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Setup is matched and no branch is swapped or mislabeled | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| No undeclared anomaly, accidental natural explanation, or unrelated visual defect | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Event completion, observation tail, and final visibility are sufficient for training use | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Emitted or propagated effects visibly originate at their named source and move continuously | NOT APPLICABLE |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Sources, actuators, and instruments are visually recognizable or explicitly and truthfully introduced | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Guides and incidental shadows are anchored, unambiguous, and do not resemble a second anomaly | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Applicable phenomenon-specific checks pass with task-appropriate evidence | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |

## Timebase and playback integrity

| Check | Result | Evidence |
|---|---|---|
| Source/simulation time per recorded frame and video FPS are recorded | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Outer steps per recorded frame are distinct from internal solver substeps | NOT APPLICABLE |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Physical/source seconds per video second is computed or explicitly not applicable | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Playback speed is intentional, visually plausible, pair-matched, and not a label shortcut | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Any timebase change was followed by fresh event, mask, completion, and decoded-video audit | NOT APPLICABLE |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |

## Optional simulator-profile result

NOT APPLICABLE: no simulator-native claim; analytical trajectories are authoritative and official Blender renders them (Eevee RGB for the helium chamber; Workbench for the other apparatus and all masks).

## Semantic matrix

| Title | README | True prompt | CF prompt | Scoring | Operator | Rendered behavior | Result |
|---|---|---|---|---|---|---|---|
| 过阻尼滑块却反复振荡 | generators/overdamped_spring_spurious_oscillation/README.md | metadata descriptions.true | metadata descriptions.counterfactual | decoded-audit.json + independent.json | registered trajectory operator | native and browser videos, both seeds | PASS |

## Verified passes

- All 4 native streams per case were independently decoded: 120 frames, strict mask, exact red/off-mask equality and exact pre-intervention pair equality.
- Consecutive native evidence frames, full scene geometry and actual browser playback/seek were inspected for both seeds.
- 100000 recipes passed static audit; 3 controlled primary physical/event axes were rendered; all 5 axes passed static coverage and final-spec wiring checks. This does not claim 100000 videos have been rendered.

## Successful-render runtime provenance

Use `HISTORICAL PARTIAL` only for unchanged artifacts already approved before the provenance
workflow was adopted. It is non-blocking and must not be used for new or replacement renders.

| Check | Result | Evidence |
|---|---|---|
| Every submitted case maps to one successful witness | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Witness binds exact commit, clean/declared source state, command/profile, and case/seed set | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Applicable interpreter, dependencies, simulator, renderer, encoder, OS, accelerator/driver, and container/image are recorded | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Delivered artifacts match witness SHA-256 inventory | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Reproduction recipe is present and not mislabeled as historical evidence | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Nested runtimes have component witnesses | NOT APPLICABLE |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |

## Client-facing artifact consistency

| Check | Result | Evidence |
|---|---|---|
| Binary mask shown as white foreground on black | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| QA overlays use one red convention across all cases | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Overlay highlight matches mask and excludes shadows/background | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Overlay files load, seek, and match the delivery media contract | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Actual target-browser playback has correct colors and no blank, green/magenta, or channel-swapped streams | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Browser mask is black/white and browser overlay matches CF outside red active-mask pixels | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Any normalized overlays are identified as review-only derivatives | NOT APPLICABLE |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |

## Scale-readiness result

| Check | Result | Evidence |
|---|---|---|
| CGC-v1 interface and profile space | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Physical axes and final-spec wiring | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Controlled one-axis probes produce intended geometry/trajectory/decoded changes | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Two formal cases are materially different across multiple relevant details | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| No dead, metadata-only, imperceptible, or rejection-collapsed axes | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Diversity is distributed across primary-axis buckets rather than dominated by one axis | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Nuisance variation is shared within each pair and does not leak the label | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Expanded prompts remain exact without exposing incidental scale/profile shortcuts | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Time mapping remains plausible and label-independent across scale profiles | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Declared target and audited seed count | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Deterministic profile/signature coverage | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Axis policy or justified narrow-phenomenon exception | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Disjoint sharding and accepted-case quota | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Manifest provenance and safe resume | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |
| Runtime and decoded fail-closed audits | PASS |Independent decoded audit + native temporal crops + actual browser receipt; see review-evidence and case metadata. |

## Commands and artifacts checked

- Clean exact PR HEAD; official bpy 4.5.3, Python/OS/encoder versions and hardware recorded in successful runtime-witness.json.
- Compile, physics/geometry tests, CLI, static population, native renders, official runtime audit/index, compatible resume and incompatible-quota rejection passed.
- https://asysama.github.io/counterfactual-real-apparatus-reviews-20261011/overdamped_spring_spurious_oscillation/c0e5c2b71b4c4a695bc916237c34d3c6928a7333/index.html; packet-manifest.json; seeds 42 and 98.

## Re-review requirements

- Any source/HEAD or render change requires fresh affected artifacts and a full applicable audit before a Sara application.

The automatic independent receipt deliberately retains its original browser/visual PENDING fields; completion is established by the separate actual-browser-playback.json and visual-inspection.json receipts.
Thermal time-lapse is explicitly 600x; all other generators use real-time matched branches. No solver substeps are claimed. Nested runtimes and simulator-native profiles are not applicable. Browser streams are lossy review derivatives; native RGB files define masks and exact pixel checks.

## Independently measured physics, by case

```json
[
  {
    "case_id": "overdamped_spring_spurious_oscillation_00000042",
    "physical_witnesses": {
      "critical_ratio": 1.3277777777777777,
      "cf_zero_crossing_frames": [
        38,
        52,
        65,
        79,
        93,
        107
      ],
      "true_final_displacement": 8.310218497188277e-05,
      "energy_never_grows": true,
      "release_pin_clearance_m": 0.01749999999999996,
      "evidence_frame": 39
    }
  },
  {
    "case_id": "overdamped_spring_spurious_oscillation_00000098",
    "physical_witnesses": {
      "critical_ratio": 1.5999999999999999,
      "cf_zero_crossing_frames": [
        42,
        56,
        69,
        83,
        97,
        111
      ],
      "true_final_displacement": 0.0006419820240302801,
      "energy_never_grows": true,
      "release_pin_clearance_m": 0.01749999999999996,
      "evidence_frame": 43
    }
  }
]
```

## Resolved batch-operation finding

Unused Blender data accumulated in the superseded apparatus head. Current committed cleanup retains all live geometry and purges unused mesh/curve/material/camera/light IDs. The official regression covers six real cases, both branches and event/final states; the separate independent construction receipt shows constant counts across three cases. See overdamped_spring_spurious_oscillation-bounded-resources.json (current PASS) and overdamped_spring_spurious_oscillation-superseded-resource-growth.json (historical FAIL) in review-evidence.
