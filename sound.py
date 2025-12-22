from pygame import mixer

from resource_path import resource_path

shoot_sound = None
end_sound = None


def init_sounds():
    global shoot_sound, end_sound
    if not shoot_sound or not end_sound:
        try:
            shoot_sound = mixer.Sound(resource_path("assets/shoot_2.wav"))
            shoot_sound.set_volume(0.1)
            end_sound = mixer.Sound(resource_path("assets/gameover.wav"))
            end_sound.set_volume(0.6)

        except Exception as e:
            print(f"Error: Could not load sound files: {e}")


def shooting_sound():
    if shoot_sound:
        shoot_sound.play()


def gameover():
    if end_sound:
        mixer.music.pause()
        end_sound.play()
