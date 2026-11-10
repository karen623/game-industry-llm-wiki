---
title: Claude（Anthropic）
type: model
tags: [vendor, claude]
sources: [anthropic-prompting-best-practices]
updated: 2026-11-10
---

# Claude（Anthropic）

## 定義
Anthropic 開發的大型語言模型系列。組上專案「AI 提示工程教學遊戲」的回答 AI、評分 AI 也使用 Claude。

## 提示上的特點（來源：[[anthropic-prompting-best-practices]]）
- 對清楚、明確的指令反應很好 → [[be-clear-and-direct]]
- 官方特別推薦用 XML 標籤分段 → [[xml-tags]]
- 新世代模型有內建思考，手動 CoT 只是備案 → [[extended-thinking]]、[[chain-of-thought]]
- 不同世代差異很大：例如有些模型會自己驗證答案，再要求 [[self-check]] 反而會過度驗證。
  **官方建議：針對特定模型的技巧，換模型前要用自己的評測重新檢查。**

## 待補
- 與 GPT 的比較已整理在 [[anthropic-vs-openai-guides]]；Gemini 待 ingest Google 官方指南

## 相關頁面
[[extended-thinking]] · [[xml-tags]] · [[role-prompting]] · [[chain-of-thought]] · [[gpt]] · [[evals]]

## 來源
[[anthropic-prompting-best-practices]]
