---
title: 檢索增強生成（Retrieval-Augmented Generation, RAG）
type: concept
tags: [context, knowledge-base]
sources: [openai-prompt-engineering-guide, 2026-karpathy-llm-wiki]
updated: 2026-11-10
---

# 檢索增強生成（RAG）

## 定義
把模型訓練資料裡沒有的內容（例如公司文件）**在提問時找出來、放進 prompt**，讓模型根據這些內容回答。可以用向量資料庫或檔案搜尋工具（來源：[[openai-prompt-engineering-guide]]）。

## 要注意
- 放進來的內容受 context window（脈絡長度）限制（來源：[[openai-prompt-engineering-guide]]）。
- Karpathy 指出：一般 RAG 每次提問都從頭找、從頭生成，**知識不會累積** → 這是 [[llm-wiki]] 想解決的問題（來源：[[2026-karpathy-llm-wiki]]）。
- 和 [[react]] 一樣，讓回答有外部資料當依據，有助於減少 [[hallucination]]（推論）。

## 相關頁面
[[llm-wiki]] · [[react]] · [[hallucination]] · [[xml-tags]]

## 來源
[[openai-prompt-engineering-guide]] · [[2026-karpathy-llm-wiki]]
