#Software Engineering Internship Placement — Technical Screening Task

This repository contains a simple Python script that processes prompts from a text file and saves the results.
It shows reading input, processing each item, and saving outputs in a way that can be re-run without duplicating.

## What the script does

- Reads a list of prompts from a file called prompts.txt (one prompt per line).  
- For each prompt:
  - Sends it to a mock LLM function (call_llm) that simulates processing.  
  - Saves the resulting response to a separate text file in the outputs folder.  
  - Skips prompts that were already processed to prevent duplication.  
- Ensures the script is idempotent - running it multiple times won’t overwrite existing outputs.  
- Provides simple console messages to show which prompts were processed.

## How it works

1. read_file(filename) – reads all prompts from a text file.  
2. call_llm(prompt) – simulates an LLM by returning "Processed: {prompt}".  
3. prompt_to_filename(prompt) – converts each prompt to a readable filename for storage.  
4. process_prompts(prompts) – loops through each prompt, checks if it has already been processed, calls the LLM, and writes the response to a file.  

## Usage
- Make sure Python 3 is installed
- Add your prompts to prompts.txt (one per line)
- Run the script:
 - python main.py
- Check the outputs folder for processed prompts

## Part 2 — Human Approval (Design)
- I would structure the workflow by moving from a simple file-check approach to a tracking system using a JSON file.After generating a response from the LLM, it is first marked as pending instead of being saved immediately.
- Instead of saving responses directly to .txt files, the script would first store each prompt and its response in this JSON file.
- I would represent each prompt with a state to track progress:
    - pending — response has been generated but waiting for human review/approval
    - approved — response  accepted and saved to the outputs folder
    - rejected — response is discarded and marked to avoid reprocessing
- For pending items, I would prompt the user to either approve or reject each response.(e.g. Approve (Y/N))
- If a prompt is approved, I would save the response to a file and update its state to approved.
- If a prompt is rejected, I would not save the response and update its state to rejected.
- I would use the JSON file to keep track of progress across runs, so the script only shows pending items that still need review.
- To ensure idempotency, the script would skip all prompts that are already marked as approved or rejected, and only process or review those marked as pending.

## Part 3 — Reflection

The hardest part of this task was ensuring the script could be re-run without duplicating work or overwriting existing outputs. I learned that this can be solved through idempotency, by checking whether an output already exists before processing a prompt. Initially, I overcomplicated the solution, but simplifying it to a one-file-per-prompt approach made the workflow much clearer and more maintainable.

If I had more time, I would implement a JSON state file to track each prompt’s status across runs and extend the script with a human approval step and metadata tracking. This would allow the system to pick up exactly where it left off and make the workflow stronger and easier to maintain. Overall, this task reminded me that simple, clear code is always easier to maintain.
