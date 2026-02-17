# 🏗️ Tower Builder Game

A fun and engaging tower-building game built with Python and Pygame! Stack blocks to build the tallest tower you can while managing physics and stability.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 Game Features

- **Simple Gameplay**: Easy to learn, challenging to master
- **Physics System**: Realistic gravity and collision detection
- **Scoring System**: Points based on tower height and blocks placed
- **High Score Tracking**: Compete against your personal best
- **Clean Graphics**: Colorful pixel-style aesthetic
- **Game States**: Menu, playing, and game over screens

## 🎯 How to Play

### Objective
Build the tallest tower possible by stacking blocks on top of each other!

### Controls
- **← / →** (Arrow Keys): Move the current block left or right
- **SPACE**: Place the block
- **ESC**: Return to menu (during gameplay) or quit (in menu)

### Gameplay Mechanics
1. A new block appears at the top of the screen
2. Use arrow keys to position it
3. Press SPACE to drop the block
4. The block falls with gravity and settles when it lands
5. Stack blocks carefully - they need at least 30% overlap to be stable
6. Earn points for each block placed, with height-based multipliers
7. Game ends if a block falls off screen or maximum blocks reached

### Scoring
- **Base Score**: 10 points per block
- **Height Multiplier**: Increases every 100 pixels of tower height
- **Final Score**: Base Score × Height Multiplier

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.5.0 or higher

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/SebasO1/SebasO1.git
cd SebasO1/tower_builder
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install Pygame directly:
```bash
pip install pygame
```

### Step 3: Run the Game
```bash
python tower_builder.py
```

Or make it executable and run directly:
```bash
chmod +x tower_builder.py
./tower_builder.py
```

## 🎨 Game Screens

### Main Menu
- Displays game title and instructions
- Shows high score
- Press SPACE to start

### Playing
- Active gameplay with block stacking
- Real-time score and height display
- Current high score shown

### Game Over
- Shows final score and reason for game ending
- Displays "NEW HIGH SCORE!" if you beat your record
- Options to play again or return to menu

## 🏆 Tips for High Scores

1. **Center Your Blocks**: Try to keep blocks centered for better stability
2. **Watch the Overlap**: Ensure good horizontal overlap (at least 30%)
3. **Build Steadily**: Don't rush - precise placement is key
4. **Height Multiplier**: The taller your tower, the more points per block
5. **Stay Calm**: Take your time positioning each block

## 🛠️ Technical Details

### Architecture
- **Main Game Loop**: Runs at 60 FPS for smooth gameplay
- **Block Physics**: Custom gravity and collision detection system
- **State Management**: Clean separation of menu, playing, and game over states
- **Data Persistence**: High scores saved in `high_score.json`

### Key Classes
- **Block**: Represents individual blocks with physics properties
- **Game**: Main game controller managing state, logic, and rendering

### Physics System
- Gravity acceleration: 0.5 pixels/frame²
- Maximum fall speed: 15 pixels/frame
- Stability threshold: 30% horizontal overlap required
- Collision detection: Rectangle-based with overlap calculation

## 📝 File Structure

```
tower_builder/
├── tower_builder.py      # Main game file
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── high_score.json      # Auto-generated high score file
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pygame'"
**Solution**: Install Pygame using `pip install pygame`

### Issue: Game window doesn't appear
**Solution**: Ensure you have a display/graphics environment. For headless systems, you may need to set up a virtual display.

### Issue: Game runs slowly
**Solution**: Close other applications to free up system resources. The game is optimized to run at 60 FPS on most systems.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📜 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

Created by Sebastián Olaya Sánchez (SebasO1)

- 🌐 [GitHub](https://github.com/SebasO1)
- 💼 [LinkedIn](https://www.linkedin.com/in/sebastián-olaya-sánchez-639554348)

## 🎮 Game Inspiration

Inspired by classic tower-building games like:
- Nokia Tower Building Game
- Tower Bloxx
- Stack

---

**Enjoy building your towers! 🏗️🎮**
