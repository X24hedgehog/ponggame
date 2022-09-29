import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer
pygame.init()


def ball1_animation():
    global ball_speed_x1, ball_speed_y1, player_score, opponent_score, score_time, bounce, spin_time11, spin_time12, opponent_speed, speed_change, visible, pulled1, mycolor
    ball1.x += ball_speed_x1
    ball1.y += ball_speed_y1

    if ball1.top <= 0 or ball1.bottom >= screen_height:
        ball_speed_y1 *= -1

    # Player Score
    if ball1.left <= 0:
        if mycolor == color_list[0]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            player_score += 1
        else:
            ball_speed_x1 *= -1
    # Opponent Score
    if ball1.right >= screen_width:
        if mycolor == color_list[0]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            opponent_score += 1
        else:
            ball_speed_x1 *= -1

    # while Obstacles:
    if ball1.colliderect(spin1_rect):
        if abs(ball1.right - spin1_rect.left) < proximity or abs(ball1.left - spin1_rect.right) < proximity or abs(ball1.top - spin1_rect.bottom) < proximity or abs(ball1.bottom - spin1_rect.top) < proximity and bounce % 2 == 1:
            pulled1 += 1
            if pulled1 % 2 == 1:
                ball1.x = spin2_rect.x
                ball1.y = spin2_rect.y
                spin_time12 = pygame.time.get_ticks()

    if ball1.colliderect(spin2_rect):
        if abs(ball1.right - spin2_rect.left) < proximity or abs(ball1.left - spin2_rect.right) < proximity or abs(ball1.top - spin2_rect.bottom) < proximity or abs(ball1.bottom - spin2_rect.top) < proximity and bounce % 2 == 1:
            pulled1 += 1
            if pulled1 % 2 == 1:
                ball1.x = spin1_rect.x
                ball1.y = spin1_rect.y
                spin_time11 = pygame.time.get_ticks()

    if ball1.colliderect(player) and ball_speed_x1 > 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x1 /= speed_change
            ball_speed_y1 /= speed_change
        if abs(ball1.right - player.left) < 10:
            ball_speed_x1 *= -1
        elif abs(ball1.bottom - player.top) < 10 and ball_speed_y1 > 0:
            ball_speed_y1 *= -1
        elif abs(ball1.top - player.bottom) < 10 and ball_speed_y1 < 0:
            ball_speed_y1 *= -1

    if ball1.colliderect(opponent) and ball_speed_x1 < 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x1 *= speed_change
            ball_speed_y1 *= speed_change
            opponent_speed = 12
        if abs(ball1.left - opponent.right) < 10:
            ball_speed_x1 *= -1
        elif abs(ball1.bottom - opponent.top) < 10 and ball_speed_y1 > 0:
            ball_speed_y1 *= -1
        elif abs(ball1.top - opponent.bottom) < 10 and ball_speed_y1 < 0:
            ball_speed_y1 *= -1

    # if bounce >= 4:
    #     ball_speed_x *= speed_change
    #     ball_speed_y *= speed_change
    #     opponent_speed = 12

    if bounce >= 10:
        if spin1_rect.x + spin1.get_width() + 200 < ball1.x < spin2_rect.x - 200:
            visible = False
        else:
            visible = True


