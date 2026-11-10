---
title: 零樣本思維鏈（Zero-shot CoT）
type: technique
tags: [reasoning]
sources: [2022-kojima-zero-shot-cot]
updated: 2026-11-10
---

# 零樣本思維鏈（Zero-shot Chain-of-Thought）

## 一句話定義
不給任何範例，只在問題後加上 **"Let's think step by step"**（讓我們一步一步思考），就能引出 [[chain-of-thought]] 推理。

## 怎麼用
```text
Q: 一個雜耍演員有 16 顆球，其中一半是高爾夫球，高爾夫球裡又有一半是藍色的。藍色高爾夫球有幾顆？
A: Let's think step by step.
```
原論文用了兩階段：先讓模型產生推理，再用第二個 prompt 從推理中擷取最終答案。

## 為什麼有效
一句通用的觸發語，就能讓模型進入「寫出推理過程」的模式，不必替每種任務設計範例（來源：[[2022-kojima-zero-shot-cot]]）。

## 效果（text-davinci-002）
| 資料集 | 一般 zero-shot | Zero-shot CoT |
|---|---|---|
| MultiArith | 17.7% | 78.7% |
| GSM8K | 10.4% | 40.7% |

## 適用／不適用情境
- ✅ 沒時間做範例、任務種類多變時，很好用的基準做法
- ⚠️ 對有內建思考的新模型，通常不需要再加這句 → 見 [[extended-thinking]]

## 常見錯誤
- 以為加了這句就一定比 few-shot 好：論文提出它是當作**強力基準（baseline）**，不是萬靈丹 → 見 [[few-shot-cot-vs-zero-shot-cot]]

## 相關頁面
[[chain-of-thought]] · [[zero-shot-prompting]] · [[few-shot-cot-vs-zero-shot-cot]] · [[2026-do-we-still-need-step-by-step]]

## 來源
[[2022-kojima-zero-shot-cot]]
