<div align= "center">
  <h1> LogEval: A Comprehensive Benchmark Suite for Large Language Models In Log Analysis </h1>
</div>

## Table of Contents

- [Introduction](#introduction)
- [LogEval Methods](#LogEval-methods)
- [Datasets](#datasets)
- [Evaluation Measures](#evaluation-measures)
- [Benchmark Results](#benchmark-results)
<!---
    - [Log Parsing](#log-parsing)
    - [Log Anomaly Detection](#log-anomaly-detection)
    - [Log Failure Diagnosis](#log-failure-diagnosis)
    - [Log Summary](#log-summary)
    - [Performance on Inference Time and Average Token](#performance-on-inference-time-and-average-token)
    - [Performance on Different parameters](#performance-on-different-parameters)
    - [Performance on Different Languages](#performance-on-different-languages)
-->

## Introduction

LogEval is a benchmark suite for LLMs in log analysis tasks, to evaluate LLMs’ capabilities in log analysis at different competency levels for the first time.
<img src="./figures/framework.png">

## LogEval Methods

LogEval evaluated various LLMs on LogEval to understand their abilities in addressing different types of questions (multiple-choice and open-ended) and various log analysis tasks. The table below provides an overview of these LLMs along with their references.

| Time | Paper            | Model                    | Reference                                                    |
| ---- | ----- |--------------------------| -----  |
| 2023  | GPT-4 Technical Report | GPT-4                    |  https://platform.openai.com/docs/api-reference/chat/create |
| 2022  | https://openai.com/blog/chatgpt | GPT-3.5                  |  https://platform.openai.com/docs/api-reference/chat/create |
| 2024  | https://www.anthropic.com/news/claude-3-family | Claude-3-Sonnet          | https://www.anthropic.com/api | 
| 2023 | Gemini: A Family of Highly Capable Multimodal Models | Gemini-Pro               | https://gemini.google.com/app |
| 2023 | Mistral 7B | Mistral-7B               | https://github.com/mistralai/mistral-src |
| 2024 | InternLM2 Technical Report | InternLM2-Chat-7B/20B    | https://github.com/InternLM/InternLM |
| 2023 | https://codefuse.yuque.com/eoxx1u/iuztli/scqgrm7zr4v0e7mg | DevOps-Model-7B/14B-Chat | https://github.com/codefuse-ai/CodeFuse-DevOps-Model |
| 2023 | https://github.com/FlagAI-Open/Aquila2/blob/main/README_CN.md | AquilaChat2-7B           | https://github.com/FlagAI-Open/Aquila2/ |
| 2024 | https://zhipuai.cn/devday | ChatGLM4                 | https://open.bigmodel.cn/dev/api#glm-4 |
| 2023 | Llama 2: Open Foundation and Fine-Tuned Chat Models | LLaMA-2-7/13/70B         | https://github.com/meta-llama/llama |
| 2024 | https://qwenlm.github.io/blog/qwen1.5/ | Qwen-1.5-7/14/72B-Chat   | https://github.com/QwenLM/Qwen1.5 |
| 2023 | Baichuan 2: Open Large-scale Language Models | Baichuan2-13B-Chat       | https://github.com/baichuan-inc/Baichuan2 |

## Datasets

LogEval selects 4,000 publicly available log data entries and designs 15 different prompts for each task to ensure the comprehensiveness and fairness of the evaluation. The tables below provides an overview of sources of log data entries and some of the reference of 15 different prompts.

| Task                                | Dataset     | The number of log entries | Reference                                                    |
|-------------------------------------|-------------|---------------------------|--------------------------------------------------------------|
| Log parsing & Log anomaly detection |BGL|2000|https://github.com/logpai/loghub|
| Log parsing & Log anomaly detection |Thunderbird|2000|https://github.com/logpai/loghub|
| Log failure diagnosis               |cmcc|45880|undisclosed|
| Log failure diagnosis               |aliyun|34120|https://tianchi.aliyun.com/dataset/121954|
| Log summary                         |BGL|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|
| Log summary                         |HDFS|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|
| Log summary                         |HPC|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|
| Log summary                         |Spark|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|
| Log summary                         |Zookeeper|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|
| Log summary                         |Proxifier|2000|https://github.com/WeibinMeng/LogSummary/tree/main/data/summary/logs|

<table>
  <tr>
    <th>Task</th>
    <th>English</th>
    <th>Chinese</th>
  </tr>
  <tr>
    <td rowspan="3">Log parsing</td>
    <td>
      1.Parse the following log into a template format，replacing variable parts with a wildcard <*>：[log]
    </td>
    <td>
      1.将以下日志解析为结构化模板，用<*>替换变量部分：[log]
    </td>
  </tr>
  <tr>
    <td>
      2.Replace the variable parts with <*> to convert the following log into a structured template: [log]
    </td>
    <td>
      2.用 <*> 代替变量部分，将以下日志转换为结构化模板:[log]
    </td>
  </tr>
  <tr>
    <td>
      3.Transform the raw log [log] into a log template by replacing variable segments with <*>
    </td>
    <td>
      3.用 <*>替换变量部分，将原始日志 [log] 转换为日志模板
    </td>
  </tr>
  <tr>
    <td rowspan="3">Log anomaly detection</td>
    <td>1.Please review the log entry and explicitly mark it as "normal" or "abnormal," only output "normal" or "abnormal.</td>
    <td>1.请审查日志，并明确标记为“正常”或“异常”，只输出“正常”或“异常”即可</td>
  </tr>
  <tr>
    <td>2.Analyze the content of the log entry, directly classify it as "normal" or "abnormal," only output "normal" or "abnormal."</td>
    <td>2.分析日志中的内容，直接分类为“正常”或“异常”，只输出“正常”或“异常”即可</td>
  </tr>
  <tr>
    <td>3.Please check the log entry, and determine whether it belongs to the "normal" category or the "abnormal" category, only output "normal" or "abnormal."</td>
    <td>3.请检查日志，并判断其为“正常”类别，还是“异常”类别，只输出“正常”或“异常”即可</td>
  </tr>
  <tr>
    <td rowspan="3">Log failure diagnosis</td>
    <td>1.In our data scenario, there are several types of faults {fault types}. Analyze the log [log] and identify the type of fault that occurred. Only output the fault type.</td>
    <td>1.我们的数据场景有以下几种故障{故障类型}，分析日志 [log]，识别出现的故障类型，只输出故障类型即可</td>
  </tr>
  <tr>
    <td>2.In our data scenario, there are several types of faults {fault types}. Based on the information in the log [log], determine which type of fault the log represents. Only output the fault type.</td>
    <td>2.我们的数据场景有以下几种故障{故障类型}，根据日志 [log] 中的信息，判断日志是哪类故障，只输出故障类型即可</td>
  </tr>
  <tr>
    <td>3.In our data scenario, there are several types of faults {fault types}. Use the detailed information provided by the log [log] to conduct an in-depth analysis to determine the category of the fault. Only output the fault type.</td>
    <td>3.我们的数据场景有以下几种故障{故障类型}，使用日志 [log] 提供的详细信息，进行深入分析以确定故障的类别，只输出故障类型即可</td>
  </tr>
  <tr>
    <td rowspan="3">Log summary</td>
    <td>1.Analyze the following 20 logs [log], extract key information, phrases, sentences, or recurring content to generate a summary, only output the summary.</td>
    <td>1.分析以下20条日志 [log]，提取其中的关键信息、短语、句子或重复出现的内容，以生成摘要，只输出摘要即可</td>
  </tr>
  <tr>
    <td>2.Extract the most important events, phrases, and activities or recurring content from the following 20 logs [log], create a concise log overview, only output the summary.</td>
    <td>2.从以下20条日志 [log] 中提取最重要的事件、短语和活动或重复出现的内容，生成一个简明的日志概要，只输出摘要即可</td>
  </tr>
  <tr>
    <td>3.Extract key events, sentence phrases, or recurring information from the following 20 logs [log] to form a comprehensive summary, only output the summary.</td>
    <td>3.从以下20条日志 [log] 中提取关键事件、句子短语或重复出现的信息，以形成一个全面的摘要，只输出摘要即可</td>
  </tr>
</table>

## Evaluation Measures

The benchmark covers tasks such as Log Parsing(Subjective Questions), Log Anomaly Detection, Log Failure Diagnosis(Objective Questions), and Log Summary(Subjective Questions).

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

4. Log summary

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
    <td>undisclosed</td>
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
    <td> Log Summary </td>
    <td> LogSummary </td>
    <td>https://github.com/LogSummary/code-and-datasets</td>
  </tr>
</table>

## Benchmark Results

The Accuracy in zero-shot Naive Q&A:
<img src="figures/The Accuracy in zero-shot Naive Q&A.png">

The Accuracy in few-shot Naive Q&A:
<img src="figures/The Accuracy in few-shot Naive Q&A.png">

<!---
### Log Parsing
Log Parsing Zero shot/few shot Chinese Naive Q&A Accuracy
<img src="./figures/3.png">
Log Parsing Zero shot/few shot English Naive Q&A Accuracy
<img src="./figures/4.png">
### Log Anomaly Detection
Log Anomaly Detection zero shot/few shot Chinese Naive Q&A Accuracy
<img src="./figures/5.png">
Log Anomaly Detection zero shot/few shot English Naive Q&A Accuracy
<img src="./figures/6.png">
Log Anomaly Detection zero shot/few shot Chinese Naive Q&A F1-score
<img src="./figures/7.png">
Log Anomaly Detection zero shot/few shot English Naive Q&A F1-score
<img src="./figures/8.png">
Log Anomaly Detection zero shot/few shot Chinese SC Q&A Accuracy
<img src="./figures/17.png">
Log Anomaly Detection zero shot/few shot English SC Q&A Accuracy
<img src="./figures/18.png">
Log Anomaly Detection zero shot/few shot Chinese SC Q&A F1 score
<img src="./figures/19.png">
Log Anomaly Detection zero shot/few shot English SC Q&A F1-score
<img src="./figures/20.png">
Log Anomaly Detection zero shot/few shot English SC Variance
<img src="./figures/33.png">
Log Anomaly Detection zero shot/few shot Chinese SC Variance
<img src="./figures/34.png">
### Log Failure Diagnosis
Log Failure Diagnosis Zero shot/few shot Chinese Naive Q&A Accuracy
<img src="./figures/10.png">
Log Failure Diagnosis Zero shot/few shot English Naive Q&A Accuracy
<img src="./figures/11.png">
Log Failure Diagnosis Zero shot/few shot Chinese Naive Q&A F1-score
<img src="./figures/12.png">
Log Failure Diagnosis Zero shot/few shot English Naive Q&A F1-score
<img src="./figures/13.png">
Log Failure Diagnosis zero shot/few shot Chinese SC Q&A Accuracy
<img src="./figures/21.png">
Log Failure Diagnosis zero shot/few shot English SC Q&A Accuracy
<img src="./figures/22.png">
Log Failure Diagnosis zero shot/few shot Chinese SC Q&A F1 score
<img src="./figures/23.png">
Log Failure Diagnosis zero shot/few shot English SC Q&A F1 score
<img src="./figures/24.png">
Log Failure Diagnosis zero shot/few shot English SC Variance
<img src="./figures/35.png">
Log Failure Diagnosis zero shot/few shot Chinese SC Variance
<img src="./figures/36.png">
### Log Summary
Log Summary Zero shot/few shot Chinese Naive Q&A Accuracy
<img src="./figures/15.png">
Log Summary Zero shot/few shot English Naive Q&A Accuracy
<img src="./figures/16.png">
### Performance on Inference Time and Average Token
The Inference Time in the Naive Q&A situation in log analysis by zero shot
<img src="./figures/25.png">
The Average Token in the Naive Q&A situation in log analysis by zero shot
<img src="./figures/26.png">
### Performance on Different parameters
The Accuracy of LLaMa2 and Qwen1.5 in zero-shot English Naive Q&A
<img src="./figures/27.png">
### Performance on Different Languages
The performance of LLMs on failure diagnosis tasks under the "zero-shot" naive Q&A in both Chinese and English test sets
<img src="./figures/29.png">
-->