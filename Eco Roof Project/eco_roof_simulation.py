import pygame
import sys
import math
import webbrowser

pygame.init()

# Screen settings
WIDTH, HEIGHT = 1800, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roof Absorption and Reflection")

#Data for Images
asphalt_img = pygame.image.load('asphalt.png').convert()
asphalt_img = pygame.transform.scale(asphalt_img, (150, 45))
steel_img = pygame.image.load('steel.png').convert()
steel_img = pygame.transform.scale(steel_img, (150, 45))
concrete_img = pygame.image.load('concrete.png').convert()
concrete_img = pygame.transform.scale(concrete_img, (150, 45))

#Albetos
font = pygame.font.SysFont('Roboto', 30)
res = (720, 720)

Solar_radiation_Summer=5.54
Solar_radiation_Winter=3.28
# kWh/m**2
Roof_Area_avg=185.81
#m^2
Energy_used_AC_avg=25
Energy_used_heating_avg=26
#kWh
ba_asphalt_white = 0.35
ba_asphalt_black = 0.055
ba_asphalt_red = 0.075
ba_asphalt_yellow = 0.25
ba_asphalt_blue = 0.15
ba_asphalt_green = 0.15

ba_steel_white = 0.85
ba_steel_black = 0.15
ba_steel_red = 0.375
ba_steel_yellow_bronze = 0.55
ba_steel_blue = 0.45
ba_steel_green = 0.45

ba_concrete_black = 0.1
ba_concrete_white = 0.7
ba_concrete_red = 0.4
ba_concrete_yellow_beige = 0.4
ba_concrete_blue = 0.4
ba_concrete_green = 0.4

#Button Functions
def asphalt_white():
   absorbed=1-ba_asphalt_white
   return absorbed
def asphalt_black():
   absorbed=1-ba_asphalt_black
   return absorbed
def asphalt_red():
   absorbed=1-ba_asphalt_red
   return absorbed
def asphalt_yellow():
   absorbed=1-ba_asphalt_yellow
   return absorbed
def asphalt_blue():
   absorbed=1-ba_asphalt_blue
   return absorbed
def asphalt_green():
   absorbed=1-ba_asphalt_green
   return absorbed

def steel_white():
   absorbed = 1 - ba_steel_white
   return absorbed
def steel_black():
   absorbed = 1 - ba_steel_black
   return absorbed
def steel_red():
   absorbed = 1 - ba_steel_red
   return absorbed
def steel_yellow():
   absorbed = 1 - ba_steel_yellow_bronze
   return absorbed
def steel_blue():
   absorbed = 1 - ba_steel_blue
   return absorbed
def steel_green():
   absorbed = 1 - ba_steel_green
   return absorbed

def concrete_white():
   absorbed = 1 - ba_concrete_white
   return absorbed
def concrete_black():
   absorbed = 1 - ba_concrete_black
   return absorbed
def concrete_red():
   absorbed = 1 - ba_concrete_red
   return absorbed
def concrete_yellow():
   absorbed = 1 - ba_concrete_yellow_beige
   return absorbed
def concrete_blue():
   absorbed = 1 - ba_concrete_blue
   return absorbed
def concrete_green():
   absorbed = 1 - ba_concrete_green
   return absorbed

class ButtonMaterial:
    def __init__(self, image, x ,y ,width ,height, text=""):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False

    def draw(self):
        action = False
        screen.blit(self.image, (self.x, self.y))
        text_surface = font.render(self.text, True, (250, 250, 250))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

class ButtonColors:
    def __init__(self, color_outline, x ,y ,width ,height, text=""):
        self.color_outline = color_outline
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False

    def draw(self):
        action = False
        pygame.draw.rect(screen, self.color_outline, self.rect)
        text_surface = font.render(self.text, True, (177, 177, 177))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

