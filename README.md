# Cubeb
## PyGame group project made for Computer Science II (Python) @ Howard University [CSCI 136-02 Fall 2021, Group #14]

Hello! This is Cubeb, soon being the repository for a 2D platformer game made using the PyGame library.

Currently, the game is controllable with arrow keys/zxc, wasd/jkl, numpad/123, and controller d-pad/face buttons.

This game currently runs at a windowed 1280x720.

Left and Right Arrow keys do what you'd expect. 
Up Arrow and Z map as jump, X maps as shoot, and C maps to your grenade.
As of 12/13 7:30 AM, there are two currently playable levels; a third tutorial level is in the works. 

[Project proposal: https://docs.google.com/document/d/1RulH314LERlbpVUxJNrRWT88P7ziuJKV94BrBrSf9gk/edit?usp=sharing ]

TO-DO:

Assets
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

Stretchable screen and fullscreen with Alt + Enter

Tutorial level
	- Gradually let the player explore the game mechanics as the level goes, without need for signs or prompts.
		- Start the player with no ammo or grenades, give them later when necessary
		- Design the level to let them figure out how to platform; slowly expose the player to traps/pits
		- Give them a safe spot for their first enemy encounter

Stage select and options on main menu + pause menu + death screen
	- Options menu
		- Make graphic (or open text file) showing all possible button/key inputs
		- Change resolution/fullscreen



STRETCH FEATURES (For added polish):

Create variance on sound effects

Run button with Shift/RT, give small increase to vertical velocity if running and jumping at the same time

Double jump with half of the first jump's verticality

Weapon upgrades
	- The more enemies you kill, adds to UI
	- Each level increases damage output and rate of fire
	- Possibly increase explosion radius

New tiles
	- Double jump refiller: lets the player jump again once collected
	- Coin : Collectable, adds to score, would be on top-right corner
	- Bouncepad: boosts the player vertically
	- Spikes: halves the player's health

Melee attacks that change properties depending on the direction held (requires new added movement buttons, sprites collision checks...)