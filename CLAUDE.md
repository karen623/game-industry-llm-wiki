# CLAUDE.md — Prompt Engineering LLM Wiki（schema）

這份檔案是這個 wiki 的「憲法」。任何 AI 助理（Claude Code 等）在這個資料夾裡工作前
**一定要先讀完這份**，並嚴格照這裡的結構與流程維護 wiki。

> 作法參考 Andrej Karpathy 的 LLM Wiki：不是每次提問才去翻原始文件（傳統 RAG），
> 而是由 LLM **持續編寫、維護一份互相連結的 Markdown wiki**，知識會隨每次 ingest 累積。

- 主題：**Prompt Engineering（提示工程）**——技巧、原理、模型差異、實際應用與失敗案例。
- 用途：生成式 AI 課程的**個人作業**。作業要求與驗收標準見 `requirements.md`。
- 語言：wiki 頁面一律用**繁體中文**撰寫；專有名詞第一次出現時附英文原文，
  例如「思維鏈（Chain-of-Thought, CoT）」。原始資料可以是英文。

---

## 1. 三層結構

```
GenAI_LLM_Wiki/
├── CLAUDE.md          ← 本檔：schema 與工作流程（人改，AI 不擅自改）
├── raw/               ← 第 1 層：原始資料，唯讀，AI 不可修改或刪除
│   ├── articles/      網路文章、部落格（存成 .md）
│   ├── papers/        論文（PDF 或 .md 摘錄）
│   ├── guides/        官方文件／指南（Anthropic、OpenAI、Google 等）
│   ├── transcripts/   影片、演講、Podcast 逐字稿
│   └── assets/        圖片等附件
├── wiki/              ← 第 2 層：由 AI 撰寫與維護
│   ├── index.md       總目錄（每次 ingest 都要更新）
│   ├── log.md         操作紀錄（只往下追加，不改舊紀錄）
│   ├── overview.md    整個領域的總覽／地圖
│   ├── sources/       每份原始資料一頁摘要
│   ├── concepts/      概念頁（例：幻覺、Context Window、In-context Learning）
│   ├── techniques/    技巧頁（例：Few-shot、CoT、ReAct、Role Prompting）
│   ├── models/        模型／廠商頁（例：Claude、GPT、Gemini 的提示差異）
│   ├── comparisons/   比較頁（例：Zero-shot vs Few-shot）
│   └── queries/       值得保存的問答結果
└── sources.md         待蒐集／已蒐集素材清單（人和 AI 都可以更新）
```

## 2. 頁面格式

### 2.1 檔名

- 全小寫英文、以 `-` 連接：`chain-of-thought.md`、`few-shot-prompting.md`。
- 來源摘要頁：`sources/<年份>-<簡短名稱>.md`，例：`sources/2022-wei-cot-paper.md`。

### 2.2 每頁開頭的 frontmatter

```yaml
---
title: 思維鏈（Chain-of-Thought, CoT）
type: technique        # concept | technique | model | comparison | source | query
tags: [reasoning, prompting-basics]
sources: [2022-wei-cot-paper, anthropic-prompt-guide]   # 對應 wiki/sources/ 的檔名
updated: 2026-11-10
---
```

### 2.3 技巧頁（techniques/）建議段落

1. **一句話定義**
2. **怎麼用**：步驟＋最小範例 prompt（用 code block）
3. **為什麼有效**：背後原理
4. **適用／不適用情境**
5. **常見錯誤**
6. **相關頁面**：`[[...]]` 連結
7. **來源**：列出引用的 source 頁

概念頁、模型頁可以比照調整，但「定義」「相關頁面」「來源」三段必須有。

### 2.4 連結規則

- 頁面之間用 wiki 連結：`[[chain-of-thought]]`（不寫副檔名、不寫資料夾）。
- 每個新頁面**至少連出 2 個**相關頁面，也要回頭在相關頁面加上連回來的連結。
- 提到還沒建立的概念也可以先寫 `[[xxx]]`，lint 時再決定要不要建頁。

### 2.5 引用與可信度

- 每個重要論點都要能追溯到 `sources/` 裡的某一頁，寫成：`（來源：[[2022-wei-cot-paper]]）`。
- 不同來源說法衝突時，**不要自己選邊**，在頁面中加一段「⚠️ 不同說法」並列出各來源。
- 沒有來源支持的推論要標註「（推論）」。

## 3. 工作流程

### 3.1 Ingest（加入一份新資料）

觸發：使用者說「ingest raw/xxx」或「把這份資料加進 wiki」。

1. 完整讀過原始資料。
2. 先跟使用者簡短報告 3–5 個重點，確認要強調什麼（使用者說「直接做」就跳過）。
3. 在 `wiki/sources/` 建立這份資料的摘要頁。
4. 找出它涉及的概念／技巧／模型：
   - 已有頁面 → 補充新資訊、加上來源；有衝突就照 2.5 處理。
   - 沒有頁面 → 新建。
   一次 ingest 通常會動到 5–15 個頁面，這是正常的。
5. 更新 `wiki/index.md`、必要時更新 `wiki/overview.md`。
6. 在 `wiki/log.md` 最下方追加一筆紀錄（格式見 log.md）。
7. 在 `sources.md` 把該素材標成已 ingest。

### 3.2 Query（向 wiki 提問）

1. 先讀 `wiki/index.md` 找到相關頁面，再讀這些頁面回答；**不要直接去翻 raw/**，
   除非 wiki 內容不足（此時要說明「wiki 沒有涵蓋，以下參考原始資料」）。
2. 回答要附上引用的 wiki 頁面連結。
3. 如果答案有保存價值（比較、整理、教學範例），詢問使用者後存到 `wiki/queries/`，
   並更新 index 和 log。

### 3.3 Lint（健康檢查）

觸發：使用者說「lint wiki」。檢查並回報（先報告，經同意再修）：

- 沒有任何頁面連入的孤兒頁
- 被提到很多次、卻還沒有自己頁面的 `[[概念]]`
- 頁面之間互相矛盾的說法
- 缺少來源或 frontmatter 的頁面
- 可能已過時的資訊（例如舊模型的限制）
- 建議接下來要蒐集的新素材（寫進 `sources.md`）

## 4. 禁止事項

- 不可修改、刪除、搬移 `raw/` 裡的任何檔案。
- 不可編造來源、論文、作者或數據；不確定就說不確定。
- 不可大段複製原文（受著作權保護），用自己的話摘要，引用原句一次不超過一兩句。
- 不可刪除 `log.md` 的舊紀錄。
- 不可在沒有告知使用者的情況下改這份 `CLAUDE.md`；要改 schema 先提議。
