# Doral Academy AI Tutor

A local AI tutoring system designed for K-12 educational environments.  
The system provides safe, guided tutoring using a Socratic teaching approach while running entirely on a local server.

The project integrates a web-based chat interface with a locally hosted large language model using Ollama.

---

## Overview

The Doral Academy AI Tutor allows students to ask questions about academic subjects and receive guided assistance from an AI tutor.

Instead of providing direct answers, the system encourages learning through structured guidance.

Key features:

- Local AI inference (no external APIs required)
- Socratic teaching method
- K-12 safety guardrails
- Browser-based interface
- Mathematical equation rendering (MathJax)
- Markdown formatted responses
- Conversation memory
- School server deployment

---

## System Architecture

Student Browser
      |
      | HTTP
      |
Flask Web Server
      |
      | API request
      |
Ollama AI Runtime
      |
DeepSeek-R1-8B Model

---

## Repository Structure
