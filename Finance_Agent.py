from phi.agent import Agent
from phi.model.groq import Groq
#from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    symbols= {
        "Tesla" : "TSLA",
        "Apple" : "AAPL",
        "Microsoft" : "MSFT",
        "Amazon" : "AMZN",
        "Google" : "GOOGL",
    }

    return symbols.get(company, "Unknown")

agent = Agent( 
    model=Groq(id="llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True, 
    markdown=True,
    instructions=["Use tables to display data."],
    debug_mode=True,
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for XOM and TSLA")