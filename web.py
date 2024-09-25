import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Contador con Pygame")

# Configurar fuente
font = pygame.font.Font(None, 74)  # Fuente predeterminada con tamaño 74

# Configurar colores
white = (255, 255, 255)
black = (0, 0, 0)

# Inicializar contador
counter = 0

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter += 1  # Incrementar contador al presionar espacio
            elif event.key == pygame.K_BACKSPACE:
                counter -= 1  # Decrementar contador al presionar borrar

    # Limpiar la pantalla
    screen.fill(white)

    # Renderizar texto del contador
    text = font.render(str(counter), True, black)
    
    # Posicionar texto en el centro de la pantalla
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    
    # Mostrar texto en la pantalla
    screen.blit(text, text_rect)

    # Actualizar pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
sys.exit()
