PongGame class:

Represents the Pong game.
Defines constants for screen dimensions, ball speed, paddle speed, and a white color.
Initializes the game state in the constructor (__init__) with paddle positions, ball position, ball speed, and scores.
Handles events such as key presses for paddle movement (handle_events method).
Updates the game state, including ball and paddle positions, and handles scoring (update_game_state method).
Provides methods to retrieve scores and paddle positions.

TestPongGame class:
Inherits from unittest.TestCase and contains test cases for the PongGame class.
The setUp method initializes a PongGame instance for each test case.

Test Cases:
test_paddle_movement: Testing the movement of paddles in response to key events. key up down left right
test_ball_movement: Testing the movement of the ball in the game.
test_scoring: Testing the score logic when the ball goes out of bounds.

Mocking:
Mocks the Pygame event using MagicMock for testing paddle movement.

Execution:
The codes will  execute the test cases when : main module (if __name__ == '__main__':).



REFERENCES 
pygame documentation
Reference: unittest.mock — mock object library
youtube:https://youtu.be/9gu4BsqjQrA?si=nSUn6643wCqAb7SU


