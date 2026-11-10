---
title: 請模型自我檢查（Self-check）
type: technique
tags: [reasoning, verification]
sources: [anthropic-prompting-best-practices]
updated: 2026-11-10
---

# 請模型自我檢查（Self-check）

## 一句話定義
在 prompt 結尾要求模型「完成前，依照某些標準檢查自己的答案」。

## 怎麼用
```text
……完成前，請用以下標準驗證你的答案：1) 所有數字加總正確 2) 單位一致。
```

## 適用／不適用情境（來源：[[anthropic-prompting-best-practices]]）
- ✅ 程式、數學這類可以驗證的任務，抓錯很有效
- ⚠️ 有些新模型本來就會自我驗證，再加這類指示會**過度驗證**，增加成本和延遲 → 見 [[claude]]

## 相關頁面
[[chain-of-thought]] · [[extended-thinking]] · [[self-consistency]] · [[hallucination]]

## 來源
[[anthropic-prompting-best-practices]]
