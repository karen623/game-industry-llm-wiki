---
title: 零樣本提示（Zero-shot Prompting）
type: technique
tags: [prompting-basics]
sources: [2022-kojima-zero-shot-cot]
updated: 2026-11-10
---

# 零樣本提示（Zero-shot Prompting）

## 一句話定義
不給任何範例，直接用指令描述任務，讓模型作答。

## 怎麼用
```text
請把以下評論分類為 正面／負面／中立：「客服回覆很慢，但產品品質不錯。」
```

## 為什麼重要
Kojima 等人建議：在花力氣做範例或微調之前，**先試試零樣本能做到多好**（來源：[[2022-kojima-zero-shot-cot]]）。
加上一句觸發語就變成 [[zero-shot-cot]]。

## 什麼時候要改用 few-shot
輸出格式要求很嚴格、或任務有特殊判斷標準時 → [[few-shot-prompting]]（推論）

## 相關頁面
[[few-shot-prompting]] · [[zero-shot-cot]] · [[be-clear-and-direct]]

## 來源
[[2022-kojima-zero-shot-cot]]
