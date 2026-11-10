---
title: 角色提示（Role Prompting）
type: technique
tags: [prompting-basics]
sources: [anthropic-prompting-best-practices, openai-prompt-engineering-guide]
updated: 2026-11-10
---

# 角色提示（Role Prompting）

## 一句話定義
在 system prompt 設定模型扮演的角色，讓行為和語氣聚焦在你的情境。

## 怎麼用
```text
System: 你是一位耐心的高中數學老師，擅長用生活例子解釋觀念。
```
官方指南指出：**就算只有一句話也會有差**（來源：[[anthropic-prompting-best-practices]]）。

## 訊息角色的權限（來源：[[openai-prompt-engineering-guide]]）
- **developer** 訊息（開發者寫的規則）權限高於 **user** 訊息（使用者輸入）。
- 比喻：developer 訊息像函式定義，user 訊息像函式的參數。
- 實務：角色和規則放 system／developer 訊息，使用者的問題放 user 訊息。

## 相關頁面
[[be-clear-and-direct]] · [[claude]] · [[gpt]] · [[anthropic-vs-openai-guides]]

## 來源
[[anthropic-prompting-best-practices]] · [[openai-prompt-engineering-guide]]
