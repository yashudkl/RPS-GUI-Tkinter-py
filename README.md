# ✊✋✌️ Rock Paper Scissors GUI

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A **modern, feature-rich Rock Paper Scissors game** with a polished Tkinter GUI, real-time scoreboard, move history, and customizable difficulty levels. Perfect for casual play or learning Python GUI development!

---

## 🎮 Features

✨ **Modern GUI**
- Clean, responsive interface built with `ttk` (themed Tkinter)
- Real-time scoreboard tracking Player, Computer, and Ties
- Large, colorful result display with contextual emojis and messages
- Smooth button animations with click feedback (green flash on press)

📊 **Score Tracking & Rounds**
- Live scoreboard showing current game state
- Round counter with visual feedback
- **Customizable game modes**: Best of 3, Best of 5, Best of 10, or **Endless mode**
- Automatic game-over detection and victory screen

🎯 **Gameplay Experience**
- Side-by-side versus display with player and computer choice images
- Color-coded result messages:
  - 🟢 **Green** for victories
  - 🔴 **Red** for defeats  
  - ⚫ **Gray** for ties
- Descriptive outcome text (e.g., "Rock crushes Scissors – You Win!")

📝 **Move History Panel**
- Scrollable history log showing last 12 rounds
- Color-coded entries matching game outcome
- Auto-scroll to latest move
- Read-only design prevents accidental edits

🎛️ **Control & Flexibility**
- **New Game** button for complete game reset
- **Reset Round** button to clear current display
- **Difficulty selector** to change game mode mid-session
- Re-enables buttons after game-over
- Preserves difficulty choice across resets

---

## 📸 Screenshots & Demo

> 💡 **Pro Tip**: Add actual screenshots by placing images in a `./screenshots/` folder and updating these paths!

![Gameplay Demo](./screenshots/gameplay.gif)
*Game in action: player chooses Rock, computer reveals Paper, result display shows the outcome.*

![Main Menu](./screenshots/main-menu.png)
*Clean title screen with difficulty selector and scoreboard.*

![Game Over](./screenshots/game-over.png)
*Victory screen with final scores and move history.*

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.7+** | Core game logic and mechanics |
| **Tkinter** | GUI framework with modern `ttk` widgets |
| **Pillow (PIL)** | Image loading and display (rock/paper/scissors icons) |
| **OS/sys** | File path handling and system integration |

---

## 📥 Installation

