---
title: GPT 與推理模型（OpenAI）
type: model
tags: [vendor, openai]
sources: [openai-prompt-engineering-guide]
updated: 2026-11-10
---

# GPT 與推理模型（OpenAI）

## 定義
OpenAI 的模型分成兩類（來源：[[openai-prompt-engineering-guide]]）：
- **推理模型**：內部會產生思維鏈，擅長複雜多步驟任務，較慢、較貴 → 類似 [[extended-thinking]]
- **GPT 模型**：快、便宜，需要明確指令

## 提示上的特點
- 推理模型像**資深同事**：給高層目標就好；GPT 模型像**資淺同事**：要給明確步驟與輸出格式。
- 用 developer 訊息放規則、user 訊息放輸入 → [[role-prompting]]
- 建議的四段結構：Identity → Instructions → Examples → Context → [[xml-tags]]
- 常重複的內容放 prompt 開頭，可以利用 prompt caching。
- 正式環境固定模型版本＋評測 → [[evals]]

## 相關頁面
[[claude]] · [[anthropic-vs-openai-guides]] · [[extended-thinking]] · [[evals]]

## 來源
[[openai-prompt-engineering-guide]]
