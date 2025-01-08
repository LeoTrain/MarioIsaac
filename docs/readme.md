# **Platformer Game (WIP)**

Welcome to the development of my **2D Platformer**! This game is being built with Python using the Pygame library, focusing on smooth mechanics, interesting characters, and challenging levels. While it's still a work in progress, you can already see the game's foundation taking shape.

## 🎮 **Gameplay Overview**
This platformer will have the following exciting features:
- **Dynamic Characters**: Play as a variety of characters, each with unique abilities.
- **Challenging Levels**: Navigate through levels filled with moving platforms, enemies, and puzzles.
- **Enemies**: Fight against Goblins and other foes in your quest.
- **Power-ups & Items**: Collect different items to boost your abilities and reach hidden areas.
- **Smooth Movement**: Jump, sprint, and interact with the world seamlessly using intuitive controls.

![Gameplay Example](path_to_screenshot_1)

## 🛠️ **Project Structure**
The project is split into several key components to ensure maintainability and scalability:
- **`main.py`**: Entry point of the game where all elements come together.
- **`game.py`**: Main game loop that handles the core game logic.
- **`level.py`**: Manages the level design, including loading tiles and handling collisions.
- **`player.py`**: Defines the Player class, focusing on movement, jumping, and interaction.
- **`goblin.py`**: Introduces the Goblin enemies and their behaviors.
- **`base_character.py`**: Abstract class that defines shared characteristics of all in-game characters.
- **`moving_tile.py`**: Implements moving platforms for added gameplay challenge.
- **`tile.py`**: Handles static tiles, like ground blocks or walls.

![Character Animation](path_to_screenshot_2)

## 🔧 **How to Run the Game**
To run the game locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourgame.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game from outside of the folder:
    ```bash
    python3 -m MarioIsaac.main
    ```

Make sure you have Python and Pygame installed!

## 🚀 **Future Plans**
- **Additional Levels**: More intricate and challenging levels are planned.
- **Boss Fights**: Unique boss battles to spice up the adventure.
- **Multiplayer Mode**: Cooperative or competitive gameplay with friends.
- **Enhanced Graphics**: Adding more detailed sprite animations and background elements.

![Level Preview](path_to_screenshot_3)

## 🤝 **Contributing**
Feel free to contribute ideas, report bugs, or submit pull requests. This project is still under active development, and any contributions are welcome!

[To-Do's](/MarioIsaac/docs/todos.md)
