"""wiki 健康檢查（C0 / K 檢查）。用法：python3 scripts/check_wiki.py

只讀 wiki/，不修改任何檔案。輸出 Markdown 報告到標準輸出；有不通過的項目時結束碼為 1。
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wiki")
FOLDERS = {"sources": "source", "companies": "company", "platforms": "platform",
           "franchises": "franchise", "concepts": "concept", "comparisons": "comparison",
           "queries": "query"}
REQUIRED = ["title", "type", "tags", "sources", "updated"]
LINK = re.compile(r"\[\[([^\]|#]+)")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.split("#")[0].strip()
    return fm


pages = {}
for folder, typ in FOLDERS.items():
    for f in sorted(glob.glob(os.path.join(ROOT, folder, "*.md"))):
        pages[os.path.basename(f)[:-3]] = (folder, typ, open(f, encoding="utf-8").read())
overview = open(os.path.join(ROOT, "overview.md"), encoding="utf-8").read()
index = open(os.path.join(ROOT, "index.md"), encoding="utf-8").read()

results = []  # (check, ok, detail)

# 1 frontmatter
bad = []
for p, (folder, typ, t) in pages.items():
    fm = frontmatter(t)
    if fm is None or any(k not in fm for k in REQUIRED):
        bad.append(p)
    elif fm["type"] != typ:
        bad.append(f"{p}（type 寫 {fm['type']}，資料夾是 {folder}）")
results.append(("每頁都有完整 frontmatter，type 與資料夾一致", not bad, "、".join(bad) or f"{len(pages)} 頁"))

# 2 sources field
bad = []
for p, (folder, typ, t) in pages.items():
    if typ == "source":
        continue
    srcs = [s.strip() for s in (frontmatter(t) or {}).get("sources", "").strip("[]").split(",") if s.strip()]
    if not srcs or any(s not in pages or pages[s][1] != "source" for s in srcs):
        bad.append(p)
results.append(("非來源頁都有 sources，且都指向存在的來源頁", not bad, "、".join(bad) or "OK"))

# 3 out-links >= 2, orphans, broken links
out = {p: {l.strip() for l in LINK.findall(t)} - {p} for p, (_, _, t) in pages.items()}
few = [p for p, ls in out.items() if len([l for l in ls if l in pages]) < 2]
results.append(("每頁至少連出 2 個頁面", not few, "、".join(few) or "OK"))
inbound = {p: 0 for p in pages}
for p, ls in out.items():
    for l in ls:
        if l in inbound:
            inbound[l] += 1
orph = [p for p, n in inbound.items() if n == 0 and p not in LINK.findall(overview)]
results.append(("沒有孤兒頁", not orph, "、".join(orph) or "OK"))
broken = sorted({l for ls in out.values() for l in ls if l not in pages and l != "overview"})
planned = set(re.findall(r"☐\s*\[\[([^\]]+)\]\]", overview))
unplanned = [b for b in broken if b not in planned]
results.append(("斷掉的連結只能是總覽裡 ☐ 規劃中的主題", not unplanned,
                "、".join(unplanned) if unplanned else f"斷連結 {len(broken)} 個，皆為規劃中"))

# 4 index
missing = [p for p in pages if f"[[{p}]]" not in index]
results.append(("每頁都列在 index.md", not missing, "、".join(missing) or "OK"))

# 5 counts consistency (added after the 00-snapshot miscount)
by_type = {}
for _, typ, _ in pages.values():
    by_type[typ] = by_type.get(typ, 0) + 1
total = len(pages) + 1  # + overview
m = re.search(r"(\d+)\s*個頁面", index)
claimed = int(m.group(1)) if m else None
results.append(("index 宣稱的頁數＝實際頁數（分類加總＋總覽）", claimed == total,
                f"index 寫 {claimed}，實際 {total}（" + "、".join(f"{k} {v}" for k, v in sorted(by_type.items())) + "＋總覽 1）"))

# 6 numbers traceable to raw (added for the game-industry topic)
raw_text = ""
for f in glob.glob(os.path.join(ROOT, "..", "raw", "**", "*.md"), recursive=True):
    raw_text += open(f, encoding="utf-8").read()
raw_norm = raw_text.replace(",", "")
NUM = re.compile(r"[+−-]?\d[\d,]*\.?\d*(?:%|M)")
untraced = []
for p, (_, _, t) in pages.items():
    body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
    for line in body.splitlines():
        if "計算" in line or "推論" in line:
            continue
        for n in NUM.findall(line):
            core = n.lstrip("+−-").replace(",", "").rstrip("M")  # raw 寫「6.49 百萬台」，wiki 寫 6.49M
            if core not in raw_norm:
                untraced.append(f"{p}: {n}")
results.append(("數字都能在 raw 筆記找到（計算值要標「計算」）", not untraced,
                "、".join(untraced[:10]) or "OK"))

# stats
edges = {tuple(sorted((a, b))) for a, ls in out.items() for b in ls if b in pages}
deg = {p: 0 for p in pages}
for a, b in edges:
    deg[a] += 1
    deg[b] += 1
top = sorted(deg.items(), key=lambda x: -x[1])[:4]
inf = sum(t.count("（推論）") for _, _, t in pages.values())

print("## wiki 健康檢查結果\n")
print("| 檢查 | 結果 | 說明 |\n|---|---|---|")
for name, ok, detail in results:
    print(f"| {name} | {'✅' if ok else '❌'} | {detail} |")
print(f"\n- 頁面 {total}（含總覽）、圖譜 {len(pages)} 節點 {len(edges)} 條連結、標註（推論）{inf} 處")
print("- 連結最多：" + "、".join(f"{p}（{d}）" for p, d in top))
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
