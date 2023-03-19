#====== IMPORTS ======#
import json
from time import ctime
import os
from math import sin

import pygame

import src
from assets.languages import langs as lang

#====== CONFIG ======#
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Untitled Project")
clock = pygame.time.Clock()

#====== VARIABLES ======#
config = json.load(open('assets/config/config.json', 'r'))
fps = config["fps"]
clang = lang.clang  # current language
tick = 0
intro = True
cursor = "idle"
sprites = {}    # import all sprites into a dictionary from assets/sprites
for sprite_file in [file for file in os.listdir('assets/sprites') if file.endswith('.png')]:
    sprite_name = os.path.splitext(sprite_file)[0] 
    sprites[sprite_name] = [pygame.image.load(os.path.join('assets/sprites', sprite_file)).convert_alpha(),pygame.image.load(os.path.join('assets/sprites', sprite_file)).convert_alpha().get_rect()]

#====== GAME LOOP ======#
running = True
while running:
    #== Config ==#
    screen.fill((0,0,0))
    # due to font_mindustry don't support some 西里爾字母, when the language is on Noschkariski it HAVE TO change font
    if clang == lang.NOS:
        fontset = src.font_arialUnicode
    else:
        fontset = src.font_mindustry


    #== Events ==#
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # pause will make it later
            # intro skipping
            if 0 <= tick <= 14*fps:
                src.swap2.play()
                if 0 <= tick <= 1.5*fps:
                    tick = 1.5*fps
                if 1.6*fps <= tick <= 4*fps:
                    tick = 3.9*fps
                if 4.1*fps <= tick <= 9*fps:
                    tick = 10*fps
                if 10.1*fps <= tick <= 12*fps:
                    tick = 12*fps
                if 12.1*fps <= tick <= 14*fps:
                    tick = 14*fps
        # cursor
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = "click"
        elif event.type == pygame.MOUSEBUTTONUP:
            cursor = "idle"

    #== Intro ==#
    if intro:
        if 0 <= tick < 1.5*fps:
            src.render_text(src.font_arialUnicode(18).render(f"[{ctime()}] {clang.text_helloWorld[0]}", True, (255,255,255)), (0,0))
        elif tick == 1.5*fps:
            src.title_1.play()
        elif 1.5*fps <= tick <= 3.5*fps:
            src.render_text(fontset(48).render(clang.text_intro1[0], True, (255,255,255)), (0,0))
        elif tick == 4*fps:
            src.title_2.play()
        elif 5*fps <= tick <= 9*fps:
            fade_gb = (255-(max(0, min(255, (int((tick/fps)*200)-1250)))))
            fade_r = (255-(max(0, min(255, (int((tick/fps)*200)-1500)))))
            src.render_text(fontset(64).render(clang.text_intro2[0], True, (fade_r,fade_gb,fade_gb)), (0,-30))
            src.render_text(fontset(48).render(clang.text_intro2[1], True, (fade_r,fade_gb,fade_gb)), (0,30))
        elif 10*fps <= tick <= 12*fps:
            fade_rgb = max(0, int((sin(1.6*((tick/fps)-10)))*255))
            src.render_text(fontset(64).render("Inspired by", True, (fade_rgb,fade_rgb,fade_rgb)), (0,-30))
            src.render_text(fontset(48).render("111% - Random Dice", True, (fade_rgb,fade_rgb,fade_rgb)), (0,30))
        elif 12*fps <= tick <= 14*fps:
            fade_rgb = max(0, int((sin(1.6*((tick/fps)-12)))*255))
            src.render_text(fontset(64).render("Inspired by", True, (fade_rgb,fade_rgb,fade_rgb)), (0,-30))
            src.render_text(fontset(48).render("Anuke - Mindustry", True, (fade_rgb,fade_rgb,fade_rgb)), (0,30))
        elif tick >= 15*fps-1:
            pygame.mixer.stop()
            intro = False
    
    #== Language Select ==#
    elif not intro:
        if tick == 15*fps:
            src.swap1.play()
        if tick >= 15*fps:
            src.render_text(fontset(64).render(clang.text_lang_select[0], True, (255,255,255)), (0,-350))
            # also need a under line
        if tick == 15.5*fps:
            src.swap2.play()
        if tick >= 15.5*fps:
            # eng lang button render
            pass
        if tick == 15.55*fps:
            src.swap2.play()
        if tick >= 15.55*fps:
            # zh-tw lang button render
            pass
        if tick == 15.6*fps:
            src.swap2.play()
        if tick >= 15.6*fps:
            # zh-cn lang button render
            pass
        if tick == 15.65*fps:
            src.swap2.play()
        if tick >= 15.65*fps:
            # sch lang button render
            pass
        if tick == 15.7*fps:
            src.swap2.play()
        if tick >= 15.7*fps:
            # nos lang button render
            pass
        if tick == 15.75*fps:
            src.swap2.play()
        if tick >= 15.75*fps:
            # debug lang button render
            pass

    #== Cursor ==#
    if not intro:
        for cursor_rect in [sprites["cursor_idle"][1], sprites["cursor_click"][1], sprites["cursor_reject"][1]]:
            cursor_rect.center = pygame.mouse.get_pos()
        if cursor == "idle":
            screen.blit(sprites["cursor_idle"][0], sprites["cursor_idle"][1])
        elif cursor == "click":
            screen.blit(sprites["cursor_click"][0], sprites["cursor_click"][1])
        elif cursor == "reject":
            screen.blit(sprites["cursor_reject"][0], sprites["cursor_reject"][1])

    #== Loop Update ==#
    tick += 1
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()