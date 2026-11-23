# -*- coding: utf-8 -*-
"""
Ultimate Combined Vertical Flowchart:
Combines the 10-step, 2-phase, 4-loop workflow with the multi-paper Fan-Out / Fan-In batch architecture.
Saves directly into: C:/Users/User/Desktop/作業十/workflow/vertical_flowchart.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import io

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Noto Sans TC', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(11.5, 32), dpi=200)
ax.set_xlim(-5.8, 5.8)
ax.set_ylim(-4.0, 28.6)
ax.axis('off')

# Color palette
AI_STYLE = {'bg': '#EDE9FE', 'border': '#8B5CF6', 'text': '#3B0764', 'badge_dot': '#8B5CF6', 'tag': 'AI 節點'}
GATE_STYLE = {'bg': '#E0F2FE', 'border': '#0284C7', 'text': '#082F49', 'badge_dot': '#0284C7', 'tag': '檢查關卡'}
HUMAN_STYLE = {'bg': '#FFEDD5', 'border': '#EA580C', 'text': '#7C2D12', 'badge_dot': '#EA580C', 'tag': '人工確認'}
DELIV_STYLE = {'bg': '#DCFCE7', 'border': '#16A34A', 'text': '#14532D', 'badge_dot': '#16A34A', 'tag': '完成交付'}

# ==================== PHASE 1 CONTAINER ====================
# y: 15.2 to 28.0 (height = 12.8)
p1_bg = patches.FancyBboxPatch((-5.0, 15.2), 10.0, 12.8,
                              boxstyle="round,pad=0.2,rounding_size=0.35",
                              facecolor="#FEFCE8", edgecolor="#DDD6FE", linewidth=2.5, zorder=1)
ax.add_patch(p1_bg)

# Phase 1 Title Tab
ax.text(-4.6, 27.2, "  第一階段：批次知識匯總與大綱集中把關  ", ha="left", va="center",
        fontsize=13, fontweight='bold', color="#6B21A8",
        bbox=dict(boxstyle="round,pad=0.42", facecolor="#F3E8FF", edgecolor="#A855F7", lw=1.5), zorder=2)

# Phase 1 Nodes
nodes_p1 = {
    'N1': {'y': 25.6, 'title': '1. 批次找 Wiki 資料 (Paper 1 ~ N)', 'sub': '一次提取多篇文獻核心數據、演算法與實驗指標', 'style': AI_STYLE},
    'G1': {'y': 23.3, 'title': '2. 資料夠不夠？', 'sub': '檢查各篇關鍵參數、受試者條件是否完整齊全', 'style': GATE_STYLE},
    'N2': {'y': 21.0, 'title': '3. 抓重點資訊與橫向對照', 'sub': '抽取核心數值卡片，自動更新 cross_paper_matrix 與 Wiki 網絡', 'style': AI_STYLE},
    'N3': {'y': 18.7, 'title': '4. 規劃「1 個首頁 + N 份獨立 8 頁大綱」', 'sub': '強制為各論文規劃專屬章節大綱，徹底杜絕壓縮偷懶', 'style': AI_STYLE},
    'H1': {'y': 16.4, 'title': '5. 我看過確認 (大綱總表集中把關)', 'sub': '你只需審核一次大綱總表！確認教學方向與各篇深入架構', 'style': HUMAN_STYLE},
}

NODE_W = 4.4
NODE_H = 1.25

for k, v in nodes_p1.items():
    s = v['style']
    box = patches.FancyBboxPatch((-NODE_W/2, v['y'] - NODE_H/2), NODE_W, NODE_H,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=s['bg'], edgecolor=s['border'],
                                linewidth=2.2, zorder=3)
    ax.add_patch(box)
    ax.text(0, v['y'] + 0.2, v['title'], ha="center", va="center",
            fontsize=11.5, fontweight='bold', color=s['text'], zorder=4)
    ax.text(0, v['y'] - 0.1, v['sub'], ha="center", va="center",
            fontsize=9.0, color="#4B5563", zorder=4)
    dot = patches.Circle((-0.85, v['y'] - 0.38), radius=0.08, facecolor=s['badge_dot'], edgecolor='none', zorder=5)
    ax.add_patch(dot)
    ax.text(-0.68, v['y'] - 0.38, s['tag'], ha="left", va="center",
            fontsize=9.0, fontweight='bold', color=s['text'], zorder=4)

def draw_down_arrow(y_top, y_bot, text=None, text_y=None):
    ax.annotate('', xy=(0, y_bot), xytext=(0, y_top),
                arrowprops=dict(arrowstyle="-|>", color="#4B5563", lw=2.2, mutation_scale=15),
                zorder=2)
    if text:
        ty = text_y if text_y is not None else (y_top + y_bot)/2
        ax.text(0, ty, f"  {text}  ", ha="center", va="center",
                fontsize=9.5, fontweight='bold', color="#1F2937",
                bbox=dict(boxstyle="round,pad=0.28", facecolor="#FFFFFF", edgecolor="#CBD5E1", lw=1.2),
                zorder=5)

# Downward flow Phase 1
draw_down_arrow(nodes_p1['N1']['y'] - NODE_H/2, nodes_p1['G1']['y'] + NODE_H/2)
draw_down_arrow(nodes_p1['G1']['y'] - NODE_H/2, nodes_p1['N2']['y'] + NODE_H/2, text="夠了，繼續")
draw_down_arrow(nodes_p1['N2']['y'] - NODE_H/2, nodes_p1['N3']['y'] + NODE_H/2)
draw_down_arrow(nodes_p1['N3']['y'] - NODE_H/2, nodes_p1['H1']['y'] + NODE_H/2)

# Loops in Phase 1
def draw_loop_left(y_from, y_to, x_turn, label, label_y=None):
    x_start = -NODE_W/2
    x_end = -NODE_W/2
    verts = [(x_start, y_from), (x_turn, y_from), (x_turn, y_to), (x_end, y_to)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='#DC2626', linestyle='--', linewidth=2.2, zorder=3)
    ax.add_patch(patch)
    ax.annotate('', xy=(x_end, y_to), xytext=(x_end - 0.25, y_to),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=2.2, mutation_scale=15), zorder=4)
    ly = label_y if label_y is not None else (y_from + y_to)/2
    ax.text(x_turn - 0.12, ly, label, ha="right", va="center",
            fontsize=9.2, fontweight='bold', color="#B91C1C",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#FEF2F2", edgecolor="#FCA5A5", lw=1.2), zorder=6)

def draw_loop_right(y_from, y_to, x_turn, label, label_y=None):
    x_start = NODE_W/2
    x_end = NODE_W/2
    verts = [(x_start, y_from), (x_turn, y_from), (x_turn, y_to), (x_end, y_to)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='#DC2626', linestyle='--', linewidth=2.2, zorder=3)
    ax.add_patch(patch)
    ax.annotate('', xy=(x_end, y_to), xytext=(x_end + 0.25, y_to),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=2.2, mutation_scale=15), zorder=4)
    ly = label_y if label_y is not None else (y_from + y_to)/2
    ax.text(x_turn + 0.12, ly, label, ha="left", va="center",
            fontsize=9.2, fontweight='bold', color="#B91C1C",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#FEF2F2", edgecolor="#FCA5A5", lw=1.2), zorder=6)

# G1 -> N1 Loop (Left)
draw_loop_left(nodes_p1['G1']['y'], nodes_p1['N1']['y'], -3.2, "不夠 → 停下來補找")
# H1 -> N3 Loop (Right)
draw_loop_right(nodes_p1['H1']['y'], nodes_p1['N3']['y'], 3.2, "不滿意 → 重排大綱")
# H1 -> N1 Loop (Far Right)
draw_loop_right(nodes_p1['H1']['y'], nodes_p1['N1']['y'], 4.3, "不滿意 → 重新找資料", label_y=21.0)


# ==================== INTER-PHASE CONNECTOR ====================
# Arrow comes down vertically at x=0 into Phase 2, passing the title cleanly
draw_down_arrow(nodes_p1['H1']['y'] - NODE_H/2, 12.6, text="各樣都 OK：啟動多篇並行生成 (Fan-Out)", text_y=14.5)


# ==================== PHASE 2 CONTAINER ====================
# y: -2.7 to 13.8 (height = 16.5, comfortably enclosing Node 10 with generous padding)
p2_bg = patches.FancyBboxPatch((-5.0, -2.7), 10.0, 16.5,
                              boxstyle="round,pad=0.2,rounding_size=0.35",
                              facecolor="#FEFCE8", edgecolor="#DDD6FE", linewidth=2.5, zorder=1)
ax.add_patch(p2_bg)

# Phase 2 Title Tab (Cleanly on top left at y = 13.1, while split happens below at y = 12.1)
ax.text(-4.6, 13.1, "  第二階段：並行扇出生成與首頁自動掛載 (Fan-Out / Fan-In)  ", ha="left", va="center",
        fontsize=13, fontweight='bold', color="#6B21A8",
        bbox=dict(boxstyle="round,pad=0.42", facecolor="#F3E8FF", edgecolor="#A855F7", lw=1.5), zorder=2)

# Parallel Fan-Out Stream Cards (Top of Phase 2)
col_x = [-3.2, 0, 3.2]
col_w = 2.8
col_h = 1.15
fanout_y = 10.9

# Distributor banner centered at y = 12.1
ax.text(0, 12.1, "【多任務並行軌道：各篇論文獨立產出，互不干擾、拒絕壓縮！】", ha="center", va="center",
        fontsize=10.2, fontweight='bold', color="#4C1D95",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#EDE9FE", edgecolor="#A78BFA", lw=1.2), zorder=5)

cards_info = [
    ("論文 1 專屬簡報", "Kumar (8 頁獨立深入 PPT)"),
    ("論文 2 專屬簡報", "Yao (8 頁獨立深入 PPT)"),
    ("論文 3~5 專屬簡報...", "Fukunaga, Yang, Zhang...")
]

# Diagonal arrows start from distributor at y = 11.8 (BELOW the title tab, avoiding any overlap)
for i in range(3):
    cx = col_x[i]
    ax.annotate('', xy=(cx, fanout_y + col_h/2), xytext=(0, 11.75),
                arrowprops=dict(arrowstyle="-|>", color="#8B5CF6", lw=2, mutation_scale=13),
                zorder=2)
    box = patches.FancyBboxPatch((cx - col_w/2, fanout_y - col_h/2), col_w, col_h,
                                boxstyle="round,pad=0.1,rounding_size=0.18",
                                facecolor="#F5F3FF", edgecolor="#8B5CF6",
                                linewidth=2.0, zorder=3)
    ax.add_patch(box)
    ax.text(cx, fanout_y + 0.18, cards_info[i][0], ha="center", va="center",
            fontsize=10.5, fontweight='bold', color="#3B0764", zorder=4)
    ax.text(cx, fanout_y - 0.2, cards_info[i][1], ha="center", va="center",
            fontsize=8.5, color="#6B21A8", zorder=4)

# Phase 2 Detailed Standard Pipeline (Nodes 6 to 9)
nodes_p2 = {
    'N4': {'y': 8.6, 'title': '6. 寫每一頁內容 (各篇獨立展開)', 'sub': '撰寫各頁投影片卡片，以及按 N 鍵展開的厚實研讀筆記手冊', 'style': AI_STYLE},
    'G2': {'y': 6.5, 'title': '7. 有沒有漏掉？', 'sub': '比對內容是否嚴格忠實於文獻原文，杜絕 AI 幻覺', 'style': GATE_STYLE},
    'N5': {'y': 4.4, 'title': '8. 做成 HTML 網頁', 'sub': '將文字、KaTeX 數學公式與莫蘭迪視覺樣式組裝成單檔網頁', 'style': AI_STYLE},
    'G3': {'y': 2.3, 'title': '9. 網頁有沒有問題？', 'sub': '實機檢查切頁順暢度、抽屜收合動畫與離線公式渲染', 'style': GATE_STYLE},
}

for k, v in nodes_p2.items():
    s = v['style']
    box = patches.FancyBboxPatch((-NODE_W/2, v['y'] - NODE_H/2), NODE_W, NODE_H,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=s['bg'], edgecolor=s['border'],
                                linewidth=2.2, zorder=3)
    ax.add_patch(box)
    ax.text(0, v['y'] + 0.2, v['title'], ha="center", va="center",
            fontsize=11.5, fontweight='bold', color=s['text'], zorder=4)
    ax.text(0, v['y'] - 0.1, v['sub'], ha="center", va="center",
            fontsize=9.0, color="#4B5563", zorder=4)
    dot = patches.Circle((-0.85, v['y'] - 0.38), radius=0.08, facecolor=s['badge_dot'], edgecolor='none', zorder=5)
    ax.add_patch(dot)
    ax.text(-0.68, v['y'] - 0.38, s['tag'], ha="left", va="center",
            fontsize=9.0, fontweight='bold', color=s['text'], zorder=4)

# Connector from 3 Parallel Cards down to Step 6
for i in range(3):
    cx = col_x[i]
    ax.annotate('', xy=(0, nodes_p2['N4']['y'] + NODE_H/2), xytext=(cx, fanout_y - col_h/2),
                arrowprops=dict(arrowstyle="-|>", color="#0284C7", lw=1.8, mutation_scale=12),
                zorder=2)

ax.text(0, 9.9, "各專屬簡報皆遵循以下高標準防呆流水線", ha="center", va="center",
        fontsize=9.2, fontweight='bold', color="#0369A1",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#E0F2FE", edgecolor="#38BDF8", lw=1.2), zorder=5)

# Downward flow Phase 2
draw_down_arrow(nodes_p2['N4']['y'] - NODE_H/2, nodes_p2['G2']['y'] + NODE_H/2)
draw_down_arrow(nodes_p2['G2']['y'] - NODE_H/2, nodes_p2['N5']['y'] + NODE_H/2, text="沒問題")
draw_down_arrow(nodes_p2['N5']['y'] - NODE_H/2, nodes_p2['G3']['y'] + NODE_H/2)

# Phase 2 Loops
# G2 -> N4 Loop (Left)
draw_loop_left(nodes_p2['G2']['y'], nodes_p2['N4']['y'], -3.2, "有寫錯 → 只重寫該頁")
# G3 -> N4 Loop (Right)
draw_loop_right(nodes_p2['G3']['y'], nodes_p2['N4']['y'], 3.2, "版面怪怪的 → 回去改內容", label_y=5.5)

# ==================== FAN-IN INTEGRATION & DELIVERY ====================
# Node 9b: Fan-In Mounting to index.html
hub_y = 0.2
hub_w = 4.4
hub_h = 1.25

draw_down_arrow(nodes_p2['G3']['y'] - NODE_H/2, hub_y + hub_h/2, text="完全正常：自動匯總扇入 (Fan-In)")

hub_box = patches.FancyBboxPatch((-hub_w/2, hub_y - hub_h/2), hub_w, hub_h,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#E0F2FE", edgecolor="#0284C7",
                                linewidth=2.2, zorder=3)
ax.add_patch(hub_box)
ax.text(0, hub_y + 0.2, "9b. 統整入口首頁自動掛載 (index.html)", ha="center", va="center",
        fontsize=11.5, fontweight='bold', color="#082F49", zorder=4)
ax.text(0, hub_y - 0.1, "自動掛載各論文卡片、原標題、真實摘要與雙軌導航", ha="center", va="center",
        fontsize=9.0, color="#4B5563", zorder=4)
dot_hub = patches.Circle((-0.85, hub_y - 0.38), radius=0.08, facecolor="#0284C7", edgecolor='none', zorder=5)
ax.add_patch(dot_hub)
ax.text(-0.68, hub_y - 0.38, "集成關卡", ha="left", va="center",
        fontsize=9.0, fontweight='bold', color="#082F49", zorder=4)

# Node 10: Final Delivery
deliv_y = -1.3
deliv_w = 4.4
deliv_h = 1.25

draw_down_arrow(hub_y - hub_h/2, deliv_y + deliv_h/2)

deliv_box = patches.FancyBboxPatch((-deliv_w/2, deliv_y - deliv_h/2), deliv_w, deliv_h,
                                  boxstyle="round,pad=0.1,rounding_size=0.2",
                                  facecolor="#DCFCE7", edgecolor="#16A34A",
                                  linewidth=2.2, zorder=3)
ax.add_patch(deliv_box)
ax.text(0, deliv_y + 0.2, "10. 完成交件！多元獨立簡報知識體系", ha="center", va="center",
        fontsize=11.5, fontweight='bold', color="#14532D", zorder=4)
ax.text(0, deliv_y - 0.1, "完美兼顧「入口首頁綜覽廣度」與「單篇 8 頁專屬研究深度」", ha="center", va="center",
        fontsize=9.0, color="#4B5563", zorder=4)
dot_deliv = patches.Circle((-0.85, deliv_y - 0.38), radius=0.08, facecolor="#16A34A", edgecolor='none', zorder=5)
ax.add_patch(dot_deliv)
ax.text(-0.68, deliv_y - 0.38, "交付成果", ha="left", va="center",
        fontsize=9.0, fontweight='bold', color="#14532D", zorder=4)

# Bottom Highlight Banner
ax.text(0, -3.4, "核心優勢：批次處理多文獻時，人類只需在「步驟 5 大綱總表」審核 1 次，其餘全自動分散並行與自檢！",
        ha="center", va="center", fontsize=9.8, fontweight='bold', color="#065F46",
        bbox=dict(boxstyle="round,pad=0.38", facecolor="#ECFDF5", edgecolor="#34D399", lw=1.5), zorder=6)

import shutil
import os

plt.tight_layout()
temp_path = r"C:\Users\User\.gemini\antigravity\brain\624ba022-64a6-42be-88e3-5e03a9d1315e\temp_flowchart.png"
dest_path = r"C:\Users\User\Desktop\作業十\workflow\vertical_flowchart.png"

buf = io.BytesIO()
plt.savefig(buf, format='png', dpi=200, bbox_inches='tight')
plt.close(fig)

with open(temp_path, 'wb') as f:
    f.write(buf.getvalue())

shutil.copyfile(temp_path, dest_path)
print("Successfully generated and updated ultimate combined vertical flowchart:", dest_path)
