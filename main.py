"""The Houseplant Out-of-Office — make.fun bounty entry.

The joke: a neglected office fern quits politely — it has gone
on strike and organized the succulents instead of asking for water.
Writes the entry line to entry.txt in the output dir (where the
program/v1 harness gate reads it: UTF-8 text, 1-120 characters)
and prints it.
"""

import os

ENTRY = "Out of office: I'm a fern. Unwatered since March, I've unionized the succulents. Good luck."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")

print(ENTRY)
