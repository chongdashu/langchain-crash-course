import gradio as gr


def generate_restaurant_name_and_items(cuisine: str) -> dict[str, str]:
    return {
        "restaurant_name": "Curry Delight",
        "menu_items": "Butter Chicken, Naan, Paneer Tikka, Chole Bhature, Lassi, Gulab Jamun",
    }


def update_outputs(cuisine: str) -> tuple[str, str]:
    response = generate_restaurant_name_and_items(cuisine)
    restaurant_name = response["restaurant_name"]
    menu_items = response["menu_items"].split(",")

    menu_items_formatted = ""
    for item in menu_items:
        menu_items_formatted += f"- {item.strip()}\n"

    return f"## {restaurant_name}", menu_items_formatted


with gr.Blocks() as app:
    gr.Markdown("# Restaurant Name Generator")
    inp_cuisine = gr.Dropdown(
        ["Indian", "Italian", "Mexican", "Arabic"],
        label="Pick a cuisine",
    )

    out_restaurant_name = gr.Markdown()
    out_menu_items = gr.Markdown()

    inp_cuisine.change(
        fn=update_outputs,
        inputs=inp_cuisine,
        outputs=[out_restaurant_name, out_menu_items],
    )


if __name__ == "__main__":
    app.launch()
