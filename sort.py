import pygame
import random
import time

from pygame.constants import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_ESCAPE, K_SPACE, QUIT

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
grey = (220, 220, 220)
display_width, display_height = 900, 600
WIDTH, HEIGHT = display_width, display_height
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms")

x = 40
y = 10
width = 10


font = pygame.font.SysFont(None, 20)
    

def insertion_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            draw_height(arr)
            pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * (j), y, (820/(n*2)), arr[j]))
            pygame.display.update()
            time.sleep(1/60)
        pygame.display.update()
        arr[j+1] = key
        draw_window()
        draw_height(arr)
        pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * (i), y, (820/(n*2)), arr[i]))
        pygame.display.update()
        time.sleep(1/60)
        if (is_sorted(arr)): 
            end = time.time()
            break
    draw_window()
    draw_height(arr)
    draw_sorted(arr)
    return end-start

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        min_ = i
        j = i+1
        for j in range(i+1, n):
            if arr[j] < arr[min_]:
                min_ = j
            draw_window()
            draw_height(arr)
            pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * (j-1), y, (820/(n*2)), arr[j-1]))
            pygame.display.update()
            time.sleep(1/60)
        arr[i], arr[min_] = arr[min_], arr[i]
        draw_window()
        draw_height(arr)
        pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * (i-1), y, (820/(n*2)), arr[i-1]))
        pygame.display.update()
        draw_height(arr)
        pygame.display.update()
        time.sleep(1/60)
        if (is_sorted(arr)):
            end = time.time()
            break
    draw_window()
    draw_height(arr)
    draw_sorted(arr)
    return end-start
            



def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
            draw_window()
            draw_height(arr)
            pygame.draw.rect(win, (255, 0, 0), (x + (820/n)+ (820/n) * j, y, (820/(n*2)), arr[j+1]))
            pygame.display.update()
            time.sleep(1/60)
        if (is_sorted(arr)): break
    end = time.time()
    draw_window()
    draw_height(arr)
    draw_sorted(arr)
    return end-start
    

def shell_sort(arr):
    start = time.time()
    n = len(arr)
    gap = int(n/3)
    while gap > 0:
        for i in range(int(gap), n):
            temp = arr[i]
            j = i
            while j >= gap and arr[int(j-gap)] > temp:
                arr[int(j)] = arr[int(j-gap)]
                draw_window()
                draw_height(arr)
                pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * j, y, (820/(n*2)), arr[int(j)]))
                pygame.display.update()
                time.sleep(1/60)
                j -= gap
            arr[int(j)] = temp
            draw_window()
            draw_height(arr)
            pygame.draw.rect(win, (255, 0, 0), (x + (820/n) * j, y, (820/(n*2)), arr[int(j)]))
            pygame.display.update()
            time.sleep(1/60)
            if is_sorted(arr): 
                end = time.time()
                draw_window()
                draw_height(arr)
                draw_sorted(arr)
                return end-start

        gap /= 3
        if is_sorted(arr): 
            end = time.time()
            draw_window()
            draw_height(arr)
            draw_sorted(arr)
            return end-start
    


def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        else: 
            # print("Array is not sorted.")     #for debugging
            return False
    # print("Array is sorted.")         #for debugging
    return True

