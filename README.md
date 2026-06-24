# AI Startup Co-Founder Agent

An AI-powered multi-agent system that helps founders evaluate startup ideas by generating market research, competitor analysis, business strategies, risk assessments, MVP plans, financial projections, SWOT analyses, startup scores, and executive summaries.

---

## Features

* Multi-Agent AI Architecture
* Market Research Analysis
* Competitor Analysis
* Business Strategy Generation
* Risk Assessment
* SWOT Analysis
* Financial Projections
* MVP Roadmap Planning
* Startup Scoring & Investment Recommendation
* Executive Summary Generation
* TXT Report Export
* PDF Report Export
* Timestamped Reports
* Individual Agent Outputs

---

## Architecture

The system uses specialized AI agents that work together to generate a comprehensive startup evaluation report.

Agents:

1. Executive Summary Agent
2. Market Research Agent
3. Competitor Analysis Agent
4. Business Strategy Agent
5. Risk Assessment Agent
6. SWOT Analysis Agent
7. Financial Projection Agent
8. MVP Planning Agent
9. Startup Scoring Agent

---

## Tech Stack

* Python
* OpenRouter API
* DeepSeek Chat V3
* ReportLab
* python-dotenv

---

## Project Structure

```text
AI-Startup-CoFounder-Agent/
│
├── agents/
│   ├── market_agent.py
│   ├── competitor_agent.py
│   ├── business_agent.py
│   ├── risk_agent.py
│   ├── swot_agent.py
│   ├── financial_agent.py
│   ├── mvp_agent.py
│   ├── scoring_agent.py
│   └── executive_summary_agent.py
│
├── reports/
│
├── main.py
├── llm_client.py
├── pdf_generator.py
├── .env
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI-Startup-CoFounder-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

---

## Output

The system generates:

* Executive Summary
* Market Research Report
* Competitor Analysis
* Business Strategy
* Risk Assessment
* SWOT Analysis
* Financial Projections
* MVP Roadmap
* Startup Score & Recommendation

Reports are exported as:

* TXT files
* PDF files

---

## Future Improvements

* Streamlit Web Interface
* Interactive Dashboard
* Multi-LLM Support
* Startup Pitch Deck Generator
* Investor Matching System

---

## Author

Gautam
B.Tech AI & Data Science
Chaitanya Bharathi Institute of Technology (CBIT)
