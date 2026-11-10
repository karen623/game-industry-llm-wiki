---
title: 內建思考與推理模型（Extended / Adaptive Thinking, Reasoning Models）
type: concept
tags: [reasoning, model-feature, claude]
sources: [anthropic-prompting-best-practices, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# 內建思考（Extended / Adaptive Thinking）

## 定義
模型在正式回答前，先在獨立的「思考區塊」裡推理。可以把它看成 **[[chain-of-thought]] 被做進模型本身**，不再需要靠 prompt 引出。

## 在 Claude 上的運作（來源：[[anthropic-prompting-best-practices]]）
- **Adaptive thinking**：模型依兩件事自行決定想多少：`effort` 參數，以及問題有多複雜。
- 簡單問題會直接回答，複雜問題會想比較久。
- 舊模型用 `budget_tokens` 手動設定思考量（extended thinking）；新模型改用 `effort` 調整。
- 部分最新模型思考**一直開著**，無法關閉。

## 在 OpenAI 上（來源：[[openai-prompt-engineering-guide]]）
- OpenAI 把這類模型稱為**推理模型（reasoning models）**：內部產生思維鏈，擅長複雜任務，但較慢、較貴。
- 推理模型像**資深同事**，給高層目標即可；一般 GPT 模型像**資淺同事**，需要明確步驟 → [[gpt]]

## 對寫 prompt 的影響（兩家指南一致，見 [[anthropic-vs-openai-guides]]）
- 寫「想得周全一點」這類一般性指示，通常比手寫逐步流程好。
- 範例（[[few-shot-prompting]]）仍然有效，會影響模型思考的方式。
- 想太多時：在 prompt 裡要求「選定方法就堅持」，或降低 `effort`。
- 手動 CoT 降為備案；某些新模型上，要求把推理寫在 `<thinking>` 標籤的 prompt 可能被拒絕。

## 相關頁面
[[chain-of-thought]] · [[zero-shot-cot]] · [[self-check]] · [[claude]] · [[gpt]] · [[anthropic-vs-openai-guides]] · [[emergent-abilities]] · [[2026-do-we-still-need-step-by-step]]

## 來源
[[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]]
