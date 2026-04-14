# OmnyPark AI Parking Assistant (RAG-based Chatbot Prototype)

## Overview

The OmnyPark AI Parking Assistant is a domain-specific chatbot prototype developed to demonstrate how Artificial Intelligence can improve the public parking experience. This assistant leverages a Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-aware responses to user queries related to parking policies.

The solution showcases how users can quickly understand parking tariffs, free hours, validation rules, and weekend or public holiday policies through natural language interaction.

Unlike generic chatbots, this assistant relies on a structured knowledge base and retrieval pipeline to ensure that responses remain grounded, consistent, and reliable.

---

## Problem Statement

Parking policies are often difficult for users to interpret due to fragmented information across signage, ticketing systems, and websites. Users frequently struggle to understand:

- How long parking is free
- What charges apply after free hours
- Whether validations extend parking time
- If parking rules differ on weekends or public holidays

This project demonstrates how an AI assistant can simplify these interactions by delivering instant, easy-to-understand answers.

---

## Solution Approach

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline, combining document retrieval with large language model reasoning.

The workflow consists of the following steps:

1. Parking policy documents are stored as structured text files
2. Documents are split into smaller chunks for efficient processing
3. Each chunk is converted into embeddings using a Sentence Transformers model
4. Embeddings are stored in a ChromaDB vector database
5. When a user submits a query, relevant chunks are retrieved using similarity search
6. Google Gemini generates a response based only on the retrieved context

This architecture significantly reduces hallucinations and ensures that answers remain grounded in the provided knowledge base.

---

## Chunking Strategy

To preserve contextual continuity and improve retrieval quality, documents are split using an overlapping chunking strategy.

- **Chunk Size:** 500 characters  
- **Chunk Overlap:** 50 characters  

The overlap ensures that important information spanning across chunk boundaries is retained, allowing the retrieval system to capture complete context and improve answer accuracy.

---

## Dataset Description and Maintenance

The dataset consists of structured text files stored in the `data/` directory. Each file represents a specific aspect of parking policy, including:

- tariffs and pricing rules
- free parking duration
- validation policies
- weekend and public holiday rules
- frequently asked questions

The dataset is designed to be modular and easily maintainable. Updates can be made by modifying or adding text files without changing the core system logic. This makes the system scalable and adaptable for real-world deployments across multiple locations.

Dataset reference:
https://github.com/vivekranjan765/omnypark-parking-ai-assistant/tree/main/data

---

## Project Scope

This assistant is designed to handle a clearly defined set of parking-related queries, including:

- parking charges and tariffs  
- free parking duration  
- cinema or retail validation rules  
- weekend parking policies  
- public holiday parking policies  
- general parking FAQs  

The current prototype does **not** support:

- real-time parking availability  
- live payment processing  
- integration with external parking systems  
- location-based dynamic pricing  

This scope definition ensures clarity of use and aligns the system with its intended purpose as a policy assistant.

---

## Architecture Overview

The system is composed of the following components:

- **Knowledge Base:** Structured text files (`data/`)  
- **Embedding Model:** Sentence Transformers (MiniLM)  
- **Vector Store:** ChromaDB  
- **Language Model:** Google Gemini  
- **Interface:** Streamlit-based UI  

---

## Features

- Natural language query handling for parking policies  
- Context-aware responses using retrieval-based generation  
- Lightweight and modular architecture  
- Secure API key management using environment variables  
- Easy local deployment for testing and evaluation  

---

## Sample Questions

Users can interact with the assistant using queries such as:

- What are the parking charges per hour?  
- How many free hours do I get?  
- Can cinema visitors get extra parking time?  
- Is parking free on weekends?  
- Is parking free on public holidays?  
- Where can I validate my parking?  

---

## Expected Output

The assistant generates concise and user-friendly responses based strictly on the knowledge base.

Example:

**Question:**  
What are the parking charges per hour?

**Answer:**  
First 3 hours are free. After the free period, parking is charged at AED 20 per hour. Official site signage remains final.

---

## Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vivekranjan765/omnypark-parking-ai-assistant
cd omnypark-parking-ai-assistant