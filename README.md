# Snake Game (Python - Turtle)

This project is a Python-based recreation of the legendary Nokia 3310 Snake game,
A special appearance by the "Vishal Snake" and "Thala" segments inspired by memes

---

## Screenshot

![Gameplay](Gameplay.png)

---

## Gameplay

* Control the snake using arrow keys
* Eat the food to grow longer
* Each food increases your score
* Game ends if:

  * Snake hits the wall
  * Snake collides with itself

---

## Project Structure

```
Retro Snake Game/

├── assets/
│   ├── Gameplay.png
│   └── Updated_gameplay.png
│
├── src/
    ├── food.py
    ├── scoreboard.py
    ├── game.py
    ├── snake.py
    └── high_score.txt
```

---

### Files Overview

* **game.py** → Main game loop and controls
* **snake.py** → Snake movement and growth logic
* **food.py** → Random food generation
* **scoreboard.py** → Score + high score system
* **high_score.txt** → Stores highest score locally

---

## Controls

| Key     | Action     |
| ------- | ---------- |
| ↑ Arrow | Move Up    |
| ↓ Arrow | Move Down  |
| ← Arrow | Move Left  |
| → Arrow | Move Right |

---

## Features

* Smooth snake movement
* Food spawning at random positions
* Score + High Score system (saved locally)
* Collision detection (wall + self)
* Classic retro green theme