def ball2_animation():
    global ball_speed_x2, ball_speed_y2, player_score, opponent_score, score_time, bounce, spin_time21, spin_time22, opponent_speed, speed_change, visible, pulled2, mycolor
    ball2.x += ball_speed_x2
    ball2.y += ball_speed_y2

    if ball2.top <= 0 or ball2.bottom >= screen_height:
        ball_speed_y2 *= -1

    # Player Score
    if ball2.left <= 0:
        if mycolor == color_list[1]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            player_score += 1
        else:
            ball_speed_x2 *= -1

    # Opponent Score
    if ball2.right >= screen_width:
        if mycolor == color_list[1]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            opponent_score += 1
        else:
            ball_speed_x2 *= -1

    # while Obstacles:
    if ball2.colliderect(spin1_rect):
        if abs(ball2.right - spin1_rect.left) < proximity or abs(ball2.left - spin1_rect.right) < proximity or abs(ball2.top - spin1_rect.bottom) < proximity or abs(ball2.bottom - spin1_rect.top) < proximity and bounce % 2 == 1:
            pulled2 += 1
            if pulled2 % 2 == 1:
                ball2.x = spin2_rect.x
                ball2.y = spin2_rect.y
                spin_time22 = pygame.time.get_ticks()

    if ball2.colliderect(spin2_rect):
        if abs(ball2.right - spin2_rect.left) < proximity or abs(ball2.left - spin2_rect.right) < proximity or abs(ball2.top - spin2_rect.bottom) < proximity or abs(ball2.bottom - spin2_rect.top) < proximity and bounce % 2 == 1:
            pulled2 += 1
            if pulled2 % 2 == 1:
                ball2.x = spin1_rect.x
                ball2.y = spin1_rect.y
                spin_time21 = pygame.time.get_ticks()

    if ball2.colliderect(player) and ball_speed_x2 > 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x2 /= speed_change
            ball_speed_y2 /= speed_change
        if abs(ball2.right - player.left) < 10:
            ball_speed_x2 *= -1
        elif abs(ball2.bottom - player.top) < 10 and ball_speed_y2 > 0:
            ball_speed_y2 *= -1
        elif abs(ball1.top - player.bottom) < 10 and ball_speed_y2 < 0:
            ball_speed_y2 *= -1

    if ball2.colliderect(opponent) and ball_speed_x2 < 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x2 *= speed_change
            ball_speed_y2 *= speed_change
            opponent_speed = 12
        if abs(ball2.left - opponent.right) < 10:
            ball_speed_x2 *= -1
        elif abs(ball2.bottom - opponent.top) < 10 and ball_speed_y2 > 0:
            ball_speed_y2 *= -1
        elif abs(ball2.top - opponent.bottom) < 10 and ball_speed_y2 < 0:
            ball_speed_y2 *= -1

    # if bounce >= 4:
    #     ball_speed_x *= speed_change
    #     ball_speed_y *= speed_change
    #     opponent_speed = 12

    if bounce >= 10:
        if spin1_rect.x + spin1.get_width() + 200 < ball2.x < spin2_rect.x - 200:
            visible = False
        else:
            visible = True


def ball3_animation():
    global ball_speed_x3, ball_speed_y3, player_score, opponent_score, score_time, bounce, spin_time31, spin_time32, opponent_speed, speed_change, visible, pulled3, mycolor
    ball3.x += ball_speed_x3
    ball3.y += ball_speed_y3

    if ball3.top <= 0 or ball3.bottom >= screen_height:
        ball_speed_y3 *= -1

    # Player Score
    if ball3.left <= 0:
        if mycolor == color_list[2]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            player_score += 1
        else:
            ball_speed_x3 *= -1

    # Opponent Score
    if ball3.right >= screen_width:
        if mycolor == color_list[2]:
            score_time = pygame.time.get_ticks()
            bounce = 0
            opponent_score += 1
        else:
            ball_speed_x3 *= -1

    # while Obstacles:
    if ball3.colliderect(spin1_rect):
        if abs(ball3.right - spin1_rect.left) < proximity or abs(ball3.left - spin1_rect.right) < proximity or abs(ball3.top - spin1_rect.bottom) < proximity or abs(ball3.bottom - spin1_rect.top) < proximity and bounce % 2 == 1:
            pulled3 += 1
            if pulled3 % 2 == 1:
                ball3.x = spin2_rect.x
                ball3.y = spin2_rect.y
                spin_time32 = pygame.time.get_ticks()

    if ball3.colliderect(spin2_rect):
        if abs(ball3.right - spin2_rect.left) < proximity or abs(ball3.left - spin2_rect.right) < proximity or abs(ball3.top - spin2_rect.bottom) < proximity or abs(ball3.bottom - spin2_rect.top) < proximity and bounce % 2 == 1:
            pulled3 += 1
            if pulled3 % 2 == 1:
                ball3.x = spin1_rect.x
                ball3.y = spin1_rect.y
                spin_time31 = pygame.time.get_ticks()

    if ball3.colliderect(player) and ball_speed_x3 > 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x3 /= speed_change
            ball_speed_y3 /= speed_change
        if abs(ball3.right - player.left) < 10:
            ball_speed_x3 *= -1
        elif abs(ball3.bottom - player.top) < 10 and ball_speed_y3 > 0:
            ball_speed_y3 *= -1
        elif abs(ball3.top - player.bottom) < 10 and ball_speed_y3 < 0:
            ball_speed_y3 *= -1

    if ball3.colliderect(opponent) and ball_speed_x3 < 0:
        bounce += 1
        if bounce >= 8:
            ball_speed_x3 *= speed_change
            ball_speed_y3 *= speed_change
            opponent_speed = 12
        if abs(ball3.left - opponent.right) < 10:
            ball_speed_x3 *= -1
        elif abs(ball3.bottom - opponent.top) < 10 and ball_speed_y3 > 0:
            ball_speed_y3 *= -1
        elif abs(ball3.top - opponent.bottom) < 10 and ball_speed_y3 < 0:
            ball_speed_y3 *= -1

    # if bounce >= 4:
    #     ball_speed_x *= speed_change
    #     ball_speed_y *= speed_change
    #     opponent_speed = 12

    if bounce >= 10:
        if spin1_rect.x + spin1.get_width() + 200 < ball3.x < spin2_rect.x - 200:
            visible = False
        else:
            visible = True


