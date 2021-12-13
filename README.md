# Cubeb
## PyGame group project made for Computer Science II (Python) @ Howard University [CSCI 136-02 Fall 2021, Group #14]

Hello! This is Cubeb, soon being the repository for a 2D platformer game made using the PyGame library.

The game is playable with arrow keys/zxc, wasd/jkl, numpad/123, and controller d-pad/face buttons.

The application currently runs at a windowed 1280x720.

Left and Right Arrow keys do what you'd expect. 
Up Arrow and Z map as jump, X maps as shoot, and C maps to your grenade.
As of 12/13 7:30 AM, there are two currently playable levels; a third tutorial level is in the works. 

[Project proposal: https://docs.google.com/document/d/1RulH314LERlbpVUxJNrRWT88P7ziuJKV94BrBrSf9gk/edit?usp=sharing ]

TO-DO (Essential):

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

Polish jump physics
	- Fix jump sound playing mid-jump
	- Allow changing jump altitude depending on how long jump button is held

Stretchable screen and fullscreen with Alt + Enter

Tutorial level
	- Gradually let the player explore the game mechanics as the level goes, without need for signs or prompts
		- Start the player with no ammo or grenades, give them later when necessary
		- Design the level to let them figure out how to platform; slowly expose the player to traps/pits
		- Give them a safe spot for their first enemy encounter



STRETCH FEATURES (For added polish):

Polish sound effects
	- Add separate player & enemy death SFX
	- Add variance to the jump/shoot/grenade/death SFX

Add two harder levels after the first three
	- Design one around hard platforming alone, then design one around hard platforming + enemies

Stage select and options on main menu + pause menu + death screen
	- Options menu
		- Make graphic (or open text file) showing all possible button/key inputs
		- Change resolution/fullscreen

Either make boxes do something, like turn into Ammo/HP, or remove them entirely

Add Double Jump, offering half of the first jump's verticality

Add Run button with Shift/RT
	- Give small increase to vertical velocity if running and jumping at the same time
	- Make a toggleable option for running automatically or not

New tiles
	- Double jump refiller: lets the player jump again once collected
	- Coin : Collectable, adds to score, would be on top-right corner
	- Bouncepad: boosts the player vertically
	- Spikes: halves the player's health

Melee attacks that change properties depending on the direction held (requires new added movement buttons, sprites collision checks...)

Weapon upgrades
	- The more enemies you kill, your level increases and is shown at top-right
	- Each level increases damage output, size of bullets/explosions, and max HP