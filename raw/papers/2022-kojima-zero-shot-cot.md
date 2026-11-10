# [剪輯筆記] Large Language Models are Zero-Shot Reasoners

- 作者：Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, Yusuke Iwasawa
- 出處：arXiv:2205.11916（2022-05），NeurIPS 2022 接受
- 網址：https://arxiv.org/abs/2205.11916
- 擷取日期：2026-11-10
- 說明：repo 只存摘要筆記；全文請見上方連結。

## 摘要重點（依論文摘要整理）
- 不需要任何範例，只要在答案前加上一句 "Let's think step by step"，就能引出多步驟推理（Zero-shot-CoT）。
- 模型：InstructGPT（text-davinci-002）、PaLM 540B。
- 結果（text-davinci-002）：MultiArith 17.7% → 78.7%；GSM8K 10.4% → 40.7%。PaLM 也有相近幅度的提升。
- 測試任務：算術（MultiArith、GSM8K、AQUA-RAT、SVAMP）、符號推理（Last Letter、Coin Flip）、
  其他邏輯推理（Date Understanding、Tracking Shuffled Objects）。
- 主張：LLM 本身就是不錯的零樣本推理者；在做微調資料或 few-shot 範例之前，應該先試試零樣本提示的能力。
