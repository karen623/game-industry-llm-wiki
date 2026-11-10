# [剪輯筆記] ReAct: Synergizing Reasoning and Acting in Language Models

- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 出處：arXiv:2210.03629（2022-10-06 首次提交；v3 修訂於 2023-03-10），ICLR 2023
- 網址：https://arxiv.org/abs/2210.03629
- 擷取日期：2026-11-10（只讀了摘要頁）

## 摘要重點
- 背景：「推理」（如 CoT）和「行動」（如產生行動計畫）過去大多分開研究。
- 方法：讓 LLM **交錯產生推理軌跡（reasoning traces）與任務行動（actions）**。
  推理幫模型建立、追蹤、更新行動計畫並處理例外；行動讓模型從外部來源取得資訊。
- 問答（HotpotQA）與事實查核（FEVER）：模型透過簡單的 **Wikipedia API** 互動。摘要沒有給這兩項的具體數字。
- 互動式決策（ALFWorld、WebShop）：只用 1–2 個範例，成功率比模仿學習與強化學習方法分別**高 34% 與 10%（絕對值）**。
- 作者主張：靠查 Wikipedia 讓推理有依據，ReAct 能**減少 CoT 常見的幻覺與錯誤傳遞**；
  其解題軌跡也比沒有推理軌跡的方法更容易解讀、更可信。
