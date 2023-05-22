import pygame
from datetime import datetime
 
# Initialize pygame library
pygame.init()

 
# Define the size of the pygame window and add a caption
screen = pygame.display.set_mode((470,180))
pygame.display.set_caption('Digital Clock')
 
 
# Add a digital font (DS-Digital) and specify the font size. Create two font kinds (small and big)
smallFont = pygame.font.SysFont('DS-Digital',30)
bigFont = pygame.font.SysFont('DS-Digital',135)
 
# Define the colors to be used
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
 
 # create lists for days and months...
days = ['Monday,', 'Tuesday,', 'Wednesday,' ,'Thursday,', 'Friday,', 'Saturday,', 'Sunday,']
months = ['January /', 'February /', 'March /', 'April /', 'May /', 'June /', 'July /', 'August /','September /', 'October /', 'November /', 'December /']
 
 
running = True
 
# Use a while loop 
while running:
    screen.fill(blue) #fill with blue color
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
 
 
    time_now = datetime.now()
    today = datetime.today()
 
    # split the time variable as minutes and hour and convert back to integer.
    minute = time_now.strftime('%M:%S')
    hour = int(time_now.strftime('%H'))
 
    year = time_now.strftime("%d / %Y")
    month = int(time_now.strftime('%m'))
    day = today.weekday()
    day = days[day]
    month = months[month-1]
 
    # Set "AM" or "PM", Subtract 12 from the hour variable if it's greater than 12.
    am = 'AM'
    if hour > 12:
        hour = hour - 12
        am = 'PM'
 
    # Create a new time variable to store the hour and minute values as an f-string
    time = f'{hour}:{minute}'
 
    # Create variables for the texts to be displayed, stating the two kinds of fonts (big and small) plus the color of the text.
    time_text = bigFont.render(time, True, green)
    month_text = smallFont.render(month, True, white)
    year_text = smallFont.render(year, True, white)
    am_text = smallFont.render(am, True, white)
    day_text = smallFont.render(day, True, white)
 
    # Define text-character positions
    screen.blit(time_text, (15,15))
    screen.blit(month_text, (150, 142))
    screen.blit(year_text, (260, 142))
    screen.blit(am_text, (380, 5))
    screen.blit(day_text, (30, 142))
 
    # update the time displayed.
    pygame.display.update()