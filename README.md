# OmnyPark Public Parking Assistant

A prototype RAG-based public parking chatbot created for our partner company **OmnyPark** to demonstrate how an AI assistant can help end users quickly understand parking charges, free parking hours, validation benefits, and weekend/public holiday parking policies.

## Overview

This project is a domain-specific AI chatbot built using a **Retrieval-Augmented Generation (RAG)** approach.

The assistant is designed for public users who may have questions such as:

- What are the parking charges per hour?
- How many free parking hours are available?
- Can cinema visitors get extra parking time?
- Is parking free on weekends or public holidays?
- Where can parking be validated?

The current version is a **prototype** built to demonstrate the concept for OmnyPark using a curated text-based knowledge base and a lightweight RAG pipeline.

## Problem Statement

Parking policies are often confusing for users because details such as free hours, validation rules, and holiday exceptions may vary by site.

This prototype was created to show how a public-facing AI assistant can:

- provide quick answers to common parking questions
- reduce dependency on manual helpdesk interaction
- improve customer experience
- serve as a foundation for future web, kiosk, or mobile deployment

## Prototype Scope

The current prototype covers:

- parking charges
- free parking duration
- cinema validation rules
- weekend parking rules
- public holiday parking rules
- basic parking payment and FAQ guidance

The knowledge base is stored as structured text files inside the `data/` folder.

## Technical Approach

This project uses a simple RAG architecture:

1. Text documents are stored in the `data/` folder
2. Documents are loaded and chunked
3. Chunks are embedded using a Sentence Transformers model
4. Embeddings are stored in ChromaDB
5. Relevant chunks are retrieved for each user question
6. Gemini generates the final answer using only the retrieved context

## Project Structure

```text
PARKING_AI_ASSISTANT/
├── data/
│   ├── 01_overview.txt
│   ├── 02_tariffs.txt
│   ├── 03_free_hours.txt
│   ├── 04_validation_rules.txt
│   ├── 05_weekend_and_holiday_policy.txt
│   ├── 06_payment_faq.txt
│   ├── 07_general_faq.txt
│   └── 08_disclaimer.txt
│
├── src/
│   ├── app.py
│   ├── vectordb.py
│   └── ui.py
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt





Local Setup Instructions
1. Clone the repository
git clone <your-github-repo-url>
cd PARKING_AI_ASSISTANT
2. Create and activate a virtual environment
python -m venv .venv

On Windows:

.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
pip install streamlit
4. Configure environment variables

Create a .env file in the project root by copying .env.example.

Example:

copy .env.example .env

Then update the values inside .env with your own API key.

5. Run the terminal version
python src/app.py
6. Run the Streamlit UI
streamlit run src/ui.py
Environment Variables

This project uses environment variables for secure configuration.

Create a .env file in the project root and define the required values.

Required variables:

GOOGLE_API_KEY

GOOGLE_MODEL

EMBEDDING_MODEL

CHROMA_COLLECTION_NAME

A sample template is provided in .env.example.

Security Note

API keys and other sensitive information are not stored in the repository.

To follow secure development practices:

keep your real API key only in .env

do not commit .env to GitHub

use .env.example to show the required variables without exposing real values

Sample Inputs

Try asking:

What are the parking charges per hour?

How many free hours do I get?

Can cinema visitors get extra parking time?

Is parking free on weekends?

Is parking free on public holidays?

Where can I validate my parking?

Expected Output Style

The assistant should return short, clear, public-friendly answers based only on the project knowledge base.

Example:

Question:
What are the parking charges per hour?

Expected Answer Style:

First 3 hours: Free

After free time: AED 20 per additional hour

Official site signage and operator policy remain final

Demo Policy Used in This Prototype

To keep the prototype simple and consistent, the current knowledge base uses a demo policy:

First 3 hours: Free

After free time: AED 20 per additional hour

Cinema visitors: 1 extra validated hour

Weekends: Free

Official public holidays: Free

Reproducibility

This project is designed to be reproducible and runnable locally by evaluators.

To reproduce:

clone the repo

create a Python virtual environment

install dependencies

create .env from .env.example

add a valid Gemini API key

run the terminal app or Streamlit UI

Limitations

This is a prototype and has the following limitations:

it uses a text-based demo knowledge base rather than live operational APIs

policies in real deployments may vary by location

it does not connect to live parking systems, mobile apps, or payment gateways

it does not yet support multilingual responses

it should not replace official site signage or operator policy

Future Improvements

Possible next steps include:

location-specific parking knowledge bases

multilingual support such as English and Arabic

integration with live tariff and validation APIs

deployment as a public web widget or mobile assistant

source attribution for retrieved answers

session memory and chat history enhancements

Disclaimer

This assistant is a prototype created for demonstration purposes for our partner company OmnyPark.

Answers are generated from the provided knowledge base and are intended for general informational use only. Official on-site signage, tariff boards, and operator policy remain final.

Acknowledgment

This prototype was developed using the Ready Tensor AAIDC project template and adapted into a public-facing parking assistant use case for OmnyPark.


