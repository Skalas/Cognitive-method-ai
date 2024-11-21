def load_prompt_template(file_path) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()
    return prompt_template


def get_prompt(prompt_template, **params) -> str:
    return prompt_template.format(**params)
