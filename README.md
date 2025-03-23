# Turtle-Race

A Python-based racing game where player bets on one of six colored turtles to win a race. Built using the Turtle graphics library.

## Features

- 6 different colored turtles (red, orange, yellow, green, blue, purple)
- Betting system for player interaction
- Random movement for unpredictable races
- Visual race track with finish line
- Winner detection and bet outcome display

## Implementation Details

The game uses:
- Turtle graphics for visual elements
- Random number generation for turtle movement
- Screen event handling
- Multiple turtle objects
- Coordinate system for race boundaries

## How to Play

1. Run the [`main.py`](main.py) script
2. Enter your bet when prompted by choosing a turtle color:
   - red
   - orange
   - yellow
   - green
   - blue
   - purple
3. Watch the race unfold
4. The first turtle to reach the right edge wins
5. You'll be notified if you won or lost your bet

## Technical Details

- Screen dimensions: 500x400 pixels
- Starting line: x=-230
- Finish line: x=230
- Random movement range: 0-10 pixels per step
- Turtle spacing: 30 pixels vertically

## Dependencies

- Python 3.x
- turtle (built-in library)
- random (built-in library)

## File Structure

- [`main.py`](main.py): Core game logic and implementation
- `README.md`: This documentation
- `LICENSE`: MIT license file
