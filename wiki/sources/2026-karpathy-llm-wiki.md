---
title: Karpathy 2026 — LLM Wiki（本 wiki 的方法論來源）
type: source
tags: [method, knowledge-base]
sources: []
updated: 2026-11-10
---

# Karpathy 2026 — LLM Wiki

- 原始資料：`raw/articles/2026-karpathy-llm-wiki.md`（GitHub Gist，2026-04-04）
- 性質：「點子文件」，描述一種模式而不是具體實作

## 一句話
不要每次提問才從原始文件撈資料（[[rag]]），而是讓 LLM **持續維護一份會累積的 wiki** → [[llm-wiki]]。

## 重點
- 三層：raw（不可變）、wiki（LLM 維護）、schema（如 CLAUDE.md）。
- 三種操作：ingest（一份資料可能動到 10–15 頁）、query（好答案存回 wiki）、lint（找矛盾、孤兒頁、缺口）。
- index.md 在約 100 份資料、數百頁的規模下就夠用，不需要 embedding 式 RAG。
- 為什麼有效：維護成本是人類 wiki 失敗的主因，LLM 讓維護成本趨近於零。
- 限制：lint 只找問題，**不保證事實正確**。

## 在 wiki 中被用在
[[llm-wiki]] · [[rag]]
