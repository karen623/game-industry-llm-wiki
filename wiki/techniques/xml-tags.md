---
title: 用 XML 標籤結構化 prompt
type: technique
tags: [prompting-basics, formatting, claude]
sources: [anthropic-prompting-best-practices, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# 用 XML 標籤結構化 prompt

## 一句話定義
用 `<instructions>`、`<context>`、`<input>` 這類標籤，把 prompt 裡不同性質的內容分開，減少模型誤解。

## 怎麼用
```xml
<instructions>根據文件回答問題，最終答案放在 <answer> 標籤。</instructions>
<documents>
  <document index="1">……</document>
  <document index="2">……</document>
</documents>
<question>……</question>
```

## 原則（來源：[[anthropic-prompting-best-practices]]）
- 標籤名稱要一致、有描述性
- 內容有階層時就巢狀（`<documents>` 裡放多個 `<document>`）
- 範例用 `<example>`／`<examples>` → [[few-shot-prompting]]
- 要求最終答案放在 `<answer>`，方便程式擷取 → [[chain-of-thought]]

## OpenAI 的四段結構（來源：[[openai-prompt-engineering-guide]]）
OpenAI 建議 Markdown 標題＋XML 標籤並用，developer 訊息依序寫：
```markdown
# Identity      ← 你是誰、語氣
# Instructions  ← 規則條列
# Examples      ← 用 <example> 標籤包的範例
# Context       ← 文件、資料（通常放最後）
```

## 相關頁面
[[few-shot-prompting]] · [[chain-of-thought]] · [[be-clear-and-direct]] · [[claude]] · [[gpt]] · [[rag]] · [[anthropic-vs-openai-guides]]

## 來源
[[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]]
