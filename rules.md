# Project Arcana Rules

## Note
*Version: 20170706*

This rule set is part of the alpha phase of development. There is no promise of a working game yet, just some vague guidelines to help develop the final rules.

## Combat
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

Here, atk is the player's arcana's attack, def is the defending arcana's defense, level is the player's arcana's level, power is the power rating of the move being used, STAB is Same Type Attack Bonus, and weakness is a bonus from from the weakness chart. This will often generate a number with decimals. Ignore everything past the decimal point and just use the whole number. For example, if the formula gave a result of 3.834, the actual value will be 3. When looking up the weakness on the weakness chart, use the type of the move against the type of the defending arcana. If the arcana has more than one type, use the one that gives a higher bonus.

### Status Effects
A status effect includes things like poison, sleep, or being trapped in vines. For this version, please ignore any status effects induced by moves. These will be implemented in a future version.

### Weakness
Some arcana types are weak against certain types of moves. Also, some are resistant to certain types of moves. To find out if a type is strong or weak against another type, check the chart below:

| Move     | Defending Arcana                    |
|---------:|-------------------------------------|
| Bug      | Grass Psychic                       |
|     *NVE*| Fire Fight Poison Flying Ghost      |
| Dragon   | Dragon                              |
|     *NVE*|                                     |
| Electric | Water Flying                        |
|     *NVE*| Electric Grass Dragon (Ground)      |
| Fight    | Normal Ice Rock                     |
|     *NVE*| Poison Flying Psychic Bug           |
| Fire     | Grass Ice Bug                       |
|     *NVE*| Fire Water Rock Dragon              |
| Flying   | Grass Fight Bug                     |
|     *NVE*| Electric Rock                       |
| Ghost    | Psychic Ghost                       |
|     *NVE*| (Normal)                            |
| Grass    | Water Ground Rock                   |
|     *NVE*| Fire Grass Poison Flying Bug Dragon |
| Ground   | Fire Electric Poison Rock           |
|     *NVE*| Grass Bug (Flying)                  |
| Ice      | Grass Ground Flying Dragon          |
|     *NVE*| Fire Water Ice                      |
| Normal   |                                     |
|     *NVE*| Rock (Ghost)                        |
| Poison   | Grass                               |
|     *NVE*| Poison Ground Rock Ghost            |
| Psychic  | Fight Poison                        |
|     *NVE*| Psychic                             |
| Rock     | Fire Ice Flying Bug                 |
|     *NVE*| Fight Ground                        |
| Water    | Fire Ground Rock                    |
|     *NVE*| Water Grass Dragon                  |

To use this chart, look up the attacking move type. If the defending arcana's type is in the row next to the move type, that move does double damage. If the move is in the *Not Very Effective* row, that move does half damage.
