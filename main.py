import pygame
import random

pygame.init()

# Kích thước màn hình
width, height = 400, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Thông số trò chơi
bird_width, bird_height = 30, 30
pipe_width, pipe_height = 60, 500
pipe_gap = 150
bird_x, bird_y = 50, height // 2
bird_speed = 0
gravity = 0.5
jump_speed = -10
pipe_speed = 5

# Biến toàn cục
pipes = []

def draw():
    win.fill(black)
    pygame.draw.rect(win, yellow, (bird_x, bird_y, bird_width, bird_height))
    for pipe in pipes:
        pygame.draw.rect(win, green, pipe[0])  # Vẽ ống trên
        pygame.draw.rect(win, green, pipe[1])  # Vẽ ống dưới
    pygame.display.update()

def create_pipe():
    max_pipe_height = height - pipe_gap - 50  # Giới hạn chiều cao của ống
    y = random.randint(0, max_pipe_height)  # Đảm bảo y luôn hợp lệ
    pipe_top = pygame.Rect(width, y, pipe_width, pipe_height)
    pipe_bottom = pygame.Rect(width, y + pipe_height + pipe_gap, pipe_width, height)
    return pipe_top, pipe_bottom

def main():
    global bird_y, bird_speed, pipes
    run = True
    clock = pygame.time.Clock()
    pipes = [create_pipe()]

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = jump_speed

        bird_speed += gravity
        bird_y += bird_speed

        # Di chuyển và thêm ống mới
        for pipe in pipes:
            pipe[0].x -= pipe_speed
            pipe[1].x -= pipe_speed

        if pipes[0][0].x < -pipe_width:
            pipes.pop(0)
            pipes.append(create_pipe())

        # Kiểm tra va chạm
        bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
        if bird_y < 0 or bird_y + bird_height > height:
            print("Game Over")
            run = False
        for pipe in pipes:
            if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
                print("Game Over")
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
