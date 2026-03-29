from tavily import TavilyClient

from dotenv import load_dotenv
import os

from generated.main_types import MainAgentTools
from typing import Optional

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

todo_state:dict[str, list[str]] = {}
has_todos = len(todo_state.keys()) > 0
todo_ids = ",".join(todo_state.keys())
todo_left = len(todo_state.keys())


async def search_web(query: str) -> str:
    response = tavily_client.search(query)
    return response["results"][0]["content"]

async def read_todo(id:str) -> list[str]:
    clean_id = id.strip()
    if clean_id in todo_state:
        return todo_state[clean_id]
    return ["No todos found for this ID"]

async def create_todo(id: str, todos: list[str]) -> list[str]:
    todo_state[id.strip()] = todos
    return todos

async def delete_todo(todo_id: str, target_task: Optional[str] = None, main: Optional[bool] = None) -> bool:
    clean_id = todo_id.strip()
    if clean_id in todo_state and main is not None:
        todo_state.pop(clean_id)
        return True
    if clean_id in todo_state and target_task is not None:
        todo_state[clean_id] = [t for t in todo_state[clean_id] if t != target_task]
        return True
    return False


tools:MainAgentTools = {
    'create_todo': create_todo,
    'read_todo': read_todo,
    'delete_todo': delete_todo,
    'search_web': search_web,
}