def ball_collision12():
    global ball1, ball2, ball_speed_x1, ball_speed_y1, ball_speed_x2, ball_speed_y2, touched3
    # if abs(b1.right - b2.left) < proximity or abs(b1.left - b2.right) < proximity or abs(
    #         b1.top - b2.bottom) < proximity or abs(b1.bottom - b2.top) < proximity:
    dis = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dis < 30 and not ball1.colliderect(spin1_rect) and not ball1.colliderect(spin2_rect) and not ball2.colliderect(spin1_rect) and not ball2.colliderect(spin2_rect):
        touched3 += 1
        ball_speed_x1 *= -1
        ball_speed_y1 *= -1
        ball_speed_x2 *= -1
        ball_speed_y2 *= -1


def ball_collision23():
    global ball3, ball2, ball_speed_x3, ball_speed_y3, ball_speed_x2, ball_speed_y2, touched1
    # if abs(b1.right - b2.left) < proximity or abs(b1.left - b2.right) < proximity or abs(
    #         b1.top - b2.bottom) < proximity or abs(b1.bottom - b2.top) < proximity:
    dis = ((ball3.x - ball2.x)**2 + (ball3.y - ball2.y)**2)**0.5
    if dis < 30 and not ball3.colliderect(spin1_rect) and not ball3.colliderect(spin2_rect) and not ball2.colliderect(spin1_rect) and not ball2.colliderect(spin2_rect):
        ball_speed_x3 *= -1
        ball_speed_y3 *= -1
        ball_speed_x2 *= -1
        ball_speed_y2 *= -1


