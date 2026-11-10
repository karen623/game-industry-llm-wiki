# [剪輯筆記] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- 作者：Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- 出處：arXiv:2201.11903（2022-01-28 首次提交，v6 修訂於 2023-01-10）
- 網址：https://arxiv.org/abs/2201.11903
- 擷取日期：2026-11-10
- 說明：為避免著作權問題，repo 只存摘要筆記；全文請點上方連結閱讀或另存 PDF 於本機。

## 摘要重點（依論文摘要整理）
- 提出「思維鏈提示」：在 prompt 裡放幾個**示範了中間推理步驟**的範例（few-shot exemplars），
  讓模型在回答前也寫出自己的逐步推理。
- 在三個大型語言模型上實驗，任務涵蓋算術、常識、符號推理。
- 一個 540B 參數的模型只用 8 個 CoT 範例，就在 GSM8K（數學應用題）達到當時最佳，
  超越經過微調、並加上驗證器（verifier）的 GPT-3。
- 作者主張：這種推理能力會在**足夠大的模型**中自然湧現。
