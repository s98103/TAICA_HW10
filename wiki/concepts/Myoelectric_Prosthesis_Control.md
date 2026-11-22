# Myoelectric Prosthesis Control (肌電義肢控制)

- **概念分類**: 生醫工程 / 人機介面 (Human-Machine Interface, HMI)
- **相關論文**: [[kumar2013_finger_flexions_semg]]
- **相關技術**: [[Volume_Conduction_Theory]], [[Wavelet_Maxima_Density]], [[Twin_SVM]]

---

## 1. 概念定義
肌電義肢控制（Myoelectric Prosthesis Control）是指透過採集截肢患者殘肢表面肌肉在收縮時產生的微弱生物電位（表面肌電訊號 sEMG），經過放大、前處理、特徵萃取與機器學習模式辨識，將患者的大腦運動意圖解碼為機器人關節馬達控制指令的閉環控制系統。

---

## 2. 工程與臨床實務的核心挑戰

### 2.1 延遲門檻與即時性 (Real-time Latency Constraints)
根據人體工學與神經生理反饋研究，肌電義肢系統的端到端延遲（訊號擷取 + 特徵運算 + 分類決策 + 馬達驅動）必須嚴格控制在 **$300\text{ ms}$** 以內。若延遲超過 $300\text{ ms}$，使用者會產生明顯的卡頓感與控制脫節，甚至引發動作不協調而導致義肢被放棄使用。

### 2.2 電極位移敏感度 (Electrode Displacement Problem)
多通道肌電陣列（16~32 通道）雖能提供較豐富的空間資訊，但極度依賴感測器的精準貼合位置。當截肢者穿脫義肢接受腔 (Prosthetic Socket)、流汗、或隨日常活動產生微小滑移（僅數毫米）時，訊號特徵分佈即會嚴重漂移，造成系統失靈。
- **解決方案**: 如 [[kumar2013_finger_flexions_semg]] 所示，改採單通道設計搭配物理體導電不變量特徵（如 [[Wavelet_Maxima_Density]]），能大幅提升對電極位移的容忍度。

### 2.3 截肢者肌肉萎縮與神經重塑 (Muscle Atrophy & Plasticity)
截肢患者的殘肢通常面臨：
- **肌肉廢用性萎縮 (Disuse Atrophy)**：肌纖維橫截面積縮小，運動單元動作電位振幅減弱。
- **解剖結構變異**：外科手術修整殘肢時，肌肉附著點被切除或重置，導致特定肌群的體導電傳導路徑改變。
- **臨床解法**：雙側動作訓練 (Bilateral Action Training) 與鏡像療法，透過健側手的協同動作喚醒患側大腦皮質運動區的神經元連結。
