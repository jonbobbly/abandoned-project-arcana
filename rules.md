# Project Arcana Rules

## Note
*v0.0.1-alpha1*

This rule set is part of the early phase of development. There is no promise of a working game yet, just some vague guidelines to help develop the final rules.

Also, while the rules make reference to "saving" various pieces of information in the game, such as which arcana you have caught, right now there is no official system for tracking and recording such information. That is something that I'm going to let grow out of various playtests and time.

## Arcana Stats
An arcana has various kinds of stats. These are its Base Stats, Individual Values (IVs) and Effort Values (EVs).

### Base Stats
The Base Stats are the stats that are common to a Form. All arcana with the same Form have the same Base Stats.

### IVs and EVs
Individual Values are specific to each arcana. They are determined when the arcana hatch and never change through-out an arcana's life. Effort Values, on the other hand, can be changed through dedicated training at a gym.

*Note: EVs and EV training are not in this version. Please count all EVs as 0.*

### Arcana Levels and XP
As an arcana wins in combat, they earn XP. After a certain amount of XP has been attained, the arcana will "level up." When an arcana reaches a higher level, it will be more powerful in combat. Some arcana even change into more powerful forms after they have reached certain levels.


## Wild Combat
Combat is one of the central components of Project Arcana. Most of the player's time is spent in combat. There are two main types of combat: between the player and wild Arcana, and between the player and other arcana trainers.

### Rounds and Turns
A fight is broken down into rounds. There is always at least one round, but fights can go one for as long as both opponents are able to battle. A round is divided into turns, one for each arcana fighting.

### Beginning Wild Combat
To setup a wild battle, the player first "sends out" their first arcana. Then, an opponent is chosen based on the rules for the area. Usually by rolling dice against an encounter table.

### Round Start
At the beginning of each round, the speed stats of the arcana are compared. The one with the highest stat goes first.

### Player's Turn
When it's the player's turn, they may choose among four options: attacking, using an item, switching out arcana, or running from battle.

### Opponent's Turn
Unless stated otherwise by the rules of the area, all wild arcana will choose to attack on their turn. Which move they choose is determined by dice rolls.

### Inflicting Damage
Moves with a power rating above 0 can do damage, either physical or "special," according to the move's category. To determine how much damage, consider the following formula:

(atk / def)(level / 100)( power )( STAB )( weakness )

<dl>
<dt>atk</dt>
<dd>The Player's Attack</dd>

<dt>def</dt>
<dd>The Foe's Defense</dd>

<dt>level</dt>
<dd>The Player's Level</dd>

<dt>power</dt>
<dd>The power of the attacking move</dd>

<dt>STAB</dt>
<dd>Same Type Attack Bonus. If the attacking move matches one of the types of the arcana using it, STAB = 1.5, otherwise STAB = 1.</dd>

<dt>weakness</dt>
<dd>This is found by reading the chart in the Weakness section.</dd>
</dl>

This will often generate a number with decimals. Ignore everything past the decimal point and just use the whole number. For example, if the formula gave a result of 3.834, the actual value will be 3. 

### Status Effects
A status effect includes things like poison, sleep, or being trapped in vines. For this version, please ignore any status effects induced by moves. These will be implemented in a future version.

### Weakness
Some arcana types are weak against certain types of moves. Also, some are resistant to certain types of moves. To find out if a type is strong or weak against another type, check the chart below:

| Move     | Bonus | Defending Arcana                    |
|---------:|:-----:|-------------------------------------|
| Bug      | Super | Grass Psychic                       |
|          | NVE   | Fire Fight Poison Flying Ghost      |
| Dragon   | Super | Dragon                              |
| Electric | Super | Water Flying                        |
|          | NVE   | Electric Grass Dragon (Ground)      |
| Fight    | Super | Normal Ice Rock                     |
|          | NVE   | Poison Flying Psychic Bug           |
| Fire     | Super | Grass Ice Bug                       |
|          | NVE   | Fire Water Rock Dragon              |
| Flying   | Super | Grass Fight Bug                     |
|          | NVE   | Electric Rock                       |
| Ghost    | Super | Psychic Ghost                       |
|          | NVE   | (Normal)                            |
| Grass    | Super | Water Ground Rock                   |
|          | NVE   | Fire Grass Poison Flying Bug Dragon |
| Ground   | Super | Fire Electric Poison Rock           |
|          | NVE   | Grass Bug (Flying)                  |
| Ice      | Super | Grass Ground Flying Dragon          |
|          | NVE   | Fire Water Ice                      |
| Normal   | NVE   | Rock (Ghost)                        |
| Poison   | Super | Grass                               |
|          | NVE   | Poison Ground Rock Ghost            |
| Psychic  | Super | Fight Poison                        |
|          | NVE   | Psychic                             |
| Rock     | Super | Fire Ice Flying Bug                 |
|          | NVE   | Fight Ground                        |
| Water    | Super | Fire Ground Rock                    |
|          | NVE   | Water Grass Dragon                  |

To use this chart, look up the attacking move type. If the defending arcana's type is in the row labeled "Super", that move is super effective and deals double damage. If the defending arcana's type is in the "NVE" row, that move is Not Very Effective and deals half damage. If the defending arcana's type is in parentheses, the move deals no damage.

### Fainting
When an arcana runs out of HP, it faints and is unable to battle. When that happens, XP is awarded.

