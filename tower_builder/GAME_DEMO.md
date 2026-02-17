# Tower Builder Game - Visual Overview

## Game Screenshots (Text-Based Visualization)

### Main Menu Screen
```
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║                      TOWER BUILDER                             ║
║                                                                ║
║                Build the tallest tower you can!                ║
║                                                                ║
║                         Controls:                              ║
║                   ← → : Move block left/right                  ║
║                      SPACE : Place block                       ║
║                                                                ║
║                    Press SPACE to start                        ║
║                                                                ║
║                     High Score: 150                            ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

### Playing Screen
```
╔════════════════════════════════════════════════════════════════╗
║ Score: 150                                                     ║
║ Height: 240                                                    ║
║ High: 150                                                      ║
║                                                                ║
║                      ┌────────┐                                ║
║                      │ BLOCK  │  ← Current block               ║
║                      └────────┘                                ║
║                                                                ║
║                                                                ║
║                      ┌────────┐                                ║
║                      │ BLOCK  │                                ║
║                    ┌─┴────────┴─┐                              ║
║                    │   BLOCK    │                              ║
║                  ┌─┴────────────┴─┐                            ║
║                  │     BLOCK      │                            ║
║                ┌─┴────────────────┴─┐                          ║
║                │       BLOCK        │                          ║
║              ┌─┴────────────────────┴─┐                        ║
║              │        BLOCK           │                        ║
║══════════════════════════════════════════════════════════════  ║
║███████████████████ GROUND ███████████████████████████████████  ║
║                                                                ║
║              ← → to move, SPACE to place                       ║
╚════════════════════════════════════════════════════════════════╝
```

### Game Over Screen
```
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║                      GAME OVER                                 ║
║                                                                ║
║                 Block fell off screen!                         ║
║                                                                ║
║                  Final Score: 320                              ║
║                                                                ║
║                  NEW HIGH SCORE!                               ║
║                                                                ║
║              Press SPACE to play again                         ║
║                Press ESC for menu                              ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

## Gameplay Flow

1. **Start**: Game begins at main menu
2. **Spawn Block**: A new colored block appears at the top
3. **Move**: Use arrow keys to position the block
4. **Place**: Press SPACE to drop the block
5. **Physics**: Block falls with gravity and lands on ground or other blocks
6. **Stability Check**: Block needs 30% overlap to be stable
7. **Score**: Points awarded based on tower height
8. **Repeat**: New block spawns, continue building
9. **Game Over**: Tower collapses or block falls off screen

## Features Highlights

### Block Colors
The game features 6 different colored blocks:
- 🟥 Light Red
- 🟦 Light Blue  
- 🟩 Light Green
- 🟨 Yellow
- 🟧 Orange
- 🟪 Purple

### Scoring System
```
Base Score = 10 points per block
Height Multiplier = 1 + (tower_height ÷ 100)
Final Score = Base Score × Height Multiplier
```

Example:
- At height 0-99px: 10 points per block
- At height 100-199px: 20 points per block
- At height 200-299px: 30 points per block
- And so on...

### Physics System
- Gravity: 0.5 pixels/frame²
- Max fall speed: 15 pixels/frame
- Collision detection: Rectangle-based
- Stability threshold: 30% horizontal overlap

## Game Tips

1. **Center Your Blocks**: Build straight up for maximum stability
2. **Watch the Overlap**: Ensure blocks overlap by at least 30%
3. **Take Your Time**: Precise placement is more important than speed
4. **Height Matters**: Taller towers = higher score multipliers
5. **Stay Calm**: One mistake can end the game!

## Technical Details

- **Language**: Python 3.7+
- **Framework**: Pygame 2.5.0+
- **FPS**: 60 frames per second
- **Resolution**: 800x600 pixels
- **Max Blocks**: 50 blocks per game
