import argparse
import pyautogui
import time

parser = argparse.ArgumentParser(
    description="Create frames for Minecraft block animations using Isometric Renders mod"
)
parser.add_argument("--scale", type=int, help="Render scale", required=True)
parser.add_argument("--rotation", type=int, help="Render rotation", required=True)
parser.add_argument("--slant", type=int, help="Render slant", required=True)
parser.add_argument(
    "--time",
    type=float,
    help="Approximate total time for animation in seconds",
    required=True,
)
args = parser.parse_args()


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


# Make user focus on Minecraft window
def focus_on_minecraft():
    print("You have 10 seconds to focus on Minecraft window")
    for t in range(10, 0, -1):
        print(f"Starting in {t} seconds")
        time.sleep(1)


# Run command in Minecraft chat
def exec_minecraft_command(command: str):
    pyautogui.press("t")
    pyautogui.write(command)
    pyautogui.press("enter")


# Export frame in Minecraft to file
def export_frame():
    pyautogui.moveTo(1910, 60)
    pyautogui.scroll(-10000)
    time.sleep(0.5)
    exportLocation = pyautogui.locateCenterOnScreen("imgs/export.png", confidence=0.60)
    pyautogui.moveTo(exportLocation.x - 200, exportLocation.y)
    pyautogui.click()


# Set render properties in Minecraft
def set_render_properties(scale: int, rotation: int, slant: int):
    # Get options box location
    optionsBox = pyautogui.locateOnScreen("imgs/options.png", confidence=0.60)
    optionsLocation = pyautogui.Point(optionsBox.left, optionsBox.top)

    # Set scale
    pyautogui.moveTo(optionsLocation.x + 75, optionsLocation.y + 125)
    set_render_property(pyautogui.position().x, pyautogui.position().y, scale)

    # Set rotation
    pyautogui.moveRel(0, 125)
    set_render_property(pyautogui.position().x, pyautogui.position().y, rotation)

    # Set slant
    pyautogui.moveRel(0, 125)
    set_render_property(pyautogui.position().x, pyautogui.position().y, slant)


# Set render property at postion (x, y) to value
def set_render_property(x: int, y: int, value: any):
    # Set location of input field
    pyautogui.moveTo(x, y)

    # Enter value
    pyautogui.click()
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.write(str(value))


# Minecraft commands
render_command = "/isorender area"
next_frame_command = "/tick step"

# Screen positions
scale_input = (1210, 215)
rotation_input = (1210, 330)
slant_input = (1210, 475)

FRAME_DURATION = 0.05  # seconds

if __name__ == "__main__":
    # Render settings

    print("Starting animation process...\n")

    # Set focus on Minecraft window
    focus_on_minecraft()

    # Set scale, rotation, slant
    exec_minecraft_command(render_command)
    set_render_properties(args.scale, args.rotation, args.slant)
    time.sleep(1)
    pyautogui.press("esc")

    time_elapsed = 0
    while time_elapsed < args.time:
        # Render frame
        exec_minecraft_command(render_command)
        export_frame()
        pyautogui.press("esc")

        # Goto next frame
        time_elapsed += FRAME_DURATION
        exec_minecraft_command(next_frame_command)
        time.sleep(0.25)

        print(f"Frame {round(time_elapsed * 20)} ({time_elapsed:.2f}s) rendered")
