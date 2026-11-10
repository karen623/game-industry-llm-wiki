---
title: 少樣本提示（Few-shot / Multishot Prompting）
type: technique
tags: [prompting-basics, core]
sources: [anthropic-prompting-best-practices, 2022-wei-cot-paper, openai-prompt-engineering-guide, 2022-yao-react]
updated: 2026-11-10
---

# 少樣本提示（Few-shot Prompting）

## 一句話定義
在 prompt 裡放幾個「輸入 → 輸出」的範例，讓模型照著範例的格式、語氣、做法回答。

## 怎麼用
```xml
請把客戶評論分類為 正面／負面／中立。

<examples>
  <example>評論：出貨超快，包裝也很用心！ → 正面</example>
  <example>評論：等了兩週還沒到。 → 負面</example>
  <example>評論：東西跟照片差不多。 → 中立</example>
</examples>

評論：客服回覆很慢，但產品品質不錯。 →
```

## 好範例的三個條件（來源：[[anthropic-prompting-best-practices]]）
- **相關**：貼近實際使用情境
- **多樣**：涵蓋邊界情況，避免模型學到不該學的規律
- **有結構**：用 `<example>` 標籤包起來 → [[xml-tags]]
- 建議 **3–5 個**範例
- OpenAI 也建議範例要**多樣**，並放在 developer 訊息裡；few-shot 可以取代微調（來源：[[openai-prompt-engineering-guide]]）

## 延伸
- 範例裡加上推理步驟 → 就是 Few-shot [[chain-of-thought]]（來源：[[2022-wei-cot-paper]]）
- [[react]] 只用 1–2 個「想法＋行動」的範例，就能教會模型交錯推理與查資料（來源：[[2022-yao-react]]）
- 對有內建思考的模型，範例仍然有用，會影響模型思考的方式（來源：[[anthropic-prompting-best-practices]]）

## 常見錯誤
- 範例都長得很像 → 模型過度模仿某種格式或長度
- 範例和指令混在一起，沒有分隔 → 模型分不清哪些是範例、哪些是要做的事

## 相關頁面
[[zero-shot-prompting]] · [[chain-of-thought]] · [[xml-tags]] · [[react]] · [[few-shot-cot-vs-zero-shot-cot]] · [[anthropic-vs-openai-guides]]

## 來源
[[anthropic-prompting-best-practices]] · [[2022-wei-cot-paper]] · [[openai-prompt-engineering-guide]] · [[2022-yao-react]]
