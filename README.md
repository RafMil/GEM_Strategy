# GEM Strategy

The **GEM Strategy** project is a Python-based implementation of the Global Equities Momentum (GEM) strategy.  
It is designed to be **scalable, automated, and fully cloud-based**, with no local dependencies.

## Project Goals
- Fetch financial market data (e.g., ETFs) automatically.
- Store data in a **cloud PostgreSQL database** (Supabase).
- Run scheduled jobs (ETL) in the cloud using **GitHub Actions**.
- Provide an **interactive dashboard** (Streamlit Cloud), available 24/7 via link.
- Build a clean, modular, and extensible codebase that can be expanded with new ideas.

## Planned Architecture
- **GitHub Actions (cron jobs)** → Fetch data (yfinance, APIs)  
- **PostgreSQL (Supabase cloud DB)** → Store and manage financial data  
- **Streamlit Cloud** → Interactive dashboard available online 24/7  

## Technologies
- **Python** – core language  
  - `yfinance`, `pandas`, `sqlalchemy`  
- **Database** – PostgreSQL on [Supabase](https://supabase.com/)  
- **Automation** – GitHub Actions (cron jobs)  
- **Dashboard** – Streamlit Cloud  

## Next Steps
1. Initialize basic project structure (`src/`, `data/`, `notebooks/`, `tests/`).  
2. Configure Supabase PostgreSQL instance.  
3. Add data ingestion script (yfinance → PostgreSQL).  
4. Set up GitHub Actions workflow for scheduled jobs.  
5. Deploy first version of Streamlit dashboard.  
