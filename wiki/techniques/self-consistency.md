---
title: 自我一致性（Self-Consistency）
type: technique
tags: [reasoning]
sources: [2022-wang-self-consistency]
updated: 2026-11-10
---

# 自我一致性（Self-Consistency）

## 一句話定義
對同一題**抽樣多條推理路徑**，最後選出現最多次（最一致）的答案，而不是只相信一條推理。

## 怎麼用
1. 用 [[chain-of-thought]] 的 prompt，讓模型回答同一題好幾次（提高隨機性，例如 temperature > 0）。
2. 從每次的推理中取出最終答案。
3. 多數決選出最常出現的答案。

```text
（同一題問 5 次）→ 答案：11, 11, 9, 11, 11 → 選 11
```

## 為什麼有效
複雜問題通常有很多種解法，但正確答案只有一個；錯誤的推理則容易各錯各的（來源：[[2022-wang-self-consistency]]）。

## 效果（相對於 CoT）
論文摘要沒有說明這些是百分點還是相對提升（來源：[[2022-wang-self-consistency]]）。

| 資料集 | 提升 |
|---|---|
| GSM8K | +17.9% |
| AQuA | +12.2% |
| SVAMP | +11.0% |
| StrategyQA | +6.4% |
| ARC-challenge | +3.9% |

## 適用／不適用情境
- ✅ 答案可以比對的任務：數學、選擇題、分類
- ❌ 開放式寫作：很難判斷哪些答案「一致」（推論）
- ⚠️ 成本是單次的好幾倍，因為要問很多次（推論）

## 相關頁面
[[chain-of-thought]] · [[self-check]] · [[react]]

## 來源
[[2022-wang-self-consistency]]
