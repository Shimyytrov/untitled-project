debug = False
import pygame as core
import time
import sys
import random
import json

#===== Saves =====#
settings = {    # default settings
    "lang": "ENG",
    "default": True
}
with open('./assets/json/settings.json', 'r') as settings_json:
    settings = json.load(settings_json)

core.init()
core.display.set_caption("Untitled Project")
core.mouse.set_visible(False)
fps = 50    # fps
fps_clock = core.time.Clock() # clock
screen_info = core.display.Info() # get screen info
width, height = screen_info.current_w, screen_info.current_h    # get screen (width, height)
screen = core.display.set_mode((width, height))   # full screen
def font_mindustry(fontsize):   # load font custom size function
    return core.font.Font('./assets/fonts/mindustry.ttf', int(fontsize))
def font_arialUnicode(fontsize):   # load font custom size function
    return core.font.Font('./assets/fonts/arialUnicode.ttf', int(fontsize))
sound_title_1 = core.mixer.Sound('./assets/sounds/title1.wav')
sound_title_2 = core.mixer.Sound('./assets/sounds/title2.wav')
sound_swap1 = core.mixer.Sound('./assets/sounds/swap1.wav')
sound_click = core.mixer.Sound('./assets/sounds/click.wav')
cursor_idle_img = core.image.load('./assets/sprites-raw/cursor_idle.png').convert()
cursor_idle_rect = cursor_idle_img.get_rect()
cursor_click_img = core.image.load('./assets/sprites-raw/cursor_click.png').convert()
cursor_click_rect = cursor_click_img.get_rect()
cursor_reject_img = core.image.load('./assets/sprites-raw/cursor_reject.png').convert()
cursor_reject_rect = cursor_reject_img.get_rect()

def play_track(file, loop, fade_ms):    # play track function
    core.mixer.music.load(f'./assets/tracks/{file}.ogg')
    core.mixer.music.play(loop, fade_ms)

intro = True
tick = 0
ctime = time.ctime()
cursor = "idle"
cursor_rejected = True

#=== Title vars ===#
logo1_line_alpha = 255
logo1_red_alpha = 0
def render_logo1(line_text, font, offset): # render logo1line
    logo1_line = font.render(line_text, True, (255, 255, 255))
    logo1_line.set_alpha(logo1_line_alpha)
    logo1_rec = logo1_line.get_rect()
    logo1_rec.center = (width/2, (height/2)+offset)
    return logo1_line, logo1_rec
def render_red1(line_text, font, offset): # render logo1line
    logo1_red = font.render(line_text, True, (196, 0, 0))
    logo1_red.set_alpha(logo1_red_alpha)
    logo1_red_rec = logo1_red.get_rect()
    logo1_red_rec.center = (width/2, (height/2)+offset)
    return logo1_red, logo1_red_rec
while intro:
    mouse_pos = (0, 0)
    screen.fill((0, 0, 0))

    # events
    for event in core.event.get():
        if event.type == core.KEYDOWN and event.key == core.K_ESCAPE or event.type == core.QUIT: # quit
         core.quit()
         sys.exit()
    if 0 <= tick <= 49:
        logo0 = render_logo1("["+ctime+"] "+"Hello world!", font_arialUnicode(18), 0)
        screen.blit(logo0[0], logo0[1])
    if tick == 50:
        sound_title_1.play()
    if 50 <= tick <= 150:
        logo0 = render_logo1("A Untitled Project", font_mindustry(48), 0)
        screen.blit(logo0[0], logo0[1])
    if tick == 200:
        sound_title_2.play()
    if 250 <= tick <= 450:
        logo0 = render_logo1("Produced by", font_mindustry(64), -30)
        logo1 = render_logo1("Shimyytrov Studio", font_mindustry(48), 30)
        logoRED0 = render_red1("Produced by", font_mindustry(64), -30)
        logoRED1 = render_red1("Shimyytrov Studio", font_mindustry(48), 30)
        screen.blit(logo0[0], logo0[1])
        screen.blit(logo1[0], logo1[1])
        screen.blit(logoRED0[0], logoRED0[1])
        screen.blit(logoRED1[0], logoRED1[1])
    if 275 <= tick <= 325:
        logo1_red_alpha += 1
    if 325 <= tick < 365:
        logo1_red_alpha += 5
    if tick == 365:
        logo1_red_alpha = 255
    if 375 <= tick <= 450:
        logo1_red_alpha -= 3.4
        logo1_line_alpha -= 10
    if tick == 450:
        logo1_line_alpha = 0
        logo1_red_alpha = 0
    if tick == 500:
        intro = False
    tick += 1
    core.display.flip()
    fps_clock.tick(fps)
    
# After intro
cursor_rejected = False
if settings["default"]:
    lang_selected2 = False
    tick = 0
elif not settings["default"]:
    lang_selected2 = True
    tick = 0
while True:
    screen.fill((0, 0, 0))
    # events
    for event in core.event.get():
         if event.type == core.KEYDOWN and event.key == core.K_ESCAPE or event.type == core.QUIT: # quit
            core.quit()
            sys.exit()
         if event.type == core.MOUSEBUTTONDOWN:
            cursor = "click"
         if event.type == core.MOUSEBUTTONUP:
            cursor = "idle"
    
    if not cursor_rejected:
         if cursor == "idle":
              cursor_idle_rect.center = core.mouse.get_pos()
              screen.blit(cursor_idle_img, cursor_idle_rect)
         elif cursor == "click":
              cursor_click_rect.center = core.mouse.get_pos()
              screen.blit(cursor_click_img, cursor_click_rect)
    
    if tick == 50:
        play_track("cave_ambience", -1, 0)
    if tick == 100:
        sound_swap1.play()
    tick += 1
    core.display.flip()
    fps_clock.tick(fps)