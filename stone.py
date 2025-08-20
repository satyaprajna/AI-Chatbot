
import random
#from pyscript import Element

      # Define the choices
choices = ["Stone", "Paper", "Scissors"]

      # Function to get computer's move
def get_computer_move():
          return random.choice(choices)

      # Function to determine the result of the game
def determine_winner(user_move, computer_move):
          if user_move == computer_move:
              return "It's a draw!"
          elif (user_move == "Stone" and computer_move == "Scissors") or \
               (user_move == "Paper" and computer_move == "Stone") or \
               (user_move == "Scissors" and computer_move == "Paper"):
              return "You win!"
          else:
              return "You lose!"

      # Function to handle user's move
def user_move_selected(move):
          # Get computer's move
          computer_move = get_computer_move()

          # Update the UI with both moves
          Element("user_move").write(move)
          Element("computer_move").write(computer_move)

          # Determine the winner
          result = determine_winner(move, computer_move)
          Element("result").write(result)

       # Event listeners for the buttons
Element("stone_button").element.addEventListener("click", lambda e: user_move_selected("Stone"))
Element("paper_button").element.addEventListener("click", lambda e: user_move_selected("Paper"))
Element("scissors_button").element.addEventListener("click", lambda e: user_move_selected("Scissors"))
