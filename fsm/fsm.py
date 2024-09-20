class StateMachine:
    def __init__(self, state_machine_definition):
        self.state_machine_definition = state_machine_definition
        self.value = state_machine_definition["initialState"]

    def transition(self, current_state, event):
        current_state_definition = self.state_machine_definition[current_state]
        destination_transition = current_state_definition["transitions"].get(event)
        if not destination_transition:
            return

        destination_state = destination_transition["target"]
        destination_state_definition = self.state_machine_definition[destination_state]

        destination_transition["action"]()
        current_state_definition["actions"]["onExit"]()
        destination_state_definition["actions"]["onEnter"]()

        self.value = destination_state
        return self.value

def create_machine(state_machine_definition):
    return StateMachine(state_machine_definition)

if __name__ == "__main__":
    state_machine_definition = {
        "initialState": "off",
        "off": {
            "actions": {
                "onEnter": lambda: print("off: onEnter"),
                "onExit": lambda: print("off: onExit")
            },
            "transitions": {
                "switch": {
                    "target": "on",
                    "action": lambda: print('transition action for "switch" in "off" state')
                }
            }
        },
        "on": {
            "actions": {
                "onEnter": lambda: print("on: onEnter"),
                "onExit": lambda: print("on: onExit")
            },
            "transitions": {
                "switch": {
                    "target": "off",
                    "action": lambda: print('transition action for "switch" in "on" state')
                }
            }
        }
    }

    machine = create_machine(state_machine_definition)

    state = machine.value
    print(f"current state: {state}")
    state = machine.transition(state, "switch")
    print(f"current state: {state}")
    state = machine.transition(state, "switch")
    print(f"current state: {state}")
