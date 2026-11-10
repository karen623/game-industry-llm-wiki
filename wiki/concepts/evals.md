---
title: 評測（Evals）與固定模型版本
type: concept
tags: [evaluation, production]
sources: [openai-prompt-engineering-guide, anthropic-prompting-best-practices]
updated: 2026-11-10
---

# 評測（Evals）與固定模型版本

## 定義
用一組固定的測試題，**量測 prompt 的效果**，在修改 prompt 或升級模型時比較前後差異。

## 兩家官方指南的說法
- OpenAI：輸出不是確定性的，正式環境要**固定模型版本（pin snapshot）**，並建立測試與評測（來源：[[openai-prompt-engineering-guide]]）。
- Anthropic：針對特定模型量測出來的技巧，換到別的模型前要**用自己的評測重新檢查**（來源：[[anthropic-prompting-best-practices]]）。
- 兩者一致：**提示技巧會隨模型改變，要靠評測確認**，呼應 [[emergent-abilities]] 和 [[chain-of-thought]] 的演進。

## 給組上遊戲專案的啟示（推論）
評分 AI 本身也是一個 prompt，換模型或改評分規則時，應該用一組固定的學生作答來比較評分結果。

## 相關頁面
[[anthropic-vs-openai-guides]] · [[emergent-abilities]] · [[claude]] · [[gpt]]

## 來源
[[openai-prompt-engineering-guide]] · [[anthropic-prompting-best-practices]]
