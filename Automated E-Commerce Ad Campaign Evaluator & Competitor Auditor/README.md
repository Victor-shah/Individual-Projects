# Agentic E-Commerce Ad Copy Inspector

An agentic, zero-cost AI workflow that automates ad copy creation and brand compliance validation. Performed by **LangGraph** for multi-step orchestration, **FastMCP** (Model Context Protocol) for tool integration, and **Ollama** (`qwen2.5:3b`) for private, local LLM execution.

---

## Architecture Overview

This project implements a **Generator-Evaluator** pattern to eliminate manual review overhead while preventing hallucinated or off-brand marketing copy.

```text
       ┌─────────────────────────┐
       │   LangGraph Engine      │
       │  (Orchestration Loop)   │
       └───────────┬─────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐ ┌──────────────────┐
│ Local Inference  │ │  FastMCP Server  │
│  (Ollama 3B)     │ │  (Tool Layer)    │
└──────────────────┘ └──────────────────┘

```
## What is the problem?
Marketing team wastes hours of their time writing ad copy and verifying brand safety compliance. Basically, looking for forbidden words, poor brand alignment and hallucinations. Our objective is to build an
automated system that generates ad copy, verify compliance via custom tools, and automatically loops to fix errors by the final output. 

## What data do I have?
1. Input data: Product ID or Campaign brief
2. Reference data: Banned words list, Brand Guidelines
3. Generated data: Draft text, tool execution output, iteration state tracking

## What approach fits?
1. Orchestration layer: A LangGraph finite state machine containing explicit state nodes.
2. Tool layer: A fast MCP server exposing python functions.
3. Inference layer: A local, open weight LLM running through Ollama.

## How do I evaluate it?
1. Deterministic checks: Validation rules via python (checking if banned words exist or max character count exceeded).
2. LLM as a judge loop.
3. Convergence rate: Tracking percentage of generated inputs that reach an approved state.

## How do I deploy it?
1. Local developer environment
2. Production packaging: It runs heedlessly on a cloud server (AWS, EC2, GCP, Azure)

## How do I monitor it?
1. Execution tracking: LangSmith or Arize Phoenix to monitor step-by-step state transitions, node input, token consumptions
2. Structured logs: Output JSON logs tracking tool

## What can go wrong?
1. Infinite loops
2. Small LLM Hallucinations
3. Port/Server disconnections
