# Sensory-Motor Closed-Loop (感覺-運動閉環控制)

- **概念分類**: 神經生物學 / 閉環神經復健與生醫人機工程
- **相關論文**: [[zhang2026_vibrotactile_neurorehabilitation_review]], [[kumar2013_finger_flexions_semg]], [[yang2026_gesture_classification_semg_motion]]
- **相關技術**: [[Myoelectric_Prosthesis_Control]], [[Multimodal_Sensor_Fusion]]

---

## 1. 概念核心定義 (Core Definition)
**感覺-運動閉環控制（Sensory-Motor Closed-Loop Control）** 是指在人機介面與神經復健系統中，將「大腦向外輸出運動指令（Motor Out）」與「外周環境向內反饋體感刺激（Sensory In）」在時間與空間上深度閉合的雙向神經控制範式。

傳統肌電義肢屬於純前饋的「開環控制」，使用者只能依靠眼睛看來調整抓握；而閉環系統透過**振動觸覺刺激（Vibrotactile Stimulation, VTS）**等技術，將假手的握力大小與滑動狀態即時編碼傳遞回人體皮膚感受器，喚醒大腦本體感覺。

---

## 2. 開環控制 vs. 閉環控制系統架構對比
```text
【傳統開環架構】 (視覺依賴、極易疲勞)
大腦皮質 ──(sEMG)──► 解碼演算法 ────► 機械假手抓握 
   ▲                                       │
   └─────────────── (眼睛視覺監視代償) ────┘

【智慧閉環架構】 (神經身心一體、自適應閉環)
大腦皮質 (M1) ──(sEMG)──► 解碼演算法 ──► 機械假手抓握 
   ▲                                       │ (抓握力道 / 微滑移)
   │                                       ▼
大腦體感 (S1) ◄───(皮膚神經傳入)─── 振動觸覺致動器 (LRA)
```

---

## 3. 皮質可塑性與長時程增強機理 (LTP-like Neuroplasticity)
當外周振動觸覺傳入刺激與大腦主動發出的運動意圖在毫秒級時間窗口內同步發生時，遵循 **Hebbian 突觸學習法則**：

$$\Delta w_{ij} = \eta \cdot a_i(\text{S1}) \cdot a_j(\text{M1})$$

1. **體感皮質 (S1) 活化**：振動刺激激活真皮乳頭層巴齊尼氏小體 (Pacinian) 與邁斯納氏小體 (Meissner)，脈衝經脊髓後索薄束/楔束投射至 S1；
2. **皮質內互惠投射**：S1 神經元透過皮質內水平聯絡纖維直接興奮相鄰初級運動皮質 (M1) 錐體神經元；
3. **腦電 ERD 調控**：引發對側感覺運動皮質區 $\mu$ (8–12 Hz) 與 $\beta$ (13–30 Hz) 頻帶事件相關去同步化 (ERD)，提高大腦興奮度；
4. **長時程增強 (LTP)**：突觸傳導效率產生結構性持續增強，加速中風受損神經通路的側支發芽與運動功能重塑！

---

## 4. 臨床療效實證 (PRISMA 35 項文獻薈萃)
根據 [[zhang2026_vibrotactile_neurorehabilitation_review]] 系統性綜述之實證數據：
- **上肢運動總分顯著提升**：多項隨機對照試驗 (RCT) 證實 VTS 顯著提升 Fugl-Meyer 上肢運動評分 (FMA-UE)，改善幅度超越最小臨床重要差異值 (MCID = 5.25 分)；
- **屈肌痙攣顯著緩解**：針對拮抗肌的高頻振動刺激誘導肌梭 Ia 類神經纖維突觸前抑制，改良 Ashworth 痙攣量表 (MAS) 評分平均顯著下降 0.5–1 級；
- **BCI 解碼精準度倍增**：在運動想像腦機介面中，引入即時振動反饋使意圖分類精確率平均提升 8%~15%。
