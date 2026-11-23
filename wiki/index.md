# LLM Wiki 總目錄索引 (Index)

> 本索引頁為本 Wiki 知識庫之全景導覽地圖。收錄 5 篇前臂肌電解碼與神經復健核心文獻、8 大跨篇核心概念網與跨篇綜合對照矩陣。

---

## 1. 論文專頁庫 (Papers, 5 篇收錄完成)
1. [[kumar2013_finger_flexions_semg]] — *Kumar et al. (2013)*: 提出基於體導電與小波極大值密度的單通道 sEMG 手指動作辨識，健全者 93.41%，截肢者 81.87%，展現極高抗電極位移強健性。
2. [[yao2020_forearm_muscles_antivibration]] — *Yao et al. (2020)*: 評估防震手套與外力振動下前臂肌群 (FDS 等) 的肌電活化增強與肌肉骨骼負荷，建立物理干擾下的肌電漂移基準。
3. [[fukunaga2023_flexor_pronator_semg]] — *Fukunaga et al. (2023)*: 探討橈側屈指淺肌 (FDS) 與旋前肌群在阻力運動下的選擇性活化 (Selective Activation)，揭示深淺肌腹神經招募規律。
4. [[yang2026_gesture_classification_semg_motion]] — *Yang et al. (2026)*: 結合 6 通道 sEMG (FDS+FDP) 與手指運動手套的多模態融合手勢分類系統，中風患者與健全者辨識率突破 90%。
5. [[zhang2026_vibrotactile_neurorehabilitation_review]] — *Zhang et al. (2026)*: 系統性回顧 35 項臨床文獻，探討振動觸覺刺激 (VTS) 在上肢神經復健中的神經重塑機制，補齊智慧假手之感覺-動作閉環。

---

## 2. 核心概念與方法網 (Concepts, 8 大知識節點)
- [[Volume_Conduction_Theory]] — 體導電理論：描述生物電位在各向異性肌肉組織中的傳導物理模型與距離振幅反比衰減規律 ($A \propto 1/d^p$)。
- [[Wavelet_Maxima_Density]] — 小波極大值密度 (WMD)：利用雙正交小波 `bior3.3` 跨尺度偵測動作電位微觀奇異點，結合放電密度與振幅進行抗干擾特徵萃取。
- [[Twin_SVM]] — 孿生支援向量機 (TSVM)：求解一對非平行超平面的二次規劃機器學習演算法，運算加速 4 倍並適應生醫肌電非對稱幾何分佈。
- [[Myoelectric_Prosthesis_Control]] — 肌電義肢控制：探討 300ms 即時控制延遲黃金門檻、電極滑移致錯應對、殘肢肌肉廢用性萎縮與雙側鏡像訓練機制。
- [[Sensory_Motor_Closed_Loop]] — 感覺-運動閉環控制：破解開環假手的認知疲勞死穴，利用振動觸覺刺激 (VTS) 活化 S1-M1 感覺運動節律 (mu/beta ERD) 與長時程增強 (LTP)。
- [[Selective_Muscle_Activation]] — 骨骼肌選擇性活化：深入前臂屈肌-旋前肌群 (FPM)，解析尺偏 (FCU 40.3% MVC) 與旋前 (PT 73.0% / FDS 63.9% MVC) 的神經運動單元差異化招募。
- [[Multimodal_Sensor_Fusion]] — 多模態感測融合：結合「前向神經發力意圖 (sEMG)」與「終端運動軌跡 (柔性彎曲手套)」，配合 SG 濾波與 STFT，突破中風病理噪聲干擾 (>90% 辨識率)。
- [[EMG_Normalization_and_Fatigue]] — 肌電正規化與肌肉負荷評估：比較最大自主收縮 (MVC) 與同等握力次最大基準之方法學差異，解析防震手套 +48% 肌電激增與頻譜左移疲勞現象。

---

## 3. 綜合對比與基準測試 (Comparisons)
- [[cross_paper_matrix]] — 跨論文技術路線與臨床應用綜合比較矩陣：5 篇論文感測通道、肌群、演算法與神經人機介面定位全對照。
