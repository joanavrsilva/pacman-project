<h1 align="center">Pacman</h1>

![gameplay](https://user-images.githubusercontent.com/83631970/141517282-263b2e0f-5384-4af3-abf7-7a8da8dc8451.gif)

[Click here to view the live project :link:]

Pac-Man is a 1980 maze action video game developed and released by Namco for arcades.

# Table Of Contents

1. [Introduction](#introduction)

2. [User Experience (UX)](#user-experience)

3. [Features](#features)

4. [Languages Used](#languages-used)

5. [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

7. [Testing](#testing)

8. [Deployment](#deployment)
    - [GitHub](#github-pages)
    - [Heroku](#heroku)
    
9. [Credits](#credits)


# Introduction

Pac-Man is an action maze chase video game; the player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts — Blinky (red), Pinky (pink), Inky (cyan), and Clyde (orange) — that pursue him. When Pac-Man eats all of the dots, the player advances to the next level. If Pac-Man makes contact with a ghost, he will lose a life; the game ends when all lives are lost. Each of the four ghosts have their own unique, distinct artificial intelligence (A.I.), or "personalities"; Blinky gives direct chase to Pac-Man, Pinky and Inky try to position themselves in front of Pac-Man, usually by cornering him, and Clyde will switch between chasing Pac-Man and fleeing from him.

Placed at the four corners of the maze are large flashing "energizers", or "power pellets". Eating these will cause the ghosts to turn blue with a dizzied expression and reverse direction. Pac-Man can eat blue ghosts for bonus points; when eaten, their eyes make their way back to the center box in the maze, where the ghosts "regenerate" and resume their normal activity. Eating multiple blue ghosts in succession increases their point value. After a certain amount of time, blue-colored ghosts will flash white before turning back into their normal, lethal form. Eating a certain number of dots in a level will cause a bonus item - usually in the form of a fruit – to appear underneath the center box, which can be eaten for bonus points.

The game increases in difficulty as the player progresses; the ghosts become faster and the energizers' effect decreases in duration to the point where the ghosts will no longer turn blue and edible. To the sides of the maze are two "warp tunnels", which allow Pac-Man and the ghosts to travel to the opposite side of the screen. Ghosts become slower when entering and exiting these tunnels.

Text from [Wikipedia](https://en.wikipedia.org/wiki/Pac-Man)

# User Experience

# Features

## Design
### Colour Scheme


## Wireframes


# Languages Used

-   [Python](https://pt.wikipedia.org/wiki/Python)

# Frameworks Libraries and Programs Used

1. [Git](https://git-scm.com/)

2. [GitHub](https://github.com/)

3. [Heroku](https://www.heroku.com/)

4. [Pygame](https://pypi.org/project/pygame/)

# Testing

    - [PEP8 online check](http://pep8online.com/) - Succesfully passed through the PEP8 validator.

    - [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) - Was used to check homepage page performance


# Deployment

## Heroku

- To deploy the app using Heroku, go through the following steps:

    1. Use pip3 freeze > `requirements.txt` to create a list of the dependencies.

    2. Create a `Procfile` by running this command on the CLI: `echo web: python app.py > Procfile`

    3. Run `git add .`, `git commit -m`, and `git push`, to push the project files to your GitHub repository.

    4. Navigate to Heroku, log in and create a new app by clicking on the 'New' and 'Create New App'. Enter your app name and select your region and create app.

    5. Under the 'Deploy' tab, select 'GitHub - Connect to GitHub'.
    
    6. Enter your repository's name in the input field, and connect once found.

# Credits

- [Wikipedia](https://en.wikipedia.org/wiki/Pac-Man) - Pacmam text and history.

- [Code Institute Course](https://codeinstitute.net/) - template.

- [Pygame](https://pypi.org/project/pygame/)

- [PacmamGame] Devin Leamy pacman project