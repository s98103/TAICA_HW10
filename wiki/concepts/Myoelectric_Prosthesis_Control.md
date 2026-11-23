# Myoelectric Prosthesis Control (肌電義肢控制)

- **概念分類**: 生醫工程 / 智慧仿生神經人機介面 (HMI)
- **相關論文**: [[kumar2013_finger_flexions_semg]], [[fukunaga2023_flexor_pronator_semg]], [[yao2020_forearm_muscles_antivibration]], [[yang2026_gesture_classification_semg_motion]], [[zhang2026_vibrotactile_neurorehabilitation_review]]
- **相關技術**: [[Volume_Conduction_Theory]], [[Wavelet_Maxima_Density]], [[Twin_SVM]], [[Sensory_Motor_Closed_Loop]]

---

## 1. 概念核心定義 (Core Definition)
**肌電義肢控制（Myoelectric Prosthesis Control）** 是指透過穿戴於截肢殘肢或肌肉表面的電極，採集肌肉收縮時產生的微弱生物電位（表面肌電訊號 sEMG），經前置放大、濾波、特徵萃取與模式辨識演算法，將大腦運動意圖解碼為假手關節電機控制指令的智慧人機工程系統。

---

## 2. 臨床應用的「四大死穴」 (The Four Fatal Flaws)
現代先進仿生機械手在實驗室基準集上辨識率常突破 95%，但進入臨床後棄用率高達 **30%~50%**，其根本原因在於四大工程障礙：
1. **電極位移致錯 (Electrode Displacement)**：患者穿脫接受腔 (Socket)、流汗或前臂晃動引發 1~2 mm 微小滑移，破壞空間幾何特徵分佈；
2. **多通道穿戴繁瑣 (Self-administration Barrier)**：傳統 16~32 通道電極陣列極難由患者在家中精準貼附；
3. **物理負載干擾 (External Load Shift)**：如 [[yao2020_forearm_muscles_antivibration]] 所揭示，提重物或穿手套使肌電基線產生 22%~78% 漂移；
4. **感覺反饋缺失 (Open-Loop Syndrome)**：如 [[zhang2026_vibrotactile_neurorehabilitation_review]] 所揭示，缺乏觸覺回饋導致嚴重視覺疲勞與肢體異物感。

---

## 3. 人因工學之 300 ms 即時延遲黃金門檻 (Latency Constraints)
根據臨床神經工程學研究，人腦發出動作意圖至假手機械做出反應的端到端延遲：

$$\tau_{\text{total}} = \tau_{\text{window}} + \tau_{\text{feature}} + \tau_{\text{ML}} + \tau_{\text{motor}} < 300\text{ ms}$$

| 延遲時間區間 | 使用者主觀心理感受 | 控制協調性與臨床後果 |
| :--- | :--- | :--- |
| **$\le 100\text{ ms}$** | 毫無察覺延遲 | 人機合一，如同操控自己的原生肉體 |
| **$100 - 200\text{ ms}$** | 可接受的極微延遲 | 控制流暢，大腦自發適應 |
| **$200 - 300\text{ ms}$** | 察覺微小遲滯 | 尚可操控，處於黃金極限門檻 |
| **$> 300\text{ ms}$** | 明顯動作延遲脫節 | **大腦反覆發出錯誤修正指令引發控制震盪，最終棄用！** |

*Kumar (2013) 實測 200 ms 滑動窗準確率未顯著下降，為後續藍牙傳輸與電機響應預留了充裕時間餘裕。*

---

## 4. 殘肢肌肉廢用性萎縮與解剖重塑 (Pathological Atrophy)
前臂截肢患者的生醫訊號環境與健全人存在巨大病理差異：
- **廢用性萎縮 (Disuse Atrophy)**：肌纖維橫截面積縮小，動作電位振幅下降 40%~60%，信噪比大幅惡化；
- **肌成形術幾何改變 (Myoplasty Remodeling)**：外科手術將屈伸肌腱縫合於殘端骨膜，改變了肌肉拉力方向與體導電幾何傳導；
- **解決方案**：結合雙側鏡像動作訓練 (Bilateral Action Training) 與微觀小波特徵，在萎縮殘肢上依然取得 81.87% 的高準確率。

---

## 5. 本知識庫 5 篇文獻之神經工程閉環架構
```text
[患者運動意圖] 
      │ (Kumar 2013: 單通道體導電 + WMD 抗位移解碼)
      ▼
[前臂深淺肌群] ◄─── (Fukunaga 2023: 揭示 FDS 與旋前肌選擇性神經招募)
      │ 
      │ (Yao 2020: 預防外力與手套負載引起的 48% 肌電基線漂移)
      ▼
[多模態感測融合] (Yang 2026: 6通道 sEMG + 柔性彎曲手套 >90% 解碼)
      │
      ▼
[智慧仿生手動作] 
      │ 
      │ (Zhang 2026: 握力傳感器 ➔ 微型 LRA 振動刺激殘肢皮膚)
      ▼
[感覺-動作閉環] ──► [大腦體感皮質 S1 喚醒 ➔ M1 皮質重塑 LTP]
```
