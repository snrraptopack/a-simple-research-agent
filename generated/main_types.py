# Auto-generated types for MainAgent
# Do not edit manually
import os
import json
from typing import TypedDict, Callable, Awaitable, Any, List, Dict, Union, Optional, Protocol, Literal, overload

# NotRequired is 3.11+; fall back to typing_extensions for 3.9/3.10
try:
    from typing import NotRequired
except ImportError:
    from typing_extensions import NotRequired

try:
    from auwgent_sdk import TypedAuwgent, create_auwgent, Middleware, MiddlewareContext, SessionState, AuwgentToolError
except ImportError:
    # For local testing if auwgent is not installed via pip
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from auwgent_sdk import TypedAuwgent, create_auwgent, Middleware, MiddlewareContext, SessionState, AuwgentToolError

class MainAgentInput(TypedDict, total=False):
    pass

class MainAgentOutput(TypedDict, total=False):
    pass

class MainAgentContext(TypedDict, total=False):
    user_name: str
    has_todos: bool
    todo_id: str
    todos_left: float

class MainAgentTools(TypedDict, total=False):
    # use this tool to search the web for information
    search_web: Callable[[str], Awaitable[str]]

    # use this tool to create todos you will use to solve the problem
    create_todo: Callable[[str, List[str]], Awaitable[List[str]]]

    # use this tool to read a todo
    read_todo: Callable[[str], Awaitable[List[str]]]

    # use this tool to delete a todo
    delete_todo: Callable[[str, Optional[str], Optional[bool]], Awaitable[bool]]

MainAgentCustomIntents = Union[
    TypedDict('_PlaningCustomIntent', {"name": Literal["Planing"], "value": {"planing": str}}, total=False),
    TypedDict('_DialogueCustomIntent', {"name": Literal["Dialogue"], "value": {"question": str}}, total=False),
]

class MainAgentResponseTextIntent(TypedDict, total=False):
    text: str

MainAgentResponseSchemaIntent = MainAgentOutput

class MainAgentErrorIntent(TypedDict, total=False):
    message: str
MainAgentIntentValue = Union[
    MainAgentResponseTextIntent,
    MainAgentResponseSchemaIntent,
    MainAgentErrorIntent,
]
MainAgentIntentName = Literal["response_text", "response_schema", "error"]

MainAgentIntentHandler = Callable[[MainAgentIntentName, MainAgentIntentValue, str], Awaitable[Optional[Dict[str, Any]]]]
MainAgentPartialIntentHandler = Callable[[MainAgentIntentName, MainAgentIntentValue, str], None]

class MainAgentIntentHandlers(TypedDict, total=False):
    response_text: Callable[[MainAgentResponseTextIntent], Awaitable[Any]]
    response_schema: Callable[[MainAgentResponseSchemaIntent], Awaitable[Any]]
    error: Callable[[MainAgentErrorIntent], Awaitable[Any]]

class MainAgentPartialIntentHandlers(TypedDict, total=False):
    response_text: Callable[[MainAgentResponseTextIntent], None]
    response_schema: Callable[[MainAgentResponseSchemaIntent], None]
    error: Callable[[MainAgentErrorIntent], None]

class MainAgentApiKeys(TypedDict, total=False):
    my_groq_apiApiKey: str  # API key for custom provider 'my-groq-api'

class MainAgentAgent(TypedAuwgent[Any, MainAgentContext, MainAgentOutput, MainAgentTools]):
    @overload
    def on_intent(self, callback: Callable[[Literal["response_text"], MainAgentResponseTextIntent, str], Awaitable[Optional[Dict[str, Any]]]]) -> None: ...
    @overload
    def on_intent(self, callback: Callable[[Literal["response_schema"], MainAgentResponseSchemaIntent, str], Awaitable[Optional[Dict[str, Any]]]]) -> None: ...
    @overload
    def on_intent(self, callback: Callable[[Literal["error"], MainAgentErrorIntent, str], Awaitable[Optional[Dict[str, Any]]]]) -> None: ...
    def on_intent(self, callback: MainAgentIntentHandler) -> None:
        return super().on_intent(callback)

    @overload
    def on_intent_partial(self, callback: Callable[[Literal["response_text"], MainAgentResponseTextIntent, str], None]) -> None: ...
    @overload
    def on_intent_partial(self, callback: Callable[[Literal["response_schema"], MainAgentResponseSchemaIntent, str], None]) -> None: ...
    @overload
    def on_intent_partial(self, callback: Callable[[Literal["error"], MainAgentErrorIntent, str], None]) -> None: ...
    def on_intent_partial(self, callback: MainAgentPartialIntentHandler) -> None:
        return super().on_intent_partial(callback)

    def on_handlers(self, handlers: MainAgentIntentHandlers) -> None:
        return super().on_handlers(handlers)

    def on_handlers_partial(self, handlers: MainAgentPartialIntentHandlers) -> None:
        return super().on_handlers_partial(handlers)

MainAgentMiddleware = Middleware

class MainAgentConfig(TypedDict, total=False):
    tools: NotRequired['MainAgentTools']
    middleware: NotRequired[List['MainAgentMiddleware']]
    context: NotRequired['MainAgentContext']
    apiKeys: NotRequired['MainAgentApiKeys']

def createMainAgent(config: MainAgentConfig) -> 'MainAgentAgent':
    """Create a fully configured MainAgent agent from config."""
    ir_path = os.path.join(os.path.dirname(__file__), "main.agent.json")
    with open(ir_path, "r", encoding="utf-8") as f:
        ir_dict = json.load(f)
    return create_auwgent(ir_dict, config)

auwgent = createMainAgent
AuwgentTools = MainAgentTools
AuwgentConfig = MainAgentConfig
AuwgentAgent = MainAgentAgent
AuwgentMiddleware = MainAgentMiddleware
AuwgentContext = MainAgentContext
AuwgentIntentName = MainAgentIntentName
AuwgentIntentValue = MainAgentIntentValue
AuwgentIntentHandler = MainAgentIntentHandler
AuwgentPartialIntentHandler = MainAgentPartialIntentHandler
AuwgentIntentHandlers = MainAgentIntentHandlers
AuwgentPartialIntentHandlers = MainAgentPartialIntentHandlers