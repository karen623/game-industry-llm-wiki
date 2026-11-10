---
title: Few-shot CoT vs Zero-shot CoT
type: comparison
tags: [reasoning]
sources: [2022-wei-cot-paper, 2022-kojima-zero-shot-cot, anthropic-prompting-best-practices]
updated: 2026-11-10
---

# Few-shot CoT vs Zero-shot CoT

| | Few-shot CoT | Zero-shot CoT |
|---|---|---|
| 提出 | [[2022-wei-cot-paper]]（2022-01） | [[2022-kojima-zero-shot-cot]]（2022-05） |
| 做法 | 放幾個含推理步驟的範例 | 加一句 "Let's think step by step" |
| 準備成本 | 高：每種任務都要設計範例 | 幾乎為零 |
| 控制力 | 高：可以示範想要的推理方式與格式 | 低：推理方式由模型決定 |
| 論文定位 | 在 GSM8K 達到當時最佳 | 當作強力的零樣本**基準** |
| 新模型上 | 範例仍會影響內建思考 | 通常被內建思考取代 |

## 怎麼選
1. 先試 Zero-shot（或直接用模型的 [[extended-thinking]]），成本最低。
2. 推理方式或輸出格式不符需求時，再加範例改成 Few-shot。
3. 這個順序與 Kojima 等人「先探索零樣本能力」的建議一致（來源：[[2022-kojima-zero-shot-cot]]），
   也和官方指南「範例仍有效」相符（來源：[[anthropic-prompting-best-practices]]）。

## 相關頁面
[[chain-of-thought]] · [[zero-shot-cot]] · [[few-shot-prompting]] · [[zero-shot-prompting]]
