# SB3-tutorial

This repository contains code for the tutorial on using Stable Baselines 3 for creating custom environments and custom policies.

## Contents 

1. [Installation](#installation) 
2. [Custom Environment](#custom-environment)
3. [Evaluation](#evaluation)

## Installation

To install the python libraries using ```conda``` execute the following command: 

```
conda env create -f environment.yml
```
## Custom Environment

```selection_env.py``` contains the code for our custom environment. The ```SelectionEnv``` class implements the custom environment and it extends from the OpenAI Gymnasium Environment ```gymnasium.Env```

The method ```reset```  is used for resetting the environment and initializing the state. The method ```step``` executes an action in the current state and returns the next state, reward, and an indication whether the episode is completed or not. 

