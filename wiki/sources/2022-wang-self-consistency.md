---
title: Wang et al. 2022 — Self-Consistency（自我一致性）
type: source
tags: [paper, reasoning]
sources: []
updated: 2026-11-10
---

# Wang et al. 2022 — Self-Consistency Improves Chain of Thought Reasoning

- 原始資料：`raw/papers/2022-wang-self-consistency.md`（arXiv:2203.11171，ICLR 2023）
- 作者：Xuezhi Wang、Jason Wei、Denny Zhou 等（與 [[2022-wei-cot-paper]] 同一個團隊）

## 一句話
不要只取一條推理，**多抽幾條、投票選最一致的答案** → [[self-consistency]]。

## 重點
- 取代 [[chain-of-thought]] 的貪婪解碼。
- 相對於 CoT 的提升：GSM8K +17.9%、SVAMP +11.0%、AQuA +12.2%、StrategyQA +6.4%、ARC-challenge +3.9%
  （摘要沒說明是百分點還是相對提升）。

## 在 wiki 中被用在
[[self-consistency]] · [[chain-of-thought]]
