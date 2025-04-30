import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Challenge Game")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

# Define the font
font = pygame.font.SysFont("Arial", 36)

# Quiz data: (question, [options], correct_index)
demo_quiz_data = [
    ("What Song genre do you think it is?", ["Choir", "Classical", "Rap", "Soundtrack"], 3),
    ("What song do you think the song has been featured in?", ["Movie", "Video Game", "Podcast", "Animated Show"], 1),
    ("Who wrote do you think wrote it?", ["Live singer", "Music Composer", "Foreign Arist", "Idk"], 1),
    ("Have you heard the song before", ["Yes", "No",], 0)
]

# Game state
current_q = 0
score = 0

# Corresponding music files (ensure the correct file paths and extensions)
music_files = [
    "UBWSorrow.mp3",
    "SnakeEater.mp3"
    ]


# Function to draw questions and options
def draw_question(index):
    screen.fill(WHITE)
    question, options, _ = demo_quiz_data[index]
    question_surface = font.render(question, True, BLACK)
    screen.blit(question_surface, (50, 50))

    for i, option in enumerate(options):
        pygame.draw.rect(screen, GRAY, (50, 150 + i * 60, 700, 50))
        option_surface = font.render(option, True, BLACK)
        screen.blit(option_surface, (60, 160 + i * 60))
    pygame.display.flip()


# Function to play music
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)  # Loop music


# Function to stop music
def stop_music():
    pygame.mixer.music.stop()


# Function to reset the game
def reset_game():
    global current_q, score
    current_q = 0
    score = 0
    random.shuffle(music_files)  # Shuffle the songs for each new game


# Start the first music and quiz
reset_game()  # Call reset_game to initialize the first round with shuffled music
play_music(music_files[current_q])
draw_question(current_q)

running = True  # Initialize running variable

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(4):
                if 50 <= x <= 750 and (150 + i * 60) <= y <= (200 + i * 60):
                    _, _, correct_index = demo_quiz_data[current_q]

                    # Check if selected answer is correct
                    if i == correct_index:
                        score += 1
                        feedback = "Correct!"
                    else:
                        feedback = "Wrong!"

                    # Show feedback on screen
                    screen.fill(WHITE)
                    feedback_surface = font.render(feedback, True, BLUE)
                    screen.blit(feedback_surface, (WIDTH // 2 - 100, HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.wait(1000)

                    # Move to next question
                    current_q += 1
                    if current_q >= len(demo_quiz_data):
                        stop_music()
                        screen.fill(WHITE)
                        result_surface = font.render(
                            f"The songs was were {music_files} Quiz Complete! Your score: {score}/{len(demo_quiz_data)}",
                            True,
                            BLACK
                        )
                        screen.blit(result_surface, (150, HEIGHT // 2))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                    else:
                        draw_question(current_q)  # Show next question

pygame.quit()
sys.exit()