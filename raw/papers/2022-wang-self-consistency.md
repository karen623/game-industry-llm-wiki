# [剪輯筆記] Self-Consistency Improves Chain of Thought Reasoning in Language Models

- 作者：Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- 出處：arXiv:2203.11171（2022-03-21 首次提交；v4 修訂於 2023-03-07），ICLR 2023
- 網址：https://arxiv.org/abs/2203.11171
- 擷取日期：2026-11-10（只讀了摘要頁）

## 摘要重點
- 方法：取代 CoT 原本的貪婪解碼（greedy decoding，只取一條最可能的推理）。
  改成**抽樣多條不同的推理路徑**，再選出**在這些路徑中最一致的答案**（對路徑做邊際化）。
- 直覺：複雜問題通常有多種解法，但正確答案會是同一個。
- 結果（相對於 CoT 提示的提升）：GSM8K +17.9%、SVAMP +11.0%、AQuA +12.2%、StrategyQA +6.4%、ARC-challenge +3.9%。
  摘要沒有說明這些是百分點還是相對提升。
