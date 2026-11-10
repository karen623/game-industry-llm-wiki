# 01 大綱（階段 1 產出）

- 版本：**v0.2 ✅ 已確認（C1 通過，2026-11-10）**：保留全部 16 頁
- 依據：`00-snapshot.md` v2（8 份資料、30 頁、109 條連結）
- 預設條件（⚠️ 待你確認）：課堂報告、聽眾是同學和老師、約 15 分鐘 → 16 頁（時間不夠時可刪的頁面標 ✂️）

## 故事線
**問題**（為什麼需要 LLM Wiki）→ **方法**（怎麼建 wiki、怎麼做簡報）→ **成果**（wiki 裡學到什麼，沿著總覽的三條故事線：推理演進、指南共識、可靠性）→ **反思**（缺口與下一步）

## 逐頁大綱

| # | 段落 | 標題 | 一句話重點 | 引用 |
|---|---|---|---|---|
| 1 | 開場 | 用 LLM Wiki 打造 Prompt Engineering 知識庫 | 讓 AI 持續整理一份會成長的知識庫 | — |
| 2 | 問題 | 為什麼不只用 RAG？ | RAG 每次都重新找；wiki 把整理好的結果留下來、越用越完整 | llm-wiki、rag、2026-karpathy-llm-wiki |
| 3 | 方法 | 三層結構 × 三種操作 | raw → wiki ← schema；ingest、query、lint 讓 wiki 持續變好 | llm-wiki、CLAUDE.md |
| 4 | 方法 | 知識會累積：兩次 ingest 的變化 | 3 → 8 份資料，17 → 30 頁，51 → 109 條連結 | 00-snapshot、log、index |
| 5 | 方法 | 簡報也用 graph 流程產生 | 6 個階段＋5 道檢查關卡，不通過就退回 | slides/pipeline/README.md |
| 6 | 成果 | 知識圖譜 | 思維鏈（20 條連結）是整張網的中心 | 00-snapshot（圖譜資料） |
| 7 ✂️ | 成果 | 這個領域有多大？ | The Prompt Report 整理出 58 種技巧、33 個術語 | 2024-schulhoff-prompt-report、overview |
| 8 | 成果·推理演進 | 思維鏈的演進時間軸 | 手寫範例 → 多數決 → 一句觸發語 → 推理＋行動 → 模型內建思考 | chain-of-thought、2022-wei-cot-paper、self-consistency、zero-shot-cot、react、extended-thinking |
| 9 | 成果·推理演進 | 數字會說話 | 一句「Let's think step by step」讓 GSM8K 10.4% → 40.7%；多數決再 +17.9% | zero-shot-cot、self-consistency |
| 10 | 成果·推理演進 | 來源說法不同時 | wiki 並列不同說法，不選邊；差異來自模型世代不同 | chain-of-thought |
| 11 | 成果·指南共識 | Anthropic vs OpenAI 官方指南 | 兩家沒有矛盾，共同核心是「依模型能力調整寫法」 | anthropic-vs-openai-guides、claude、gpt |
| 12 | 成果·指南共識 | 兩家都推薦的實用技巧 | 清楚直接、給範例、用標籤分段、設定角色 | be-clear-and-direct、few-shot-prompting、xml-tags、role-prompting |
| 13 | 成果·可靠性 | 怎麼讓答案更可靠 | ReAct 查資料減少幻覺、自我檢查、用 evals 驗證 | react、hallucination、self-check、evals |
| 14 ✂️ | 成果 | Query 也會存回 wiki | 「還需要 step by step 嗎？」答案：看模型有沒有內建思考 | 2026-do-we-still-need-step-by-step |
| 15 | 反思 | Lint 找到的缺口 | 5 個主題還沒有頁面；論文只讀了摘要；下一批素材 | 00-snapshot、sources.md |
| 16 | 結尾 | 知識會累積的 AI 筆記 | 累積、可追溯、會自我檢查 | — |

## 跟 v0.1 的差別
- **第 2、3 頁**：Karpathy 原文已 ingest，改引用正式來源 `2026-karpathy-llm-wiki`、`llm-wiki`、`rag`。
- **第 4 頁**：改成「兩次 ingest 的前後對比」，直接展示知識累積。
- **新增第 7 頁**（Prompt Report，58 種技巧）、**第 11 頁**（兩家指南的共識）、**第 13 頁**（可靠性：ReAct／幻覺／evals）。
- **第 8 頁**時間軸從 3 個節點擴充成 5 個（加入 Self-Consistency、ReAct）。
- **第 9 頁**加入 Self-Consistency 的數字。
- **刪除** v0.1 第 10 頁「Few-shot CoT vs Zero-shot CoT」：結論「先試 zero-shot，不夠再加範例」併入第 12 頁講稿。
- 第 15 頁「Lint 缺口」從 8 個規劃主題減少為 5 個。

## C1 自動檢查結果
| 檢查 | 結果 |
|---|---|
| 每頁都有一句話重點 | ✅ 16／16 |
| 每頁至少引用 1 個 wiki 頁面（封面、結尾除外） | ✅ 14／14；所有引用的頁面都存在 |
| 頁數符合時間 | ⚠️ 16 頁約 16 分鐘；刪掉 ✂️ 兩頁約 14 分鐘。**要看實際報告時間** |
| 段落順序 問題 → 方法 → 成果 → 反思 | ✅ |
| 作業要求的項目都有對應頁面 | ⚠️ **還不知道作業要求** |
| 大綱裡的數字都能在 wiki 找到 | ✅ 10.4%→40.7%（zero-shot-cot）、+17.9%（self-consistency）、58／33（schulhoff）、20 條連結與 3→8、17→30、51→109（00-snapshot） |

## 等你確認的問題
1. 報告時間多長？有沒有頁數限制？
2. 老師有沒有規定一定要包含的項目（例如：動機、方法、成果、分工、心得）？
3. 要不要保留第 5 頁「簡報也用 graph 流程產生」？
4. 標 ✂️ 的第 7、14 頁要留還是刪？
5. 還有沒有想新增或刪除的頁面？

## 修改紀錄
- v0.2 確認（2026-11-10）：組員確認，16 頁全部保留（含 ✂️ 第 7、14 頁）。
- v0.2（2026-11-10）：wiki 更新到快照 v2（8 份資料），依新內容重做。改動見「跟 v0.1 的差別」。
- v0.1（2026-11-10）：初稿（依快照 v1）。已過期。