### Prerequisites
- **Python 3.7** or higher ([Download](https://www.python.org/downloads/))
- **pip** (usually bundled with Python)

### Step-by-Step Setup

**1. Clone the Repository**
```bash
git clone https://github.com/yashudkl/RPS-GUI-Tkinter-py.git
cd RPS-GUI-Tkinter-py
```

**2. Install Dependencies**
```bash
pip install pillow
```
> Note: Tkinter is included with most Python installations. If missing, install via your package manager:
> - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
> - **macOS**: `brew install python-tk`
> - **Windows**: Tkinter is bundled with Python installer

**3. Verify Image Assets**
Ensure the `img/` folder contains:
- `rock.png`
- `paper.png`
- `scissor.png`

**4. Run the Game**
```bash
python main.py
```

The game window will launch automatically! 🚀

---

## 🎮 How to Play

1. **Select Difficulty** (Optional)
   - Use the "Game Mode" dropdown at the top
   - Choose: **Best of 3** | **Best of 5** | **Best of 10** | **Endless**
   - Default: Best of 5 (first to 3 wins)

2. **Make Your Choice**
   - Click one of the three buttons: **Rock** | **Paper** | **Scissors**
   - Watch your choice animate on screen (button flashes green for feedback)

3. **Compare Results**
   - Computer makes a random choice
   - Result displays with color coding:
     - 🟢 Green = You won
     - 🔴 Red = You lost
     - ⚫ Gray = Tie
   - Detailed message shows *how* you won (e.g., "Paper covers Rock")

4. **Win Conditions**
   - **Modes with win targets** (Best of 3/5/10): Game ends when someone reaches the win threshold
   - **Endless mode**: Play indefinitely until you click "New Game"

5. **Control Your Game**
   - **Reset Round**: Clear current display without affecting scores
   - **New Game**: Complete reset—scores, rounds, and history

6. **Track Your History**
   - Scroll through the **Move History** panel at the bottom
   - See every past round with outcome colors

---

## 🕹️ Gameplay & Controls

| Action | Control |
|--------|---------|
| **Choose Rock** | Click the "Rock" button |
| **Choose Paper** | Click the "Paper" button |
| **Choose Scissors** | Click the "Scissors" button |
| **Change Difficulty** | Use the "Game Mode" dropdown |
| **Clear Current Round** | Click "Reset Round" button |
| **Start New Game** | Click "New Game" button |
| **View History** | Scroll the "Move History" panel |

---

## 📁 Project Structure

```
RPS-GUI-Tkinter-py/
├── main.py                 # Main game logic and GUI
├── README.md              # This file
├── img/
│   ├── rock.png          # Rock choice image
│   ├── paper.png         # Paper choice image
│   └── scissor.png       # Scissors choice image
└── screenshots/          # (Optional) Game screenshots for README
    ├── gameplay.gif
    ├── main-menu.png
    └── game-over.png
```

---

## 🚀 Future Improvements & Roadmap

Exciting features planned for future versions:

- 🎵 **Sound Effects** – Add audio feedback for wins/losses/clicks
- 🌙 **Dark Theme Toggle** – Implement light/dark mode switcher
- 🏆 **High Score Tracking** – Save best scores to a JSON file
- 🧩 **Rock-Paper-Scissors-Lizard-Spock** – Expand with 5 options
- 📊 **Statistics Dashboard** – Win rate %, favorite move, performance over time
- 🎯 **Difficulty AI** – Different computer strategies (easy/medium/hard)
- 🌐 **Multiplayer** – Play against friends locally
- 💾 **Game Saves** – Load/save game state
- 🎨 **Custom Themes** – User-selectable color schemes

Have an idea? [Open an issue](https://github.com/yashudkl/RPS-GUI-Tkinter-py/issues) or submit a PR!

---

## 🤝 Contributing

Contributions are **always welcome**! Here's how to get involved:

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/my-feature`
3. **Commit your changes**: `git commit -m "Add my feature"`
4. **Push to the branch**: `git push origin feature/my-feature`
5. **Open a Pull Request** and describe your changes!

### Code Style
- Follow [PEP 8](https://pep8.org/) conventions
- Use clear variable and function names
- Add comments for complex logic
- Test thoroughly before submitting

---

## 📄 License

This project is licensed under the **MIT License** – you're free to use, modify, and distribute it.  
See the [LICENSE](LICENSE) file for details, or view the full license at https://opensource.org/licenses/MIT.

---

## 👤 Author & Credits

**Developed by**: [Yash Udkl](https://github.com/yashudkl)

**Built with**:
- 🐍 Python & Tkinter (excellent for beginner-friendly GUI projects)
- 🖼️ [Pillow](https://python-pillow.org/) – Image processing library
- ❤️ Open-source passion

**Special thanks** to the Python and Tkinter communities for excellent documentation!

---

## 📞 Questions? Feedback?

- 💬 **Open an Issue** – Report bugs or request features on [GitHub Issues](https://github.com/yashudkl/RPS-GUI-Tkinter-py/issues)
- 🌟 **Star the Repo** – Show some love if you enjoy the game!
- 📧 **Contact** – Reach out via GitHub

---

## 🎉 Enjoy the Game!

**Have fun playing!** Whether you're just passing time or learning Python GUI development, we hope you enjoy our Rock Paper Scissors experience. 

**Now go win some rounds!** ✊✋✌️

---

<div align="center">

**[⬆ Back to Top](#-rock-paper-scissors-gui)**

Made with ❤️ by the RPS community

</div>