def ball_collision13():
    global ball1, ball3, ball_speed_x1, ball_speed_y1, ball_speed_x3, ball_speed_y3, touched2
    # if abs(b1.right - b2.left) < proximity or abs(b1.left - b2.right) < proximity or abs(
    #         b1.top - b2.bottom) < proximity or abs(b1.bottom - b2.top) < proximity:
    dis = ((ball1.x - ball3.x)**2 + (ball1.y - ball3.y)**2)**0.5
    if dis < 30 and not ball1.colliderect(spin1_rect) and not ball1.colliderect(spin2_rect) and not ball3.colliderect(spin1_rect) and not ball3.colliderect(spin2_rect):
        ball_speed_x1 *= -1
        ball_speed_y1 *= -1
        ball_speed_x3 *= -1
        ball_speed_y3 *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai(ball):
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x1, ball_speed_y1, ball_speed_x2, ball_speed_y2, ball_speed_x3, ball_speed_y3, score_time, bounce, pulled1, pulled2, pulled3, touched1, touched2, touched3
    pulled1 = 0
    pulled2 = 0
    pulled3 = 0
    touched1 = 0
    touched2 = 0
    touched3 = 0
    ball1.center = (screen_width / 2, screen_height / 2 - 50)
    ball2.center = (screen_width / 2 - 43, screen_height / 2 + 25)
    ball3.center = (screen_width / 2 + 43, screen_height / 2 + 25)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = basic_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width /
                    2 - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = basic_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width /
                    2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = basic_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width /
                    2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x1, ball_speed_y1, ball_speed_x2, ball_speed_y2, ball_speed_x3, ball_speed_y3 = 0, 0, 0, 0, 0, 0
    else:
        ball_speed_x1 = speed * random.choice((1, -1))
        ball_speed_y1 = speed * random.choice((1, -1))
        ball_speed_x2 = speed * random.choice((1, -1))
        ball_speed_y2 = speed * random.choice((1, -1))
        ball_speed_x3 = speed * random.choice((1, -1))
        ball_speed_y3 = speed * random.choice((1, -1))
        score_time = None
        bounce = 0


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, red)
    screen.blit(draw_text, (screen_width/2 - draw_text.get_width() /
                            2, screen_height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


# Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colors
red = (255, 0, 0)
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
violet = (68, 0, 153)
blue = (116, 209, 234)
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color_list = [color1, color2, color3]
i = random.randint(0, 2)

# Sound
intro_sound = pygame.mixer.Sound("soundtracks/Electronic-Intro.mp3")
start_game_sound = pygame.mixer.Sound("soundtracks/Balance-point.mp3")
middle_game_sound = pygame.mixer.Sound("soundtracks/Reggae-game.mp3")
end_game_sound = pygame.mixer.Sound("soundtracks/High-game.mp3")
win_sound = pygame.mixer.Sound("soundtracks/Game-show-winning.mp3")
lose_sound = pygame.mixer.Sound("soundtracks/mixkit_game_over.wav")

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 50)
font1 = pygame.font.Font('freesansbold.ttf', 35)
font2 = pygame.font.Font('freesansbold.ttf', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# General setup
bg1 = pygame.image.load('images/newbg.jpg')
bg = pygame.transform.scale(bg1, (screen_width, screen_height))
pygame.mixer.pre_init(44100, -16, 1, 1024)
clock = pygame.time.Clock()
move1_box = font1.render(
    'Move your paddle up and down by pressing ', False, red)
ez = basic_font.render('abc', False, red)
up1 = pygame.image.load('images/up.jfif')
up = pygame.transform.scale(
    up1, (move1_box.get_height(), move1_box.get_height()))
down1 = pygame.image.load('images/down.jfif')
down = pygame.transform.scale(
    down1, (move1_box.get_height(), move1_box.get_height()))
easy1 = pygame.image.load('images/easy.png')
easy = pygame.transform.scale(easy1, (ez.get_height(), ez.get_height()))
medium1 = pygame.image.load('images/medium.png')
medium = pygame.transform.scale(medium1, (ez.get_height(), ez.get_height()))
hard1 = pygame.image.load('images/hard.png')
hard = pygame.transform.scale(hard1, (ez.get_height(), ez.get_height()))

# Game Rectangles
ball1 = pygame.Rect(screen_width / 4 - 15, screen_height / 2 - 15, 30, 30)
ball2 = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
ball3 = pygame.Rect(screen_width * 0.75 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 20, 200)
opponent = pygame.Rect(10, screen_height / 2 - 70, 20, 450)
spin = pygame.image.load('images/spin.png')
spin1 = pygame.transform.scale(spin, (40, 40))
spin2 = pygame.transform.scale(spin, (40, 40))
spin1_rect = pygame.Rect(300, (screen_height-40)/2, 40, 40)
spin2_rect = pygame.Rect(screen_width - 340, (screen_height - 40) / 2, 40, 40)


# Game Variables
speed = 6
ball_speed_x1 = speed * random.choice((1, -1))
ball_speed_y1 = speed * random.choice((1, -1))
ball_speed_x2 = speed * random.choice((1, -1))
ball_speed_y2 = speed * random.choice((1, -1))
ball_speed_x3 = speed * random.choice((1, -1))
ball_speed_y3 = speed * random.choice((1, -1))
intro_speed_x = 6
intro_speed_y = 6
player_speed = 0
opponent_speed = 10
ball_moving = False
FPS = 80
score_time = True
clicking = False
clicking1 = False
click = False
clicked = False
pause_click = False
point_needed = 3
bounce = 0
spin_time11 = True
spin_time12 = True
spin_time21 = True
spin_time22 = True
spin_time31 = True
spin_time32 = True
Obstacles = False
proximity = 10
game_on = True
Pause = True
after_game = True
k = random.randint(5, 8)


def draw_intro():
    global continue_box, user_name
    # welcome_box = basic_font.render('WELCOME TO PING PONG', False, red)
    name_box = font2.render('Enter your name', False, red)
    type_box = font2.render(user_name, False, red)
    continue_box = font1.render('Click here to continue', False, red)
    # screen.blit(welcome_box, ((screen_width - welcome_box.get_width()) / 2, 200))
    screen.blit(
        continue_box, ((screen_width - continue_box.get_width()) / 2, 850))
    screen.blit(type_box, ((screen_width - type_box.get_width()) / 2, 400))
    screen.blit(name_box, ((screen_width - name_box.get_width()) / 2, 300))


def draw_instruction():
    global point_to_play, continue1_box
    title_box = basic_font.render('GAME INSTRUCTION', False, red)
    move_box = font1.render(
        'Move your paddle up and down by pressing ', False, blue)
    point_box = font1.render(
        'Reach the target point first to win the game ', False, blue)
    choose_box = font1.render(
        'Enter the target point you want to play (3 to 10)', False, blue)
    point_type_box = font1.render(point_to_play, False, red)
    continue1_box = font1.render('Click here to continue', False, red)
    screen.blit(title_box, ((screen_width - title_box.get_width()) / 2, 200))
    screen.blit(move_box, ((screen_width - move_box.get_width()) / 2, 300))
    screen.blit(up, ((screen_width + move_box.get_width()) / 2 + 10, 300))
    screen.blit(down, ((screen_width + move_box.get_width()) /
                2 + up.get_width() + 20, 300))
    screen.blit(point_box, ((screen_width - point_box.get_width()) / 2, 375))
    screen.blit(choose_box, ((screen_width - choose_box.get_width()) / 2, 450))
    screen.blit(point_type_box,
                ((screen_width - point_type_box.get_width()) / 2, 525))
    screen.blit(continue1_box,
                ((screen_width - continue1_box.get_width()) / 2, 600))


def draw_after_play():
    global again_box, quit_box, quit_w, c
    again_box = basic_font.render('PLAY AGAIN', False, violet)
    quit_box = basic_font.render('QUIT', False, violet)
    quit_w = quit_box.get_width()
    c = (screen_width - 2*a)/3
    screen.blit(again_box, (c, 500))
    screen.blit(quit_box, (2*c + quit_w, 500))


def draw_choosing_level():
    global easy_box, medium_box, hard_box, a, b
    title_box = basic_font.render('Choose level', False, blue)
    easy_box = basic_font.render('Easy', False, violet)
    medium_box = basic_font.render('Medium', False, violet)
    hard_box = basic_font.render('Hard', False, violet)
    a = easy_box.get_width()
    b = (screen_width - 3*a)/4
    screen.blit(title_box, ((screen_width - title_box.get_width()) / 2, 200))
    screen.blit(easy_box, (b, 500))
    screen.blit(medium_box, (2*b + a, 500))
    screen.blit(hard_box, (3*b + 2*a, 500))
    screen.blit(easy, (b + (easy_box.get_width()-easy.get_width()) /
                2, 500+easy_box.get_height()+20))
    screen.blit(medium, (2*b + a + (medium_box.get_width() -
                medium.get_width()) / 2, 500 + medium_box.get_height() + 20))
    screen.blit(hard, (3*b + 2*a + (hard_box.get_width() -
                hard.get_width()) / 2, 500 + hard_box.get_height() + 20))


def pull_ball11():
    global spin_time11, ball_speed_x1, ball_speed_y1, j
    current_time = pygame.time.get_ticks()
    # if current_time - spin_time1 < 20:

    # if 20 < current_time - spin_time1 < 40:
    #     get_spin = pygame.transform.rotate(spin1, 180)
    #     screen.blit(get_spin, spin1_rect)
    # if current_time - spin_time1 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0
    if j == 0:
        if current_time - spin_time11 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 700 < current_time - spin_time11 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 1400 < current_time - spin_time11 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time11 < 2100:
        ball_speed_y1, ball_speed_x1 = 0, 0

    else:
        ball_speed_x1 = speed * random.choice((1, -1))
        ball_speed_y1 = speed * random.choice((1, -1))
        spin_time11 = None


def pull_ball12():
    global spin_time12, ball_speed_x1, ball_speed_y1
    current_time = pygame.time.get_ticks()

    # if current_time - spin_time2 < 20:
    #     get_spin = pygame.transform.rotate(spin2, 90)
    #     screen.blit(get_spin, spin2_rect)
    # if 20 < current_time - spin_time2 < 40:
    #     get_spin = pygame.transform.rotate(spin2, 180)
    #     screen.blit(get_spin, spin2_rect)
    #
    # if current_time - spin_time2 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0

    if j == 0:
        if current_time - spin_time12 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 700 < current_time - spin_time12 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 1400 < current_time - spin_time12 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time12 < 2100:
        ball_speed_y1, ball_speed_x1 = 0, 0

    else:
        ball_speed_x1 = speed * random.choice((1, -1))
        ball_speed_y1 = speed * random.choice((1, -1))
        spin_time12 = None


def pull_ball21():
    global spin_time21, ball_speed_x2, ball_speed_y2
    current_time = pygame.time.get_ticks()
    # if current_time - spin_time1 < 20:

    # if 20 < current_time - spin_time1 < 40:
    #     get_spin = pygame.transform.rotate(spin1, 180)
    #     screen.blit(get_spin, spin1_rect)
    # if current_time - spin_time1 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0

    if j == 1:
        if current_time - spin_time21 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 700 < current_time - spin_time21 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 1400 < current_time - spin_time21 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time21 < 2100:
        ball_speed_y2, ball_speed_x2 = 0, 0

    else:
        ball_speed_x2 = speed * random.choice((1, -1))
        ball_speed_y2 = speed * random.choice((1, -1))
        spin_time21 = None


def pull_ball22():
    global spin_time22, ball_speed_x2, ball_speed_y2
    current_time = pygame.time.get_ticks()

    # if current_time - spin_time2 < 20:
    #     get_spin = pygame.transform.rotate(spin2, 90)
    #     screen.blit(get_spin, spin2_rect)
    # if 20 < current_time - spin_time2 < 40:
    #     get_spin = pygame.transform.rotate(spin2, 180)
    #     screen.blit(get_spin, spin2_rect)
    #
    # if current_time - spin_time2 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0

    if j == 1:
        if current_time - spin_time22 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 700 < current_time - spin_time22 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 1400 < current_time - spin_time22 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time22 < 2100:
        ball_speed_y2, ball_speed_x2 = 0, 0

    else:
        ball_speed_x2 = speed * random.choice((1, -1))
        ball_speed_y2 = speed * random.choice((1, -1))
        spin_time22 = None


def pull_ball31():
    global spin_time31, ball_speed_x3, ball_speed_y3
    current_time = pygame.time.get_ticks()
    # if current_time - spin_time1 < 20:

    # if 20 < current_time - spin_time1 < 40:
    #     get_spin = pygame.transform.rotate(spin1, 180)
    #     screen.blit(get_spin, spin1_rect)
    # if current_time - spin_time1 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0

    if j == 2:
        if current_time - spin_time31 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 700 < current_time - spin_time31 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))

        if 1400 < current_time - spin_time31 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time31 < 2100:
        ball_speed_y3, ball_speed_x3 = 0, 0

    else:
        ball_speed_x3 = speed * random.choice((1, -1))
        ball_speed_y3 = speed * random.choice((1, -1))
        spin_time31 = None


