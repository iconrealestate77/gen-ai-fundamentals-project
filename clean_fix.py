import json

path="starter/gen_ai_fundamentals_project_starter.ipynb"

with open(path) as f:
    nb=json.load(f)

# Cell 6
text="".join(nb["cells"][6]["source"])
text=text.replace(
"lora_rank = **********  # Explain your choice",
"lora_rank = 16  # LoRA rank"
)
nb["cells"][6]["source"]=text.splitlines(True)

# Cell 10
text="".join(nb["cells"][10]["source"])
text=text.replace(
'SYSTEM_PROMPT = """**********"""',
'''SYSTEM_PROMPT = """
You are a careful reasoning assistant.
Solve problems step by step.
For counting letters, list each letter and maintain a running count.

Example:
Question: How many g are in engage?

1. e - 0
2. n - 0
3. g - 1
4. a - 1
5. g - 2
6. e - 2

Final answer: 2
"""'''
)
nb["cells"][10]["source"]=text.splitlines(True)

# Cell 19
text="".join(nb["cells"][19]["source"])
text=text.replace(
"# matches = **********",
"matches = re.findall(pattern, response)"
)
nb["cells"][19]["source"]=text.splitlines(True)

# Cell 27
text="".join(nb["cells"][27]["source"])
text=text.replace(
"# **********  # Complete the list comprehension",
"1.0 if str(r) == str(a) else 0.0"
)
nb["cells"][27]["source"]=text.splitlines(True)

# Cell 31
text="".join(nb["cells"][31]["source"])
text=text.replace("# learning_rate=**********,","learning_rate=5e-6,")
text=text.replace("# beta=**********,","beta=0.04,")
text=text.replace("# per_device_train_batch_size=**********,","per_device_train_batch_size=1,")
nb["cells"][31]["source"]=text.splitlines(True)

# Cell 36
text="".join(nb["cells"][36]["source"])
text=text.replace(
"# max_steps=**********,  # ~60min",
"max_steps=50,"
)
nb["cells"][36]["source"]=text.splitlines(True)

# Cell 42
text="".join(nb["cells"][42]["source"])
text=text.replace(
"# **********",
"""item = ds[0]
print(item)"""
)
nb["cells"][42]["source"]=text.splitlines(True)

# Cell 45
text="".join(nb["cells"][45]["source"])
text=text.replace(
"# **********",
"""question = "What is the capital of France?"
print(question)"""
)
nb["cells"][45]["source"]=text.splitlines(True)

with open(path,"w") as f:
    json.dump(nb,f,indent=2)

print("Clean patch completed")
