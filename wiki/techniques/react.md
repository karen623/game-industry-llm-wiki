---
title: ReAct（推理＋行動）
type: technique
tags: [reasoning, agents, tools]
sources: [2022-yao-react]
updated: 2026-11-10
---

# ReAct（Reasoning + Acting）

## 一句話定義
讓模型**交錯產生「想法」和「行動」**：想一下 → 呼叫工具查資料 → 看結果 → 再想，直到能回答。

## 怎麼用
```text
Question: 某部電影的導演是哪一年出生的？
Thought 1: 我要先查這部電影的導演是誰。
Action 1: Search[電影名稱]
Observation 1: ……導演是 X……
Thought 2: 接著查 X 的出生年。
Action 2: Search[X]
Observation 2: ……
Thought 3: 找到答案了。
Action 3: Finish[答案]
```
（格式示意，依論文概念改寫）

## 為什麼有效
- 推理幫模型擬定、追蹤、修正行動計畫；行動讓模型取得外部資訊（來源：[[2022-yao-react]]）。
- 推理有外部資料當依據，能減少純 [[chain-of-thought]] 的 [[hallucination]]。
- 解題軌跡（想法＋行動）寫出來，人比較容易解讀、檢查（來源：[[2022-yao-react]]）。

## 效果
- 問答（HotpotQA）、事實查核（FEVER）：透過簡單的 Wikipedia API 查資料；摘要沒有給具體數字（來源：[[2022-yao-react]]）。
- ALFWorld、WebShop：只用 1–2 個範例，成功率比模仿學習／強化學習方法高 34%、10%（絕對值）。

## 適用／不適用情境
- ✅ 需要查資料、多步驟操作的任務（問答、事實查核、網購、agent）
- ❌ 不需要外部資訊的純推理題，用 [[chain-of-thought]] 就好（推論）

## 延伸
現在的 agent 和工具呼叫（tool use）就是建立在這個想法上；OpenAI 指南也建議 agent 在呼叫工具前簡短說明原因（來源：[[openai-prompt-engineering-guide]]）。

## 相關頁面
[[chain-of-thought]] · [[hallucination]] · [[rag]] · [[self-consistency]]

## 來源
[[2022-yao-react]] · [[openai-prompt-engineering-guide]]
