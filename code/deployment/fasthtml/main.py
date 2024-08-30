from os import getenv

from openai import OpenAI

from fasthtml.common import *

# Set up the app, including daisyui and tailwind for the chat component
hdrs = (
    picolink,
    Script(src="https://cdn.tailwindcss.com"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css",
    ),
)
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-lg mx-auto")

# Set up a chat model (https://claudette.answer.ai/)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
)
model = "mistralai/mistral-7b-instruct:free"


# Chat message component (renders a chat bubble)
def ChatMessage(msg, user):
    bubble_class = "chat-bubble-primary" if user else "chat-bubble-secondary"
    chat_class = "chat-end" if user else "chat-start"
    return Div(cls=f"chat {chat_class}")(
        Div("user" if user else "assistant", cls="chat-header"),
        Div(msg, cls=f"chat-bubble {bubble_class}"),
        Hidden(msg, name="messages"),
    )


# The input field for the user message. Also used to clear the
# input field after sending a message via an OOB swap
def ChatInput():
    return Input(
        name="msg",
        id="msg-input",
        placeholder="Type a message",
        cls="input input-bordered w-full",
        hx_swap_oob="true",
    )


# The main screen
@app.get
def index():
    page = Form(hx_post=send, hx_target="#chatlist", hx_swap="beforeend")(
        Div(id="chatlist", cls="chat-box h-[73vh] overflow-y-auto"),
        Div(cls="flex space-x-2 mt-2")(
            Group(ChatInput(), Button("Send", cls="btn btn-primary"))
        ),
    )
    return Titled("Chatbot Demo", page)


# Handle the form submission
@app.post
def send(msg: str, messages: list[str] = None):
    if not messages:
        messages = []
    messages.append(msg.rstrip())
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": msg.rstrip(),
            },
        ],
    )
    return (
        ChatMessage(msg, True),  # The user's message
        ChatMessage(
            completion.choices[0].message.content.rstrip(), False
        ),  # The chatbot's response
        ChatInput(),
    )  # And clear the input field via an OOB swap


serve()
