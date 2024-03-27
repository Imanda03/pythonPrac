class FramerPuzzle;

def __init__(self, state=None):
    """Initial State where all four are on right Side"""
    if state:
        self.state = state
    else:
        self.state = {"left": {""},
                        "right": {"F", "W", "S", "C",""}}
    
    self.possible_actions = [("F", "", "<"), ("F","", ">"), ("F","W", "<"), ("F","W", ">"),("F","C", "<"), ("F","C", "<") ]


def is_goal(self):
    """All four on the left side. """

    goal_state = {"Left": {"F", "W", "S", "C",""}, "Right": {""}}

    return self.state == goal_state

def is_valid_action(self,action):
    """"Check if the action is valid action"""

    if action not in self.possible_actions:
        return False
    
    if action[2] == "<":
        return (action[0] in self.state["Right"]) and (action[1] in self.state["Left"])
        print ("not in Right")
    else:
        return (action[0] in self.state["Right"]) and (action[1] in self.state["Left"])
        print ("not in Left")

def next_action(self):
    temp = []
    for action in self.possible_actions:
        if self.is_valid_action(action):
            temp.append(action)
    return temp

def move(self,action):
         if not self.is_valid_action(action):
            raise Exception("Error: Invalid action")
         
         if action[2] == "<":
             self.state["Left"].add(action[0])
             self.state["Right"].remove(action[0])
             if action[1] == "":
                 return
             self.state["Left"].add(action[1])
             self.state["Right"].remove(action[1])
        