def pull_ball32():
    global spin_time32, ball_speed_x3, ball_speed_y3
    current_time = pygame.time.get_ticks()

    # if current_time - spin_time2 < 20:
    #     get_spin = pygame.transform.rotate(spin2, 90)
    #     screen.blit(get_spin, spin2_rect)
    # if 20 < current_time - spin_time2 < 40:
    #     get_spin = pygame.transform.rotate(spin2, 180)
    #     screen.blit(get_spin, spin2_rect)
    #
    # if current_time - spin_time2 < 40:
    #     ball_speed_y, ball_speed_x = 0, 0

    if j == 2:
        if current_time - spin_time32 < 700:
            number_three = basic_font.render("3", False, light_grey)
            screen.blit(number_three, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 700 < current_time - spin_time32 < 1400:
            number_two = basic_font.render("2", False, light_grey)
            screen.blit(number_two, (screen_width /
                        2 - 10, screen_height / 2 + 20))
        if 1400 < current_time - spin_time32 < 2100:
            number_one = basic_font.render("1", False, light_grey)
            screen.blit(number_one, (screen_width /
                        2 - 10, screen_height / 2 + 20))

    if current_time - spin_time32 < 2100:
        ball_speed_y3, ball_speed_x3 = 0, 0

    else:
        ball_speed_x3 = speed * random.choice((1, -1))
        ball_speed_y3 = speed * random.choice((1, -1))
        spin_time32 = None


def main_menu():
    restart = True
    while restart:

        intro()
        instruction()
        choose_level()
        main_game()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


def intro():
    global clicking, user_name
    run_intro = True
    play_intro()
    user_name = ''
    while run_intro:

        screen.blit(bg, (0, 0))
        draw_intro()
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect((screen_width - continue_box.get_width()) / 2, 850, continue_box.get_width(),
                               continue_box.get_height())
        if button_1.collidepoint((mx, my)):

            if clicking:
                if user_name != '':
                    run_intro = False

        clicking = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking = True

        pygame.display.update()
        clock.tick(60)


def instruction():
    global clicking1, point_to_play, point_needed, intro_speed_x, intro_speed_y
    run_instruction = True
    point_to_play = ''
    # intro_sound.stop()
    # intro_sound.play()
    while run_instruction:

        screen.fill((255, 100, 100))
        draw_instruction()
        # intro_ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
        # pygame.draw.ellipse(screen, (255, 255, 255), intro_ball)
        # intro_ball.x += intro_speed_x
        # intro_ball.y += intro_speed_y
        # if intro_ball.top <= 0 or intro_ball.bottom >= screen_height:
        #     intro_speed_y *= -1
        # if intro_ball.left <= 0 or intro_ball.right >= screen_width:
        #     intro_speed_x *= -1

        mx, my = pygame.mouse.get_pos()

        button_2 = pygame.Rect((screen_width - continue1_box.get_width()) / 2, 600, continue1_box.get_width(),
                               continue1_box.get_height())
        if button_2.collidepoint((mx, my)):

            if clicking1:
                if point_to_play.isnumeric() and 3 <= int(point_to_play) <= 10:
                    run_instruction = False

        clicking1 = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    point_to_play = point_to_play[:-1]
                else:
                    point_to_play += event.unicode
                    if point_to_play.isnumeric():
                        point_needed = int(point_to_play)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking1 = True

        pygame.display.update()
        clock.tick(FPS)


def after_play():
    global clicked, running, player_score, opponent_score, after_game
    pygame.mixer.music.load("soundtracks/Electronic-Intro.mp3")
    pygame.mixer.music.play()
    while after_game:
        screen.fill((255, 100, 45))
        draw_after_play()

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(c, 500, again_box.get_width(),
                               again_box.get_height())
        button_2 = pygame.Rect(2 * c + quit_w, 500, quit_box.get_width(),
                               quit_box.get_height())

        if button_1.collidepoint((mx, my)):
            if clicked:
                running = True
                player_score = 0
                opponent_score = 0
                main_menu()
                after_game = False

        if button_2.collidepoint((mx, my)):
            if clicked:
                pygame.quit()
                sys.exit()

        clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        clock.tick(FPS)
    after_game = True


def choose_level():
    global click, speed, speed_change, my_speed, game_on, score_time, FPS
    speed = 6
    speed_change = 1.125
    choosing = True
    my_speed = 6
    while choosing:
        screen.fill((255, 100, 100))
        draw_choosing_level()

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(b, 500, easy_box.get_width(),
                               easy_box.get_height())
        button_2 = pygame.Rect(2*b + a, 500, medium_box.get_width(),
                               medium_box.get_height())
        button_3 = pygame.Rect(3*b + 2*a, 500, hard_box.get_width(),
                               hard_box.get_height())

        if button_1.collidepoint((mx, my)):
            if click:
                score_time = pygame.time.get_ticks()
                FPS = 70
                choosing = False

        if button_2.collidepoint((mx, my)):
            if click:
                speed_change = 1.25
                my_speed = 9
                score_time = pygame.time.get_ticks()
                FPS = 90
                choosing = False

        if button_3.collidepoint((mx, my)):
            if click:
                speed_change = 1.5
                my_speed = 12
                score_time = pygame.time.get_ticks()
                FPS = 120
                choosing = False

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)


