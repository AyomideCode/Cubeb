# Cubeb
## PyGame group project made for Computer Science II (Python) @ Howard University [CSCI 136-02 Fall 2021, Group #14]

Hello! This is Cubeb, soon being the repository for a 2D platformer game made using the PyGame library.

The game is playable with arrow keys/zxc, wasd/jkl, numpad/123, and controller d-pad/face buttons.

The application runs and is built around a windowed 1280x720. 
If you press F, F11 or Enter/Return, the game goes to fullscreen 720p.
Press Enter/Return again to go back, or press Esc at any time to close the game.

Left and Right Arrow keys do what you'd expect. 
Up Arrow and Z map as jump, X maps as shoot, and C maps to your grenade.

As of 12/13 7:30 AM, there are two currently playable levels; a third tutorial level is in the works. 

[Project proposal: https://docs.google.com/document/d/1RulH314LERlbpVUxJNrRWT88P7ziuJKV94BrBrSf9gk/edit?usp=sharing ]
[Project documentation: https://docs.google.com/document/d/1-xpwDip9mAC_HL3XQkx64S-SfMZn75iuFHx7e2mdhyI/edit?usp=sharing]

## TO-DO (Essential):


Assets ✔

    - Music ✔
	- Sound effects ✔
	- Sprites ✔
        - Replace bullets with kunai ✔
        - Replace player soldier with ninja girl ✔
		- Replace enemy soldier with ninja guy ✔
        - Replace grenade with laser bomb ✔
        - Replace background and add parallax to the new one ✔
        - Replace tileset ✔

Alternate keybinding support (allow multiple input methods to do the same actions in-game) ✔

Controller support (d-pad and face buttons) ✔

Polish jump physics ✔

	- Fix jump sound playing while in mid-air ✔
	- Allow changing jump altitude and gravity, depending on how long the jump input is held ✔
	- Fix the game letting you jump the frame you hit the ground, if you pressed jump in the air ✔

Fullscreen ✔

Fix the screen scrolling too far and causing clipping at the end of each level ✔

Implement tutorial level

	- Gradually let the player explore the game mechanics as the level goes, without need for signs or prompts
		- Start the player with no ammo or grenades—give them later when necessary
		- Design the level to let them figure out how to platform; slowly expose the player to traps/pits
		- Give them a safe spot for their first enemy encounter



## STRETCH FEATURES (For potential-added polish/better game-feel):


Add polish to effects

	- Add flash to enemy death animation
	- Add separate player & enemy running/death SFX
	- Add variance to the jump/shoot/grenade/death SFX
		- Add visual variance to grenade explosions

Stage select and options on main menu, pause menu & death screen

	- Options menu:
		- Make graphic (or open text file) showing all possible button/key inputs
		- Change resolution/fullscreen
		- Toggle on/off buttons/keybindings

Press a jump input after dying, & R at any time, to quickly restart the level
		
Add two levels to play after the first three

	- Design one around hard platforming alone, then design one around hard platforming + enemies

Add Game Over/Thanks for Playing screen once player has beaten all levels

	- Tally the amounts of Time/HP/Ammo/Grenades used, both per level and in total

After level 5, offer two toggleable movement options:

	- Double Jump, offering half of the first jump's verticality
	- Run with Shift/RT
		- Give small increase to vertical velocity if running and jumping at the same time
		- Make a toggleable option for running automatically or not

## STRETCHHHHHHHHH FEATURES (Becauae imagination is a great thing):

New tiles

	- Jump refiller: lets the player jump again once collected
	- Coin : Collectable, adds to score, would be on top-right corner
	- Bouncepad: boosts the player vertically
	- Speedpad: boosts the player horizontally
	- Spikes: halves the player's health
	- Explosive box: Has 1 HP, both player and enemy can blow it up

Melee attacks that change depending on the direction held (requires new added movement buttons, sprites & collision checks...)

	- Make AI capable of meleeing you too, but with a predictable windup before the attack (assuming melee would do a lot of damage)

Level-up/score system

	- The more enemies you kill, the higher your level 
		- A meter for it will be shown at top-right
	- Each level increases movement speed, damage output, size of bullets/explosions, and max HP
	- A score system that incentivises the player to fight enemies (add a score/combo counter at top right)

2 more levels that expand upon the added movement options/tiles/melee/upgrades
