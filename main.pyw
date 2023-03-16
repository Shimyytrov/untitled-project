debug = False
import pygame as core
import time
import sys
import random
import json
import assets.languages.langs as langs

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
def font_mindustry2(fontsize):   # load font custom size function
    return core.font.Font('./assets/fonts/mindustry.ttf', int(128/fontsize))
def font_arialUnicode(fontsize):   # load font custom size function
    return core.font.Font('./assets/fonts/arialUnicode.ttf', int(fontsize))
sound_title_1 = core.mixer.Sound('./assets/sounds/title1.wav')
sound_title_2 = core.mixer.Sound('./assets/sounds/title2.wav')
sound_swap1 = core.mixer.Sound('./assets/sounds/swap1.wav')
sound_swap2 = core.mixer.Sound('./assets/sounds/swap2.wav')
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

clang = settings["lang"]
intro = True
tick = 0
ctime = time.ctime()
cursor = "idle"
cursor_rejected = True

#=== Title vars ===#
lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
logo1_line_alpha = 255
logo1_red_alpha = 0
header_alpha = 255
lang0W, lang0H = font_mindustry2(3.5).render("######", True, (255,255,255)).get_size()   # default use font size (width, height)

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
def render_header(line_text, font, color): # render logo1line
    header_line = font.render(line_text, True, color)
    header_line.set_alpha(header_alpha)
    header_rec = header_line.get_rect()
    header_rec.center = (width/2, (height/10))
    return header_line, header_rec
def render_langs(text, color, offset): # render langs button and outline
    lang = font_mindustry2(3.5).render(text, True, color)
    lang_rec = lang.get_rect()
    lang_rec.center = (width/2, height*(offset/10))
    langW, langH = lang.get_size()
    lang_outline = core.Rect(0, 0 , langW+lang0W*0.2, lang0H*1.4)
    lang_outline.center = (width/2, height*(offset/10))
    screen.blit(lang, lang_rec)
    return lang, lang_outline
def lang_pressed(lang, langsec, langcolor, offset): # when langs button pressed
    global button_cooldown, Hlocation, langW, langH, lang_selected1, lang1_Bcolor, lang2_Bcolor, lang3_Bcolor, lang4_Bcolor, lang5_Bcolor, lang6_Bcolor
    if not button_cooldown:
        button_cooldown = True
        lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
        langs.selected_language = langsec
        settings["lang"] = f"{langs.selected_language.__name__}"
        save_settings()
        langW, langH = lang.get_size()
        Hlocation = height*(offset/10)
        lang_selected1 = True
        sound_click.play()
        time.sleep(0.1)
        button_cooldown = False

if clang == "NOS":
    fontset = font_arialUnicode
else:
    fontset = font_mindustry
while intro:
    mouse_pos = (0, 0)
    screen.fill((0, 0, 0))

    # events
    for event in core.event.get():
        if event.type == core.QUIT: # quit
            core.quit()
            sys.exit()
        if event.type == core.KEYDOWN and event.key == core.K_ESCAPE: # skip
            intro = False
            sound_click.play()
    if 0 <= tick <= 49:
        logo0 = render_logo1("["+ctime+"] "+langs.clang.text_helloWorld[0], font_arialUnicode(18), 0)
        screen.blit(logo0[0], logo0[1])
    if tick == 50:
        sound_title_1.play()
    if 50 <= tick <= 150:
        logo0 = render_logo1(langs.clang.text_intro1[0], fontset(48), 0)
        screen.blit(logo0[0], logo0[1])
    if tick == 200:
        sound_title_2.play()
    if 250 <= tick <= 450:
        logo0 = render_logo1(langs.clang.text_intro2U[0], fontset(64), -30)
        logo1 = render_logo1(langs.clang.text_intro2D[0], fontset(48), 30)
        logoRED0 = render_red1(langs.clang.text_intro2U[0], fontset(64), -30)
        logoRED1 = render_red1(langs.clang.text_intro2D[0], fontset(48), 30)
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
    if 450 < tick <= 550:
        logo0 = render_logo1("Inspired by", fontset(64), -30)
        logo1 = render_logo1("111% - Random Dice", fontset(48), 30)
        screen.blit(logo0[0], logo0[1])
        screen.blit(logo1[0], logo1[1])
    if 450 < tick <= 475:
        logo1_line_alpha += 11
    if tick == 476:
        logo1_line_alpha = 255
    if 525 <= tick < 550:
        logo1_line_alpha -= 11
    if tick == 550:
        logo1_line_alpha = 0
    if 550 < tick <= 650:
        logo0 = render_logo1("Inspired by", fontset(64), -30)
        logo1 = render_logo1("Anuke - Mindustry", fontset(48), 30)
        screen.blit(logo0[0], logo0[1])
        screen.blit(logo1[0], logo1[1])
    if 550 < tick <= 575:
        logo1_line_alpha += 11
    if tick == 576:
        logo1_line_alpha = 255
    if 625 <= tick < 650:
        logo1_line_alpha -= 11
    if tick == 650:
        logo1_line_alpha = 0
    if tick == 700:
        intro = False
    tick += 1
    core.display.flip()
    fps_clock.tick(fps)
    
