# Twin Support Vector Machines (TSVM, 孿生支援向量機)

- **概念分類**: 機器學習 / 監督式模式辨識演算法
- **相關論文**: [[kumar2013_finger_flexions_semg]], [[yang2024_gesture_classification_semg_motion]]
- **相關技術**: [[Wavelet_Maxima_Density]], [[Myoelectric_Prosthesis_Control]]

---

## 1. 概念核心定義 (Core Definition)
**孿生支援向量機（Twin Support Vector Machine, TSVM）** 是由 Jayadeva 等人於 2007 年提出的一種革新性機器學習分類演算法。

傳統支援向量機 (Standard SVM) 旨在求解**單一最大間隔分離超平面 (Maximum Margin Separating Hyperplane)**，強求兩類樣本對稱分佈在超平面兩側。  
而 TSVM 的核心思想則是求解**一對非平行的超平面（A Pair of Non-parallel Hyperplanes）**：
- 第一個超平面專門貼合第一類樣本，同時盡可能遠離第二類樣本；
- 第二個超平面專門貼合第二類樣本，同時盡可能遠離第一類樣本。

---

## 2. 數學規劃與二次規劃問題 (QPP Formulation)
設第一類訓練樣本矩陣為 $\mathbf{A} \in \mathbb{R}^{m_1 \times n}$，第二類訓練樣本矩陣為 $\mathbf{B} \in \mathbb{R}^{m_2 \times n}$。  
求解一對非平行超平面：
$$x^T w_1 + b_1 = 0 \quad (\text{超平面 1}), \qquad x^T w_2 + b_2 = 0 \quad (\text{超平面 2})$$

### 二次規劃問題 1 (TSVM-1)：
$$\min_{w_1, b_1, q} \frac{1}{2} \|\mathbf{A} w_1 + e_1 b_1\|^2 + c_1 e_2^T q$$
$$\text{subject to} \quad -(\mathbf{B} w_1 + e_2 b_1) + q \ge e_2, \quad q \ge 0$$
- **幾何含義**：最小化類別 1 樣本矩陣 $\mathbf{A}$ 到超平面 1 的距離平方和（貼近類別 1），同時約束類別 2 樣本矩陣 $\mathbf{B}$ 距離超平面 1 至少大於 1，$q$ 為鬆弛變數，$c_1$ 為懲罰參數。

### 二次規劃問題 2 (TSVM-2)：
$$\min_{w_2, b_2, p} \frac{1}{2} \|\mathbf{B} w_2 + e_2 b_2\|^2 + c_2 e_1^T p$$
$$\text{subject to} \quad (\mathbf{A} w_2 + e_1 b_2) + p \ge e_1, \quad p \ge 0$$

---

## 3. 幾何垂直距離決策準則 (Decision Rule)
對於一個未知的測試特徵向量 $\mathbf{x} \in \mathbb{R}^n$，分別計算其至兩個非平行超平面的正交歐式幾何距離：

$$d_1(\mathbf{x}) = \frac{|\mathbf{x}^T w_1 + b_1|}{\|w_1\|}, \qquad d_2(\mathbf{x}) = \frac{|\mathbf{x}^T w_2 + b_2|}{\|w_2\|}$$

測試樣本被指派至**幾何距離較近**的超平面所對應的類別：
$$\text{Class}(\mathbf{x}) = \arg\min_{k \in \{1, 2\}} d_k(\mathbf{x})$$

---

## 4. 運算複雜度與生醫肌電優勢剖析

### 1. 運算速度整整提升近 4 倍
- **標準 SVM**：需求解一個維度為 $(m_1 + m_2)$ 的大型二次規劃問題，時間複雜度約為 $\mathcal{O}((m_1 + m_2)^3)$；
- **TSVM**：將問題拆解為兩個規模分別為 $m_1$ 與 $m_2$ 的獨立小型二次規劃問題，整體時間複雜度降為 $\mathcal{O}(m_1^3) + \mathcal{O}(m_2^3)$。
- **推論**：若 $m_1 \approx m_2 = m$，則標準 SVM 耗時 $(2m)^3 = 8m^3$，而 TSVM 僅需 $m^3 + m^3 = 2m^3$，**理論運算速度快了 4 倍**！

### 2. 極度適應生醫肌電之非對稱分佈
生醫肌電訊號在不同手指收縮時，因肌纖維招募數量不同，特徵空間的協方差矩陣極不對稱（如無名指發力集中、中指發力離散）。標準 SVM 強求單一對稱平分超平面容易過擬合，而 TSVM 雙超平面各自獨立調整旋轉角度，完美包容了生醫訊號的幾何不對稱性。

---

## 5. 跨篇演算法演進關聯
- 在 [[kumar2013_finger_flexions_semg]] 中，TSVM 與 2D WMD 特徵配合，達成 $93.41\%$ 準確率與微秒級推論；
- 在 [[yang2024_gesture_classification_semg_motion]] 中，研究進一步將傳統 SVM 與高效率梯度提升樹 **LightGBM** 進行對比，展現了生醫機器學習從核方法走向樹模型與神經網路的演進軌跡。