def draw_sorted(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            pygame.draw.rect(win, (0, 255, 0), (x + (820/n) * i, y, (820/(n*2)), arr[i]))
            pygame.draw.rect(win, (0, 255, 0), (x + (820/n) * (i+1), y, (820/(n*2)), arr[i+1] ))
            pygame.display.update()
            time.sleep(1/60)
            continue
        else: return False
    return True


def draw_height(arr):
    n = len(arr)
    for i in range(len(arr)):
        pygame.draw.rect(win, (255, 255, 255), (x + (820/n) * i, y, (820/(n*2)), arr[i]))
    pygame.display.update()
           

def draw_window():
    pygame.draw.rect(win, black, (0, 0, display_width, 400))
    pygame.display.update()

def draw_text_window():
    pygame.draw.rect(win, white, (0, 400, display_width, 200))
    pygame.display.update()

def draw_text(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    pygame.draw.rect(win, white, (x-50, y, display_width, 30))
    win.blit(screen_text, [x, y+8])

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == K_1:
                return 1
            if event.type == pygame.KEYDOWN and event.key == K_2:
                return 2
            if event.type == pygame.KEYDOWN and event.key == K_3:
                return 3
            if event.type == pygame.KEYDOWN and event.key == K_4:
                return 4

def show_time(time_taken, x, y):
    sort_time = font.render("Sorting Time: {0:.4f} seconds".format(time_taken), True, black)
    pygame.draw.rect(win, white, (x-50, y, display_width, 30))
    win.blit(sort_time, [x, y+8])


def run_animation():
    reverse_40 = [385-n*5 for n in range(0, 40)]
    reverse_120 = [385-n for n in range(0, 120)]
    random_40 = random.sample(range(1, 385), 40)
    random_120 = random.sample(range(1, 385), 120)
    almo_sorted_40 = [n*5 for n in range(1, 40)]
    for i in range(2, 39):
        if i % 2 == 0:
            almo_sorted_40[i], almo_sorted_40[i-1] = almo_sorted_40[i-1], almo_sorted_40[i]
        else: continue
    almo_sorted_120 = [n*3 for n in range(1,120)]
    for i in range(2, 119):
        if i % 2 == 0:
            almo_sorted_120[i], almo_sorted_120[i-1] = almo_sorted_120[i-1], almo_sorted_120[i]
        else: continue
    # print(almo_sorted_40)

    choice = 0
    choice = wait()
    if choice == 1:
        draw_text_window()
        draw_text("Running Bubble Sort...(40 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(random_40)   
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Bubble Sort...(120 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(random_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Bubble Sort...(40 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(reverse_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Bubble Sort...(120 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(reverse_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Bubble Sort...(40 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(almo_sorted_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Bubble Sort...(120 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = bubble_sort(almo_sorted_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
    if choice == 2:
        draw_text_window()
        draw_text("Running Selection Sort...(40 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(random_40)   
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Selection Sort...(120 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(random_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Selection Sort...(40 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(reverse_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Selection Sort...(120 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(reverse_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Selection Sort...(40 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(almo_sorted_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Selection Sort...(120 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = selection_sort(almo_sorted_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
    if choice == 3:
        draw_text_window()
        draw_text("Running Insertion Sort...(40 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(random_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Insertion Sort...(120 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(random_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Insertion Sort...(40 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(reverse_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Insertion Sort...(120 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(reverse_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Insertion Sort...(40 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(almo_sorted_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Insertion Sort...(120 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = insertion_sort(almo_sorted_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
    if choice == 4:
        draw_text_window()
        draw_text("Running Shell Sort...(40 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(random_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Shell Sort...(120 Items Random)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(random_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Shell Sort...(40 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(reverse_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Shell Sort...(120 Items Reversed)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(reverse_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Shell Sort...(40 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(almo_sorted_40)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)
        draw_text_window()
        draw_text("Running Shell Sort...(120 Items Almost Sorted)", black, 50, 450)
        draw_text("Sorting Time: In Progress...", black, 50, 500)
        time_taken = shell_sort(almo_sorted_120)
        show_time(time_taken, 50, 500)
        pygame.display.update()
        time.sleep(2)

def main():
    pygame.init()
    # draw_height()
    # font = pygame.font.SysFont(None, 48)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            
            draw_text("Sorting Algorithms (40 random, 120 random, 40 reversed, 120 reversed, 40 almost sorted, 120 almost sorted)", black, 50, 400)
            draw_text("Bubble Sort:    Press 1", black, 50, 430)
            draw_text("Selection Sort: Press 2", black, 50, 460)
            draw_text("Insertion Sort: Press 3", black, 50, 490)
            draw_text("Shell Sort:     Press 4", black, 50, 520)
            pygame.display.update()
            run_animation()

    pygame.quit()

if __name__ == "__main__":
    main()