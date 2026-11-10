---
title: Wei et al. 2022 — Chain-of-Thought Prompting（CoT 原始論文）
type: source
tags: [paper, reasoning]
sources: []
updated: 2026-11-10
---

# Wei et al. 2022 — Chain-of-Thought Prompting Elicits Reasoning in LLMs

- 原始資料：`raw/papers/2022-wei-cot.md`（arXiv:2201.11903）
- 作者：Jason Wei、Denny Zhou 等（Google）

## 一句話
在 [[few-shot-prompting]] 的範例裡**示範推理過程**，模型就會跟著先推理再回答。這篇論文提出了 [[chain-of-thought]]。

## 重點
- 方法：放幾個「問題 → 中間推理步驟 → 答案」的範例。
- 任務：算術、常識、符號推理。
- 結果：540B 模型加上 8 個 CoT 範例，在 GSM8K 達到當時最佳，超越經過微調的 GPT-3＋驗證器。
- 主張：推理能力在夠大的模型中會「湧現」→ 見 [[emergent-abilities]]。

## 在 wiki 中被用在
- [[chain-of-thought]]、[[few-shot-prompting]]、[[emergent-abilities]]、[[few-shot-cot-vs-zero-shot-cot]]
