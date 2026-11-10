# [剪輯筆記] OpenAI — Prompt engineering（官方提示指南）

- 出處：OpenAI API 文件
- 網址：https://developers.openai.com/api/docs/guides/prompt-engineering
  （舊網址 platform.openai.com/docs/guides/prompt-engineering 會轉址到這裡）
- 擷取日期：2026-11-10；文件會持續更新，內容以擷取當下為準。
- 說明：repo 只存重點筆記。

## 選模型
- **推理模型（reasoning models）**：內部會產生思維鏈，擅長複雜多步驟任務，但較慢、較貴。
- **GPT 模型**：快、便宜，但需要**明確的指令**。
- 大模型與小模型（mini／nano）是能力和速度、成本的取捨。

## 迭代與評測
- 輸出不是確定性的，提示工程是技巧加上反覆迭代。
- 正式環境要**固定模型版本（pin snapshot）**，並建立測試與**評測（evals）**，在改 prompt 或升級模型時量測效果。

## 訊息角色
- `instructions` 參數設定高層行為（語氣、目標、範例），優先於 `input`。
- `developer` 訊息（開發者）權限高於 `user` 訊息（使用者）。
- 比喻：developer 訊息像函式定義（規則與邏輯），user 訊息像函式的參數。

## 用 Markdown 和 XML 排版
- Markdown 標題、清單區分段落與層級；XML 標籤標出文件等內容的起訖，屬性可加上中繼資料。
- 建議的 developer 訊息四段結構：**Identity（身分）→ Instructions（指令）→ Examples（範例）→ Context（脈絡）**，脈絡通常放最後。

## 其他技巧
- **Prompt caching**：常重複使用的內容放在 prompt 開頭，可以省成本和延遲。
- **Few-shot**：在 developer 訊息放幾個輸入／輸出範例，取代微調；範例要多樣。
- **Context 與 RAG**：把模型訓練資料沒有的內容放進 prompt（可以用向量資料庫或檔案搜尋工具）；要留意 context window 大小。
- **Agent 任務**：要求模型完成前先完整規劃、在關鍵步驟說明為什麼要呼叫工具、用 TODO 或評分標準追蹤進度。

## 推理模型 vs GPT 模型的提示差異
- 推理模型通常適合**高層次的指引**，細節可以自己想；GPT 模型適合**明確、精確的指令**。
- 文件的比喻：推理模型像**資深同事**，GPT 模型像**資淺同事**。
