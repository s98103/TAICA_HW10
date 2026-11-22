# Wavelet Maxima Density (WMD, 小波極大值密度)

- **概念分類**: 訊號處理 / 特徵萃取演算法
- **相關論文**: [[kumar2013_finger_flexions_semg]]
- **相關技術**: [[Volume_Conduction_Theory]], [[Twin_SVM]]

---

## 1. 概念定義
小波極大值密度 (Wavelet Maxima Density, WMD) 是一種針對非平穩、微弱生醫電氣訊號（如手指微動作引發的低振幅表面肌電 sEMG）所設計的非線性時頻特徵萃取方法。

該方法結合了連續/離散小波轉換（Wavelet Transform）的多解析度奇異點偵測能力，以及生物組織 [[Volume_Conduction_Theory]] 的振幅分佈特性。它不依賴傳統全域訊號統計量（如 MAV, RMS），而是精確定位運動單元動作電位 (MUAP) 所引發的微觀奇異點，並量化其在不同時間窗內的發生頻率與振幅強度。

---

## 2. 演算法推導流程

### 2.1 小波轉換與奇異點識別 (Singularity Detection)
採用具備良好時頻局部化與對稱相位特性的雙正交小波（Bi-orthogonal Wavelet，如 `bior3.3`）對訊號 $f(x)$ 進行連續尺度分解。

在尺度 $s$ 下，小波係數局部極大值 (Local Maxima) 滿足：
$$W f(s, x_{n-1}) < W f(s, x_n) > W f(s, x_{n+1})$$
其中 $n$ 為時域採樣點索引。

### 2.2 跨尺度傳播濾除 (Interscale Maxima Tracking)
真實肌纖維去極化產生的 MUAP 奇異點在小波域中具備跨尺度穩定傳播的物理特徵：
- **有效奇異點 (Accepted Maxima)**：若某局部極大值能夠在所有尺度中持續出現，並且沿著尺度坐標從最細微尺度（Finest Scale）穩定傳播至最粗糙尺度（Coarsest Scale），則判定為肌肉收縮訊號。
- **雜訊瞬態剔除 (Noise Rejection)**：若極大值僅在單一或局部尺度孤立出現，則視為高頻隨機熱雜訊或運動偽影 (Motion Artifacts)，予以濾除。

### 2.3 特徵向量建構 (Feature Vector Construction)
以滑動時間窗（通常為 $200\text{ ms} \sim 300\text{ ms}$）分割訊號：
1. **峰值密度 ($D_{\text{peaks}}$)**：
   $$D_{\text{peaks}} = \frac{N_{\text{accepted}}}{T_{\text{window}}}$$
   反映運動單元被招募（Motor Unit Recruitment）的頻率與活化程度。
2. **平均振幅 ($\mu_{\text{mag}}$)**：
   $$\mu_{\text{mag}} = \frac{1}{N_{\text{accepted}}} \sum_{i=1}^{N_{\text{accepted}}} |W f(s_{\text{finest}}, x_i)|$$
   反映收縮肌肉與電極的空間幾何距離強度。

---

## 3. 技術優勢
1. **抗干擾能力高**: 傳統頻譜濾波對非平穩背景肌電雜訊無能為力，WMD 透過跨尺度驗證直接消除了無關雜訊。
2. **抗電極偏移強健性**: 當電極位置發生微小位移時，全域頻譜特徵通常劇烈改變，但 MUAP 的跨尺度奇異點特徵結構維持不變，僅有振幅平滑縮放，使分類器保持高準確率（在 [[kumar2013_finger_flexions_semg]] 中電極位移僅下降 1% 準確率）。
