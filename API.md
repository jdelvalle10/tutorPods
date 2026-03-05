# API Documentation

Base URL:

http://localhost:5000

------------------------------------------------------------------------

## POST /chat

Send conversation history to the AI tutor.

### Request

Content-Type: application/json

Example:

{ "messages": \[ {"role": "user", "content": "Explain photosynthesis"}
\] }

------------------------------------------------------------------------

### Response

{ "response": "Let's think about the role of sunlight in plants..." }

------------------------------------------------------------------------

### Error Responses

403 -- Guardrail triggered

{ "response": "Please keep your questions appropriate for a classroom
environment." }

500 -- Model error

{ "error": "Failed to connect to the AI model." }