roof_color = 'black'
material = 'steel'
display_text = f''
"""Materials"""
button_steel = ButtonMaterial(steel_img, 100, 100, 150, 45, "Steel")
button_asphalt = ButtonMaterial(asphalt_img, 350, 100, 150, 45, "Asphalt")
button_concrete = ButtonMaterial(concrete_img, 600, 100, 150, 45, "Concrete")
"""Colours"""
button_black = ButtonColors('black', 100, 175, 100, 45, "Black")
button_white = ButtonColors('white', 250, 175, 100, 45, "White")
button_red = ButtonColors('red', 400, 175, 100, 45, "Red")
button_yellow = ButtonColors('yellow', 550, 175, 100, 45, "Yellow")
button_blue = ButtonColors('blue', 700, 175, 100, 45, "Blue")
button_green = ButtonColors('dark green', 850, 175, 100, 45, "Green")

# Colors
GRAY_76_HOUSE_COLOUR = (194, 194, 194, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_RAYS_COLOUR = (255, 185, 15, 255)
SKY_BLUE_SUMMER_SKY_COLOUR = (135, 206, 235, 255)
BISQUE_GUTTER_COLOUR = (255, 228, 196, 255)
CHRISTMAS_LIGHTS_GREEN_STRING = (0, 100, 0, 255)
WINTER_SKY_BLUE = (224,224,240)

progress_speed = 0.01
progress = 0

# Coordinates of Triangular Roof
x_1_triangle: int = 0
y_1_triangle: int = 800
x_2_triangle: int = 0
y_2_triangle: int = 500
x_3_triangle: int = 640
y_3_triangle: int = 800

# Coordinates of Sun
sun_radius = 75
sun_center_x = 800
sun_center_y = 150

y_start_point_ray_1 = 130
x_start_point_ray_1 = sun_center_x - (math.sqrt(sun_radius ** 2 - (sun_center_y - y_start_point_ray_1) ** 2))

y_start_point_ray_2 = 150
x_start_point_ray_2 = 800

y_start_point_ray_3 = 170
x_start_point_ray_3 = sun_center_x + (math.sqrt(sun_radius ** 2 - (sun_center_y - y_start_point_ray_1) ** 2))

# Draw the house
def draw_house():
    pygame.draw.polygon(screen, GRAY_76_HOUSE_COLOUR, [(0,800),(500,800),(500,1000),(0,1000)])
    pygame.draw.circle(screen, SUN_RAYS_COLOUR, (sun_center_x, sun_center_y), sun_radius, 0)

def draw_clouds():
    pygame.draw.circle(screen, WHITE, (400, 240), 50,0,)
    pygame.draw.circle(screen, WHITE, (350, 240), 30,0)
    pygame.draw.circle(screen, WHITE, (450, 240), 30,0)

    pygame.draw.circle(screen, WHITE, (125, 100), 50,0)
    pygame.draw.circle(screen, WHITE, (75, 100), 30,0)
    pygame.draw.circle(screen, WHITE, (175, 100), 30,0)

    pygame.draw.circle(screen, WHITE, (700, 120), 50,0)
    pygame.draw.circle(screen, WHITE, (650, 120), 30,0)
    pygame.draw.circle(screen, WHITE, (750, 120), 30,0)

    pygame.draw.circle(screen, WHITE, (1050, 250), 50, 0)
    pygame.draw.circle(screen, WHITE, (1000, 250), 30, 0)
    pygame.draw.circle(screen, WHITE, (1100, 250), 30, 0)

    pygame.draw.circle(screen, WHITE, (1250, 80), 50, 0)
    pygame.draw.circle(screen, WHITE, (1200, 80), 30, 0)
    pygame.draw.circle(screen, WHITE, (1300, 80), 30, 0)

    pygame.draw.circle(screen, WHITE, (1450, 270), 50, 0)
    pygame.draw.circle(screen, WHITE, (1400, 270), 30, 0)
    pygame.draw.circle(screen, WHITE, (1500, 270), 30, 0)

    pygame.draw.circle(screen, WHITE, (1700, 160), 50, 0)
    pygame.draw.circle(screen, WHITE, (1650, 160), 30, 0)
    pygame.draw.circle(screen, WHITE, (1750, 160), 30, 0)

def draw_gutter():
    pygame.draw.polygon(screen, BISQUE_GUTTER_COLOUR, [(x_1_triangle, y_1_triangle), (x_3_triangle, y_3_triangle), (620, 830), (0, 830),])

def snowy_gutter():
    number_of_repeats = int(x_3_triangle/10)
    x=0
    for i in range(number_of_repeats):
        pygame.draw.circle(screen, WHITE, (x,800), 9, 0)
        x = x + 10

# Roof slope and intercept calculations
def roof_slope() -> float:
    return (y_3_triangle - y_2_triangle) / (x_3_triangle - x_2_triangle)

def initial_value_roof() -> float:
    return y_3_triangle - roof_slope() * x_3_triangle

def theta_1_house():
    base_of_the_roof: float = (x_3_triangle - x_1_triangle)
    height_of_the_roof: float = abs(y_3_triangle - y_1_triangle)
    angle_incline: float = math.atan(height_of_the_roof - base_of_the_roof)
    return angle_incline

def theta_2():
    angle_between_normal_and_horizontal_axis: float = 90 - theta_1_house()
    return angle_between_normal_and_horizontal_axis

# ALL RAY 1 CALCULATIONS START HERE
# Intersection point calculations - Ray #1
def x_point_of_intersection_ray_1():
    return 50

def y_point_of_intersection_ray_1():
    return roof_slope() * x_point_of_intersection_ray_1() + initial_value_roof()

# Tracing ray progressively
def tracing_ray_1(progress):
    start_pos_ray_1 = (x_start_point_ray_1, y_start_point_ray_1)
    end_pos_ray_1 = (x_point_of_intersection_ray_1(),y_point_of_intersection_ray_1())
    current_end_x_ray_1 = start_pos_ray_1[0] + (end_pos_ray_1[0] - start_pos_ray_1[0]) * progress
    current_end_y_ray_1 = start_pos_ray_1[1] + (end_pos_ray_1[1] - start_pos_ray_1[1]) * progress
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_ray_1,(current_end_x_ray_1, current_end_y_ray_1),5)

