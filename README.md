# Example: Actions - Sales results & Computer uptime

This example gets you started in creating Actions for [Robocorp Action Server](https://github.com/robocorp/robo/tree/master/action_server/docs#readme).

`Actions` and `Action Server` enable you to "give your AI Agents hands" meaning that your AI/LLM Agent can help your users perform distinct actions that get executed based on the LLM discussion.

## Quickstart

👉 Follow the Action Server [Quickstart guide](https://github.com/robocorp/robocorp?tab=readme-ov-file#%EF%B8%8F-quickstart) in the main repository.


## Dependency management

We recommend placing your dependencies in [conda.yaml](conda.yaml).

👉 More on [managing your dependencies](https://github.com/robocorp/robocorp?tab=readme-ov-file#what-makes-a-python-function-an-%EF%B8%8Faction) in the main repository.


## Actions in VS Code 

👉 Using [Robocorp Code extension for VS Code](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code), you can get everything set up and running in VS Code in no time.

The template has a few files that enable the extension to find and set up your action environment and provide code completion. There is also a side panel where we have and will add some easy-to-use functionalities.

When debugging your Actions Python code, you probably do not want to give the inputs every time you run and always be running the Action Server, so you can set your test inputs in a [input.json](./devdata/input.json) and just run/debug your Python code.


## What does this example Action do?

This has two Actions: 
1. Submit sales results to Robot Spare Industries website. Sales target needs to be between 5.000 and 100.000 in increments of 5.000.   
Example prompt: "Submit sales results for John Doe. He has a target of 35.000 and the result is 40k."

![Sales Target](/docs/sales_target.png)

2. Get the uptime from users Windows or macOS computer.  
Example prompt: "How long has my computer been running?"

Robocorp provides a [bunch of libraries](https://pypi.org/search/?q=robocorp-); you can make your own. The sky is the limit.

🚀 Now, go get'em

