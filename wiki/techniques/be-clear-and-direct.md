---
title: 清楚直接＋說明原因
type: technique
tags: [prompting-basics, core]
sources: [anthropic-prompting-best-practices, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# 清楚直接＋說明原因

## 一句話定義
把模型當成**聰明但不了解你情境的新同事**：講清楚要什麼、格式與限制，並說明「為什麼」。

## 怎麼用
| 較差 | 較好 |
|---|---|
| `絕對不要用刪節號` | `你的回答會被語音引擎朗讀，引擎不會唸刪節號，所以不要使用刪節號。` |
| `做一個分析儀表板` | `做一個分析儀表板，盡量加入相關功能和互動，不要只做基本款。` |

（範例改寫自 [[anthropic-prompting-best-practices]]）

## 檢驗法
把 prompt 給一個不了解任務的同事看：**他看不懂，模型也會看不懂**。

## 為什麼有效
說明原因後，模型可以把規則推廣到沒有明寫的情況（來源：[[anthropic-prompting-best-practices]]）。

## 要多明確？看模型（來源：[[openai-prompt-engineering-guide]]）
- 一般 GPT 模型：要寫出明確的邏輯、資料與輸出格式（像交代資淺同事）。
- 推理模型：給高層目標即可（像交代資深同事）→ [[extended-thinking]]

## 相關頁面
[[role-prompting]] · [[xml-tags]] · [[zero-shot-prompting]] · [[gpt]]

## 來源
[[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]]
