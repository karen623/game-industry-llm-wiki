# [剪輯筆記] Anthropic — Prompting best practices（Claude 官方提示指南）

- 出處：Claude 官方文件（platform.claude.com）
- 網址：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  （舊的 chain-of-thought 頁面網址現在會轉址到這頁）
- 擷取日期：2026-11-10；文件會持續更新，內容以擷取當下為準。
- 說明：repo 只存重點筆記，不存全文。

## 一般原則
- **清楚直接**：把 Claude 當成聰明但不了解你情境的新同事。檢驗法：把 prompt 給一個不了解任務的同事看，
  他看不懂，模型也會看不懂。順序重要時用編號步驟。
- **說明背後的原因**：例如不要只寫「絕對不要用刪節號」，而是說明「輸出會被語音朗讀，所以不要用刪節號」，
  模型能從解釋推廣。
- **善用範例（few-shot / multishot）**：範例要貼近實際用途、多樣、用 `<example>` 標籤包起來；建議 3–5 個。
- **用 XML 標籤結構化**：用 `<instructions>`、`<context>`、`<input>` 等區分不同內容；標籤名稱一致，可巢狀。
- **給角色**：在 system prompt 設定角色，一句話就有差。

## 思考與推理（thinking）
- 新一代 Claude 有內建的「思考」（adaptive thinking）：模型依 `effort` 參數與問題難度自行決定要想多少。
  部分最新模型思考一直開著。
- **一般性指示優於逐步規定**：「想得周全一點」常常比人工寫好的步驟清單效果更好。
- **範例在思考模式下仍有效**：範例會影響模型思考時的做法；每個範例寫出問題、方法、預期答案。
- **手動 CoT 是備案**：思考關閉時，可以請模型先推理再回答，並把最終答案放在 `<answer>` 標籤方便擷取。
  但在最新幾代模型上應改用內建思考（必要時降低 effort）；要求把推理寫在 `<thinking>` 標籤裡的 prompt
  可能會被拒絕。
- **請模型自我檢查**：結尾加上「完成前，依照〔測試標準〕驗證你的答案」，對程式與數學特別有效；
  但部分新模型本來就會自我驗證，多加反而造成過度驗證。
- 模型可能想太多：可以在 prompt 裡要求「選定方法就堅持下去」，或降低 effort。
