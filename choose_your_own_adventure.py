"""Choose‑Your‑Own‑Adventure game engine (stub).

This module provides placeholder functions for a text‑based adventure game.
In Ship 3 you will implement the `load_story` and `start_game` functions so
the game can load a small story file and present the first scene.  Additional
features such as menus, replay loops and advanced state management come in
later ships.
"""

import json
from pathlib import Path
from typing import Dict


def load_story(file_path: str) -> Dict:
    """Load a story definition from a file and return it as a data structure.

    The story file might be JSON, YAML or a custom format.  In Ship 3 you
    will parse the file and return a dictionary or another structure
    representing the narrative so you can display the opening scene.

    Args:
        file_path: C:\Users\marco\OneDrive\Documents\CODE\EdgeLabs\ship3\data\story.json

    Returns:
        A dictionary describing the story and its choices.
    """
    
    path = Path(file_path)

    # If a relative path was passed, try to resolve it relative to the
    # repository's data directory (common usage in this project).
    if not path.is_absolute():
        candidate = Path("data") / path
        if candidate.exists():
            path = candidate

    if not path.exists():
        raise FileNotFoundError(f"Story file not found: {file_path}")

    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    if not isinstance(data, dict):
        raise ValueError("Story file must contain a JSON object at top level")

    # Basic validation: ensure there is a 'start' scene
    if "start" not in data:
        raise ValueError("Story JSON must contain a 'start' scene")

    return data


def start_game(story: dict) -> None:
    """Begin the adventure using the provided story data.

    This function will handle user input, present choices and traverse
    the story graph.  In Ship 3 you will get it to print the first scene
    and prompt for a choice; later ships expand it with loops and state.

    Args:
        story: The story data structure returned by `load_story`.
    """


    # Rudimentary implementation for Ship 3: print the opening scene and
    # prompt the player once for a choice. Full traversal, validation and
    # replay behavior will be implemented in later ships.
    if not isinstance(story, dict):
        raise TypeError("story must be a dictionary as returned by load_story")

    start = story.get("start")
    if not start or "text" not in start:
        raise ValueError("story does not contain a valid 'start' scene")

    print(start["text"])

    choices = start.get("choices", {}) or {}
    if not choices:
        print("(No choices available. The adventure ends here.)")
        return

    # Present choices (numbered) and accept one selection. This is
    # intentionally simple: we accept either the choice label or a number.
    labels = list(choices.keys())
    for idx, label in enumerate(labels, start=1):
        print(f"{idx}. {label}")

    try:
        selection = input("Choose: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. Exiting game.")
        return

    # Map numeric selection to label if necessary
    chosen_label = None
    if selection.isdigit():
        idx = int(selection) - 1
        if 0 <= idx < len(labels):
            chosen_label = labels[idx]
    else:
        if selection in choices:
            chosen_label = selection

    if chosen_label is None:
        print("Invalid choice. The game will end for now.")
        return

    next_scene_key = choices[chosen_label]
    next_scene = story.get(next_scene_key)
    if not next_scene:
        print(f"Next scene '{next_scene_key}' not found. The story ends.")
        return

    # Print the following scene's text (no further interaction in this ship).
    print(next_scene.get("text", ""))


def main() -> None:
    """Entry point for the adventure game.

    When run directly, this prints a greeting.  You will replace this
    with calls to `load_story` and `start_game` after implementing them.
    """
    print("Welcome to the Choose‑Your‑Own‑Adventure game!")


if __name__ == "__main__":
    main()