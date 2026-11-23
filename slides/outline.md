# 教學簡報大綱與知識庫溯源對照 (Slides Outline & Wiki Grounding)

> **版本**: 1.0 (Shift-Left 檢查前移產物)  
> **視覺主題**: 莫蘭迪灰階石墨與啞光磚紅 (Graphite & Muted Terracotta)  
> **背景底色**: 淡霧白 `#F9F9F8` | **內文主色**: 灰調石墨 `#3E444B` | **核心強調色**: 啞光磚紅 `#A85751` | **卡片框線**: 暖石灰 `#E5E3DC`  
> **目標受眾**: 生醫工程、資訊科學初學者與研討會上台報告評審  

---

## 投影片頁面結構與 Wiki 節點對照表

| 頁碼 | 頁面主題 (Title) | 教學目標 (Pedagogical Goal) | Wiki 知識來源對照 | 筆記模式核心推導與補充 (Study Notes) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **封面：單通道表面肌電訊號的手指動作辨識** | 介紹論文全名、作者群（Kumar et al., 2013）、發表期刊與研究總體核心貢獻 | `wiki/papers/kumar2013_finger_flexions_semg.md` | 本文發表於生醫工程頂級開源期刊 JNER，奠定單通道微弱肌電辨識的經典架構。 |
| **02** | **問題意識：多通道的脆弱 vs. 單通道的困境** | 以鮮明對比點出傳統義肢控制兩大工程痛點，建立聽眾的「問題感 (Motivation)」 | `wiki/papers/kumar2013_finger_flexions_semg.md`, `wiki/concepts/Myoelectric_Prosthesis_Control.md` | 詳細列舉 19~32 通道陣列的高硬體成本與電極位移致錯率，以及 Momen 等人先前僅 56% 準確率的數據。 |
| **03** | **物理底層：人體組織的體導電理論** | 解釋為何單通道電極能分辨不同手指：肌肉各向異性傳導與距離振幅衰減規律 | `wiki/concepts/Volume_Conduction_Theory.md` | 深入推導肌肉纖維縱向電導率 $\sigma_z$ 與橫向 $\sigma_x$ 的巨大差異，以及電位隨距離反比 $A \propto 1/d^p$ 的衰減方程式。 |
| **04** | **核心演算法：小波極大值密度 (WMD)** | 拆解特徵萃取流程：雙正交小波 `bior3.3`、跨尺度奇異點追蹤與 300ms 滑動窗 | `wiki/concepts/Wavelet_Maxima_Density.md` | 展示小波極大值數學定義 $W f(s, x_{n-1}) < W f(s, x_n) > W f(s, x_{n+1})$，說明為何跨尺度追蹤能完美過濾運動偽影與隨機熱雜訊。 |
| **05** | **分類器突破：孿生支援向量機 (TSVM)** | 用視覺化對比標準 SVM vs. TSVM，解析雙非平行超平面如何克服肌電非對稱分佈 | `wiki/concepts/Twin_SVM.md` | 展開 TSVM-1 與 TSVM-2 的二次規劃問題 (QPPs) 目標函數，分析計算複雜度降低至 $1/4$ 的數學成因。 |
| **06** | **實驗成效：健全者與截肢者臨床實測** | 用清晰圖表展示 4 類手指動作的辨識率、電極位移抗性與雙側鏡像動作訓練 | `wiki/papers/kumar2013_finger_flexions_semg.md` | 展開完整實驗數據表：健全者遠端 93.41% vs. 近端 92.40%（位移僅降 1% 的強健性），截肢者通道 2 達 81.87% 的雙側訓練機制。 |
| **07** | **臨床與工程挑戰：延遲門檻與肌肉萎縮** | 探討系統如何滿足 300ms 即時控制門檻，以及殘肢肌肉萎縮與神經重塑挑戰 | `wiki/concepts/Myoelectric_Prosthesis_Control.md` | 剖析 300ms/200ms 訊號滑動窗之延遲裕度，深入討論臨床肌肉廢用性萎縮 (Disuse Atrophy) 的解剖成因與對策。 |
| **08** | **結論與未來展望：邁向直覺式肌電手** | 總結三大核心貢獻（體導電物理特徵 + 雙非平行超平面 + 單通道抗位移），展望多指協同抓握 | `wiki/papers/kumar2013_finger_flexions_semg.md`, `wiki/index.md` | 提供上台報告 1 分鐘 Takeaway 總結語，列出未來多自由度、跨日遷移學習與低功耗晶片嵌入展望。 |

---

## 檢查前移（Shift-Left）驗證要點
1. **知識一致性**: 每一頁的論點與數據（如 93.41%、81.87%、300ms、`bior3.3`）均直接源自 `wiki/`，無任何編造幻覺。
2. **初學者思維鏈 (Pedagogical Scaffolding)**:
   - 痛點引入 (Why) ➔ 物理本質 (What) ➔ 演算法推導 (How) ➔ 分類決策 (ML) ➔ 實驗數據 (Results) ➔ 臨床思考 (Limitations)。
   - 邏輯層層遞進，非技術名詞堆疊。
3. **版面與字體規格**:
   - 內文採用台灣習慣繁體中文，專有名詞維持英文。
   - 所有公式均有對應 LaTeX 標籤與中文定義，可直接由 KaTeX 渲染。
