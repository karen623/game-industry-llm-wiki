---
title: 問答：2026 年還需要在 prompt 寫「Let's think step by step」嗎？
type: query
tags: [reasoning, faq]
sources: [2022-kojima-zero-shot-cot, anthropic-prompting-best-practices]
updated: 2026-11-10
---

# 問：2026 年還需要在 prompt 寫「Let's think step by step」嗎？

## 答（根據 wiki 現有頁面）
**看模型有沒有內建思考。**

- **沒有內建思考、或思考被關閉的模型**：仍然有用。這句話在 2022 年讓 GSM8K 正確率從 10.4% 提升到 40.7%
  （[[zero-shot-cot]]，來源：[[2022-kojima-zero-shot-cot]]）。
  官方指南也把手動 CoT 列為**備案**：請模型先推理，最終答案放在 `<answer>` 標籤。
- **有內建思考的新模型**（例如新一代 [[claude]]）：通常不需要。改用 [[extended-thinking]]，
  用 `effort` 調整思考量；寫「想得周全一點」這類一般性指示就夠了。有些模型上，
  要求把推理寫在 `<thinking>` 標籤的 prompt 甚至可能被拒絕（來源：[[anthropic-prompting-best-practices]]）。

## 給組上專案（提示工程教學遊戲）的啟示（推論）
評分 AI 不應該把「有沒有寫 step by step」當成固定加分項，
而是要看學生的 prompt 有沒有配合**題目用的模型**和**任務類型**。

## 參考頁面
[[chain-of-thought]] · [[zero-shot-cot]] · [[extended-thinking]] · [[few-shot-cot-vs-zero-shot-cot]]
