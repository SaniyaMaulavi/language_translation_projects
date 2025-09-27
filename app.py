import gradio as gr
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Your OpenAI API key
api_key = "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"

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_key=api_key)

# Translation function
def translate(text, language):
    template = f"Translate the following text to {language}:\n\n{text}"
    return llm.invoke([HumanMessage(content=template)]).content

# Build Gradio UI with dark mode and styled buttons
with gr.Blocks(css="""
body {background-color: #1e1e2f; color: #ffffff; font-family: 'Segoe UI', sans-serif;}
h1, h2, h3, label {color: #ffffff;}
.gr-button.primary {background-color: #ff6b6b; color: white; border-radius: 8px;}
.gr-button.primary:hover {background-color: #ff4c4c;}
.gr-button.secondary {background-color: #4ecdc4; color: white; border-radius: 8px;}
.gr-button.secondary:hover {background-color: #3bb3aa;}
.gr-textbox, .gr-dropdown {background-color: #2e2e3f; color: white; border-radius: 8px;}
.gr-textbox textarea {color: white;}
.gr-textbox textarea::placeholder {color: #aaaaaa;}
""") as demo:

    gr.Markdown("<h2 style='text-align:center; background: linear-gradient(to right, #ff6b6b, #f7d794); padding: 15px; border-radius: 10px;'>🌐 Language Translator</h2>")
    
    with gr.Row():
        with gr.Column(scale=3):
            input_text = gr.Textbox(label="Enter text", placeholder="Type your text here...", lines=5)
            target_lang = gr.Dropdown(
                label="Translate to",
                choices=["Hindi", "English", "Marathi", "Urdu", "Korean"],
                value="Hindi"
            )
            with gr.Row():
                submit_btn = gr.Button("🚀 Translate", variant="primary")
                clear_btn = gr.Button("🧹 Clear", variant="secondary")
        with gr.Column(scale=2):
            output_text = gr.Textbox(label="Output", lines=8, interactive=False)

    submit_btn.click(translate, inputs=[input_text, target_lang], outputs=output_text)
    clear_btn.click(lambda: "", outputs=[input_text, output_text])

demo.launch()
