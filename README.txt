#About the project
    This is a Rubik's cube solver, created by using pygame. The project contains files, where we have the following notations:
        a_<name>.py - a file containing algorithm related data
        c_<name>.py - a file containing class related data
        e_<name>.py - a file containing enum related data
        v_<name>.py - a file containing visualisation related data
        <name>.json - a file containing data to be loaded/saved
        
        To open the solver run play_game.py

#Cube display
The Cube will look like this, where the letters represent the colors on a cube

                            ['y', 'y', 'y']
                            ['y', 'y', 'y']
                            ['y', 'y', 'y']
                      
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']
      ['b', 'b', 'b']       ['r', 'r', 'r']       ['g', 'g', 'g']       ['o', 'o', 'o']

                            ['w', 'w', 'w']
                            ['w', 'w', 'w']
                            ['w', 'w', 'w']

#Notations
    The sides are represented as:
        Front = Red
        Left = Blue
        Right = Green
        Back = Orange
        Up = Yellow
        Down = White

    The Program uses the standard Rubik's cube notations (U, U', B, B', ...)

#Features
    Movement Buttons
    - They can be used once you want to solve the cube manually.
    - When pressed, the movement written on it will be executed on the cube.
    
    Scramble Button
    - Randomly shuffles the cube with multiple turns - it can be used only once
    
    PC Solve Button
      - After you scramble, you will be available to choose to solve the cube manually 
        or directly make the pc solve it for you. While trying to solve it manually, you can always make the pc solve
        it for you if you give up.