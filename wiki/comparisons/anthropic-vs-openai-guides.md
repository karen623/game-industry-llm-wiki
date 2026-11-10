---
title: Anthropic vs OpenAI 官方提示指南
type: comparison
tags: [official, claude, openai]
sources: [anthropic-prompting-best-practices, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# Anthropic vs OpenAI 官方提示指南

兩份指南都是 2026-11-10 擷取的版本。

## 兩家都同意的事
| 主題 | Anthropic | OpenAI |
|---|---|---|
| 推理／思考型模型 | 一般性指示（「想周全一點」）常比手寫步驟好 | 推理模型適合高層次指引，像資深同事 |
| 結構化 | 用 XML 標籤分隔指令、文件、範例 | 用 Markdown 標題＋XML 標籤；Identity → Instructions → Examples → Context |
| 範例 | 3–5 個、相關、多樣、用 `<example>` 包起來 | 幾個多樣的輸入／輸出範例 |
| 角色 | 在 system prompt 設定角色 | developer 訊息定規則、權限高於 user |
| 換模型 | 技巧要用自己的評測重新檢查 | 固定版本＋建立評測 |

## 各自強調的重點
- **Anthropic**：說明「為什麼」，讓模型能推廣規則；自我檢查；新模型可能過度驗證或想太多。
- **OpenAI**：區分推理模型和 GPT 模型；prompt caching；agent 任務要先規劃、說明工具呼叫原因。

## 結論
兩份來源**沒有互相矛盾**。共同的核心觀念是：**依模型能力調整寫法**，有推理能力的模型給目標，一般模型給明確步驟。

## 相關頁面
[[claude]] · [[gpt]] · [[extended-thinking]] · [[xml-tags]] · [[few-shot-prompting]] · [[role-prompting]] · [[evals]]

## 來源
[[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]]
