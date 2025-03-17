# **Getting Started Guide: Create Minecraft Animations (For Beginners)**

This guide will help you create smooth animations of your Minecraft builds using the **IsometricRenders** mod. No coding experience needed!

---

## **1. Install What You Need**

### **Step 1: Install the IsometricRenders Mod**

1. Download the mod from [CurseForge](https://www.curseforge.com/minecraft/mc-mods/isometric-renders).
2. Install it using a mod loader like **Forge** or **Fabric** (follow the mod’s instructions).

### **Step 2: Install Python**

1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, check the box that says **"Add Python to PATH"**.

### **Step 3: Install FFmpeg (Easy Way!)**

**FFmpeg** is a tool to turn images into videos. Here’s how to install it:

1. Download FFmpeg from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z).
2. Unzip the folder to `C:\ffmpeg`.
3. Add FFmpeg to your PATH:
   - Press `Windows + S` and type "Environment Variables".
   - Click **"Edit the system environment variables"**.
   - Click **"Environment Variables"** > Under "System variables", select **"Path"** > Click **"Edit"**.
   - Click **"New"** and add `C:\ffmpeg\bin`.
   - Click **OK** to save.

#### **Check if FFmpeg Works**:

Open a terminal/command prompt and type:

```bash
ffmpeg -version
```

If you see version info, it’s installed!

### **Step 4: Install Python Packages**

Open a terminal/command prompt and run:

```bash
pip install pyautogui natsort
```

### **Step 5: Prepare the "Export" Screenshot**

1. In Minecraft, open the IsometricRenders GUI.
2. Take a screenshot of the **"Export" button** (use `F2` in Minecraft or the Snipping Tool).
3. Save it as `export.png` in a folder named `imgs` (create this folder in the same place as the scripts).

---

## **2. Create Your Animation**

### **Step 1: Generate Frames**

1. **Build your structure** in Minecraft (e.g., a redstone machine).
2. Run this command in a terminal (replace numbers with your settings):

   ```bash
   python create_frames.py --scale 100 --rotation 0 --slant 30 --time 5
   ```

   - `--scale`: How zoomed-in the render is (try `100`).
   - `--rotation`: Camera angle (`0`-`360`).
   - `--slant`: Tilt angle (`0`-`90`).
   - `--time`: Animation length in seconds.

3. **Switch to Minecraft** within 10 seconds! The script will auto-capture frames.

4. **Frames will be exported** to the default IsometricRenders export location (usually in the `screenshots` folder of your Minecraft directory).
   - **Tip**: After capturing frames, copy all the `area_render_XX.png` files to a new folder (e.g., `my_animation_frames`) to keep things organized.

### **Step 2: Turn Frames into a Video**

1. Move the `create_animation.py` script to the folder where your frames are (e.g., `my_animation_frames`).
2. Run this command:
   ```bash
   python create_animation.py --dir ./ --output my_animation.mp4
   ```
   - Frames are deleted by default. Add `--keep` to save them:
     ```bash
     python create_animation.py --dir ./ --output my_animation.mp4 --keep
     ```

---

## **3. Troubleshooting Tips**

### **Problem: Script clicks the wrong spot!**

- Run Minecraft in **fullscreen windowed mode** (not fullscreen).
- Adjust coordinates in `create_frames.py` (ask for help if needed!).

### **Problem: FFmpeg not found!**

- Double-check the FFmpeg installation steps above.

---

## **You’re Done!**

Your video `my_animation.mp4` will be saved in the same folder as the scripts.

For longer animations, use `concat_videos.py` to combine videos (ask for help if needed!).
