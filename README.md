# ChatGPT-Terminal-Helper

## Getting started

This is a cli-helper tool that working with ChatGPT (text-davinci-003)

## Setup

- [ ] You need to have python package to run this helper scripts. If you do not have it please install it by 
following steps:
`brew install python`
- [ ] Add following path setting to bash profile file
```
# Setting PATH for Python 3.5
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH
```
- [ ] Add aliases your terminal configuration file (like .zshrc .bashrc etc.) 
- [ ] Paste following aliases into your terminal configuration file (like .zshrc .bashrc etc.)
Please do not forget to replace #/PATH/TO/SCRIPT/# with exact path in your computer
eg. `nano ~/.zshrc`
```
alias chatgpt="python3 /PATH/TO/SCRIPT/main.py --command"
alias chatgpt_report="python3 /PATH/TO/SCRIPT/main.py --bugfix"
```
- [ ] Update src/chatgpt_query.py "openai.api_key" with your own OpenAI api key


## Usages

- [ ] Call "chatgpt {promt}" to run ChatGPT wizard!
- [ ] Call "chatgpt_report" in which dir is going to be include refactoring/bughunting process to run. HTML output will be there after it's finished. 
