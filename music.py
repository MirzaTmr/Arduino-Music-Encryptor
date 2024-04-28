import pygame
from engi1020.arduino.api import *
from time import sleep

# Initialize pygame
pygame.mixer.init()


# Definition of piano notes and their corresponding sound files
notes = {
    range(0, 79): ('A#','a1s.wav'),   
    range(79, 157): ('C#','c1s.wav'),  
    range(157, 235): ('D#', 'd1s.wav'),   
    range(235, 313): ('F#', 'f1s.wav'),   
    range(313, 391): ('G#', 'g1s.wav'),   
    range(547, 625): ('A', 'a1.wav'),   
    range(625, 703): ('B', 'b1.wav'),   
    range(391, 469): ('C', 'c1.wav'),   
    range(469, 547): ('D', 'd1.wav'),  
    range(703, 781): ('E', 'e1.wav'),   
    range(781, 859): ('F', 'f1.wav'),   
    range(859, 937): ('G', 'g1.wav'),   
    range(937, 1024): ('sp', None)
}
    

# Sample for the rotary dial
def wheel():
    print('Use dial now.')
    sleep(2)

    current_notes = None
    selected_notes = []
    while True:
        value = analog_read(0)
        for range_, (note, _) in notes.items():
            if value in range_ and note != current_notes:
                current_notes = note
                print(f"Current note: {current_notes}")
                

        button = digital_read(6) 
        if button == True:
            for range_, (note, _) in notes.items():
                if value in range_:
                    print(f"Selected note: {note}")
                    selected_notes.append(note)
            sound = analog_read(2)
            rgb_lcd_print(f'Sound Hz: {sound}')
            if sound >= 250 and sound <900
            exit = input('Is that all the notes? ')
            
            if exit.lower() == 'yes':
                break  # Exit the loop if sound exceeds
        
    return selected_notes

# To retrieve notes
def get_note_file(val):
    for range_,note_file in notes.items():
        if val in range_:
            return {'note': note_file[0], 'file': note_file[1]}
    return None

# Load and play the corresponding note's sound file
def play_note(note):
    note_info = None
    for range_,(note_,file) in notes.items():
        if note_ == note:
            note_info = (note_,file)
            break
    if note_info:  
        _,file = note_info
        if file:  
            sound = pygame.mixer.Sound(file)
            sound.play()
            sleep(0.12)


# Main function to handle user input
def main():
    rgb_lcd_colour(70,20,70)
    print("Welcome to the virtual piano!")
    sleep(1.5)
    print("Enter the select the notes you want to play (A#, C#, D#, F#, G#, C, D, E, F, G, A, B) and sp for delay.")
    sleep(1)
    #For example: C D E
    print("Enter 'quit' to exit.")
    sleep(1)
    
# add to play multiple notes
    while True:

        selected_notes = wheel()
        rgb_lcd_clear()        
        print(selected_notes)
        space = False
        
        if 'sp' in selected_notes:
            space = True
            user_time = float(input('Enter the delay you want between notes: '))
            print('Press the button to confirm selection')
            sleep(2)
            button = digital_read(6)
            if button == True:        
                for note in selected_notes:
                    sleep(0.5)
                    digital_write(4,True)
                    rgb_lcd_print(f"Playing: {note}")
                    rgb_lcd_colour(50,30,70)
                    play_note(note) 
                    digital_write(4,False)
                    rgb_lcd_clear()

                if space:
                        sleep(user_time)


                user_input = input("Type 'quit' to end or space to continue: ")
                sleep(0.5)
                if user_input.lower() == 'quit':
                    rgb_lcd_colour(0,255,0)
                    rgb_lcd_print("Exiting...")
                    sleep(1.5)
                    rgb_lcd_colour(255,0,125)
                    rgb_lcd_clear()
                    break

            else:
                rgb_lcd_colour(255,0,0)
                rgb_lcd_print("Press button!")
                buzzer_frequency(5,400)
                sleep(1)
                buzzer_stop(5)
                rgb_lcd_colour(70,20,45)
                rgb_lcd_clear()
                break
                
        

               
        else:
            sleep(2)
            print('Press the button to confirm selection')
            sleep(2)       
            button = digital_read(6)
            if button == True:        
                for note in selected_notes:
                    sleep(0.5)
                    digital_write(4,True)
                    rgb_lcd_print(f"Playing: {note}")
                    play_note(note) 
                    digital_write(4,False)
                    rgb_lcd_clear()

                user_input = input("Type 'quit' to end or space to continue: ")
                sleep(0.5)
                if user_input.lower() == 'quit':
                    rgb_lcd_colour(0,255,0)
                    rgb_lcd_print("Exiting...")
                    sleep(1.5)
                    rgb_lcd_colour(255,255,255)
                    rgb_lcd_clear()
                    break
            else:
                rgb_lcd_colour(255,0,0)
                rgb_lcd_print("Press button!")
                buzzer_frequency(5,400)
                sleep(1)
                buzzer_stop(5)
                rgb_lcd_colour(255,255,255)
                rgb_lcd_clear()
                break

               

main()

#Happy Birthday: 'C#', 'C#', 'D#', 'C#', 'F#', 'E', 'C#', 'C#', 'D#', 'C#', 'G#', 'F#', 'C#', 'C#', 'C#', 'A#', 'F#', 'E', 'D#', 'D#', 'D#', 'C#', 'F#', 'E'
#Space: 'C#', 'C#', 'D#', 'A#', 'F#', 'D#', 'C', 'D#', 'D#' 

