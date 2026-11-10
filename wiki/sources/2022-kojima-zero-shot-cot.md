---
title: Kojima et al. 2022 — Large Language Models are Zero-Shot Reasoners
type: source
tags: [paper, reasoning]
sources: []
updated: 2026-11-10
---

# Kojima et al. 2022 — Large Language Models are Zero-Shot Reasoners

- 原始資料：`raw/papers/2022-kojima-zero-shot-cot.md`（arXiv:2205.11916，NeurIPS 2022）
- 作者：Takeshi Kojima 等（東京大學、Google）

## 一句話
**不用給範例**，只要加一句 "Let's think step by step" 就能引出推理，也就是 [[zero-shot-cot]]。

## 重點
- 模型：InstructGPT（text-davinci-002）、PaLM 540B。
- 結果（text-davinci-002）：MultiArith 17.7% → 78.7%；GSM8K 10.4% → 40.7%。
- 一個萬用句子就能跨多種推理任務有效，代表模型有「未被開發的零樣本能力」。
- 建議：先試 [[zero-shot-prompting]]，再考慮做範例或微調。

## 在 wiki 中被用在
- [[zero-shot-cot]]、[[chain-of-thought]]、[[zero-shot-prompting]]、[[few-shot-cot-vs-zero-shot-cot]]
