# -*- coding: utf-8 -*-
"""
Refined vertical flowchart matching the user's diagram:
1. "3. 抓重點資訊" (updated)
2. Phase 2 banner moved to top-left to avoid arrow intersection with "各樣都 OK"
3. "9. 網頁有沒有問題" (updated)
4. Phase 2 container expanded downwards so Node 10 is comfortably enclosed.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Noto Sans TC', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10.8, 25), dpi=200)
ax.set_xlim(-5.4, 5.4)
ax.set_ylim(-2.7, 24.6)
ax.axis('off')

# Color palette matching original diagram
AI_STYLE = {'bg': '#EDE9FE', 'border': '#8B5CF6', 'text': '#3B0764', 'badge_dot': '#8B5CF6', 'tag': 'AI 節點'}
GATE_STYLE = {'bg': '#E0F2FE', 'border': '#0284C7', 'text': '#082F49', 'badge_dot': '#0284C7', 'tag': '檢查關卡'}
HUMAN_STYLE = {'bg': '#FFEDD5', 'border': '#EA580C', 'text': '#7C2D12', 'badge_dot': '#EA580C', 'tag': '人工確認'}
DELIV_STYLE = {'bg': '#DCFCE7', 'border': '#16A34A', 'text': '#14532D', 'badge_dot': '#16A34A', 'tag': '完成交付'}

# Phase 1 background (y: 11.2 to 24.0, height = 12.8)
p1_bg = patches.FancyBboxPatch((-4.7, 11.2), 9.4, 12.8,
                              boxstyle="round,pad=0.2,rounding_size=0.35",
                              facecolor="#FEFCE8", edgecolor="#DDD6FE", linewidth=2.5, zorder=1)
ax.add_patch(p1_bg)

# Phase 1 Title Badge (Top-Left aligned tab)
ax.text(-4.3, 23.2, "  第一階段：先搞清楚真的內容和大綱定好  ", ha="left", va="center",
        fontsize=13, fontweight='bold', color="#6B21A8",
        bbox=dict(boxstyle="round,pad=0.42", facecolor="#F3E8FF", edgecolor="#A855F7", lw=1.5), zorder=2)

# Phase 2 background (y: -2.2 to 10.2, height = 12.4, comfortably enclosing Node 10)
p2_bg = patches.FancyBboxPatch((-4.7, -2.2), 9.4, 12.4,
                              boxstyle="round,pad=0.2,rounding_size=0.35",
                              facecolor="#FEFCE8", edgecolor="#DDD6FE", linewidth=2.5, zorder=1)
ax.add_patch(p2_bg)

# Phase 2 Title Badge (Top-Left aligned tab, cleanly away from center arrow at x=0)
ax.text(-4.3, 9.4, "  第二階段：寫漂亮內容和做成網頁  ", ha="left", va="center",
        fontsize=13, fontweight='bold', color="#6B21A8",
        bbox=dict(boxstyle="round,pad=0.42", facecolor="#F3E8FF", edgecolor="#A855F7", lw=1.5), zorder=2)

# Node y-coordinates
nodes = {
    'N1': {'y': 21.6, 'title': '1. 找 Wiki 資料', 'style': AI_STYLE},
    'G1': {'y': 19.3, 'title': '2. 資料夠不夠？', 'style': GATE_STYLE},
    'N2': {'y': 17.0, 'title': '3. 抓重點資訊', 'style': AI_STYLE},
    'N3': {'y': 14.7, 'title': '4. 排簡報大綱', 'style': AI_STYLE},
    'H1': {'y': 12.4, 'title': '5. 我看過確認', 'style': HUMAN_STYLE},
    'N4': {'y': 7.8,  'title': '6. 寫每一頁內容', 'style': AI_STYLE},
    'G2': {'y': 5.5,  'title': '7. 有沒有漏掉？', 'style': GATE_STYLE},
    'N5': {'y': 3.2,  'title': '8. 做成 HTML 網頁', 'style': AI_STYLE},
    'G3': {'y': 0.9,  'title': '9. 網頁有沒有問題？', 'style': GATE_STYLE},
    'N6': {'y': -1.3, 'title': '10. 完成交件！', 'style': DELIV_STYLE},
}

NODE_W = 3.6
NODE_H = 1.15

# Draw Node Boxes
for k, v in nodes.items():
    s = v['style']
    box = patches.FancyBboxPatch((-NODE_W/2, v['y'] - NODE_H/2), NODE_W, NODE_H,
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=s['bg'], edgecolor=s['border'],
                                linewidth=2.2, zorder=3)
    ax.add_patch(box)
    
    # Title text
    ax.text(0, v['y'] + 0.16, v['title'], ha="center", va="center",
            fontsize=12, fontweight='bold', color=s['text'], zorder=4)
    
    # Small colored circle dot + tag text
    dot = patches.Circle((-0.7, v['y'] - 0.22), radius=0.09, facecolor=s['badge_dot'], edgecolor='none', zorder=5)
    ax.add_patch(dot)
    ax.text(-0.52, v['y'] - 0.22, s['tag'], ha="left", va="center",
            fontsize=10, fontweight='bold', color=s['text'], zorder=4)

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
draw_down_arrow(nodes['N1']['y'] - NODE_H/2, nodes['G1']['y'] + NODE_H/2)
draw_down_arrow(nodes['G1']['y'] - NODE_H/2, nodes['N2']['y'] + NODE_H/2, text="夠了，繼續")
draw_down_arrow(nodes['N2']['y'] - NODE_H/2, nodes['N3']['y'] + NODE_H/2)
draw_down_arrow(nodes['N3']['y'] - NODE_H/2, nodes['H1']['y'] + NODE_H/2)

# Inter-phase flow (5 -> 6): Connects H1 down to N4 cleanly through the gap
draw_down_arrow(nodes['H1']['y'] - NODE_H/2, nodes['N4']['y'] + NODE_H/2, text="各樣都 OK", text_y=10.5)

# Downward flow Phase 2
draw_down_arrow(nodes['N4']['y'] - NODE_H/2, nodes['G2']['y'] + NODE_H/2)
draw_down_arrow(nodes['G2']['y'] - NODE_H/2, nodes['N5']['y'] + NODE_H/2, text="沒問題")
draw_down_arrow(nodes['N5']['y'] - NODE_H/2, nodes['G3']['y'] + NODE_H/2)
draw_down_arrow(nodes['G3']['y'] - NODE_H/2, nodes['N6']['y'] + NODE_H/2, text="完全正常")

# Dashed loop return arrows
def draw_loop_left(y_from, y_to, x_turn, label, label_y=None):
    x_start = -NODE_W/2
    x_end = -NODE_W/2
    verts = [
        (x_start, y_from),
        (x_turn, y_from),
        (x_turn, y_to),
        (x_end, y_to)
    ]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='#DC2626', linestyle='--', linewidth=2.2, zorder=3)
    ax.add_patch(patch)
    ax.annotate('', xy=(x_end, y_to), xytext=(x_end - 0.25, y_to),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=2.2, mutation_scale=15),
                zorder=4)
    
    ly = label_y if label_y is not None else (y_from + y_to)/2
    ax.text(x_turn - 0.12, ly, label, ha="right", va="center",
            fontsize=9.2, fontweight='bold', color="#B91C1C",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#FEF2F2", edgecolor="#FCA5A5", lw=1.2),
            zorder=6)

def draw_loop_right(y_from, y_to, x_turn, label, label_y=None):
    x_start = NODE_W/2
    x_end = NODE_W/2
    verts = [
        (x_start, y_from),
        (x_turn, y_from),
        (x_turn, y_to),
        (x_end, y_to)
    ]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='#DC2626', linestyle='--', linewidth=2.2, zorder=3)
    ax.add_patch(patch)
    ax.annotate('', xy=(x_end, y_to), xytext=(x_end + 0.25, y_to),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=2.2, mutation_scale=15),
                zorder=4)
    
    ly = label_y if label_y is not None else (y_from + y_to)/2
    ax.text(x_turn + 0.12, ly, label, ha="left", va="center",
            fontsize=9.2, fontweight='bold', color="#B91C1C",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#FEF2F2", edgecolor="#FCA5A5", lw=1.2),
            zorder=6)

# 1. G1 -> N1: 不夠 → 停下來補找 (Left)
draw_loop_left(nodes['G1']['y'], nodes['N1']['y'], -2.9, "不夠 → 停下來補找")

# 2. H1 -> N3: 不滿意 → 重排大綱 (Right)
draw_loop_right(nodes['H1']['y'], nodes['N3']['y'], 2.9, "不滿意 → 重排大綱")

# 3. H1 -> N1: 不滿意 → 重新找資料 (Far Right)
draw_loop_right(nodes['H1']['y'], nodes['N1']['y'], 4.0, "不滿意 → 重新找資料", label_y=17.5)

# 4. G2 -> N4: 有寫錯 → 只重寫那一頁 (Left)
draw_loop_left(nodes['G2']['y'], nodes['N4']['y'], -2.9, "有寫錯 → 只重寫那一頁")

# 5. G3 -> N4: 版面怪怪的 → 回去改內容 (Right)
draw_loop_right(nodes['G3']['y'], nodes['N4']['y'], 3.2, "版面怪怪的 → 回去改內容", label_y=4.5)

import io

plt.tight_layout()
output_path = "C:/Users/User/Desktop/作業十/workflow/vertical_flowchart.png"
buf = io.BytesIO()
plt.savefig(buf, format='png', dpi=200, bbox_inches='tight')
plt.close(fig)

with open(output_path, 'wb') as f:
    f.write(buf.getvalue())
print("Successfully regenerated vertical flowchart:", output_path)
