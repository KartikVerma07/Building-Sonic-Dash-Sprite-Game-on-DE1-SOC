# Building-Sonic-Dash-Sprite-Game-on-DE1-SOC

## Flow of the Game
### Objective
  The main goal of the sprite, Sonic (37x50 in size), is to collect coins (represented as 10x10 yellow blocks). The number of coins collected determines the user's score.

### Character Actions
  Sonic has five possible actions:
    - Walk Right: Moves right using 11 sprites in a sequence (Press KEY 0).
    - Walk Left: Moves left using 11 sprites in a sequence (Press KEY 1).
    - Jump Up: Moves up using 5 sprites in a sequence (Press KEY 2).
    - Fall: Uses 1 sprite for falling (Press KEY 3).
    - Stand: Remains standing if no action is taken.
    - Details about the sprites are discussed in the "Approach for Storing Sprite Pixels in ROM" section.

### Gameplay Mechanics
Initially, the idea was to have different floor levels moving downwards, allowing Sonic to move left, right, jump up, or fall to collect coins.
Due to space constraints and compile time, this feature is postponed. For now, a white background is used between the walls.
Sonic cannot move beyond the left (50x480) and right (50x480) walls. These walls move downwards, creating the illusion of Sonic descending to collect coins.
### Future Enhancements
A moving background sprite will be added later to enhance gameplay.
A score display, which updates at the bottom right whenever Sonic collects coins, will be implemented in a future update.

## Overview of Implementation
### Storing Sprite Pixels in ROM
  - Calculation and Storage:
    - RGB values for sprite images (in .png format) are calculated and stored in .txt files using a provided Python script.
    - Each 37x50 image results in 3 .txt files (Red, Green, and Blue) in the script's directory.
  - Sprite Examples:
    - Moving Right:\
      ![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/c56553d6-2547-4644-af85-cb8396999fe6)
      - 11 sprites, each 37x50 pixels, for Red, Green, and Blue.
      - Total: 20,350 pixel values per .txt file for each color.
    - Moving Left:\
      ![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/72e368e5-6639-4e26-8cda-3bbd1372de4d)
      - Same as moving right.
    - Jumping:\
      ![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/3f881269-c065-4f24-b7bb-6d508945c726)
      - 5 sprites, each 37x50 pixels, for Red, Green, and Blue.
      - Total: 9,250 pixel values per .txt file for each color.
    - Falling and Standing:\
      ![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/55f8d47a-bbca-4c43-a7bf-9ad1872e00da)
      - 1 sprite, 37x50 pixels, for Red, Green, and Blue.
      - Total: 1,850 pixel values per .txt file for each color.
    - Walls:
      - Each wall occupies 50x480 pixels (24,000 pixels).
    - Coins:
      - Each coin is a 10x10 yellow cube.
   - Structure of Modules
     - Top Level Module: top
       - Contains instances of modules used in the project.
       - Inputs three resets from FPGA board switches:
         - SW[2]: Resetting PLL (active high).
         - SW[1]: Resetting VGA Controller Module (active low).
         - SW[0]: Resetting Pixels for game start (active low).
       - Controls for Sonic's movement:
         - KEY 0: Move Right.
         - KEY 1: Move Left.
         - KEY 2: Jump.
         - KEY 3: Fall.
   - PLL IP:
     - Generates a 25.2 MHz clock for VGA (800x525 pixels per frame at 60 frames per second).
   - VGA Controller:
     - FSM transitions between states: Active, Front Porch, Sync Pulse, and Back Porch (both Vertical and Horizontal).
   - Clock Generator:
     - Converts 25MHz clock to various frequencies like 60Hz, 30Hz, and 1Hz.
   - Pattern with Sprites:
     - Contains parameterized ROM instances for sprite movement and wall display.
     - Uses count frames and sprite counts for displaying sprite movements (walking left/right, jumping):
       - Each sprite's pixel values are iterated and displayed sequentially to create animation.
       - Example logic for walking right with 11 sprites:
         - Iterates through pixel values from 1st to 11th sprite, then loops back.
   - Coin Movement:
     - Positioned initially at (200, 10).
     - Moves downwards at 30Hz and to the right at 1Hz.

## RTL Schematic
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/70e70b59-1927-45a0-ae55-d33b4454ee9f)

## VGA Output
Start with Reset set as 1 using SW [1], Sonic stands at bottom left at reset.\
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/e24ded60-5a79-41db-8446-41015573a546)
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/bace068a-8318-47a7-ad16-612e58eff1bd)
\
Then Sonic can be moved either left, right, up (jump to) or down (fall) to collect coins.\
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/55fa7839-6786-4ea3-aa80-dc1f2288b827)
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/e8906896-fe32-40e8-8a18-70a13d3e8220)
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/d1bd4ef8-7c6f-466d-85aa-c242e449d1c2)
![image](https://github.com/KartikVerma07/Building-Sonic-Dash-Sprite-Game-on-DE1-SOC/assets/60437757/1714a54f-d9ff-4fdf-944d-a6728fb4cefa)

## License
State the license under which your project is distributed.

This project is licensed under the MIT License - see the LICENSE file for details.




    
