# Assisting Hand Gesture Classification and Rehabilitation Assessment via sEMG and Finger Motion Data

## 1. 文獻基本資訊 (Bibliographic Information)
- **論文原名：** Assisting hand gesture classification and rehabilitation assessment via sEMG and finger motion data
- **作者列表：** Xiuxiu Yang, Lingfeng Zhang, Fukui Wu, Xinran Wei, Haifeng Huang, Jun Li, Tao Hu
- **通訊作者：** Jun Li (College of Intelligent Science and Engineering, Hubei Minzu University, Enshi, China; Email: lijun72213@163.com)
- **發表期刊：** *Frontiers in Bioengineering and Biotechnology*
- **出版年份與卷期：** 2026 年, Vol. 13, Article 1533036
- **DOI：** [10.3389/fbioe.2025.1533036](https://doi.org/10.3389/fbioe.2025.1533036)
- **文獻類型：** 原創研究 (Original Research)
- **關鍵字：** classification, finger movement, machine learning algorithms, rehabilitation, sEMG, multimodal fusion

---

## 2. 一句話核心總結 (Executive Summary)
本研究研發了一套結合前臂 6 通道表面肌電 (FPL, FDS, FDP 深淺肌群) 與五指柔性彎曲感測手套的穿戴式多模態系統，在恩施醫院採集 15 位受試者（含腦卒中偏癱住院患者）共 900 組臨床動作數據，結合 SG 濾波與 STFT 時頻譜特徵，SVM、LightGBM 與 MLP 跨模型手勢分類精準度穩定突破 90%，成功突破傳統人工量表盲區，建立了客觀量化的智慧復健評估體系。

---

## 3. 研究背景與臨床痛點 (Background & Clinical Problem)
1. **中風後手精細運動障礙：**
   腦卒中引發皮質脊髓束中斷，導致上肢手指伸肌無力、屈肌張力過高與異常協同運動，手部精細功能喪失嚴重影響日常生活自理。
2. **傳統臨床量表的局限：**
   目前黃金標準（如 Fugl-Meyer FMA、ARAT）仰賴治療師肉眼主觀打分，粗粒度離散評分無法捕捉微小神經恢復，且耗費大量人力、無法居家遠程追蹤。
3. **單模態感測的致命缺陷：**
   - 純肌電 (sEMG-only)：患者患側肌電極度微弱且肌萎縮嚴重，極易受噪聲干擾；
   - 純運動學 (Kinematics-only)：無法區分病患是大腦主動發力還是被動牽拉。
   多模態「神經前饋電位 + 物理運動軌跡」互補融合是破局關鍵。

---

## 4. 研究目的與創新點 (Purpose & Innovations)
- **研究目的：** 研發穿戴式多模態手勢辨識與復健評估硬體-資料庫架構，並驗證其在真實中風患者中的辨識魯棒性與客觀評估潛力。
- **核心創新：**
  1. 整合 6 通道 sEMG 與柔性壓阻彎曲感測手套；
  2. 構建首個涵蓋不同運動障礙程度中風患者的醫院現場 900 組臨床時序數據集；
  3. 引入 SG 濾波保持波形形態，結合 STFT 時頻特徵實現輕量高效解碼。

---

## 5. 硬體架構與實驗方法 (Hardware & Methods)
1. **6 通道前臂肌電電極配置 (3 目標肌腹 × 2 通道)：**
   - **FPL (屈拇長肌, 2 通道)：** 支配拇指屈曲與對掌；
   - **FDS (橈側屈指淺肌, 2 通道)：** 支配第 2–5 指中節指骨屈曲；
   - **FDP (屈指深肌, 2 通道)：** 支配第 2–5 指遠端指骨屈曲。
2. **五指柔性運動捕捉手套：**
   - 背側縫合 5 根柔性壓阻彎曲感測器，動態量化 MCP 與 PIP 關節彎曲角度。
3. **臨床受試者與 6 類手勢資料集 (900 Trials)：**
   - 15 位臨床受試者（含偏癱住院患者與對照組）；
   - 6 種復健核心手勢（手勢 0 至 5：握拳 Fist、張手 Open、二指捏 Pinch、指點 Point、比讚 Thumb-up 與特定抓握手勢）；
   - 每位受試者重複 10 次，總計 $15 \times 6 \times 10 = 900$ 組同步數據。
4. **訊號處理流水線：**
   - **Savitzky–Golay (SG) 濾波：** 多項式擬合平滑高頻噪聲，完全不削平波形瞬態峰值，保持零相位失真；
   - **短時傅立葉變換 (STFT)：** 加窗切片生成 2D 時頻譜圖 (Spectrogram)。
5. **機器學習分類模型：**
   - SVM (RBF 核心)、LightGBM、多層感知機 (MLP)。

---

## 6. 主要實驗結果 (Key Findings & Exact Data)
- **跨模型高精準度分類表現：**
  - **LightGBM：** 交叉驗證精準度 **93.2%**，獨立測試集 **92.5%**（綜合推論速度與精準度最優）；
  - **SVM (RBF)：** 交叉驗證精準度 **91.4%**，獨立測試集 **90.8%**；
  - **MLP 類神經網路：** 交叉驗證精準度 **92.1%**，獨立測試集 **91.2%**。
- **手勢細分表現：**
  握拳 (Fist) 與張手 (Open) 準確率最高 (>96%)；捏握 (Pinch) 與指點 (Point) 在重度攣縮患者中稍有混淆 (~88%–90%)。
- 全模型在臨床病理數據集上均穩定超越 90% 精準度門檻！

---

## 7. 臨床客觀復健評估價值 (Clinical Assessment Rationale)
- **特徵流形對齊神經恢復階段：** 高功能患者特徵聚類清晰，低功能患者特徵重疊粘連，精確量化異常共同運動；
- **連續評分輸出：** 分類器輸出機率可轉化為連續客觀神經功能評分；
- **遠程智慧康復：** 支援病患居家結合遊戲進行訓練，自動回傳功能演化雷達圖。

---

## 8. 與本專案知識庫主題之關聯 (Thematic Integration)
- 將前臂肌電解碼從「義肢控制」推進至「病患主動神經復健」；
- 多模態互補架構為智慧肌電外骨骼與意圖解碼提供了最前沿範式。

---

## 9. 重要專業名詞中英對照表 (Terminology Table)
| 英文術語 | 繁體中文全稱 | 技術與醫學定義說明 |
| :--- | :--- | :--- |
| **Multimodal Fusion** | 多模態感測融合 | 結合肌電前饋電位與手套運動軌跡的雙重互補感知機制 |
| **Flexor Pollicis Longus (FPL)** | 屈拇長肌 | 前臂深層肌，專一支配拇指指間關節屈曲 |
| **Flexor Digitorum Profundus (FDP)**| 屈指深肌 | 前臂深層肌，支配 2–5 指遠節指骨屈曲，指尖精細發力主力 |
| **Savitzky–Golay Filter** | SG 多項式平滑濾波器 | 基於局部最小平方法之數位濾波器，去噪同時完美保真峰值形態 |
| **Short-Time Fourier Transform (STFT)**| 短時傅立葉變換 | 局部滑動窗時頻變換，生成二維能量時頻譜圖 (Spectrogram) |
| **LightGBM** | 輕量梯度提升機 | 基於直方圖最佳化與葉子生長之高效率決策樹機器學習架構 |
