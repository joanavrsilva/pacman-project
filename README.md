<h1 align="center">Pacman</h1>

![gameplay](https://user-images.githubusercontent.com/83631970/141517282-263b2e0f-5384-4af3-abf7-7a8da8dc8451.gif)

[Click here to view the live project :link:]

Pac-Man is a 1980 maze action video game developed and released by Namco for arcades.

This project was created for educational purposes only with the aim of training the python language.

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
Pac-Man is an action maze chase video game; the player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts — Blinky (red), Pinky (pink), Inky (cyan), and Clyde (orange) — that pursue him. When Pac-Man eats all of the dots, the player  advances to the next level. If Pac-Man makes contact with a ghost, he will lose a life; the game ends when all lives are lost. Each of the four ghosts have their own unique, distinct artificial intelligence (A.I.), or "personalities"; Blinky gives direct chase to Pac-Man, Pinky and Inky try to position themselves in front of Pac-Man, usually by cornering him, and Clyde will switch between chasing Pac-Man and fleeing from him.

Placed at the four corners of the maze are large flashing "energizers", or "power pellets". Eating these will cause the ghosts to turn blue with a dizzied expression and reverse direction. Pac-Man can eat blue ghosts for bonus points; when eaten, their eyes make their way back to the center box in the maze, where the ghosts "regenerate" and resume their normal activity. Eating multiple blue ghosts in succession increases their point value. After a certain amount of time, blue-colored ghosts will flash white before turning back into their normal, lethal form. Eating a certain number of dots in a level will cause a bonus item - usually in the form of a fruit – to appear underneath the center box, which can be eaten for bonus points.

The game increases in difficulty as the player progresses; the ghosts become faster and the energizers' effect decreases in duration to the point where the ghosts will no longer turn blue and edible. To the sides of the maze are two "warp tunnels", which allow Pac-Man and the ghosts to travel to the opposite side of the screen. Ghosts become slower when entering and exiting these tunnels.

Text from [Wikipedia](https://en.wikipedia.org/wiki/Pac-Man)

# User Experience
- ## User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the app.
        2. As a First Time Visitor, I want to be able to easily play the game.
        3. As a First Time Visitor, I want to have a good time.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find a progression of levels.
        2. As a Returning Visitor, I want to find my scores.
        3. As a Returning Visitor, I want to find it easy to play and exit the game.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to see all my scores.
        2. As a Frequent User, I want to see my high scores.
        3. As a Frequent User, I want to see different levels.

# Features 

## Design
### Colour Scheme/ Imagery
-   Board: blue and black
-   Pacman: yelow 
-   Gosths: red, yellow, blue, pink - in timer blue and white
-   Tails: light orange
-   Berries: red and orange
-   Interactive elements

## Wireframes
![Pacman](https://user-images.githubusercontent.com/83631970/158587851-c11a7819-903d-48d1-a17e-49b1e50c6869.png)


# Languages Used

-   [Python](https://pt.wikipedia.org/wiki/Python)

# Frameworks Libraries and Programs Used

1. [Git](https://git-scm.com/)

2. [GitHub](https://github.com/)

3. [Heroku](https://www.heroku.com/)

4. [Pygame](https://pypi.org/project/pygame/)

# Testing

[PEP8 online check](http://pep8online.com/) - Passed the PEP8 validator.

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) - Homepage performance


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

- [Wikipedia](https://en.wikipedia.org/wiki/Pac-Man) - Pacmam text.

- [Code Institute Course](https://codeinstitute.net/) - Full Template.

- [Pygame](https://pypi.org/project/pygame/)

- [Code](https://www.youtube.com/watch?v=qBWCuSID1rc) - Devin Leamy pacman project