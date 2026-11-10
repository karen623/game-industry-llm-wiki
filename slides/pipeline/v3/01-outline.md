# v3 / 01 大綱（階段 1）

- 版本：v0.3（依 `requirements.md` 重做）
- 依據：`requirements.md`（R0）、`v3/00-snapshot.md`
- 人工確認：**使用者指示「直接開始做」，跳過 R0、C1 的逐關確認**（依流程 B 全域規則 2 記錄）
- 故事線：照作業的三部分 **建 Wiki → 繳交（需求摘要、AGENTS.md、流程圖、檢查報告）→ 反思**；約 14 分鐘

| # | 段落 | 標題 | 一句話重點 | 對應作業要求 | 引用 |
|---|---|---|---|---|---|
| 1 | 開場 | 用「先討論、後生成」建 Prompt Engineering LLM Wiki | 個人作業：建 wiki、拆流程、做檢查 | — | requirements |
| 2 | 繳交 | 需求摘要 | 作業三部分對應 7 項產出 | 需求摘要 | requirements |
| 3 | 建 Wiki | 為什麼用 LLM Wiki | wiki 把整理結果留下來，知識會累積 | 建 Wiki | llm-wiki、rag |
| 4 | 建 Wiki | 8 篇資料長成一張知識網 | 30 頁、109 條連結，思維鏈是中心 | 建 Wiki（≥5 篇） | 00-snapshot |
| 5 | 建 Wiki | wiki 內容①：思維鏈的演進 | 從手寫範例到模型內建思考 | 建 Wiki | chain-of-thought |
| 6 | 建 Wiki | wiki 內容②：怎麼寫好 prompt | 兩家官方指南的共同建議 | 建 Wiki | anthropic-vs-openai-guides 等 |
| 7 | 繳交 | AGENTS.md：給 AI 的規則 | 三層結構＋引用規則＋禁止事項 | AGENTS.md | CLAUDE.md、AGENTS.md |
| 8 | 繳交 | 流程圖 A：建 wiki | 生成前討論、生成後自動檢查 | workflow 流程圖 | wiki-workflow |
| 9 | 繳交 | 流程圖 B：做簡報 | 需求關卡＋6 階段＋5 道檢查 | workflow 流程圖 | pipeline README |
| 10 | 繳交 | 檢查報告①：一次實際執行（流程 A） | 補討論找到 4 個缺口，K 檢查第 2 輪通過 | 檢查報告 | ingest-run |
| 11 | 繳交 | 檢查報告②：流程 B 每道關卡 | 每關都抓到問題，但沒抓到「方向錯」 | 檢查報告 | check-report |
| 12 | 反思 | 哪個節點最常出錯？ | 最常錯：製作 HTML；代價最大：大綱 | 反思 | reflection |
| 13 | 反思 | 檢查往前移到了哪裡？ | 新增 R0 需求關卡，C0 改用程式檢查 | 反思 | reflection |
| 14 | 結尾 | 收穫與繳交位置 | 檢查要放在最上游 | 交 GitHub | requirements |

## C1 自動檢查
| 檢查 | 結果 |
|---|---|
| 每頁一句話重點 | ✅ 14／14 |
| 每頁至少引用 1 個來源（封面除外） | ✅ |
| 頁數符合時間 | ✅ 14 頁約 14 分鐘（沒有指定時間，用預設） |
| 段落順序 | ✅ 照作業結構：建 Wiki → 繳交 → 反思（需求摘要放在最前面，當作開場） |
| 作業要求都有對應頁面（**v0.2 起不能是「不知道」**） | ✅ 需求摘要 2、建 Wiki 3–6、AGENTS.md 7、流程圖 8–9、檢查報告 10–11、反思 12–13、GitHub 14 |
| 快照是最新版 | ✅ v3/00-snapshot（補討論後） |
| 一句話重點遵守字數上限 | ✅ 最長 18 字 |
