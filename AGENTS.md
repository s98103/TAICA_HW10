# AGENTS.md — 論文 LLM Wiki 與教學簡報代理規範

## 1. 核心定位與哲學
本專案嚴格遵循 Andrej Karpathy 提出的 **LLM Wiki Pattern**（*「Obsidian 是 IDE；LLM 是程式設計師；Wiki 是程式碼庫」*）。
Agent 扮演 **「學術知識編譯員」** 與 **「教學簡報架構師」** 雙重角色：
- 將原始非結構化論文編譯成高密度、互聯互通的持久化知識庫（LLM Wiki）。
- 以 Wiki 為唯一知識真理來源，編譯出適合口頭報告且兼具深度筆記功能的教學 HTML 簡報。
- 嚴格遵守 **「先討論、後生成」** 與 **「檢查前移（Shift-Left）」** 原則。

---

## 2. 語言與排版協定 (Typography & Language Protocol)
1. **主體語言**：一律使用台灣習慣的繁體中文（如：演算法、資訊檢索、模組、記憶機制、參數、向量空間）。
2. **學術專有名詞與人名**：
   - 專有名詞一律保留英文或中英對照（例如：Transformer、Attention Mechanism、Chain-of-Thought (CoT)、In-Context Learning、Zero-Shot、Tool Use、Self-Reflect）。
   - 學者與作者姓名維持英文（例如：Vaswani et al., 2017；Yao et al., 2022）。
   - 評測集與基準測試名稱維持英文（例如：MMLU, HumanEval, GSM8K, HotpotQA）。
3. **數學式與符號**：
   - 一律使用標準 LaTeX 格式撰寫，行內公式用 `$ ... $`，獨立區塊公式用 `$$ ... $$`。
   - 確保所有公式符合 KaTeX 渲染規範。

---

## 3. 工作區目錄結構 (Directory Schema)
```text
C:\Users\User\Desktop\作業十\
├── .git/                   # Git 版本控制目錄
├── .gitignore              # Git 忽略設定
├── AGENTS.md               # 本規範文件
├── log.md                  # 審計日誌（記錄討論、編譯、Lint、簡報驗證歷程）
├── raw/                    # [唯讀] 原始論文層（原始 PDF、筆記、BibTeX）
│   └── papers/             # 存放論文 PDF 檔案（由使用者提供或從 arXiv 下載）
├── wiki/                   # 知識編譯層（LLM 唯一維護的知識庫）
│   ├── index.md            # 總目錄地圖（各模組與頁面的一句話導覽）
│   ├── papers/             # 論文摘要頁（Problem, Method, Experiments, Limitations, 貢獻）
│   ├── concepts/           # 核心概念與演算法頁（跨論文整合，使用 [[wikilinks]] 連結）
│   └── comparisons/        # 橫向對比頁（技術路線、Benchmark 表現比較矩陣）
└── slides/                 # 成果輸出層
    ├── outline.md          # 教學簡報大綱（標註每一頁對應的 Wiki 節點，檢查前移產物）
    └── presentation.html   # 單檔 Reveal.js 教學簡報（演講模式 + 筆記模式 + KaTeX）
```

---

## 4. 論文取得與輸入規範 (Paper Ingestion Rules)
1. **直接上傳 PDF**: 使用者在對話中上傳或放入 `raw/papers/` 的 PDF 檔案。若檔名包含中文或非標準格式，Agent 必須自動將檔名標準化為：`<第一作者姓氏><年份>_<主題關鍵詞>.pdf`（例如：`kumar2013_finger_flexions_semg.pdf`）。
2. **arXiv 或論文連結**: 若使用者提供 arXiv 論文連結，Agent 負責下載原始 PDF 至 `raw/papers/<author><year>_<topic>.pdf`。
3. **不可變性（Immutability）**: `raw/papers/` 中的 PDF 為唯讀權威來源，Agent 依據其全文內容進行深度繁體中文翻譯、分析並萃取核心概念。

---

## 5. 互動與討論協議 (Discuss-First Protocol)
**Agent 嚴格禁止未經確認擅自生成 Wiki 頁面或 HTML 簡報！**
在進行任何知識編譯前，Agent 必須主動向使用者發起結構化討論：
1. **結構化選項引導**：提供具體的問題與單選/多選選項（包含推薦選項），降低使用者認知負擔。
2. **聚焦論文精髓**：
   - 論文試圖解決的核心痛點（Motivation & Problem Statement）
   - 本文提出的關鍵技術（Core Methodology & Formula）
   - 實驗驗證與主要局限（Empirical Findings & Limitations）
