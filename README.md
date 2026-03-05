# Doral Academy AI Tutor

A local AI tutoring system designed for K‑12 educational environments.\
The system provides safe, guided tutoring using a Socratic teaching
approach while running entirely on a local server.

The project integrates a web-based chat interface with a locally hosted
large language model using Ollama.

------------------------------------------------------------------------

## Overview

The Doral Academy AI Tutor allows students to ask questions about
academic subjects and receive guided assistance from an AI tutor.

Instead of providing direct answers, the system encourages learning
through structured guidance.

Key features:

-   Local AI inference (no external APIs required)
-   Socratic teaching method
-   K‑12 safety guardrails
-   Browser-based interface
-   Mathematical equation rendering (MathJax)
-   Markdown formatted responses
-   Conversation memory
-   School server deployment

------------------------------------------------------------------------

## System Architecture

Student Browser \| \| HTTP \| Flask Web Server \| \| API request \|
Ollama AI Runtime \| DeepSeek‑R1‑8B Model

------------------------------------------------------------------------

## Repository Structure

AI-Tutor/ │ ├── tutoring_server.py ├── templates/ │ └── index.html │ ├──
static/ │ └── background.png │ ├── index.bak.html ├── index.bak.txt │
└── README.md

------------------------------------------------------------------------

## Key Components

### 1. Frontend

The interface is a browser-based chat application written in HTML and
JavaScript.

Features include:

-   Chat interface
-   Conversation history
-   Markdown rendering
-   MathJax equation rendering
-   Loading spinner
-   Responsive layout

Students send questions through the interface and responses are
displayed in formatted form.

------------------------------------------------------------------------

### 2. Backend Server

The backend is implemented using Flask.

Main responsibilities:

-   Handle student chat requests
-   Enforce safety guardrails
-   Forward requests to the local LLM
-   Return responses to the client

Main endpoint:

POST /chat

The backend receives the entire conversation history from the browser
and forwards it to the model.

------------------------------------------------------------------------

### 3. AI Model

The system runs a locally hosted model through Ollama.

Model used:

DeepSeek‑R1‑8B

This model is designed for reasoning and educational assistance.

------------------------------------------------------------------------

### 4. Safety Guardrails

To ensure safe use in K‑12 environments, prompts are filtered before
being sent to the AI model.

Blocked content categories include:

-   Violence
-   Sexual content
-   Illegal activity
-   Drugs
-   Harassment
-   Explicit language

If inappropriate content is detected:

-   The prompt is blocked
-   A warning message is returned
-   A server alert is triggered

------------------------------------------------------------------------

### 5. Socratic Teaching System Prompt

The AI tutor is configured to teach using the Socratic method.

Instead of giving direct answers, the model:

-   Asks guiding questions
-   Provides hints
-   Breaks problems into smaller steps
-   Encourages student reasoning

------------------------------------------------------------------------

## Installation

### 1. Install Python

Python 3.9 or newer recommended.

------------------------------------------------------------------------

### 2. Install dependencies

pip install flask requests

------------------------------------------------------------------------

### 3. Install Ollama

Download from:

https://ollama.ai

------------------------------------------------------------------------

### 4. Pull the model

ollama pull deepseek-r1:8b

------------------------------------------------------------------------

### 5. Start Ollama

ollama serve

------------------------------------------------------------------------

### 6. Run the server

python tutoring_server.py

Server will start on:

http://localhost:5000

------------------------------------------------------------------------

### 7. Open the interface

http://SERVER_IP:5000

Students can now access the AI tutor.

------------------------------------------------------------------------

## API Documentation

### POST /chat

Send conversation history to the AI tutor.

Request format:

{ "messages": \[ {"role": "user", "content": "What is photosynthesis?"}
\] }

Response:

{ "response": "Let's think about this together..." }

------------------------------------------------------------------------

## Security Design

The system includes multiple safety mechanisms:

### Guardrails

Keyword filtering prevents harmful prompts.

### Local inference

No student data is sent to external AI services.

### Classroom safe responses

The AI tutor refuses to:

-   Complete assignments directly
-   Generate harmful content
-   Assist cheating

------------------------------------------------------------------------

## Future Improvements

Possible upgrades include:

-   Authentication system
-   Teacher dashboards
-   Classroom analytics
-   RAG knowledge base
-   Curriculum alignment
-   Logging and monitoring

------------------------------------------------------------------------

## Author

Jose Luis Del Valle\
Cybersecurity and Artificial Intelligence Professor
