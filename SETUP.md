# Setup (5 minutes)

1. Create a **public** repository named exactly `umerahmedbaig7` (same as your username). GitHub shows its README on your profile.
2. Upload everything in this folder (`README.md`, `assets/`, `scripts/`) to that repository, then commit to `main`.
3. Pin your 6 best repositories on your profile page: TriNav, Depth-Supervised-NeRF, procuraai-invoice-auditor, django-fuel-route-optimizer, Machine-Learning-in-Robotics, Robot-Perception.
4. Open the profile in a normal browser tab. The banner, console, pipelines and skill map animate on load (they are SVG with built-in animation, no external services).

## Editing

| What | Where |
|---|---|
| Any number in the banner, charts or skill map | `scripts/build_assets.py` (the `DATA` block, `GROUPS`, `REPOS`) then `python scripts/build_assets.py` |
| Text, links, project sections | `README.md` |
| NeRF comparison GIF | `assets/nerf-compare.gif` (built from `results/*.gif` in the Depth-Supervised-NeRF repo) |

Images in the project sections are loaded straight from your repositories, so they update when you update those repos. If you rename a repo or image, update the URL in `README.md`.

## Fix these in your repositories (they undermine the numbers shown here)

- **Depth-Supervised-NeRF README** reports a 20K-iteration table (19.91 / 22.32 dB). Your paper reports 50K iterations (20.21 / 22.36 dB). Align the repo with the paper or label the old table as an earlier run.
- **Robotics-and-Reinforcement-Learning**: the MountainCarContinuous PPO result is not "solved" (all evaluation episodes end with reward about 0 after 999 steps). Correct the README or retrain.
- **TriNav**: add the 12-scenario x 10-run benchmark script and logs; remove committed `__pycache__`; fix the README structure and clone URL.
- **Robot-Modeling-and-Identification**: the repo description mentions dynamics and identification, but the code covers kinematics and Jacobians only.
- **Machine-Learning-in-Robotics**: the README marks a 92.3% test accuracy as passing a 95% target.