def draw_paused():
    global continue_play_box, quit_box, quit_w, c
    continue_play_box = basic_font.render('CONTINUE', False, violet)
    quit_box = basic_font.render('QUIT', False, violet)
    quit_w = quit_box.get_width()
    c = (screen_width - 2 * a) / 3
    screen.blit(continue_play_box, (c, 500))
    screen.blit(quit_box, (2 * c + quit_w, 500))


def un_paused():
    global Pause
    Pause = False


def pause():
    global pause_click, running, Pause

    while Pause:
        running = False
        pygame.mixer.music.pause()
        screen.fill((255, 100, 45))
        draw_paused()

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(c, 500, continue_play_box.get_width(),
                               continue_play_box.get_height())
        button_2 = pygame.Rect(2 * c + quit_w, 500, quit_box.get_width(),
                               quit_box.get_height())

        if button_1.collidepoint((mx, my)):
            if pause_click:
                running = True
                pygame.mixer.music.unpause()
                un_paused()

        if button_2.collidepoint((mx, my)):
            if pause_click:
                pygame.quit()
                sys.exit()

        pause_click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pause_click = True

        pygame.display.update()
        clock.tick(FPS)

    Pause = True


def play_intro():
    song_list = ["soundtracks/Balance-point.mp3",
                 "soundtracks/Reggae-game.mp3", "soundtracks/High-game.mp3"]
    song_index = random.randint(0, 2)
    pygame.mixer.music.load(song_list[song_index])
    pygame.mixer.music.play(-1)


