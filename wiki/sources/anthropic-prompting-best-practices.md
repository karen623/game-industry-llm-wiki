---
title: Anthropic — Prompting best practices（Claude 官方提示指南）
type: source
tags: [guide, official, claude]
sources: []
updated: 2026-11-10
---

# Anthropic — Prompting best practices

- 原始資料：`raw/guides/anthropic-prompting-best-practices.md`
- 性質：官方文件，**持續更新**；本頁依 2026-11-10 擷取的版本撰寫。

## 一句話
Claude 的官方提示指南：清楚直接、說明原因、給範例、用 XML 分段、設角色；推理部分則以模型**內建思考**為主，**手動 CoT 只是備案**。

## 重點
- 一般原則 → [[be-clear-and-direct]]、[[few-shot-prompting]]、[[xml-tags]]、[[role-prompting]]
- 思考與推理 → [[extended-thinking]]、[[chain-of-thought]]、[[self-check]]
- 模型差異 → [[claude]]

## 跟其他來源的關係
- 它補上了 2022 年論文之後的發展：CoT 從「提示技巧」變成「模型內建能力」。
  見 [[chain-of-thought]] 的「演進」段落。