# After intro
fps = 50
cursor_rejected = False
if settings["default"]:
    firstLaunch = True
    tick = 0
elif not settings["default"]:
    firstLaunch = False
    tick = 0
while firstLaunch:
    screen.fill((0,0,0))
    # events
    for event in core.event.get():
         if event.type == core.KEYDOWN and event.key == core.K_ESCAPE or event.type == core.QUIT: # quit
            core.quit()
            sys.exit()
         if event.type == core.MOUSEBUTTONDOWN:
            cursor = "click"
         if event.type == core.MOUSEBUTTONUP:
            cursor = "idle"
    
    if tick == 50:
        play_track("cave_ambience", -1, 0)
        sound_swap1.play()
    if tick >= 50:
        selectLang = render_header(langs.clang.text_lang_select[0], fontset(64), (255, 255, 255))
        screen.blit(selectLang[0], selectLang[1])
        core.draw.rect(screen, (255, 214, 99), ((width-(width/1.75))/2, (height/7)+(height/36), width/1.75, height/200)) # underline
    if tick == 75:
        sound_swap2.play()
    if tick == 77:
        sound_swap2.play()
    if tick == 79:
        sound_swap2.play()
    if tick == 81:
        sound_swap2.play()
    if tick == 83:
        sound_swap2.play()
    if tick == 85:
        sound_swap2.play()
    if tick >= 75:
        lang1, lang1_rec = render_langs("English", lang1_Bcolor, 3)
    if tick >= 77:
        lang2, lang2_rec = render_langs("中文 (台灣正體)", lang2_Bcolor, 4)
    if tick >= 79:
        lang3, lang3_rec = render_langs("中文 (中国、大马简体)", lang3_Bcolor, 5)
    if tick >= 81:
        lang4, lang4_rec = render_langs("DEBUG (For developer)", lang4_Bcolor, 6)
    if tick >= 83:
        lang5, lang5_rec = render_langs("Schmitŕovkiy (Unfinished)", lang5_Bcolor, 7)
    if tick >= 85:
        lang6, lang6_rec = render_langs("Нощкаріскі Щтор (Unfinished)", lang6_Bcolor, 8)
        
        if lang1_rec.collidepoint(mouse_pos):
            lang_pressed(lang1, langs.ENG, lang1_Bcolor, 3)
            lang1_Bcolor = 255, 214, 99
        elif lang2_rec.collidepoint(mouse_pos):
            lang_pressed(lang2, langs.TAI, lang2_Bcolor, 4)
            lang2_Bcolor = 255, 214, 99
        elif lang3_rec.collidepoint(mouse_pos): 
            lang_pressed(lang3, langs.CHI, lang3_Bcolor, 5)
            lang3_Bcolor = 255, 214, 99
        elif lang4_rec.collidepoint(mouse_pos): 
            lang_pressed(lang4, langs.debug, lang4_Bcolor, 6)
            lang4_Bcolor = 255, 214, 99
        elif lang5_rec.collidepoint(mouse_pos): 
            lang_pressed(lang5, langs.SCH, lang5_Bcolor, 7)
            lang5_Bcolor = 255, 214, 99
        elif lang6_rec.collidepoint(mouse_pos): 
            lang_pressed(lang6, langs.NOS, lang6_Bcolor, 8)
            lang6_Bcolor = 255, 214, 99
    if not cursor_rejected:
         if cursor == "idle":
              cursor_idle_rect.center = core.mouse.get_pos()
              screen.blit(cursor_idle_img, cursor_idle_rect)
         elif cursor == "click":
              cursor_click_rect.center = core.mouse.get_pos()
              screen.blit(cursor_click_img, cursor_click_rect)
    tick += 1
    core.display.flip()
    fps_clock.tick(fps)