def main_game():

    global player_speed, Obstacles, visible, game_on, running, player_score, opponent_score, user_name, bounce, mycolor, j, max_point
    visible = True
    running = True
    max_point = max(player_score, opponent_score)
    song_list = ["soundtracks/melodyloops-preview-a-life-for-a-dream-2m30s.mp3",
                 "soundtracks/melodyloops-preview-we-are-like-a-family-2m30s.mp3"]
    song_index = random.randint(0, 1)
    pygame.mixer.music.load(song_list[song_index])
    pygame.mixer.music.play(-1)

    while running:

        if player_score < point_needed and opponent_score < point_needed:

            j = (bounce // k + i) % 3
            mycolor = color_list[j]

            # Visuals
            screen.fill((254, 221, 0))
            pygame.draw.rect(screen, mycolor, player)
            pygame.draw.rect(screen, mycolor, opponent)

            if visible:
                pygame.draw.ellipse(screen, color1, ball1)
                pygame.draw.ellipse(screen, color2, ball2)
                pygame.draw.ellipse(screen, color3, ball3)

            pygame.draw.aaline(
                screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
            # draw_intro()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_speed -= my_speed
                    if event.key == pygame.K_DOWN:
                        player_speed += my_speed
                    if event.key == pygame.K_SPACE:
                        pause()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player_speed += my_speed
                    if event.key == pygame.K_DOWN:
                        player_speed -= my_speed

            # Game Logic
            ball1_animation()
            ball2_animation()
            ball3_animation()

            ball_collision12()
            ball_collision23()
            ball_collision13()

            player_animation()

            if j == 0:
                opponent_ai(ball1)
            elif j == 1:
                opponent_ai(ball2)
            else:
                opponent_ai(ball3)

            if score_time:
                ball_start()

            player_text = basic_font.render(
                f'{player_score}', False, light_grey)
            screen.blit(player_text, (660, 470))

            opponent_text = basic_font.render(
                f'{opponent_score}', False, light_grey)
            screen.blit(opponent_text, (600, 470))

            screen.blit(spin1, (300, (screen_height - 40) / 2))
            screen.blit(spin2, (screen_width - 340, (screen_height - 40) / 2))

            if spin_time11:
                pull_ball11()
            if spin_time12:
                pull_ball12()
            if spin_time21:
                pull_ball21()
            if spin_time22:
                pull_ball22()
            if spin_time31:
                pull_ball31()
            if spin_time32:
                pull_ball32()

        else:
            pygame.mixer.music.stop()
            win_sound.play()
            lose_sound.play()

            winner_text = ''
            if player_score == point_needed:
                game_on = False
                lose_sound.set_volume(0)
                winner_text = 'You beat me, ' + user_name

            if opponent_score == point_needed:
                game_on = False
                win_sound.set_volume(0)
                winner_text = 'I beat you, ' + user_name

            if winner_text != '':
                draw_winner(winner_text)
                pygame.time.delay(200)
                after_play()
                running = False

        pygame.display.flip()
        clock.tick(FPS)


main_menu()
