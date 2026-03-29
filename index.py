from generated.main_types import (
    MainAgentIntentName,
    MainAgentIntentValue,
    MainAgentContext,
    auwgent
)
import asyncio

from dotenv import load_dotenv
import os

from tools import has_todos, todo_ids,todo_left,tools

load_dotenv()



context:MainAgentContext = {
    'user_name': "Theophilus",
    'has_todos': has_todos,
    'todo_id': todo_ids,
    'todos_left': todo_left
}

agent = auwgent({
    "apiKeys": {
        "my_groq_apiApiKey": os.getenv("GROQ_API_KEY","")
    },
    "context": context,
    "tools":tools
})

def handle_intent(name:MainAgentIntentName,value:MainAgentIntentValue,agent_name:str):
    if name == "response_text":
        print(value.get("delta",""),end="")

async def handle_intent_full(name:MainAgentIntentName,value:MainAgentIntentValue,agent_name:str):
    if name != "response_text":
        print(f"{name}: {value}")

agent.on_intent_partial(handle_intent)
agent.on_intent(handle_intent_full)

async def main():
    print("Chat with the agent (type 'exit' or 'quit' to stop)\n")

    while True:
        try:
            # Get user input
            user_input = input("\nYou:").strip()

            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break

            # Skip empty inputs
            if not user_input:
                continue

            # Run the agent
            print("\nAgent: ", end="", flush=True)
            result = await agent.run(user_input)
            print()  # New line after response

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(main())
