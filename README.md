<div align="center">

<img src="assets/banner.svg" width="100%" alt="Umer Ahmed Baig Mughal: Robotics and AI engineer. Animated banner of a robot following an A-star path among obstacles, with headline results: 96.6 percent navigation success, NeRF SSIM 0.658 to 0.778, crack mAP at 50 from 0.22 to 0.53, invoice audit F1 0.82.">

<br>

[![Portfolio](https://img.shields.io/badge/Portfolio-umerahmedbaig7.github.io-0B7285?style=for-the-badge&logo=googlechrome&logoColor=white)](https://umerahmedbaig7.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-umer--ahmed--baig7-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umer-ahmed-baig7)
[![GitHub](https://img.shields.io/badge/GitHub-umerahmedbaig7-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/umerahmedbaig7)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2683--8886-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-2683-8886)
[![Email](https://img.shields.io/badge/Email-umerahmedbaig98%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umerahmedbaig98@gmail.com)

**Robotics and AI Engineer**  ·  🌐 **[Full portfolio: umerahmedbaig7.github.io](https://umerahmedbaig7.github.io/)**

</div>

## About

I build robots and ML systems that **perceive, plan and act**, and I test them until I can state exactly where they work and where they don't. MSc in Robotics and AI at **ITMO University** (CGPA 4.82/5, Diploma with Honours), with an electronics background and three years in LED photometry and R&D labs before that.

My research covers autonomous navigation (published), depth-supervised 3D reconstruction (under review), and few-shot defect detection for robotic inspection (MSc thesis). On the engineering side I build document-AI and backend systems with tests, CI and honest evaluation.

More projects, photo galleries from the ROSATOM competitions and press are on my **[portfolio website](https://umerahmedbaig7.github.io/)**.

> **Open to:** PhD and research opportunities, research collaborations, and engineering roles in robotics, perception, robot learning and applied AI.

---

## Results at a glance

<div align="center">
<img src="assets/results-console.svg" width="100%" alt="Four charts. TriLayer-Nav navigation success: DWA only 71.6 percent, A-star plus DWA 76.6 percent, TriLayer-Nav 96.6 percent over 120 runs each. Depth-supervised NeRF on Lego: PSNR 20.21, 20.71, 21.17 and 22.36 dB for none, soft, hard and hybrid supervision. Few-shot crack detection: mAP at 50 rises from 0.22 at 5 shots to 0.53 at 30 shots, 0.61 with distillation. ProcuraAI invoice audit: precision 0.70, recall 0.98, F1 0.82 on OCR documents.">
</div>

<sub>Numbers come from my papers, thesis tables and stored evaluation files. Navigation results are simulation only. NeRF results are on the synthetic Lego scene (PSNR axis starts at 18 dB). Crack-detection results use a 30-image validation set. ProcuraAI is a prototype evaluated on synthetic data that I generated, so its structured-input score is optimistic and the OCR-document score is the honest one.</sub>

---

## Featured work

### 1 &nbsp;·&nbsp; TriLayer-Nav: A* + DWA + MPC navigation &nbsp;`Published`

A three-layer navigation stack for differential-drive robots: **A\*** plans a global path, the **Dynamic Window Approach** avoids obstacles in real time, **MPC** refines the commands under non-holonomic and actuator limits, and a **PID** loop drives the wheels. Validated in MuJoCo physics simulation. First author, *Gyroscopy and Navigation*, 2026.

<table>
<tr>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/TriNav-Tri-Layer-Navigation-A-DWA-MPC/main/assets/Enviroment%20mujoco.png" width="100%" alt="MuJoCo arena with a differential-drive robot among obstacles"></td>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/TriNav-Tri-Layer-Navigation-A-DWA-MPC/main/assets/WorkFlow.png" width="100%" alt="TriLayer-Nav workflow diagram"></td>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/TriNav-Tri-Layer-Navigation-A-DWA-MPC/main/assets/Result.png" width="100%" alt="One TriLayer-Nav run: trajectory against the global path, heading, velocities, control signals and DWA versus MPC commands"></td>
</tr>
<tr>
<td align="center"><sub>MuJoCo arena</sub></td>
<td align="center"><sub>Layered architecture</sub></td>
<td align="center"><sub>One analysed run: path, heading, DWA vs MPC commands</sub></td>
</tr>
</table>

- **Result:** 96.6% success (116 / 120 runs) vs 71.6% for DWA alone and 76.6% for A\*+DWA, over 12 scenarios x 10 runs per architecture; final position error ≤ 0.2 m.
- **Setup:** 12 kg differential-drive robot, 10 x 10 m arena with narrow corridors, 50 Hz control, MuJoCo 3.3.2.
- **Limits:** simulation only; hardware tests are future work.

[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/umerahmedbaig7/TriNav-Tri-Layer-Navigation-A-DWA-MPC) [![Paper](https://img.shields.io/badge/Paper-10.1134%2FS2075108726700094-0A7285?style=flat-square)](https://doi.org/10.1134/S2075108726700094)

---

### 2 &nbsp;·&nbsp; Depth-supervised NeRF &nbsp;`Under review`

Which way of using depth improves NeRF training most when architecture, data and budget are identical? I compared four strategies on one 8x256 MLP: **RGB-only**, **soft** depth regression, **hard** depth-guided sampling with free-space and surface penalties, and a **hybrid** of both. First and corresponding author; submitted to the *Journal of The Visual Computer*.

<div align="center">
<img src="assets/nerf-compare.gif" width="100%" alt="Four novel-view renderings of the Lego scene side by side: none, soft, hard and hybrid depth supervision">
<br><sub>Novel-view renders of the Lego scene from the four training strategies (repository experiments).</sub>
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/umerahmedbaig7/Depth-Supervised-NeRF/main/Analysis/Frame_0_output.png" width="100%" alt="Ground truth and renderings for none, soft, hard and hybrid with absolute-error maps and per-frame PSNR and SSIM">
<br><sub>Validation frame 0: renderings and error maps x4 with per-frame PSNR / SSIM.</sub>
</div>

| Lego, 100 held-out views | PSNR ↑ | SSIM ↑ | MSE ↓ (x10⁻³) | MAE ↓ (x10⁻²) |
|---|:--:|:--:|:--:|:--:|
| RGB only | 20.21 dB | 0.658 | 10.15 | 4.77 |
| Soft | 20.71 dB | 0.522 | 8.83 | 4.82 |
| Hard | 21.17 dB | 0.685 | 7.88 | 3.93 |
| **Hybrid** | **22.36 dB** | **0.778** | **5.98** | **3.18** |

- Hybrid is the **only** strategy that improves both PSNR and SSIM on both scenes (Chair: 19.48 → 21.62 dB, SSIM 0.701 → 0.838).
- It reaches within 0.5 dB of the baseline's best quality after **2,000 iterations** vs 16,000 (Lego) and 19,000 (Chair).
- I also report where depth hurts: soft supervision lowers SSIM on Lego, hard guidance lowers SSIM on Chair.
- **Limits (stated in the paper):** one run per strategy, photometric metrics only, no geometric error evaluation yet.

[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/umerahmedbaig7/Depth-Supervised-NeRF)

---

### 3 &nbsp;·&nbsp; MSc thesis: few-shot structural defect detection &nbsp;`Completed`

Detecting a **new defect class from a handful of labelled images**, motivated by robotic inspection of concrete and pavement. Evaluated offline on images; no robot deployment.

<div align="center">
<img src="assets/pipeline-thesis.svg" width="100%" alt="Thesis pipeline: base detector, few-shot adaptation, distillation, robustness suite, annotation audit">
</div>

- **Base detector:** YOLOv8n on four defect classes (1,120 training images) → **0.79 mAP@50** on 140 validation images.
- **Few-shot crack class:** mAP@50 rises from **0.22 (5 images) to 0.53 (30 images)**; precision from 0.05 to 0.78, while recall on thin cracks stays the bottleneck.
- **Distillation** (T = 4, α = 0.7) lifts 30-shot validation mAP@50 to 0.61, but the gain is not consistent across shot counts.
- **Robustness:** 6 perturbations x 3 severities. At least **66% of baseline mAP** survives blur, fog, brightness and contrast shifts; large rotations are the failure mode.
- **Limits:** the crack validation set has 30 images. Thesis code is not public yet.

---

### 4 &nbsp;·&nbsp; ProcuraAI: AI invoice auditor &nbsp;`Prototype · synthetic data`

Three-way matching (purchase order ↔ delivery ↔ invoice) where **the LLM reads and explains but never decides**: money rules run in a deterministic Decimal engine, and every finding carries evidence and a confidence label.

<div align="center">
<img src="assets/pipeline-procuraai.svg" width="100%" alt="ProcuraAI pipeline: ingest, extract, match, evidence with RAG, audit, review and report">
</div>

<table>
<tr>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/procuraai-invoice-auditor/main/outputs/01_dashboard_summary.png" width="100%" alt="ProcuraAI dashboard summary with invoice counts, exposure and findings by type"></td>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/procuraai-invoice-auditor/main/outputs/02_rag_evidence_viewer.png" width="100%" alt="RAG evidence viewer showing retrieved contract and policy passages with citations"></td>
<td width="33%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/procuraai-invoice-auditor/main/outputs/08_rag_findings_human_review_queue.png" width="100%" alt="Human review queue of flagged invoices"></td>
</tr>
<tr>
<td align="center"><sub>Streamlit dashboard</sub></td>
<td align="center"><sub>RAG evidence with citations</sub></td>
<td align="center"><sub>Human-review queue</sub></td>
</tr>
</table>

- **Stack:** FastAPI + Streamlit, 4-agent **LangGraph** workflow, **FAISS + BM25** hybrid retrieval, Tesseract OCR with PyMuPDF, Pydantic, SQLAlchemy, Docker, GitHub Actions, about 5,700 lines of source and about 50 offline tests.
- **Results (72 synthetic invoices, 25 anomaly scenarios):** all 42 anomalous invoices flagged; on OCR'd documents precision **0.70**, recall **0.98**, F1 **0.82**; RAG Recall@3 = **1.00** over 70 queries.
- **Limits:** synthetic, template-based documents; not validated on real invoices; exposure totals from OCR are unreliable.

[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/umerahmedbaig7/procuraai-invoice-auditor)

---

### 5 &nbsp;·&nbsp; Hybrid ARIMAX–LSTM PM2.5 forecasting for robot-assisted monitoring &nbsp;`Co-author · under review`

<div align="center">
<img src="assets/pipeline-pm25.svg" width="100%" alt="Pipeline: data from 12 Beijing stations, preprocessing, ARIMAX, LSTM on residuals, monitoring policy">
</div>

ARIMAX captures the linear and seasonal structure; a two-layer LSTM trained on its residuals captures the rest. On 12 Beijing stations the hybrid reaches **MAE 11.20 µg/m³ and R² 0.949**, vs 26.62 / 0.765 for ARIMAX alone and 17.41 / 0.907 for LSTM alone. The forecast drives a four-state monitoring policy (patrol → emergency), evaluated by replaying historical data rather than on a physical robot. Manuscript under review at *Atmospheric Research*.

---

### 6 &nbsp;·&nbsp; Fuel Route Optimizer API &nbsp;`Completed`

A Django REST Framework service that plans a USA road trip and chooses the **cheapest fuel stops** for a 500-mile range at 10 mpg, with a live Leaflet / OpenStreetMap map.

<div align="center">
<img src="https://raw.githubusercontent.com/umerahmedbaig7/django-fuel-route-optimizer/main/output/route-map.png" width="100%" alt="Fuel route planner web interface: New York to Columbia, South Carolina, 710 miles, 2 fuel stops, total fuel cost 238 dollars, drawn on an OpenStreetMap route">
<br><sub>A real run: New York → Columbia, SC · 710.1 mi · 2 stops · $238.58 total fuel cost · $3.86 saved vs filling at the farthest station.</sub>
</div>

- **Engine:** dynamic programming over (station, fuel level) keeps every leg ≤ 500 miles including detours; one routing call per trip with caching and throttling.
- **Data:** 8,151 price rows cleaned to 6,626 US stations, placed offline by ZIP centroid (no per-row geocoding).
- **Quality:** 97 automated tests and CI.

[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/umerahmedbaig7/django-fuel-route-optimizer)

---

## More from my MSc coursework and side projects

<details>
<summary><b>Perception, estimation and learning (click to expand)</b></summary>

<br>

<table>
<tr>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Robot-Perception/main/Lab_4/results/Disparity_Map.png" width="100%" alt="Stereo disparity map computed with StereoSGBM"><br><sub><b>Stereo vision.</b> StereoSGBM disparity and depth from calibrated pairs. <a href="https://github.com/umerahmedbaig7/Robot-Perception">Robot-Perception</a></sub></td>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Robot-Perception/main/Lab_2/results/EKF_Angle_Tracking.png" width="100%" alt="Extended Kalman filter angle tracking against noisy measurements"><br><sub><b>State estimation.</b> EKF and UKF coded from the equations. <a href="https://github.com/umerahmedbaig7/Robot-Perception">Robot-Perception</a></sub></td>
</tr>
<tr>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Machine-Learning-in-Robotics/main/Lab_2/results/Prediction_Samples_Augmented.png" width="100%" alt="SegNet road-sign segmentation predictions with per-sample IoU"><br><sub><b>Segmentation.</b> SegNet on road signs, augmentation lifts test IoU 0.619 → 0.669 (README-reported). <a href="https://github.com/umerahmedbaig7/Machine-Learning-in-Robotics">Machine-Learning-in-Robotics</a></sub></td>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Machine-Learning-in-Robotics/main/Lab_3/results/tSNE_Clusters.png" width="100%" alt="t-SNE of autoencoder embeddings with KMeans clusters"><br><sub><b>Representation learning.</b> Convolutional autoencoder, t-SNE and KMeans clustering. <a href="https://github.com/umerahmedbaig7/Machine-Learning-in-Robotics">Machine-Learning-in-Robotics</a></sub></td>
</tr>
</table>

</details>

<details>
<summary><b>Planning, control and simulation (click to expand)</b></summary>

<br>

<table>
<tr>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Robot-Motion-Planning-and-Control/main/Lab_4/results/Position_Tracking_With_Payload.png" width="100%" alt="Six-joint position tracking of a Stanford arm under computed-torque control with a payload"><br><sub><b>Computed-torque control</b> of a 6-DOF Stanford arm (RK45), with a payload known to the model. <a href="https://github.com/umerahmedbaig7/Robot-Motion-Planning-and-Control">Robot-Motion-Planning-and-Control</a></sub></td>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Potential-Field-Path-Planning/main/results/3D_Field_With_Path.png" width="100%" alt="3D artificial potential field with obstacles and the planned path"><br><sub><b>Potential-field planner</b> from scratch: BFS distance transform, conical attraction, Khatib repulsion. <a href="https://github.com/umerahmedbaig7/Potential-Field-Path-Planning">Potential-Field-Path-Planning</a></sub></td>
</tr>
<tr>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Simulation-of-Robotic-Systems/main/Lab_1/results/stability_analysis.png" width="100%" alt="Stability comparison of forward Euler, backward Euler and Runge-Kutta on a damped oscillator"><br><sub><b>Numerical integration.</b> Forward Euler turns unstable above about 6 ms; RK4 and backward Euler stay stable. <a href="https://github.com/umerahmedbaig7/Simulation-of-Robotic-Systems">Simulation-of-Robotic-Systems</a></sub></td>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Robot-Modeling-and-Identification/main/Lab_3/Results/lab3_robot.png" width="100%" alt="6-DOF robotic arm configuration from forward kinematics"><br><sub><b>Manipulator kinematics.</b> DH forward kinematics, closed-form IK, symbolic Jacobian. <a href="https://github.com/umerahmedbaig7/Robot-Modeling-and-Identification">Robot-Modeling-and-Identification</a></sub></td>
</tr>
</table>

**Deep RL and physics-informed learning** ([Robotics-and-Reinforcement-Learning](https://github.com/umerahmedbaig7/Robotics-and-Reinforcement-Learning)): DQN, REINFORCE and PPO with GAE implemented from scratch; PPO stabilises Acrobot-v1 within 170 episodes; reverse-curriculum learning lifts sparse-reward MountainCar from 0% to 80–90% success; PINNs extrapolate an ODE from 50 noisy samples.

</details>

<details>
<summary><b>Optimisation and tabular ML (click to expand)</b></summary>

<br>

<table>
<tr>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/Metaheuristic-Optimization-Beale-Function/main/results/Beale_3D_Surface.png" width="100%" alt="3D surface of the Beale benchmark function"><br><sub><b>Metaheuristics.</b> Brute force, gradient descent, simulated annealing, genetic algorithm and Hooke–Jeeves on the Beale function. <a href="https://github.com/umerahmedbaig7/Metaheuristic-Optimization-Beale-Function">Beale repository</a></sub></td>
<td width="50%"><img src="https://raw.githubusercontent.com/umerahmedbaig7/freight-rate-prediction-using-LightGBM-regression/main/outputs/fig_cv_metrics.png" width="100%" alt="Rolling-origin cross-validation comparison of freight rate models by MAE and MAPE"><br><sub><b>Freight-rate forecasting.</b> LightGBM with rolling-origin validation: MAE about $45 vs $82 for the baseline on clean labels. <a href="https://github.com/umerahmedbaig7/freight-rate-prediction-using-LightGBM-regression">Freight repository</a></sub></td>
</tr>
</table>

</details>

---

## Skills, backed by code

Every dot below is a public repository with working code for that skill. No self-ratings.

<div align="center">
<img src="assets/skill-evidence-map.svg" width="100%" alt="Matrix of skills against repositories. Perception and learning: CNN and segmentation, NeRF, deep reinforcement learning, physics-informed learning, gradient boosting. Planning and control: A-star, DWA, potential fields, MPC and PID, computed-torque control, kinematics. Estimation and simulation: EKF and UKF, stereo vision, MuJoCo, numerical integration, metaheuristics. LLM and document AI: RAG, LangGraph, OCR. Software engineering: REST APIs, dynamic programming, tests and CI, scientific Python.">
</div>

**Languages and libraries:** Python · NumPy · SciPy · Matplotlib · pandas · SymPy · PyTorch · torchvision · scikit-learn · scikit-image · LightGBM · OpenCV

**Robotics:** MuJoCo · Gymnasium · Stable-Baselines3 · Robotics Toolbox for Python

**LLM and backend:** LangGraph · FAISS · BM25 · Pydantic · FastAPI · Django REST Framework · Streamlit · SQLAlchemy · Tesseract / PyMuPDF · Docker · GitHub Actions · pytest

**Earlier work (BEng thesis, 2020):** TensorFlow / Keras, Mask R-CNN, SSD, Arduino

---

## Publications

1. **U. A. B. Mughal**, A. Ali, Urwa, M. V. Abramchuk. *TriLayer-Nav: A Tri-Layer Navigation Framework Integrating A\*, Dynamic Window Approach, and Model Predictive Control for Differential-Drive Robots.* **Gyroscopy and Navigation**, 17(1), 24–33, 2026. [DOI 10.1134/S2075108726700094](https://doi.org/10.1134/S2075108726700094)
2. **U. A. B. Mughal**, A. Ali, Urwa, M. V. Abramchuk. *Depth-supervised NeRF for 3D scene reconstruction.* Submitted to the **Journal of The Visual Computer**, 2026 (under review).
3. Hybrid ARIMAX–LSTM framework for robot-assisted PM2.5 forecasting. Co-author. **Atmospheric Research**, 2026 (under review).
4. S. Memon, M. Ahmed, S. Narejo, **U. A. Baig**, B. S. Chowdhry, M. R. Anjum. *Self-Driving Car Using LiDAR Sensing and Image Processing.* **Int. J. Grid and Distributed Computing**, 13(2), 77–88, 2020. [DOI 10.33832/ijgdc.2020.13.2.06](https://doi.org/10.33832/ijgdc.2020.13.2.06) · [ResearchGate](https://www.researchgate.net/publication/350997511_SELF-DRIVING_CAR_USING_LIDAR_SENSING_AND_IMAGE_PROCESSING)

**MSc thesis:** *Development of a Few-Shot Learning Framework for Robust Structural Anomaly Detection with Robotic Inspection*, ITMO University, 2026.

---

## Education and recognition

**MSc Robotics and Artificial Intelligence**, ITMO University, Saint Petersburg · 2024–2026 · CGPA 4.82 / 5.0 · Diploma with Honours
**BEng Electronic Engineering**, Mehran University of Engineering and Technology · 2016–2019

- Open Doors International Olympiad 2024: prize-winner, Engineering & Technology (Master's track)
- ObninskTech Summer University 2025 (ROSATOM, MEPhI): 1st place, Engineering Hackathon · 1st place, Atomic Triathlon
- ObninskTech Winter School: 3rd place, Engineering Hackathon
- World Atomic Week 2025, Global HackAtom: participant representing ITMO University ([national stage results](https://hackatom.energy/en/novosti/national-stage-russia/))
- Press: [ITMO News interview, "A Master's student's perspective on robotics and AI"](https://news.itmo.ru/en/education/students/news/14899/)

---

## Get in touch

| | |
|---|---|
| 🌐 **Portfolio** | [umerahmedbaig7.github.io](https://umerahmedbaig7.github.io/) |
| 💼 **LinkedIn** | [linkedin.com/in/umer-ahmed-baig7](https://www.linkedin.com/in/umer-ahmed-baig7) |
| 💻 **GitHub** | [github.com/umerahmedbaig7](https://github.com/umerahmedbaig7) |
| 🎓 **ORCID** | [0000-0002-2683-8886](https://orcid.org/0000-0002-2683-8886) |
| ✉️ **Email** | [umerahmedbaig98@gmail.com](mailto:umerahmedbaig98@gmail.com) |
| 📍 **Location** | Hyderabad, Pakistan |

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-0B7285?style=for-the-badge&logo=googlechrome&logoColor=white)](https://umerahmedbaig7.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umer-ahmed-baig7)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/umerahmedbaig7)
[![ORCID](https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-2683-8886)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:umerahmedbaig98@gmail.com)

<sub>Robots that perceive, plan and act, with the evidence to back it up.</sub>

</div>
