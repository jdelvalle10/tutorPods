# Security Model

## Overview

The AI Tutor system is designed specifically for use in educational
environments. Security and student safety are primary design goals.

------------------------------------------------------------------------

## Safety Guardrails

Before a prompt is sent to the AI model, it is scanned for prohibited
content.

Blocked topics include:

-   violence
-   sexual content
-   illegal activities
-   drugs
-   hate speech
-   harassment
-   explicit language

If detected:

-   the request is blocked
-   the server logs the event
-   an alert is generated

------------------------------------------------------------------------

## Local Processing

All AI inference occurs locally on the school server.

Benefits:

-   student data never leaves the school network
-   protection against external data exposure
-   compliance with educational privacy policies

------------------------------------------------------------------------

## Classroom Safe Responses

The AI tutor is designed to:

-   guide learning through questions
-   avoid giving direct answers to assignments
-   encourage student reasoning

------------------------------------------------------------------------

## Monitoring

Inappropriate prompts trigger:

-   console alert
-   server notification
-   optional administrator notification
