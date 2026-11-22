# Twin Support Vector Machines (TSVM, 孿生支援向量機)

- **概念分類**: 機器學習 / 監督式分類演算法
- **相關論文**: [[kumar2013_finger_flexions_semg]]
- **相關技術**: [[Wavelet_Maxima_Density]]

---

## 1. 概念定義
孿生支援向量機 (Twin Support Vector Machines, TSVM) 是由 Jayadeva 等人於 2007 年提出的一種新型二元分類機器學習架構。

傳統支援向量機 (Standard SVM) 旨在求解**單一最大間隔分離超平面 (Maximum Margin Separating Hyperplane)**，使得兩類樣本位於超平面的兩側並保持最大距離。而 TSVM 的核心思想則是求解**一對非平行的超平面 (A Pair of Non-parallel Hyperplanes)**，每個超平面專門貼合屬於該類別的樣本，同時盡可能遠離另一類別的樣本。

---

## 2. 數學模型與公式推導

假設正類樣本矩陣為 $A \in \mathbb{R}^{m_1 \times n}$，負類樣本矩陣為 $B \in \mathbb{R}^{m_2 \times n}$。
TSVM 尋求兩個非平行超平面：
$$x^T w_1 + b_1 = 0 \quad (\text{類別 } 1 \text{ 超平面})$$
$$x^T w_2 + b_2 = 0 \quad (\text{類別 } 2 \text{ 超平面})$$

### 2.1 最佳化問題 (Quadratic Programming Problems, QPPs)

**超平面 1 的求解 (TSVM-1)**：
$$\min_{w_1, b_1, q} \frac{1}{2} \|A w_1 + e_1 b_1\|^2 + c_1 e_2^T q$$
$$\text{subject to } -(B w_1 + e_2 b_1) + q \ge e_2, \quad q \ge 0$$

- **直觀意義**: 最小化正類樣本 $A$ 到超平面 1 的平方距離總和（讓超平面 1 緊貼類別 1），同時懲罰負類樣本 $B$ 進入距離小於 1 的容忍區（$q$ 為鬆弛變數，$c_1 > 0$ 為懲罰參數）。

**超平面 2 的求解 (TSVM-2)**：
$$\min_{w_2, b_2, p} \frac{1}{2} \|B w_2 + e_2 b_2\|^2 + c_2 e_1^T p$$
$$\text{subject to } (A w_2 + e_1 b_2) + p \ge e_1, \quad p \ge 0$$

- **直觀意義**: 讓超平面 2 緊貼負類樣本 $B$，同時迫使正類樣本 $A$ 與之保持至少距離 1 的間隔。

### 2.2 預測決策準則 (Decision Rule)
給定一個新的測試樣本 $x \in \mathbb{R}^n$，計算其至兩超平面的垂直幾何距離：
$$d_1(x) = \frac{|x^T w_1 + b_1|}{\|w_1\|}, \quad d_2(x) = \frac{|x^T w_2 + b_2|}{\|w_2\|}$$
決策規則為將樣本指派至距離較近的超平面：
$$\text{Class}(x) = \arg\min_{k \in \{1, 2\}} d_k(x)$$

---

## 3. 相較於標準 SVM 的核心優勢
1. **計算效率大幅提升**:
   標準 SVM 求解一個維度為 $(m_1 + m_2)$ 的二次規劃問題，複雜度約為 $\mathcal{O}((m_1+m_2)^3)$。TSVM 拆解為兩個較小的二次規劃問題，維度分別為 $m_1$ 與 $m_2$，計算速度可提升約 4 倍。
2. **克服非對稱分佈與類別不平衡**:
   標準 SVM 隱含假設兩類別具有相同的方差或流形幾何結構；TSVM 放寬了超平面平行的約束，當生醫資料（如肌電訊號、神經放電）中不同動作類別的變異數或樣本密度極為不均時，TSVM 具有顯著更優異的分類邊界適應力。
