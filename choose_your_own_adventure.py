"""Choose‑Your‑Own‑Adventure game engine (stub).

This module provides placeholder functions for a text‑based adventure game.
In Ship 3 you will implement the `load_story` and `start_game` functions so
the game can load a small story file and present the first scene.  Additional
features such as menus, replay loops and advanced state management come in
later ships.
"""
import json
def load_story(file_path: str) -> dict:
    """Load a story definition from a file and return it as a data structure.

    The story file might be JSON, YAML or a custom format.  In Ship 3 you
    will parse the file and return a dictionary or another structure
    representing the narrative so you can display the opening scene.

    Args:
        file_path: user path to the story file.

    Returns:
        A dictionary describing the story and its choices.
     """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return {}
    return data


def start_game(story: dict) -> None:
    """Begin the adventure using the provided story data."""
    playing = True
    current_scene = "start"
    print(story[current_scene]["text"])

    while playing:
        choices = story[current_scene].get("choices", {})
        if not choices:
            print("The End.")
            break

        print("\nYour choices are:")
        for option in choices:
            print(f"- {option}")

        user_choice = input("\nWhat do you choose? ").strip().lower()

        if user_choice in choices:
            current_scene = choices[user_choice]
            print(f"DEBUG: Moving to scene '{current_scene}'")
            print(f"DEBUG: Scene keys: {list(story.keys())}")
            print("\n" + story[current_scene]["text"])
        else:
            print("Invalid choice. Please try again.")



def main() -> None:
    """Entry point for the adventure game.

    When run directly, this prints a greeting.  You will replace this
    with calls to `load_story` and `start_game` after implementing them.
    """
    start_game(load_story("C:/Users/marco/OneDrive/Documents/CODE/EdgeLabs/ship3/data/story.json"))

if __name__ == "__main__":
    main()