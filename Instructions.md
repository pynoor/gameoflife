# Conway's Game of Life

## Long in short

* Board where each cell can have two possible states:
  * Alive
  * Dead
* The goal is to calculate the next generation of the board by taking into account 4 rules (see below).

Important: not needed to implement a GUI.

## The 4 rules

* Any alive cell with less than 2 alive neighbours, dies (underpopulation)
* Any alive cell with more than 3 alive neighbours, dies (overpopulation)
* Any alive cell with exactly 2 or 3 alive neighbours, keeps being alive in the next generation.
* Any dead cell with exactly 3 alive neighbours, becomes alive in the next generation.

## Example

![Evolution example](img/example.png)

Note: we assume that the evolution affects all the cells simultaneously.

## Good to know

* We’re aiming for production-ready code.
* Feel free to use your language/technology of choice.
* It's recommended to spend not more than 2 hours with the exercise.
* You're encouraged to leverage a version control system, so we can understand the intermediate steps leading to your solution.
* Problems? Let us know, we’re always happy to help ;)
* Done? Share with us your work, ideally as link to a GitHub (or Bitbucket) repository ;)

Happy hacking! :)
