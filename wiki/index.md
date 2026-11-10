# Prompt Engineering Wiki — 總目錄

> 由 AI 維護。每次 ingest 後更新。格式：`- [[頁面]] — 一句話說明`
> 起點請看 [[overview]]；操作紀錄見 [[log]]。
> 目前：8 份來源、30 個頁面（含總覽；最後更新 2026-11-10）

## 概念（concepts）
- [[llm-wiki]] — 由 LLM 維護、會累積的知識庫（本 wiki 的方法）
- [[rag]] — 提問時檢索資料放進 prompt；知識不累積
- [[hallucination]] — 看似合理但沒根據的內容；目前收錄的對策
- [[extended-thinking]] — 內建思考／推理模型；CoT 被做進模型本身
- [[evals]] — 用固定測試量測 prompt；換模型前要重測
- [[emergent-abilities]] — 能力在模型夠大後才出現

## 技巧（techniques）
**基礎**
- [[be-clear-and-direct]] — 把模型當新同事：講清楚、說原因；明確程度看模型
- [[zero-shot-prompting]] — 不給範例、直接下指令
- [[few-shot-prompting]] — 3–5 個多樣範例控制格式與做法
- [[role-prompting]] — 設定角色；developer／user 訊息權限
- [[xml-tags]] — 用標籤與 Markdown 分段；OpenAI 四段結構

**推理**
- [[chain-of-thought]] — 先推理再回答；含 2022→2026 演進 ⭐ 核心頁
- [[zero-shot-cot]] — 一句 "Let's think step by step" 引出推理
- [[self-consistency]] — 抽多條推理、多數決
- [[react]] — 推理與查資料／呼叫工具交錯進行
- [[self-check]] — 要求模型完成前自我驗證

## 模型／廠商（models）
- [[claude]] — Anthropic；XML 標籤、內建思考、世代差異
- [[gpt]] — OpenAI；推理模型 vs GPT 模型、四段結構

## 比較（comparisons）
- [[few-shot-cot-vs-zero-shot-cot]] — 兩種 CoT 的成本、控制力、怎麼選
- [[anthropic-vs-openai-guides]] — 兩家官方指南的共同點與各自重點

## 來源摘要（sources）
**方法論**
- [[2026-karpathy-llm-wiki]] — Karpathy 2026，LLM Wiki 原文

**論文**
- [[2022-wei-cot-paper]] — Wei et al. 2022，CoT 原始論文
- [[2022-wang-self-consistency]] — Wang et al. 2022，Self-Consistency
- [[2022-kojima-zero-shot-cot]] — Kojima et al. 2022，Zero-shot CoT
- [[2022-yao-react]] — Yao et al. 2022，ReAct
- [[2024-schulhoff-prompt-report]] — Schulhoff et al. 2024，The Prompt Report（58 種技巧的分類法）

**官方指南**
- [[anthropic-prompting-best-practices]] — Claude 官方提示指南（2026-11 版）
- [[openai-prompt-engineering-guide]] — OpenAI 官方提示指南（2026-11 版）

## 保存的問答（queries）
- [[2026-do-we-still-need-step-by-step]] — 2026 年還需要寫 "Let's think step by step" 嗎？
