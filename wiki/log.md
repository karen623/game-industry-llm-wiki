# 操作紀錄（log）

> 只往下追加，不修改舊紀錄。每筆格式：
>
> ```
> ## [YYYY-MM-DD] 動作 | 對象
> - 操作者：組員名字＋AI
> - 新增頁面：...
> - 修改頁面：...
> - 備註：...
> ```
> 動作 = `init` / `ingest` / `query` / `lint`

## [2026-11-10] init | 建立 wiki 骨架
- 操作者：苡瑄＋Claude Code
- 新增頁面：index、log、overview
- 備註：建立 raw/ 與 wiki/ 資料夾結構、CLAUDE.md schema、sources.md 素材清單。

## [2026-11-10] ingest | Wei et al. 2022（CoT）、Kojima et al. 2022（Zero-shot CoT）、Anthropic Prompting best practices
- 操作者：苡瑄＋Claude Code（demo）
- 新增頁面：sources/2022-wei-cot-paper、sources/2022-kojima-zero-shot-cot、sources/anthropic-prompting-best-practices、
  techniques/chain-of-thought、zero-shot-cot、few-shot-prompting、zero-shot-prompting、xml-tags、be-clear-and-direct、
  role-prompting、self-check、concepts/emergent-abilities、extended-thinking、models/claude、
  comparisons/few-shot-cot-vs-zero-shot-cot
- 修改頁面：index、overview
- 備註：在 chain-of-thought 頁記錄「2022 論文 vs 2026 官方指南」的不同說法，結論是模型世代不同，兩者不算矛盾。
  emergent-abilities 中「多大算夠大」尚待其他來源補充。

## [2026-11-10] query | 2026 年還需要寫 "Let's think step by step" 嗎？
- 操作者：苡瑄＋Claude Code（demo）
- 新增頁面：queries/2026-do-we-still-need-step-by-step
- 修改頁面：index

## [2026-11-10] export | HTML 簡報
- 操作者：苡瑄＋Claude Code
- 產出：`slides/prompt-engineering-wiki.html`（13 頁，內容取自 wiki 現有頁面；知識圖譜依頁面間的 `[[連結]]` 自動產生，16 個節點、51 條連結）
- 修改頁面：無（wiki 內容沒有變動）

## [2026-11-10] ingest | Karpathy LLM Wiki、The Prompt Report、Self-Consistency、ReAct、OpenAI Prompt engineering
- 操作者：苡瑄＋Claude Code（組員要求一次 ingest 5 份，略過逐份確認重點）
- 新增頁面：sources/2026-karpathy-llm-wiki、sources/2024-schulhoff-prompt-report、sources/2022-wang-self-consistency、
  sources/2022-yao-react、sources/openai-prompt-engineering-guide、techniques/self-consistency、techniques/react、
  concepts/llm-wiki、concepts/rag、concepts/hallucination、concepts/evals、models/gpt、comparisons/anthropic-vs-openai-guides
- 修改頁面：chain-of-thought（演進表加入 Self-Consistency、ReAct；不同說法加入 OpenAI 觀點）、extended-thinking（加入 OpenAI 推理模型）、
  xml-tags（OpenAI 四段結構）、few-shot-prompting、role-prompting（developer／user 權限）、be-clear-and-direct、self-check、
  claude、emergent-abilities、index、overview（改寫為三條故事線＋主題地圖）
- 備註：兩家官方指南沒有互相矛盾，整理成比較頁。四篇論文都只讀了 arXiv 摘要；Self-Consistency 的提升數字，摘要沒有說明是百分點還是相對提升，已在頁面註明。
  hallucination 的成因與量測、Prompt Report 的 58 種技巧清單仍待補。

## [2026-11-10] export | HTML 簡報 v2（graph 流程）
- 操作者：苡瑄＋Claude Code
- 產出：`slides/prompt-engineering-wiki-v2.html`（16 頁，含講稿；知識圖譜 29 個節點、109 條連結）；v1 保留不刪
- 流程：依 `slides/pipeline/README.md` 的 6 個階段產生，中間產出都在 `slides/pipeline/`
  （00 快照 → 01 大綱 v0.2 → 02 逐頁內容 v0.1 → 03 HTML → 04 審閱）；C1、C2、C4 都經組員確認，C3 自動修正 2 輪後通過
- 修改頁面：無（wiki 內容沒有變動；只更正 `00-snapshot.md` 的頁面分類計數）

