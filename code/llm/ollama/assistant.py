from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from rich.pretty import pprint

assistant = Assistant(
    llm=Ollama(model="llama3.1"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response("Share a quick healthy breakfast recipe.", markdown=True)
print("\n-*- Metrics:")
pprint(assistant.llm.metrics)  # type: ignore
