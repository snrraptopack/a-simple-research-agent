# A Simple Research Agent

This project demonstrates how to use **Auwgent**, a compiler-first framework for building production-grade AI agents, to create a research agent. The agent is equipped with tools and custom intents to handle complex research tasks efficiently.

---

## Features

### Tools
The research agent has access to the following tools:

1. **Search Tool**:
   - Powered by **Tavily**, this tool allows the agent to perform web searches to gather information.

2. **State Tools**:
   - **Create Todo**: Allows the agent to create new todo items.
   - **Read Todo**: Enables the agent to read existing todo items.
   - **Delete Todo**: Lets the agent delete specific todo items.

### Custom Intents
The agent is designed with two custom intents to handle specific tasks:

1. **Dialogue Intent**:
   - Engages the user in a conversation to ask clarifying questions about complex queries.
   - Helps refine the problem statement for better results.

2. **Planning Intent**:
   - Plans the steps or layout required to solve the user’s question.
   - Provides a structured approach to tackling complex problems.

---

## How It Works

### Overview
The research agent leverages **Auwgent** to compile and manage its tools and intents. It uses the following workflow:
1. **User Input**: The user provides a question or task.
2. **Tool Usage**: The agent uses the appropriate tools (e.g., search or todo tools) to gather or manage information.
3. **Custom Intents**: For complex queries, the agent either:
   - Engages in a dialogue to clarify the question.
   - Creates a structured plan to solve the problem.

### Tools in Action
- **Search Tool**: Queries the web for relevant information.
- **Todo Tools**: Manages a list of tasks, allowing the agent to create, read, or delete todos as needed.

### Custom Intents in Action
- **Dialogue Intent**: For example, if the user asks, "How can I build a rocket?", the agent may ask follow-up questions like, "What type of rocket are you referring to?" or "What resources do you have available?"
- **Planning Intent**: The agent can break down the task into actionable steps, such as:
  1. Research rocket designs.
  2. Gather materials.

---

## Installation

### Prerequisites
- Python 3.9 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/snrraptopack/a-simple-research-agent.git
   cd a-simple-research-agent