#Angle B.S. - Ray 1
def theta_3_ray_1():
    height_of_imaginary_triangle_ray_1: float = abs(y_start_point_ray_1 - y_point_of_intersection_ray_1())
    base_of_imaginary_triangle_ray_1: float = abs(x_start_point_ray_1 - x_point_of_intersection_ray_1())
    angle_between_incident_ray_and_horizontal_axis_ray_1: float = math.atan(height_of_imaginary_triangle_ray_1/base_of_imaginary_triangle_ray_1)
    return angle_between_incident_ray_and_horizontal_axis_ray_1

def theta_4_ray_1():
    angle_of_incidence_ray_1: float = theta_2() - theta_3_ray_1()
    return angle_of_incidence_ray_1

def theta_5_ray_1():
    total_angle_ray_1: float = theta_2() + theta_4_ray_1()
    return total_angle_ray_1

# Coordinates of final point off the map
def y_coordinate_of_final_destination_ray_1():
    y_value_ray_1: int = -1000
    return y_value_ray_1

def x_coordinate_of_final_destination_ray_1():
    x_value_ray_1: float = math.sin(theta_5_ray_1())/y_coordinate_of_final_destination_ray_1()
    return x_value_ray_1

# Tracing Reflected Ray 1
def tracing_reflected_ray_1(progress):
    start_pos_reflected_ray_1 = (x_point_of_intersection_ray_1(), y_point_of_intersection_ray_1())
    end_pos_reflected_ray_1 = (x_coordinate_of_final_destination_ray_1(),y_coordinate_of_final_destination_ray_1())
    current_end_x_reflected_ray_1 = start_pos_reflected_ray_1[0] + (end_pos_reflected_ray_1[0] * progress)
    current_end_y_reflected_ray_1 = start_pos_reflected_ray_1[1] + (end_pos_reflected_ray_1[1] * progress)
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_reflected_ray_1, (current_end_x_reflected_ray_1, current_end_y_reflected_ray_1), 5)

# ALL RAY 2 CALCULATIONS START HERE
# Intersection point calculations - ray #2
def x_point_of_intersection_ray_2():
    return 200

def y_point_of_intersection_ray_2():
    return roof_slope() * x_point_of_intersection_ray_2() + initial_value_roof()