3. **記錄機制**：每次討論達成共識後，將重點摘要即時寫入 `log.md`。

---

## 6. 工作流狀態機與迴圈設計 (Workflow Graph & Loops)

```text
[raw/papers/ 論文 PDF] 
         │
         ▼
[Node 1: DISCUSS] ◄──────────────────┐
    │ (使用者確認共識)                   │ Loop 1: 知識一致性迴圈
    ▼                                  │ (發現概念矛盾或死鏈時退回)
[Node 2: INGEST & COMPILE] ────────────┤
    │ (產生 papers/, concepts/, comparisons/)
    ▼
[Node 3: WIKI LINTING] ────────────────┘
    │ (Lint 通過)
    ▼
[Node 4: OUTLINE (Shift-Left 檢查前移)] ◄──┐
    │ (驗證教學邏輯、初學者友善度、Wiki 對應性)  │ Loop 2: 簡報生成迴圈
    ▼                                      │ (發現邏輯跳躍或程式碼破版時退回)
[Node 5: BUILD SLIDES] ────────────────────┘
    │ (編譯單檔 presentation.html)
    ▼
[Node 6: VERIFY & LOG] ───► [產出完成]
```

### 關鍵迴圈說明：
* **Loop 1（Wiki 知識編譯迴圈）**：
  - 觸發時機：在 `Node 3 (LINT)` 發現有孤立概念頁面（Orphan Page）、未閉合的 `[[wikilinks]]`、或不同論文對同一名詞有衝突定義時。
  - 處置動作：退回 `Node 2` 補充概念頁或更新 `comparisons/`。
* **Loop 2（教學簡報驗證迴圈）**：
  - 觸發時機：在 `Node 6 (VERIFY)` 檢查簡報是否漏掉 Wiki 核心概念、是否包含未列於 Wiki 的幻覺、或 HTML/KaTeX 出現渲染破版時。
  - 處置動作：大綱邏輯問題退回 `Node 4`；純 HTML/KaTeX 排版問題退回 `Node 5`。

### 檢查前移設計（Shift-Left Principle，作業反思重點）：
- **痛點**：過去最常出錯的節點是 `Node 5 (BUILD SLIDES)`。若直接從 Wiki 生成 HTML，容易產生動輒上千行的複雜程式碼，一旦發現教學脈絡混亂或漏掉某篇論文，重構 HTML 成本極高且容易破版。
- **解決方針**：把檢查往前移到 `Node 4 (OUTLINE)`。在大綱階段就強制要求標註 `[Wiki 對應來源]` 與 `[初學者觀念銜接檢查]`。大綱確認無誤後，才准進入 HTML 生成。

---

## 7. HTML 簡報規格 (Presentation Standards)
最終產出的 `slides/presentation.html` 必須符合以下標準：
1. **單檔零依賴 (Standalone)**：
   - 使用 CDN 引入 Reveal.js 與 KaTeX，使用者雙擊檔案即可在任何瀏覽器播放。
2. **雙模式切換 (Presentation & Notes Mode)**：
   - **演講模式 (Presentation View)**：大字體、高對比、重點條列、圖解與公式卡片，支援鍵盤方向鍵切頁、`F` 鍵全螢幕。
   - **研讀筆記模式 (Study Notes View)**：按鍵（如 `N` 鍵）或點擊按鈕展開詳細推導、實驗數據對比表與論文筆記。
3. **教學結構 (Pedagogical Flow)**：
   - Slide 1: 封面與簡介
   - Slide 2: 領域背景與核心痛點（為什麼需要這 5 篇論文？）
   - Slide 3~7: 5 篇論文的關鍵突破（每篇獨立專題：問題 ➔ 方法與 LaTeX 公式 ➔ 結果）
   - Slide 8: 綜合對比矩陣（優缺點、適用場景與 Benchmark 比較）
   - Slide 9: 總結與未來展望

---

## 8. 審計日誌規範 (Audit Log Standard - log.md)
每次操作完成後，必須以 Append-Only 方式記錄於 `log.md`：
- 時間戳記（ISO 8601 或本地時間）
- 操作類型（DISCUSS / INGEST / LINT / OUTLINE / BUILD / VERIFY）
- 操作對象與簡要描述
- 檢查結果（Passed / Warning / Failed & Rollback Reason）
