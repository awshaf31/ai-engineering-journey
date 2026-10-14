def goal_message(name: str, role: str) ->str:
    """Return a message outlining the goal for the given name and role."""
    return f"{name} is training to become an {role} Intern"


def greet(name: str) -> str:
    """Return a welcome message for the given  name."""
    return f"Hello, {name}! Welcome to AI engineering."

def main() -> None :
    name = input ("What is your name? ")
    role = input ("Which role are you training for? ")
    message = greet(name)
    goal = goal_message(name,role)
    print(message)
    print(goal)

if __name__== "__main__":
    main()
