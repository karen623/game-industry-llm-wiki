---
title: OpenAI — Prompt engineering（OpenAI 官方提示指南）
type: source
tags: [guide, official, openai]
sources: []
updated: 2026-11-10
---

# OpenAI — Prompt engineering

- 原始資料：`raw/guides/openai-prompt-engineering-guide.md`
- 性質：官方文件，**持續更新**；本頁依 2026-11-10 擷取的版本撰寫。

## 一句話
依模型類型調整寫法：**推理模型給目標、GPT 模型給明確步驟**；用 Markdown／XML 分段，正式環境要固定版本並做評測。

## 重點
- 模型選擇 → [[gpt]]、[[extended-thinking]]
- developer／user 訊息角色 → [[role-prompting]]
- Identity → Instructions → Examples → Context 四段結構 → [[xml-tags]]
- Few-shot 範例要多樣 → [[few-shot-prompting]]
- Context 與 RAG → [[rag]]
- 固定版本＋評測 → [[evals]]

## 跟其他來源的關係
與 [[anthropic-prompting-best-practices]] 有大量相同建議 → 見 [[anthropic-vs-openai-guides]]。
