import pygame



# load font custom size function
def font_mindustry(fontsize): 
    return pygame.font.Font('./assets/fonts/mindustry.ttf', int(fontsize))
def font_arialUnicode(fontsize):
    return pygame.font.Font('./assets/fonts/arialUnicode.ttf', int(fontsize))

# center a surface to blit
def center_surface(surface, offset):
    from main import screen
    surface_rect = surface.get_rect()
    surface_rect.center = (screen.get_rect().center[0]+offset[0], screen.get_rect().center[1]+offset[1])
    return surface, surface_rect

# render intro in a certain tick
def render_text(surface, offset):
    from main import screen
    intro = center_surface(surface, offset)
    screen.blit(intro[0], intro[1])
        