## [2026-11-10] schema | CLAUDE.md 改為個人作業用語
- 操作者：苡瑄＋Claude Code（經使用者同意修改 schema）
- 修改：`CLAUDE.md` 的「組員」全部改為「使用者」（6 處）；用途說明刪除組上專案，改為「個人作業，要求見 requirements.md」
- 同時新增：`requirements.md`（需求摘要，R0 關卡）、`AGENTS.md`（指向 CLAUDE.md）；`sources.md` 刪除 5 人分工表
- 修改頁面：無（wiki 內容沒有變動）

## [2026-11-10] ingest | 補討論第二批 5 份資料（先討論、後生成）
- 操作者：苡瑄＋Claude Code（使用者指示「直接開始做」，強調重點由 AI 依 requirements.md 決定）
- 新增頁面：無
- 修改頁面：llm-wiki（先討論、一次一份；query 可輸出投影片）、self-consistency（數字單位未說明）、react（HotpotQA／FEVER、軌跡可解讀）、
  zero-shot-cot、extended-thinking（連到問答頁，修正孤兒頁）
- 檢查：新增 scripts/check_wiki.py；第 1 輪抓到孤兒頁，第 2 輪 7／7 通過。完整紀錄見 reports/ingest-run-2026-11-10.md

## [2026-11-10] export | HTML 簡報 v3（依需求摘要重做）
- 操作者：苡瑄＋Claude Code（使用者指示「直接開始做」，人工關卡改為記錄）
- 產出：`slides/prompt-engineering-wiki-v3.html`（14 頁，照作業結構：建 Wiki → 繳交 → 反思）；中間產出在 `slides/pipeline/v3/`
- 同時新增：workflows/wiki-workflow.md（流程圖 A）、reports/check-report.md、reports/reflection.md；流程 B 升到 v0.2（加入 R0 需求關卡）
- 修改頁面：無

## [2026-11-10] schema | 換主題：Prompt Engineering → 電子遊戲產業追蹤（任天堂為主）
- 操作者：苡瑄＋Claude Code（使用者決定換主題、刪除舊內容）
- 刪除：舊主題的 raw 筆記 8 份、wiki 頁面 29 頁、簡報 v1–v3 與 v2/v3 的流程中間檔（保留在 git commit 8adbb77）
- 修改：CLAUDE.md（主題、資料夾改為 companies／platforms／franchises、新增數字規則 2.3.1）、scripts/check_wiki.py、requirements.md、sources.md
- 保留：本 log 的舊紀錄（依規則不刪）、流程圖 A／B、reports/（舊主題的執行紀錄，作為流程的歷史）
- 新增 raw 筆記 5 份（尚未 ingest，等待 D1 討論）

## [2026-11-10] ingest | 任天堂上半年財報、任天堂 IR 銷量、Sony FY2026 Q2、Microsoft FY27 Q1、Newzoo 2026 預測
- 操作者：苡瑄＋Claude Code（D1：5 篇一次報告，使用者確認後生成）
- 新增頁面：sources/ 5 頁；companies/nintendo、sony、microsoft-gaming；platforms/switch-2、switch、ps5、xbox-series；
  franchises/mario-kart、pokemon；concepts/fiscal-year、installed-base、digital-sales、console-lifecycle；
  comparisons/big-three-consoles；queries/2026-why-nintendo-profit-up；overview、index 重寫
- 檢查：check_wiki.py 新增第 8 項「數字可追溯到 raw」；第 1 輪誤報 10 個（單位寫法不同），修正後 8／8 通過
- 備註：PS5 台數、Xbox 硬體 −14% 為非官方；PS5 Q2 台數有 2.6M／3.3M 兩種說法，已並列。詳見 reports/ingest-run-game-industry-2026-11-10.md

## [2026-11-10] export | HTML 簡報 v4（新主題：電子遊戲產業）
- 操作者：苡瑄＋Claude Code（沿用「直接做」，人工關卡改為記錄）
- 產出：`slides/game-industry-wiki.html`（14 頁；知識圖譜 20 節點、76 條連結）；中間產出在 `slides/pipeline/v4/`
- 同時更新：reports/reflection.md（錯誤次數與新主題的教訓）、reports/check-report.md、requirements.md、README.md
- 修改頁面：無

## [2026-11-10] export | 簡報新增第 7 頁（15 頁）
- 操作者：苡瑄＋Claude Code（使用者要求）
- 修改：`slides/game-industry-wiki.html` 新增「下一季財報進來，wiki 會怎樣？」，說明簡報和 wiki 的關係；依流程 B 的 C4 分流當作故事線問題退回階段 1
- 修改頁面：無
