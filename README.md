# Echoes Cool Python Scripts 🐍

A collection of useful, easy-to-use Python scripts for automation, design, and media manipulation. 

---

## 🎨 Perfect Hue Loop GIF Maker (`hue_loop.py`)

This script takes a static image file, dynamically shifts its hue across the entire HSV color spectrum, and compiles it into a perfectly seamless, infinitely looping GIF animation.

### Features
* 🔄 **Perfect Loops:** Calculates mathematically seamless transitions from $0^{\circ}$ to $360^{\circ}$ hue rotations.
* 🎛️ **Fully Customizable:** Easily tweak the speed, frame counts, and file paths using simple command-line arguments.
* 🎞️ **Optional Side-by-Side View:** Compare the original static image next to the shifting variant with a single flag.
* 📦 **Zero-Config Defaults:** Run it without any arguments to see it immediately look for `input.jpg` in your directory.

---

### 🚀 Getting Started

#### 1. Prerequisites
You only need Python 3 and the **Pillow** image library installed to get started.

```bash
pip install Pillow
```

#### 2. Basic Usage
Drop your source image (`.jpg` or `.png`) into the same directory as the script. To run it using all the default settings (it will look for a file named `input.jpg`), open your terminal and type:

```bash
python hue_loop.py
```

---

### ⚙️ Command-Line Arguments

You can fully customize how the script handles your files by adding flags directly in your terminal command:


| Argument Flag | Alternative Flag | Description | Default Value |
| :--- | :--- | :--- | :--- |
| `-i` | `--input` | Path to your input source image | `input.jpg` |
| `-o` | `--output` | Path and filename for your final GIF | `perfect_hue_loop.gif` |
| `-f` | `--frames` | Number of total animation frames (Higher = smoother, larger file) | `45` |
| `-d` | `--duration` | Time each frame stays on screen in milliseconds (Lower = faster cycle) | `40` |
| `-s` | `--side-by-side` | Layout modifier flag. Combines the static original image next to the shifting image. | `False` |

#### Custom Examples

* **Enable Side-by-Side Mode:**
  ```bash
  python hue_loop.py --side-by-side
  ```

* **Target a Specific Image & Output Path:**
  ```bash
  python hue_loop.py -i profile.png -o avatar_rainbow.gif
  ```

* **Make a Super Smooth, High-Speed Loop:**
  ```bash
  python hue_loop.py -i art.png -f 90 -d 15
  ```

* **View Help Menu directly in Terminal:**
  ```bash
  python hue_loop.py --help
  ```

---

### 🤝 Contributing
Feel free to fork this project, report bugs, or submit pull requests with your own cool Python scripts to expand this repository!
