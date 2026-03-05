# System Architecture

## Overview

The AI Tutor system is designed as a local AI-powered tutoring platform
deployed on a school server. Students access the system through a web
browser while the AI model runs locally on the institution's
infrastructure.

The architecture ensures:

-   privacy of student data
-   no reliance on external APIs
-   controlled educational responses
-   safety guardrails for K-12 environments

------------------------------------------------------------------------

## High-Level Architecture

Student Browser \| \| HTTP \| Flask Web Server \| \| REST API \| Ollama
Runtime \| DeepSeek-R1-8B Language Model

------------------------------------------------------------------------

## Component Description

### Web Interface

Implemented using HTML and JavaScript.

Responsibilities:

-   display chat interface
-   maintain conversation history
-   send prompts to server
-   render AI responses

Technologies:

-   HTML5
-   JavaScript
-   Marked.js for Markdown rendering
-   MathJax for equations

------------------------------------------------------------------------

### Flask Backend

The Flask server acts as the controller of the application.

Responsibilities:

-   receive user prompts
-   enforce safety guardrails
-   add system prompt
-   communicate with the AI model
-   return responses to client

Key endpoint:

POST /chat

------------------------------------------------------------------------

### AI Runtime

The system uses Ollama to run the language model locally.

Advantages:

-   local inference
-   faster response times
-   full data privacy
-   offline capability

------------------------------------------------------------------------

### AI Model

Model used:

DeepSeek-R1-8B

Capabilities:

-   reasoning
-   tutoring assistance
-   conversational interaction
-   explanation generation

------------------------------------------------------------------------

## Data Flow

1.  Student enters question
2.  Browser sends prompt to Flask server
3.  Server checks guardrails
4.  Server sends conversation to Ollama
5.  Model generates response
6.  Server returns response to browser
