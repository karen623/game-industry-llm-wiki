# Prompt Engineering LLM Wiki

生成式 AI 課程專案：參考 Karpathy 的 LLM Wiki 作法，由 AI 持續維護的 Prompt Engineering 知識庫。

- **規則與流程**：[CLAUDE.md](CLAUDE.md)（AI 和人都先讀這份）
- **素材清單與分工**：[sources.md](sources.md)
- **wiki 入口**：[wiki/index.md](wiki/index.md)、[wiki/overview.md](wiki/overview.md)
- **作業繳交物**
  - 需求摘要：[requirements.md](requirements.md)
  - AGENTS.md：[AGENTS.md](AGENTS.md)（指向 [CLAUDE.md](CLAUDE.md)）
  - 流程圖 A（建 wiki）：[workflows/wiki-workflow.md](workflows/wiki-workflow.md)；流程圖 B（做簡報）：[slides/pipeline/README.md](slides/pipeline/README.md)
  - 檢查報告：[reports/check-report.md](reports/check-report.md)；一次實際執行：[reports/ingest-run-2026-11-10.md](reports/ingest-run-2026-11-10.md)
  - 反思：[reports/reflection.md](reports/reflection.md)
- **展示簡報 v3（繳交版）**：[slides/prompt-engineering-wiki-v3.html](slides/prompt-engineering-wiki-v3.html)（用瀏覽器開啟；← → 換頁、F 全螢幕、N 顯示講稿）
  - 舊版：[v2](slides/prompt-engineering-wiki-v2.html)、[v1](slides/prompt-engineering-wiki.html)
- **wiki 健康檢查**：`python3 scripts/check_wiki.py`

## 怎麼用

1. 把素材存進 `raw/` 對應的資料夾。
2. 在這個資料夾開啟 Claude Code，說：
   - `ingest raw/papers/2022-wei-cot.pdf` → 加入一份新資料，AI 會更新相關頁面
   - `根據 wiki，Few-shot 和 CoT 可以一起用嗎？` → 向 wiki 提問
   - `lint wiki` → 健康檢查
3. 推薦用 [Obsidian](https://obsidian.md) 開啟這個資料夾瀏覽，`[[連結]]` 可以直接點，
   Graph View 可以看到知識圖譜（展示時很好用）。
