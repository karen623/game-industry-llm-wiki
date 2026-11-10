# 00 wiki 快照（階段 0 產出）

- 版本：v2（2026-11-10，ingest 5 份新資料後重跑）
- 狀態：✅ C0 通過
- 前一版 v1：3 份資料、17 頁、51 條連結

## 統計
| 項目 | v1 | **v2（目前）** |
|---|---|---|
| 原始資料（raw/） | 3 | **8**：論文 5、官方指南 2、文章 1 |
| wiki 頁面（不含 index、log） | 17 | **30**：技巧 10、概念 6、來源 8、模型 2、比較 2、問答 1、總覽 1 |
| 頁面間連結（不含總覽） | 16 節點、51 條 | **29 節點、109 條** |
| 連結最多的頁面 | chain-of-thought（12） | chain-of-thought（20）、anthropic-prompting-best-practices（13）、extended-thinking（13）、few-shot-prompting（12） |
| 標註「（推論）」 | 5 處 | 10 處 |
| 規劃中、還沒有頁面的主題 | 8 個 | 5 個：tree-of-thoughts、prompt-chaining、context-engineering、context-window、prompt-injection |

## C0 wiki 健康檢查
| 檢查 | 結果 |
|---|---|
| 每頁都有 frontmatter | ✅ |
| 非來源頁都有 sources，且 sources 都指向存在的來源頁 | ✅ |
| 沒有孤兒頁 | ✅ |
| 每頁都列在 index.md | ✅ |
| 斷掉的連結只能是規劃中的主題 | ✅ 只有總覽裡的 5 個 ☐ 主題 |

## 備註
- Karpathy 原文已 ingest → 大綱裡「方法」段落現在有正式來源（[[2026-karpathy-llm-wiki]]、[[llm-wiki]]）。
- 4 篇論文都只讀了 arXiv 摘要；Prompt Report 的 58 種技巧清單尚未 ingest。
