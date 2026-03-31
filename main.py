import os

def read_file(filename):
    try:
        with open(filename, "r") as file:
            prompts = file.readlines()
            return prompts
    except FileNotFoundError:
        print(f"File {filename} not found")
    return []


def call_llm(prompt):
    return f"Processed: {prompt}"


# turn the prompt text into a safe&readable filename
def prompt_to_filename(prompt):
    prompt = prompt.lower().strip()
    prompt = prompt.replace("?", "")
    prompt = prompt.replace(" ", "_")
    return f"{prompt}.txt"


def process_prompts(prompts):
    # make sure the outputs folder exists
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    for prompt in prompts:
        prompt = prompt.strip()

        # skip blank lines
        if not prompt:
            continue

        filename = prompt_to_filename(prompt)
        filepath = os.path.join("outputs", filename)

        # skip if already done
        if os.path.exists(filepath):
            print(f"Already processed, skipping: {prompt}")
            continue

        response = call_llm(prompt)

        # save the response
        with open(filepath, "w") as file:
            file.write(response)

        print(f"Done: {prompt}")


# run everything
prompts = read_file("prompts.txt")
process_prompts(prompts)
