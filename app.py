
import openai
import gradio as gr
import constants

openai.api_key = constants.OpenApiKey

# Initialize an empty conversation history list
conversation_history = []

# Initial system message
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input_text):
    global conversation_history

    # Add the current input to the conversation history
    conversation_history.append({"role": "user", "content": input_text, "assistant": ""})

    if input_text:
        # Add user input to the message
        messages.append({"role": "user", "content": input_text})

        # Generate assistant reply using OpenAI ChatCompletion
        chat = openai.ChatCompletion.create(model="gpt-4", messages=messages)
        reply = chat.choices[0].message.content

        # Add assistant's reply to the conversation history
        conversation_history[-1]["assistant"] = reply

        # Format the conversation history for display
        chat_history = "\n".join(
            f"User: {item['content']}\nBot: {item['assistant']}" for item in conversation_history
        )

        return f"{reply}\n\nChat History:\n{chat_history}"

# Gradio interface setup
inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply and Chat History")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot with History", description="Ask anything you want, and see the conversation history", theme="compact")\
    .launch(share=True, server_port=7860)