import pygame
import os
# keyboard conttols
KEY_PLAY_PAUSE = pygame.K_SPACE
KEY_NEXT = pygame.K_RIGHT
KEY_PREVIOUS = pygame.K_LEFT

pygame.init()
pygame.mixer.init()  # Initialize mixer

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

music_files = [os.path.join(r"C:\Users\User\Desktop\PP2 projects\PP2\lab_7\music", f) for f in os.listdir(r"C:\Users\User\Desktop\PP2 projects\PP2\lab_7\music") if f.endswith(".mp3")]
current_song = 0

# Function to play/pause music
def play_pause():
  global is_playing
  if is_playing:
    pygame.mixer.music.pause()
  else:
    pygame.mixer.music.unpause()
  is_playing = not is_playing

pygame.mixer.music.load(music_files[current_song])

is_playing = True

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == KEY_PLAY_PAUSE:
        play_pause()
      elif event.key == KEY_NEXT and current_song < len(music_files) - 1:
        current_song += 1
        pygame.mixer.music.load(music_files[current_song])
        pygame.mixer.music.play()
      elif event.key == KEY_PREVIOUS and current_song > 0:
        current_song -= 1
        pygame.mixer.music.load(music_files[current_song])
        pygame.mixer.music.play()

  screen.fill((0, 0, 0))
  pygame.display.flip()

  # Check if music finished playing (for next song handling)
  if not pygame.mixer.music.get_busy() and is_playing:
    current_song = (current_song + 1) % len(music_files)  # Wrap around to first song
    pygame.mixer.music.load(music_files[current_song])
    pygame.mixer.music.play()
pygame.quit()