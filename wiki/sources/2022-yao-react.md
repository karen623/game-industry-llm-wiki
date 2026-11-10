---
title: Yao et al. 2022 — ReAct（推理＋行動）
type: source
tags: [paper, reasoning, agents]
sources: []
updated: 2026-11-10
---

# Yao et al. 2022 — ReAct: Synergizing Reasoning and Acting in LLMs

- 原始資料：`raw/papers/2022-yao-react.md`（arXiv:2210.03629，ICLR 2023）

## 一句話
讓模型**交錯「想」和「做」**：一邊推理、一邊呼叫工具查資料 → [[react]]。

## 重點
- 問答與事實查核任務透過 Wikipedia API 查資料。
- ALFWorld、WebShop：只用 1–2 個範例，成功率比模仿學習／強化學習方法高 34% 與 10%（絕對值）。
- 作者主張：推理有外部資料當依據，能減少 [[chain-of-thought]] 常見的 [[hallucination]] 與錯誤傳遞，過程也更好解讀。

## 在 wiki 中被用在
[[react]] · [[hallucination]] · [[chain-of-thought]]
