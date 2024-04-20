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
|------|------------------|-----------|--------------------------------------------------------------|

## Datasets

LogEval selects 4,000 publicly available log data entries and designs 15 different prompts for each task to ensure the comprehensiveness and fairness of the evaluation. The table below provides an overview of sources of log data entries and the reference of 15 different prompts is .

| Dataset     | The number of log entries | Reference                                                    |
|-------------|---------------------------|--------------------------------------------------------------|

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
    <td></td>
  </tr>
  <tr>
    <td> LogRobust </td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2"> Log Parsing </td>
    <td> Drain </td>
    <td></td>
  </tr>
  <tr>
    <td> LogPPT </td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2"> Log Failure Diagnosis </td>
    <td> LogKG </td>
    <td></td>
  </tr>
  <tr>
    <td> LogCluster </td>
    <td></td>
  </tr>
  <tr>
    <td> Log Summarization Extraction </td>
    <td> LogSummary </td>
    <td></td>
  </tr>
</table>

## Benchmark Results

### Log Parsing

### Log Anomaly Detection

### Log Failure Diagnosis

### Log Summarization Extraction
