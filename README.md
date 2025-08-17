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

```mermaid
flowchart TD
    A[GitHub Actions<br>(cron jobs)] --> B[Data Fetching<br>(yfinance, APIs)]
    B --> C[PostgreSQL<br>(Supabase cloud DB)]
    C --> D[Streamlit Cloud<br>(Dashboard 24/7)]
```
## Technologies
- **Python 3.11** (core language)
- **Conda** (environment management)
- **yfinance / financial APIs** (data fetching)
- **PostgreSQL (Supabase)** (cloud database)
- **GitHub Actions** (automation & scheduling)
- **Streamlit Cloud** (dashboard hosting)
- **VS Code** (IDE & GitHub integration)

## Next Steps
1. Configure cloud PostgreSQL database (Supabase).
2. Automate data collection and storage using GitHub Actions.
3. Build initial data pipeline (ETL).
4. Deploy interactive dashboard with Streamlit Cloud.
5. Extend the project with new analytics and strategies.