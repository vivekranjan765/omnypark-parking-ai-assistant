🚗 OmnyPark AI Parking Assistant
Intelligent Parking Guidance using RAG (Retrieval-Augmented Generation)
📌 Overview

The OmnyPark AI Parking Assistant is an intelligent chatbot designed to answer parking-related queries such as:

Parking tariffs (e.g., AED/hour)
Free parking durations
Validation rules (cinema, retail, etc.)
Payment methods
General parking policies

The system is built using a Retrieval-Augmented Generation (RAG) architecture, combining:

📚 Structured parking knowledge base
🧠 Semantic search (vector embeddings)
🤖 Large Language Model (LLM)

This enables accurate, context-aware, and reliable responses, grounded in real parking data.

🎯 Problem Statement

Parking users often face confusion regarding:

Tariffs and charges
Free parking eligibility
Validation rules
Payment options

Traditional systems provide static information, leading to poor user experience.

👉 This project solves that by introducing an AI-powered conversational assistant for parking systems.

💡 Solution

The OmnyPark Assistant uses a RAG pipeline:

User asks a question
System retrieves relevant parking rules
LLM generates a contextual answer

This ensures:

❌ No hallucination
✅ Data-driven responses
⚡ Fast and scalable retrieval
🏗️ System Architecture

Flow Overview
User enters query (Streamlit UI)
Query is normalized
Converted into embeddings
Semantic search performed in ChromaDB
Top relevant chunks retrieved
LLM generates final response
🖥️ Application Preview

⚙️ Tech Stack
Frontend/UI: Streamlit
Backend: Python
Vector Database: ChromaDB
Embeddings: Sentence Transformers
LLM: OpenAI GPT (or configurable)
Environment Management: dotenv
📂 Project Structure
omnypark-parking-ai-assistant/
│
├── data/                  # Parking knowledge base (text files)
├── src/                   # Core logic
│   ├── vectordb.py        # Vector DB + embedding logic
│   ├── chatbot.py         # RAG pipeline
│   ├── ui.py              # Streamlit interface
│
├── screenshots/           # UI & architecture images
├── .env.example           # Environment template
├── requirements.txt
└── README.md
🔍 Chunking Strategy

The system uses a structured chunking approach for optimal retrieval.

Parameters
Chunk Size: ~300–500 tokens
Chunk Overlap: ~50–100 tokens
Why Chunking Matters
Ensures context continuity
Improves retrieval accuracy
Prevents loss of important rules
Example
"Parking is free for 2 hours. After that AED 10/hour applies."

Is stored in overlapping chunks so both conditions are always retrieved together.

🗂️ Dataset Maintenance

The system is fully data-driven.

How it Works
Knowledge stored as .txt files in /data
Each file represents:
Site rules
Parking policies
Validation conditions
Updating Data
Add/update files in /data
Re-run embedding process
System automatically reflects changes
Benefits
No code changes required
Easy to scale across multiple sites
Fast updates for real-world deployments
📊 Evaluation Approach

The system is tested using real-world query scenarios.

Sample Queries
Query	Expected Output
How much is parking per hour?	Tariff details
Is parking free?	Free duration
Cinema validation?	Extra time rules
After free hours?	Paid tariff
How to pay?	Payment options
Evaluation Criteria
Accuracy
Relevance
Completeness
Clarity
Observations
Semantic search improves retrieval quality
Chunk overlap enhances multi-condition responses
Responses are grounded → minimal hallucination
🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/vivekranjan765/omnypark-parking-ai-assistant.git
cd omnypark-parking-ai-assistant
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment

Create .env file:

OPENAI_API_KEY=your_api_key_here
4️⃣ Run Application
streamlit run src/ui.py
🔐 Security Best Practices
API keys are stored using .env
.env is excluded via .gitignore
.env.example provided for setup guidance
📌 Support Status
Current State

✅ Prototype / MVP

Supported
Parking queries
Tariff explanations
Validation rules
Conversational UI
Not Supported Yet
Real-time parking availability
Live API integrations
Payment systems
Production scalability
🔮 Future Roadmap
🔗 Integration with OmnyPark backend APIs
📡 Real-time parking data
📱 Mobile/Web deployment
🧠 Advanced LLM fine-tuning
🌍 Multi-location deployment
🤝 Contributing

Contributions are welcome!

Improve dataset
Enhance UI
Optimize retrieval
Add integrations
📜 License

This project is for educational and demonstration purposes.

👤 Author

Vivek Ranjan