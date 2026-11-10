---
title: 幻覺（Hallucination）
type: concept
tags: [risk, reliability]
sources: [2022-yao-react, 2026-karpathy-llm-wiki]
updated: 2026-11-10
---

# 幻覺（Hallucination）

## 定義
模型產生**看起來合理、但沒有根據或錯誤**的內容。

## wiki 目前收錄的對策
- **讓推理有外部依據**：[[react]] 透過查 Wikipedia，減少 CoT 推理中的幻覺和錯誤傳遞（來源：[[2022-yao-react]]）。
- **提供資料再回答**：[[rag]]，並要求「只根據提供的文件回答」。
- **可追溯的來源**：[[llm-wiki]] 的每個論點都連回來源頁；但 lint 不保證事實正確（來源：[[2026-karpathy-llm-wiki]]）。
- **自我檢查**：[[self-check]]、[[self-consistency]]（推論：多條推理互相比對，能抓出部分錯誤）。

## 待補
幻覺的成因、量測方法尚無來源，可以從 [[2024-schulhoff-prompt-report]] 全文或其他文獻補充。

## 相關頁面
[[react]] · [[rag]] · [[self-check]] · [[llm-wiki]]

## 來源
[[2022-yao-react]] · [[2026-karpathy-llm-wiki]]
