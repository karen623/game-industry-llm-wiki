# 一次實際執行：補討論 5 篇資料（流程 A：建 wiki）

- 日期：2026-11-10
- 範圍：第二批 ingest 的 5 份資料。第一次 ingest 時是一次做完，跳過了「先討論」。
- 流程：照 [workflows/wiki-workflow.md](../workflows/wiki-workflow.md) 的 D1 → G → K 走一次
- 自動檢查工具：`python3 scripts/check_wiki.py`

## D1 討論重點（AI 報告 → 使用者決定強調什麼）
使用者這次指示「直接開始做」（符合 `CLAUDE.md` 3.1 第 2 步的例外），所以強調哪些重點由 AI 依 `requirements.md` 決定。
選擇原則有兩個：和「怎麼寫 prompt」直接相關的優先；和作業要求（先討論、後生成、檢查流程）有關的優先。

| 來源 | AI 報告的重點（3–5 個） | 決定強調 | 對照 wiki 後發現的缺口 | 修改 |
|---|---|---|---|---|
| Karpathy — LLM Wiki | ① RAG 知識不累積 ② 三層三操作 ③ ingest 時先討論、作者偏好一次一份 ④ query 的輸出可以是投影片 ⑤ lint 不保證事實 | ③④：直接對應作業的「先討論、後生成」和 HTML 簡報 | `llm-wiki` 頁沒有寫 ③④ | `concepts/llm-wiki` 加入兩點 |
| Schulhoff — The Prompt Report | ① 術語混亂 ② 33 術語、58 技巧、40 其他模態 ③ 最佳實務 ④ 前綴提示統合分析 | ①②：說明領域範圍 | 無（已收錄） | 無 |
| Wang — Self-Consistency | ① 取代貪婪解碼 ② 多條推理取最一致 ③ GSM8K +17.9% 等 ④ 單位未說明 | ②④：避免誤用數字 | `self-consistency` 技巧頁的效果表**沒有**標註「單位未說明」，只有來源頁有 | 技巧頁加入註記 |
| Yao — ReAct | ① 推理與行動交錯 ② HotpotQA／FEVER 用 Wikipedia API ③ ALFWorld +34%、WebShop +10% ④ 減少幻覺 ⑤ 軌跡較好解讀 | ④⑤：可靠性 | `react` 頁沒有 ② 的任務名稱，也沒有 ⑤ | `techniques/react` 加入兩點 |
| OpenAI — Prompt engineering | ① 推理模型 vs GPT 模型 ② 固定版本＋評測 ③ developer／user 權限 ④ 四段結構 ⑤ prompt caching | ①：資深／資淺同事的比喻 | 無（都已收錄） | 無 |

## G 生成（修改的頁面）
- `wiki/concepts/llm-wiki.md`：加入「先討論重點、一次一份」與「query 輸出可以是投影片」
- `wiki/techniques/self-consistency.md`：效果表加上「百分點或相對提升未說明」
- `wiki/techniques/react.md`：加入 HotpotQA／FEVER，以及「軌跡較好解讀」
- `wiki/techniques/zero-shot-cot.md`、`wiki/concepts/extended-thinking.md`：補上連到問答頁的連結（K 檢查發現，見下）

## K 自動檢查（`scripts/check_wiki.py`）
| 輪次 | 結果 | 發現 | 處理 |
|---|---|---|---|
| 第 1 輪 | ❌ 1 項不通過 | **孤兒頁**：`2026-do-we-still-need-step-by-step` 沒有任何頁面連入（之前的檢查把 index 的連結也算進去，所以沒抓到） | 從 `zero-shot-cot`、`extended-thinking` 連過去 |
| 第 2 輪 | ✅ 7／7 通過 | — | — |

第 2 輪結果（摘錄）：
- 每頁都有完整 frontmatter，type 與資料夾一致 ✅（29 頁）
- 非來源頁都有 sources ✅；每頁至少連出 2 個頁面 ✅；沒有孤兒頁 ✅
- 斷掉的連結只能是規劃中的主題 ✅；每頁都列在 index ✅
- index 宣稱的頁數＝實際頁數 ✅（30＝技巧 10＋概念 6＋來源 8＋模型 2＋比較 2＋問答 1＋總覽 1）
- 統計：30 頁、29 節點、109 條連結、標註（推論）10 處

## 這次執行學到的事
- **只看摘要頁不夠**：Self-Consistency 的「單位未說明」只寫在來源頁，技巧頁引用數字時卻沒有帶過去。數字從來源頁搬到其他頁時，附註也要跟著搬。
- **檢查的定義要寫清楚**：「孤兒頁」如果把 index 的連結也算進去，就永遠抓不到。改用程式檢查之後，定義固定下來，才發現這個問題。
- 這兩點都寫進了 [反思](reflection.md)。
