<div align= "center">
  <h1> LogEval: A Comprehensive Benchmark Suite for Large Language Models In Log Analysis </h1>
</div>

## Table of Contents

- [Introduction](#introduction)
- [LogEval Methods](#LogEval-methods)
- [Datasets](#datasets)
- [Evaluation Measures](#evaluation-measures)
- [Benchmark Results](#benchmark-results)
    - [Log Parsing](#log-parsing)
    - [Log Anomaly Detection](#log-anormaly-detection)
    - [Log Failure Diagnosis](#log-failure-diagnosis)
    - [Log Summarization Extraction](#log-summary-extraction)

## Introduction

LogEval is a benchmark suite for LLMs in log analysis tasks, to evaluate LLMs’ capabilities in log analysis at different competency levels for the first time.

## LogEval Methods

LogEval evaluated various LLMs on LogEval to understand their abilities in addressing different types of questions (multiple-choice and open-ended) and various log analysis tasks. The table below provides an overview of these LLMs along with their references.

| Time | Paper            | Model     | Reference                                                    |
| ---- | ----- | ------  | -----  |
| 2023  | GPT-4 Technical Report | GPT4  |  https://platform.openai.com/docs/api-reference/chat/create |
| 2022  | https://openai.com/blog/chatgpt | GPT3.5  |  https://platform.openai.com/docs/api-reference/chat/create |
| 2024  | https://www.anthropic.com/news/claude-3-family | Claude-3-Sonnet |  
| 2023 | Gemini: A Family of Highly Capable Multimodal Models | Gemini-Pro |  |
| 2023 | Mistral 7B | Mistral 7B | https://github.com/mistralai/mistral-src |
| 2024 | InternLM2 Technical Report | InternLM2-Chat 7B/20B | https://github.com/InternLM/InternLM |
| 2023 | https://codefuse.yuque.com/eoxx1u/iuztli/scqgrm7zr4v0e7mg | DevOps-Model-Chat 7B/14B | https://github.com/codefuse-ai/CodeFuse-DevOps-Model |
| 2023 | https://github.com/FlagAI-Open/Aquila2/blob/main/README_CN.md | AquilaChat2 7B | https://github.com/FlagAI-Open/Aquila2/ |
| 2024 | https://zhipuai.cn/devday | ChatGLM4 | https://open.bigmodel.cn/dev/api#glm-4 |
| 2023 | Llama 2: Open Foundation and Fine-Tuned Chat Models | LLaMA-2 7/13/70B | https://github.com/meta-llama/llama |
| 2024 | https://qwenlm.github.io/blog/qwen1.5/ | Qwen-1.5-Chat 7/14/72B | https://github.com/QwenLM/Qwen1.5 |
| 2023 | Baichuan 2: Open Large-scale Language Models | Baichuan2-Chat 13B | https://github.com/baichuan-inc/Baichuan2 |

## Datasets

LogEval selects 4,000 publicly available log data entries and designs 15 different prompts for each task to ensure the comprehensiveness and fairness of the evaluation. The tables below provides an overview of sources of log data entries and some of the reference of 15 different prompts.

| Dataset     | The number of log entries | Reference                                                    |
|-------------|---------------------------|--------------------------------------------------------------|
|CMCC| | |
|aliyun| | |

## Evaluation Measures

The benchmark covers tasks such as Log Parsing(Subjective Questions), Log Anomaly Detection, Log Failure Diagnosis(Objective Questions), and Log Summarization Extraction(Subjective Questions).

1. Log parsing

  - Original question-answer, zero shot
  - Original question-answer, few shot

2. Log anomaly detection

  - Original question-answer, zero shot
  - Self-consistency, zero shot
  - Original question-answer, few shot
  - Self-consistency, few shot

3. Log failure diagnosis

  - Original question-answer, zero shot
  - Self-consistency, zero shot
  - Original question-answer, few shot
  - Self-consistency, few shot

4. Log summarization extraction

  - Original question-answer, zero shot
  - Original question-answer, few shot

To measure LLMs’ capabilities in log analysis better, LogEval adopts some methods as baseline, shown as the below table.

<table>
  <tr>
    <th> Log Task </th>
    <th> Method </th>
    <th> Reference </th>
  </tr>
  <tr>
    <td rowspan="2"> Log Anomaly Detection </td>
    <td> NeuralLog </td>
    <td>https://github.com/vanhoanglepsa/NeuralLog</td>
  </tr>
  <tr>
    <td> LogRobust </td>
    <td>unpublished</td>
  </tr>
  <tr>
    <td rowspan="2"> Log Parsing </td>
    <td> Drain </td>
    <td>http://appsrv.cse.cuhk.edu.hk/ ∼pjhe/Drain.py</td>
  </tr>
  <tr>
    <td> LogPPT </td>
    <td>https://github.com/LogIntelligence/LogPPT</td>
  </tr>
  <tr>
    <td rowspan="2"> Log Failure Diagnosis </td>
    <td> LogKG </td>
    <td>https://anonymous.4open.science/r/LogKG-A6BD</td>
  </tr>
  <tr>
    <td> LogCluster </td>
    <td>https://ristov.github.io/logcluster/</td>
  </tr>
  <tr>
    <td> Log Summarization Extraction </td>
    <td> LogSummary </td>
    <td>https://github.com/LogSummary/code-and-datasets</td>
  </tr>
</table>

## Benchmark Results

### Log Parsing

### Log Anomaly Detection

### Log Failure Diagnosis

### Log Summarization Extraction