# Tracing ray progressively
def tracing_ray_2(progress):
    start_pos_ray_2 = (x_start_point_ray_2, y_start_point_ray_2)
    end_pos_ray_2 = (x_point_of_intersection_ray_2(), y_point_of_intersection_ray_2())
    current_end_x_ray_2 = start_pos_ray_2[0] + (end_pos_ray_2[0] - start_pos_ray_2[0]) * progress
    current_end_y_ray_2 = start_pos_ray_2[1] + (end_pos_ray_2[1] - start_pos_ray_2[1]) * progress
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_ray_2, end_pos_ray_2, 5)

#Angle B.S. - Ray 2
def theta_3_ray_2():
    height_of_imaginary_triangle_ray_2: float = abs(y_start_point_ray_2 - y_point_of_intersection_ray_2())
    base_of_imaginary_triangle_ray_2: float = abs(x_start_point_ray_2 - x_point_of_intersection_ray_2())
    angle_between_incident_ray_and_horizontal_axis_ray_2: float = math.atan(height_of_imaginary_triangle_ray_2/base_of_imaginary_triangle_ray_2)
    return angle_between_incident_ray_and_horizontal_axis_ray_2

def theta_4_ray_2():
    angle_of_incidence_ray_2: float = theta_2() - theta_3_ray_2()
    return angle_of_incidence_ray_2

def theta_5_ray_2():
    total_angle_ray_2: float = theta_2() + theta_4_ray_2()
    return total_angle_ray_2

# Coordinates of final point off the map
def y_coordinate_of_final_destination_ray_2():
    y_value_ray_2: int = -1000
    return y_value_ray_2

def x_coordinate_of_final_destination_ray_2():
    x_value_ray_2: float = math.sin(theta_5_ray_2())/y_coordinate_of_final_destination_ray_2()
    return x_value_ray_2

# Tracing Reflected Ray 1
def tracing_reflected_ray_2(progress):
    start_pos_reflected_ray_2 = (x_point_of_intersection_ray_2(), y_point_of_intersection_ray_2())
    end_pos_reflected_ray_2 = (x_coordinate_of_final_destination_ray_2(),y_coordinate_of_final_destination_ray_2())
    current_end_x_reflected_ray_2 = start_pos_reflected_ray_2[0] + (end_pos_reflected_ray_2[0] * progress)
    current_end_y_reflected_ray_2 = start_pos_reflected_ray_2[1] + (end_pos_reflected_ray_2[1] * progress)
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_reflected_ray_2, (current_end_x_reflected_ray_2, current_end_y_reflected_ray_2), 5)

# ALL RAY 3 CALCULATIONS START HERE
# Intersection point calculations - ray #3
def x_point_of_intersection_ray_3():
    return 450

def y_point_of_intersection_ray_3():
    return roof_slope() * x_point_of_intersection_ray_3() + initial_value_roof()

# Tracing ray progressively
def tracing_ray_3(progress):
    start_pos_ray_3 = (x_start_point_ray_3, y_start_point_ray_3)
    end_pos_ray_3 = (x_point_of_intersection_ray_3(), y_point_of_intersection_ray_3())
    current_end_x_ray_3 = start_pos_ray_3[0] + (end_pos_ray_3[0] - start_pos_ray_3[0]) * progress
    current_end_y_ray_3 = start_pos_ray_3[1] + (end_pos_ray_3[1] - start_pos_ray_3[1]) * progress
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_ray_3, end_pos_ray_3, 5)

#Angle B.S. - Ray 3
def theta_3_ray_3():
    height_of_imaginary_triangle_ray_3: float = abs(y_start_point_ray_3 - y_point_of_intersection_ray_3())
    base_of_imaginary_triangle_ray_3: float = abs(x_start_point_ray_3 - x_point_of_intersection_ray_3())
    angle_between_incident_ray_and_horizontal_axis_ray_3: float = math.atan(height_of_imaginary_triangle_ray_3/base_of_imaginary_triangle_ray_3)
    return angle_between_incident_ray_and_horizontal_axis_ray_3

def theta_4_ray_3():
    angle_of_incidence_ray_3: float = theta_2() - theta_3_ray_3()
    return angle_of_incidence_ray_3

def theta_5_ray_3():
    total_angle_ray_3: float = theta_2() + theta_4_ray_3()
    return total_angle_ray_3

