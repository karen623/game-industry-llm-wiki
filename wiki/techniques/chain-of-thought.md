---
title: 思維鏈（Chain-of-Thought, CoT）
type: technique
tags: [reasoning, core]
sources: [2022-wei-cot-paper, 2022-kojima-zero-shot-cot, anthropic-prompting-best-practices, 2022-wang-self-consistency, 2022-yao-react, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# 思維鏈（Chain-of-Thought, CoT）

## 一句話定義
讓模型**先寫出中間推理步驟，再給答案**，藉此提升多步驟推理題（數學、邏輯、常識）的正確率。

## 怎麼用
有兩種主流做法：

**1. Few-shot CoT**（[[2022-wei-cot-paper]]）：在範例裡示範推理過程
```text
Q: 小明有 5 顆蘋果，又買了 2 袋，每袋 3 顆，現在有幾顆？
A: 小明原本有 5 顆。2 袋 × 3 顆 = 6 顆。5 + 6 = 11。答案是 11。

Q: 餐廳有 23 顆蛋，用掉 20 顆做午餐，又買了 6 顆，現在有幾顆？
A:
```

**2. Zero-shot CoT**（[[2022-kojima-zero-shot-cot]]）：不給範例，只加一句觸發語 → 詳見 [[zero-shot-cot]]
```text
Q: 餐廳有 23 顆蛋，用掉 20 顆做午餐，又買了 6 顆，現在有幾顆？
A: Let's think step by step.
```

**3. 結構化輸出**（[[anthropic-prompting-best-practices]]）：請模型先推理，最終答案放在 `<answer>` 標籤，方便程式擷取 → 見 [[xml-tags]]。

## 為什麼有效
- 把一個難題拆成多個小步驟，每一步都比直接跳到答案容易。
- 推理過程寫出來後，後面的文字可以「參考」前面算好的中間結果。（推論）
- 原始論文發現：這種能力要模型夠大才會出現 → [[emergent-abilities]]（來源：[[2022-wei-cot-paper]]）

## 適用／不適用情境
- ✅ 適用：數學應用題、多步驟邏輯、需要解釋過程的任務
- ❌ 不太需要：單純查事實、翻譯、簡單分類（多寫推理只會更慢、更貴）（推論）
- ⚠️ 新模型：見下方「演進」

## 演進：從提示技巧到內建能力
| 時期 | 做法 | 來源 |
|---|---|---|
| 2022 初 | 手寫推理範例（few-shot CoT） | [[2022-wei-cot-paper]] |
| 2022 春 | 抽多條推理、多數決（[[self-consistency]]） | [[2022-wang-self-consistency]] |
| 2022 中 | 一句 "Let's think step by step" 就夠 | [[2022-kojima-zero-shot-cot]] |
| 2022 秋 | 推理之間穿插查資料（[[react]]） | [[2022-yao-react]] |
| 現在 | 模型內建思考（[[extended-thinking]]），手動 CoT 降為備案 | [[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]] |

## ⚠️ 不同說法
- **2022 論文**：要明確提示模型逐步推理，正確率才會大幅提升。
- **Anthropic 官方指南（2026）**：對內建思考的新模型，「想得周全一點」這類一般性指示，常常比手寫步驟更好；
  在最新幾代 Claude 上，要求把推理寫在 `<thinking>` 標籤裡的 prompt 甚至可能被拒絕，應改用內建思考。
- **OpenAI 官方指南（2026）**：推理模型（內部會產生思維鏈）適合高層次指引；一般 GPT 模型則需要明確指令。與 Anthropic 的說法一致。
- 兩者不算矛盾，而是**模型世代不同**：使用前要先確認你用的模型有沒有內建思考 → [[claude]]。

## 常見錯誤
- 對有內建思考的模型還硬塞一大段「第一步…第二步…」：效果可能比一般指示差（來源：[[anthropic-prompting-best-practices]]）。
- 只要求推理，沒有規定最終答案的格式 → 程式很難擷取答案；可以用 `<answer>` 標籤。
- 用在不需要推理的簡單任務上，白白增加成本。

## 相關頁面
[[zero-shot-cot]] · [[few-shot-prompting]] · [[extended-thinking]] · [[self-consistency]] · [[react]] · [[hallucination]] · [[self-check]] · [[few-shot-cot-vs-zero-shot-cot]] · [[emergent-abilities]]

## 來源
[[2022-wei-cot-paper]] · [[2022-kojima-zero-shot-cot]] · [[anthropic-prompting-best-practices]] · [[2022-wang-self-consistency]] · [[2022-yao-react]] · [[openai-prompt-engineering-guide]]
