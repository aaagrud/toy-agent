## Toy-Agent

Toy agent is a toy-agent(duh!) built with free models from [OpenRouter](https://openrouter.ai/) and plain old python!
I wanted to know how agents work under the hood and that is why this exists.
Now, using this agent is a bad idea because security features other than limiting access to pwd are non-existent because **I made it for fun to learn**

## Capabilities
- Can run in a loop to solve problems
- Tool Calls:
    - Read files
    - Write files
    - Run files
    - List directories

## Setup (Again, please know what you're doing)
If you are using uv,
- uv sync (install dependencies)
- set the directory the agent can access in config.py
- create a .env and with API key `OPENROUTER_API_KEY=<your key>`
- uv run main.py "< your prompt >"
  
I have set a limit of 20 back and forths max for the agent before it taps out! You can edit in main.py

### Tech Stack
- Python
- Python OpenAI SDK
- OpenRouter API