# Coordinates of final point off the map
def y_coordinate_of_final_destination_ray_3():
    y_value_ray_3: int = -1000
    return y_value_ray_3

def x_coordinate_of_final_destination_ray_3():
    x_value_ray_3: float = math.sin(theta_5_ray_3())/y_coordinate_of_final_destination_ray_3()
    return x_value_ray_3

# Tracing Reflected Ray 3
def tracing_reflected_ray_3(progress):
    start_pos_reflected_ray_3 = (x_point_of_intersection_ray_3(), y_point_of_intersection_ray_3())
    end_pos_reflected_ray_3 = (x_coordinate_of_final_destination_ray_3(),y_coordinate_of_final_destination_ray_3())
    current_end_x_reflected_ray_3 = start_pos_reflected_ray_3[0] + (end_pos_reflected_ray_3[0] * progress)
    current_end_y_reflected_ray_3 = start_pos_reflected_ray_3[1] + (end_pos_reflected_ray_3[1] * progress)
    pygame.draw.line(screen, SUN_RAYS_COLOUR, start_pos_reflected_ray_3, (current_end_x_reflected_ray_3, current_end_y_reflected_ray_3), 5)

# Main loop
def main():
    global albedo, display_write1
    global progress
    clock = pygame.time.Clock()
    running = True
    roof_color = 'black'
    material = 'steel'
    season = 'summer'
    display_text = ""
    display_write = f''
    display_write1 =f''

    # Buttons for materials
    button_steel = ButtonMaterial(steel_img, 1070, 600, 150, 45, "Steel")
    button_asphalt = ButtonMaterial(asphalt_img, 1270, 600, 150, 45, "Asphalt")
    button_concrete = ButtonMaterial(concrete_img, 1470, 600, 150, 45, "Concrete")

    # Buttons for colors
    button_black = ButtonColors(BLACK, 1000, 775, 100, 45, "Black")
    button_white = ButtonColors(WHITE, 1125, 775, 100, 45, "White")
    button_red = ButtonColors((255, 0, 0), 1250, 775, 100, 45, "Red")
    button_yellow = ButtonColors((255, 255, 0), 1375, 775, 100, 45, "Yellow")
    button_blue = ButtonColors((0, 0, 255), 1500, 775, 100, 45, "Blue")
    button_green = ButtonColors((0, 128, 0), 1625, 775, 100, 45, "Green")
    #For Seasons
    button_winter = ButtonColors('white', 1180, 687.5, 150, 45, 'Winter')
    button_summer = ButtonColors((253, 205, 72), 1380, 687.5, 150, 45, 'Summer')

    button_info = ButtonColors('blue', 1180, 900, 400, 45, 'Link to explanatory document')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(SKY_BLUE_SUMMER_SKY_COLOUR)

        # Draw elements
        if season == 'Winter':
            screen.fill(WINTER_SKY_BLUE)

        draw_house()
        pygame.draw.polygon(screen, roof_color,[(x_1_triangle, y_1_triangle), (x_2_triangle, y_2_triangle), (x_3_triangle, y_3_triangle)])
        draw_gutter()

        progress = min(progress + progress_speed, 1)

        tracing_ray_1(progress)
        tracing_ray_2(progress)
        tracing_ray_3(progress)

        tracing_reflected_ray_1(progress)
        tracing_reflected_ray_2(progress)
        tracing_reflected_ray_3(progress)

        draw_clouds()

        # Draw buttons and check for interaction
        if button_steel.draw():
            material = 'steel'

        if button_asphalt.draw():
            material = 'asphalt'

        if button_concrete.draw():
            material = 'concrete'

        if button_black.draw():
            roof_color = 'black'

        if button_white.draw():
            roof_color = 'white'

        if button_blue.draw():
            roof_color = 'blue'

        if button_green.draw():
            roof_color = 'dark green'

        if button_yellow.draw():
            roof_color = 'yellow'

        if button_red.draw():
            roof_color = 'red'

        if button_winter.draw():
            season = 'Winter'

        if button_summer.draw():
            season = 'Summer'

        if button_info.draw():
            webbrowser.open("https://docs.google.com/document/d/1xO3_IdARXuTSwHlEOszHUg1y9jBf7o6q5dl2P16XfCw/edit?usp=sharing")

        """For black roof color"""
        if roof_color == 'black' and material == 'steel':
            display_text = f'Percentage of IR absorbed for black steel is {steel_black() * 100:.2f}%'
            albedo = ba_steel_black

        if roof_color == 'black' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for black concrete is {concrete_black() * 100:.2f}%'
            albedo = ba_concrete_black

        if roof_color == 'black' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for black asphalt is {asphalt_black() * 100:.2f}%'
            albedo = ba_asphalt_black

        """For white roof color"""
        if roof_color == 'white' and material == 'steel':
            display_text = f'Percentage of IR absorbed for white steel is {steel_white() * 100:.2f}%'
            albedo = ba_steel_white

        if roof_color == 'white' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for white concrete is {concrete_white() * 100:.2f}%'
            albedo = ba_concrete_white

        if roof_color == 'white' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for white asphalt is {asphalt_white() * 100:.2f}%'
            albedo = ba_asphalt_white

        """For red roof color"""
        if roof_color == 'red' and material == 'steel':
            display_text = f'Percentage of IR absorbed for red steel is {steel_red() * 100:.2f}%'
            albedo = ba_steel_red

        if roof_color == 'red' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for red concrete is {concrete_red() * 100:.2f}%'
            albedo = ba_concrete_red

        if roof_color == 'red' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for red asphalt is {asphalt_red() * 100:.2f}%'
            albedo = ba_asphalt_red

        """For blue roof color"""
        if roof_color == 'blue' and material == 'steel':
            display_text = f'Percentage of IR absorbed for blue steel is {steel_blue() * 100:.2f}%'
            albedo = ba_steel_blue

        if roof_color == 'blue' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for blue concrete is {concrete_blue() * 100:.2f}%'
            albedo = ba_concrete_blue

        if roof_color == 'blue' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for blue asphalt is {asphalt_blue() * 100:.2f}%'
            albedo = ba_asphalt_blue

        """For green roof color"""
        if roof_color == 'green' and material == 'steel':
            display_text = f'Percentage of IR absorbed for green steel is {steel_green() * 100:.2f}%'
            albedo = ba_steel_green

        if roof_color == 'green' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for green concrete is {concrete_green() * 100:.2f}%'
            albedo = ba_concrete_green

        if roof_color == 'green' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for green asphalt is {asphalt_green() * 100:.2f}%'
            albedo = ba_asphalt_green

        """For yellow roof color"""
        if roof_color == 'yellow' and material == 'steel':
            display_text = f'Percentage of IR absorbed for yellow steel is {steel_yellow() * 100:.2f}%'
            albedo = ba_steel_yellow_bronze

        if roof_color == 'yellow' and material == 'concrete':
            display_text = f'Percentage of IR absorbed for yellow concrete is {concrete_yellow() * 100:.2f}%'
            albedo = ba_concrete_yellow_beige

        if roof_color == 'yellow' and material == 'asphalt':
            display_text = f'Percentage of IR absorbed for yellow asphalt is {asphalt_yellow() * 100:.0f}%'
            albedo = ba_asphalt_yellow

        if season == 'Summer' :
            energy_saving_summer: float = (Solar_radiation_Summer * Roof_Area_avg * albedo) / Energy_used_AC_avg
            display_write = f"The percentage of Energy saved from your choice is {energy_saving_summer:.2f}%"
            display_write1 = f"(See explanatory document)"

        if season == 'Winter':
            energy_saving_winter = (Solar_radiation_Winter * Roof_Area_avg * (1 - albedo)) / Energy_used_heating_avg
            display_write = f"The percentage of Energy saved from your choice is {energy_saving_winter:.2f}% "
            display_write1 = f"(See explanatory document)"
            snowy_gutter()

        # Display the selected options
        text_surface = font.render(display_text, True, (0, 0, 0))
        screen.blit(text_surface, (1100, 400))

        if display_write:
            text_surface = font.render(display_write, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(1400, 500))
            screen.blit(text_surface, text_rect)

        if display_write1:
            text_surface = font.render(display_write1, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(1240, 550))
            screen.blit(text_surface, text_rect)

        # Update screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()