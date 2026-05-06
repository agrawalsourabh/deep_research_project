from cProfile import label
import os
from dotenv import load_dotenv
import gradio as gr
from research_manager import ResearchManager

load_dotenv(override=True)

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

async def run(query: str):
    async for chunk in ResearchManager().run(query=query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research project")
    query_textbox = gr.Textbox(label="What topic you want to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)


ui.launch(inbrowser=True)
