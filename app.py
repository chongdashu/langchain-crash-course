import gradio as gr
from langchain_helper import generate_restaurant_name_and_items


def update_outputs(cuisine: str) -> tuple[str, str]:
    response = generate_restaurant_name_and_items(cuisine)
    restaurant_name = response["restaurant_name"].strip()
    menu_items = response["menu_items"].split(",")

    menu_items_formatted = ""
    for item in menu_items:
        menu_items_formatted += f"- {item.strip()}\n"

    return f"# {restaurant_name}", menu_items_formatted


with gr.Blocks() as gradio_app:
    gr.Markdown("## Restaurant Name Generator")

    with gr.Row():
        with gr.Column() as left:
            inp_cuisine = gr.Dropdown(
                ["Indian", "Italian", "Mexican", "Arabic"],
                label="Pick a cuisine",
            )

        with gr.Column(variant="panel") as right:
            out_restaurant_name = gr.Markdown()
            out_menu_items = gr.Markdown()

            inp_cuisine.change(
                fn=update_outputs,
                inputs=inp_cuisine,
                outputs=[out_restaurant_name, out_menu_items],
            )


if __name__ == "__main__":
    gradio_app.launch()
