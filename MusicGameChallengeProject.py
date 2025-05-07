import unittest
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

font = pygame.font.SysFont("Arial", 36)

# Quiz data for each song
quiz_data_by_song = [
    {
        "song": "UBWSorrow.mp3",
        "questions": [
            ("What mood does this song create?", ["Somber", "a awed moment", "heroic", "It's just music dude not deep"], 0),
            ("Where might you hear this song?", ["Movie", "Video Game", "Podcast", "Animated Show"], 3),
            ("Who do you think wrote it?", ["Live singer", "Music Composer", "Foreign Artist", "Unknown Artist"], 1),
            ("Where do you think it was playing on?", ["Fate Stay Night", "Dragon Ball", "Bleach", "Naruto"], 0),
            ("Did you listen to most of the song?", ["No, Too boring, Yuck!", "Yes, Because I enjoy it, but actually I need the point"], 1)
        ]
    },
    {
        "song": "SnakeEater.mp3",
        "questions": [
            ("What mood does this song create?", ["Sad", "Heroic", "Scary", "Relaxing"], 1),
            ("Who composed this song?", ["Pop Artist", "Composer", "Rock Band", "DJ"], 1),
            ("What media is this song likely from?", ["Anime", "Video Game", "Podcast", "Movie"], 1),
            ("Who do you think is Singing?", ["Cynthia Harrell", "Kitty Heywood", "Carla White", "David Bowie"], 0),
            ("Did you listen to most of the song?", ["No, Too boring, Yuck!", "Yes, Because I enjoy it, but actually I need the point"], 1)
        ]
    },
    {
        "song": "Here'sToYou.mp3",
        "questions": [
            ("What mood does this song create?", ["Sad", "Somber", "Retro", "Funky"], 1),
            ("Who composed the song?", ["Lady Gaga", "Taylor swift", "Ennio Morricone, featuring Joan Baez", "Samuel Kim"], 2),
            ("What media was this song played in?", ["Video game", "Movie", "Youtube", "Radio"], 3),
            ("What video game do you think the song was in?", ["Metal Gear Solid", "A new game", "GTA", "Halo"], 0),
            ("Did you listen to most of the song?", ["No, Too boring, Yuck!", "Yes, Because I enjoy it, but actually I need the point"], 1)
        ]
    },
    {
        "song": "Blizzard.mp3",
        "questions": [
            ("What language do you think it is?", ["English", "Korean", "Chinese", "Japanese"], 3),
            ("What media do you think it was featured in?", ["Movie", "Animated show", "Sitcom", "Concert"], 0),
            ("Who do you think the artist??", ["TWICE", "Daichi Miura", "Lee Bul", "Bruce Lee" ], 1)
            ("")
        ]
    }
]

# Game state variables
current_q = 0
score = 0
current_round = None

# Function to draw questions and options
def draw_question(index):
    screen.fill(WHITE)
    question, options, _ = current_round["questions"][index]
    question_surface = font.render(question, True, BLACK)
    screen.blit(question_surface, (50, 50))

    for i, option in enumerate(options):
        pygame.draw.rect(screen, GRAY, (50, 150 + i * 60, 700, 50))
        option_surface = font.render(option, True, BLACK)
        screen.blit(option_surface, (60, 160 + i * 60))

    # Show progress
    progress_text = font.render(f"Question {index + 1} of {len(current_round['questions'])}", True, BLACK)
    screen.blit(progress_text, (50, 10))

    pygame.display.flip()

# Function to play music
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to reset the game
def reset_game():
    global current_q, score, current_round
    current_q = 0
    score = 0
    current_round = random.choice(quiz_data_by_song)
    play_music(current_round["song"])
    draw_question(current_q)

# Start game
reset_game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            question, options, correct_index = current_round["questions"][current_q]

            for i in range(len(options)):
                if 50 <= x <= 750 and (150 + i * 60) <= y <= (200 + i * 60):
                    if i == correct_index:
                        score += 1
                        feedback = "Correct!"
                    else:
                        feedback = "NOPE!"

                    # Show feedback
                    screen.fill(WHITE)
                    feedback_surface = font.render(feedback, True, BLUE)
                    screen.blit(feedback_surface, (WIDTH // 2 - 100, HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.wait(1000)

                    # Next question
                    current_q += 1
                    if current_q >= len(current_round["questions"]):
                        stop_music()
                        screen.fill(WHITE)
                        result_text = f"Song: {current_round['song']} | Your score: {score}/{len(current_round['questions'])}"
                        result_surface = font.render(result_text, True, BLACK)
                        screen.blit(result_surface, (150, HEIGHT // 2))
                        pygame.display.flip()
                        pygame.time.wait(4000)
                        running = False
                    else:
                        draw_question(current_q)

pygame.quit()
sys.exit()
