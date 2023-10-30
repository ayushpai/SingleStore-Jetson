import openai
from jetbot import Robot
import time

# Initialize the robot
robot = Robot()

# Define basic motion functions
def stop():
    robot.stop()

def step_forward():
    robot.forward(0.4)
    time.sleep(0.5)
    robot.stop()

def step_backward():
    robot.backward(0.4)
    time.sleep(0.5)
    robot.stop()

def step_left():
    robot.left(0.3)
    time.sleep(0.5)
    robot.stop()

def step_right():
    robot.right(0.3)
    time.sleep(0.5)
    robot.stop()

# Set up OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your API key

def get_command_from_gpt(prompt_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt_text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Command loop
while True:
    # Get command from GPT
    prompt_text = "Command the robot with one of the following actions: forward, backward, left, right, stop, exit."
    command = get_command_from_gpt(prompt_text).lower()
    
    if command == "forward":
        step_forward()
    elif command == "backward":
        step_backward()
    elif command == "left":
        step_left()
    elif command == "right":
        step_right()
    elif command == "stop":
        stop()
    elif command == "exit":
        break
    else:
        print("Invalid command!")

print("Exiting program.")
