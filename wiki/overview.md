---
title: Prompt Engineering 總覽
type: concept
tags: [overview]
sources: [2022-wei-cot-paper, 2022-kojima-zero-shot-cot, 2022-wang-self-consistency, 2022-yao-react, 2024-schulhoff-prompt-report, anthropic-prompting-best-practices, openai-prompt-engineering-guide, 2026-karpathy-llm-wiki]
updated: 2026-11-10
---

# Prompt Engineering 總覽

> 這頁是整個領域的地圖，會隨 ingest 逐步改寫。目前涵蓋「基礎」「推理」「模型差異」，以及本 wiki 的方法論。

## 這個領域有多大？
The Prompt Report 整理出 **58 種 LLM 提示技巧**、**40 種**其他模態技巧和 **33 個**術語，並指出這個領域術語混亂、知識零散（[[2024-schulhoff-prompt-report]]）。本 wiki 目前收錄其中 10 種技巧。

## 核心故事線 1：推理技巧的演進
1. **2022 年 1 月**：在範例裡示範推理 → [[chain-of-thought]]
2. **2022 年 3 月**：多抽幾條推理、多數決 → [[self-consistency]]
3. **2022 年 5 月**：一句 "Let's think step by step" 就有效 → [[zero-shot-cot]]
4. **2022 年 10 月**：推理之間穿插查資料、呼叫工具 → [[react]]（agent 的前身）
5. **現在**：模型內建思考（Anthropic）／推理模型（OpenAI），手動 CoT 降為備案 → [[extended-thinking]]

## 核心故事線 2：兩家官方指南的共識
寫 prompt 的重點不再是背技巧，而是**依模型能力調整寫法**：推理型模型給目標，一般模型給明確步驟；兩家都推薦結構化（[[xml-tags]]）、多樣範例（[[few-shot-prompting]]）、換模型要重測（[[evals]]）→ [[anthropic-vs-openai-guides]]

## 核心故事線 3：可靠性
模型會產生沒根據的內容（[[hallucination]]）。對策包括：查外部資料（[[react]]、[[rag]]）、多條推理比對（[[self-consistency]]）、自我檢查（[[self-check]]）、可追溯的知識庫（[[llm-wiki]]）。

## 主題地圖（✅ 已有頁面／☐ 規劃中）
1. **基礎**：✅ [[zero-shot-prompting]]、✅ [[few-shot-prompting]]、✅ [[role-prompting]]、✅ [[be-clear-and-direct]]、✅ [[xml-tags]]
2. **推理**：✅ [[chain-of-thought]]、✅ [[zero-shot-cot]]、✅ [[self-consistency]]、☐ [[tree-of-thoughts]]
3. **工具與代理**：✅ [[react]]、☐ [[prompt-chaining]]、☐ [[context-engineering]]
4. **模型特性**：✅ [[extended-thinking]]、✅ [[hallucination]]、☐ [[context-window]]、✅ [[claude]]、✅ [[gpt]]、☐ Gemini
5. **安全與風險**：☐ [[prompt-injection]]、☐ 越獄（jailbreak）
6. **評估**：✅ [[evals]]
7. **知識管理**：✅ [[rag]]、✅ [[llm-wiki]]

## 相關頁面
- [[index]]
- [[log]]
