---
title: LLM Wiki（由 LLM 維護的知識庫）
type: concept
tags: [method, knowledge-base]
sources: [2026-karpathy-llm-wiki]
updated: 2026-11-10
---

# LLM Wiki

## 定義
由 LLM **持續撰寫、維護**的一份互相連結的 Markdown wiki。人負責挑資料和提問，LLM 負責摘要、連結、歸檔與維護（來源：[[2026-karpathy-llm-wiki]]）。這個 wiki 本身就是用這個方法建立的。

## 和 RAG 的差別
| | [[rag]] | LLM Wiki |
|---|---|---|
| 什麼時候整理知識 | 每次提問時 | 每次加入資料時（ingest） |
| 知識會不會累積 | 不會，每次重來 | 會，結果存成頁面 |
| 矛盾 | 不容易發現 | ingest 時就標出來 |
| 規模 | 適合大量文件 | 約 100 份資料、數百頁內只靠 index 就夠 |

## 三層與三種操作
- raw（不可變）→ wiki（LLM 維護）← schema（CLAUDE.md）
- ingest、query、lint
- Ingest 時先和使用者**討論重點**再寫頁面；Karpathy 自己偏好**一次一份、親自參與**（來源：[[2026-karpathy-llm-wiki]]）。這就是「先討論、後生成」。
- Query 的輸出不限文字，也可以是表格、圖表或**投影片**（來源：[[2026-karpathy-llm-wiki]]）；本 wiki 的 HTML 簡報就是一種 query 輸出。

## 為什麼有效
人類維護的 wiki 會失敗，是因為維護成本長得比價值快；LLM 不會厭倦這些工作（來源：[[2026-karpathy-llm-wiki]]）。

## 限制
- lint 只能找出問題，**不保證事實正確**，所以每個論點都要能追溯到來源。
- 規模變大後可能還是需要搜尋工具。

## 相關頁面
[[rag]] · [[hallucination]] · [[overview]]

## 來源
[[2026-karpathy-llm-wiki]]
