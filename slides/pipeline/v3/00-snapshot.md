# v3 / 00 wiki 快照（階段 0）

- 日期：2026-11-10（補討論 5 篇之後）
- 產生方式：`python3 scripts/check_wiki.py`（C0 改由程式執行）
- 狀態：✅ C0 通過

## C0 wiki 健康檢查結果

| 檢查 | 結果 | 說明 |
|---|---|---|
| 每頁都有完整 frontmatter，type 與資料夾一致 | ✅ | 29 頁 |
| 非來源頁都有 sources，且都指向存在的來源頁 | ✅ | OK |
| 每頁至少連出 2 個頁面 | ✅ | OK |
| 沒有孤兒頁 | ✅ | OK |
| 斷掉的連結只能是總覽裡 ☐ 規劃中的主題 | ✅ | 斷連結 0 個，皆為規劃中 |
| 每頁都列在 index.md | ✅ | OK |
| index 宣稱的頁數＝實際頁數（分類加總＋總覽） | ✅ | index 寫 30，實際 30（comparison 2、concept 6、model 2、query 1、source 8、technique 10＋總覽 1） |

- 頁面 30（含總覽）、圖譜 29 節點 109 條連結、標註（推論）10 處
- 連結最多：chain-of-thought（20）、anthropic-prompting-best-practices（13）、extended-thinking（13）、openai-prompt-engineering-guide（12）

- 規劃中、還沒有頁面的主題：tree-of-thoughts、prompt-chaining、context-engineering、context-window、prompt-injection（總覽 ☐）
