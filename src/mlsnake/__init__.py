import typer
import pygame

app = typer.Typer()

@app.command()
def start() -> None:
    """Starts a game of snake"""
    print("Start MLSnake")

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

@app.command()
def stop() -> None:
    """Stops the current game of snake"""
    print("Stop MLSnake")

def main() -> None:
    app()

if __name__ == "__main__":
    main()
