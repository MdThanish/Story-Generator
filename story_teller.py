import random
import tkinter as tk
from tkinter import ttk, scrolledtext
from gtts import gTTS
import os
import pygame
from threading import Thread

class StoryGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Nish's Story Generator")

        # Initialize GUI components
        self.create_gui()

        # Initialize text-to-speech engine
        self.init_tts()

        # Bind the window close event to the cleanup method
        master.protocol("WM_DELETE_WINDOW", self.cleanup)

    def create_gui(self):
        # Label for topic selection
        self.label = tk.Label(self.master, text="Choose a Topic:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Dropdown for topic selection
        self.topic_var = tk.StringVar()
        self.topic_dropdown = ttk.Combobox(self.master, textvariable=self.topic_var)
        self.topic_dropdown['values'] = ('Animals', 'Fish', 'Forest', 'Random')
        self.topic_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Button to generate story
        self.generate_button = tk.Button(self.master, text="Generate Story", command=self.generate_story)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Text area to display generated story
        self.story_text = scrolledtext.ScrolledText(self.master, height=10, width=40, wrap=tk.WORD)
        self.story_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Button to play audio
        self.play_audio_button = tk.Button(self.master, text="Play Audio", command=self.play_audio)
        self.play_audio_button.grid(row=3, column=0, columnspan=2, pady=10)

    def init_tts(self):
        self.language = 'en'
        self.txt_file_path = 'generated_story.txt'
        self.audio_file_path = 'generated_speech.mp3'

    def generate_story(self):
        selected_topic = self.topic_var.get().lower()

        if selected_topic == "animals":
            story = (random.choice(self.when) + ', ' + random.choice(self.who) + ' went to ' +
                     random.choice(self.went) + ' ' + random.choice(self.what) + '.')
        elif selected_topic == "fish":
            story = """There was once a fisherman whose livelihood depended on his catch. One day, he was able to catch only one small fish.
                       The fish, in its desperation to live, says, "Please leave me kind sir. I am small and of no use to you. Let me back into the river and I can grow bigger. You can then catch me and make more money."
                       The wise fisherman replies, "I will not give up a certain profit for an uncertain profit."
                    """
        elif selected_topic == "forest":
            story = """The kids were lost. A group of children from a small village at the edge of the Orinoco River had stolen a canoe to have some fun, but the currents carried them far out into the delta. They shouted for help, but deep in the jungle there was no one to come to their rescue. As night fell, the children were afraid they would never be found and end up being eaten by a jaguar.
                        Tired and hungry, they were on the verge of tears when they heard a gentle whisper. They looked up to see a Moriche palm tree, waving in the wind. The palm offered the children its fruit. With food in their stomachs, the children gained strength to look around. The Moriche palm introduced them to other members of the forest and soon the children had many friends. They learned to use wood to build houses and leaves for roofs. They found places to find food and water, herbs for medicine and even ways to dress up and decorate themselves.
                        Many years later, a group of adventurers canoeing down the river were surprised to see a small settlement on a forested island deep in the jungles. The children had learned the ways of the forest and were now living comfortably amidst the labyrinth of waterways. The Moriche palm came to be known as the ‘tree of life’ and the children grew up to be the Warao Indians also known as ‘canoe people’.
                        Moral: When in trouble, look to nature for answers.
                    """
        else:
            story = (random.choice(self.Sentence_starter) + random.choice(self.character) +
                     random.choice(self.time) + random.choice(self.story_plot) +
                     random.choice(self.place) + random.choice(self.second_character) +
                     random.choice(self.age) + random.choice(self.work))

        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, story)

        # Save the generated story to a text file
        with open(self.txt_file_path, 'w') as txt_file:
            txt_file.write(story)

        # Convert the text to speech
        self.text_to_speech(story)

    def text_to_speech(self, text):
        # Use gTTS to convert text to speech
        tts = gTTS(text=text, lang=self.language, slow=False)

        # Save the speech to an audio file
        tts.save(self.audio_file_path)

    def play_audio(self):
        # Play the audio file using pygame
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_file_path)
        pygame.mixer.music.play()

    def cleanup(self):
        # Stop the audio playback and clean up resources
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.master.destroy()

# Predefined story components
StoryGeneratorApp.when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']
StoryGeneratorApp.who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
StoryGeneratorApp.went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
StoryGeneratorApp.what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']

StoryGeneratorApp.Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
StoryGeneratorApp.character = [' there lived a king.', ' there was a man named Jack.', ' there lived a farmer.']
StoryGeneratorApp.time = [' One day', ' One full-moon night']
StoryGeneratorApp.story_plot = [' he was passing by', ' he was going for a picnic to ']
StoryGeneratorApp.place = [' the mountains', ' the garden']
StoryGeneratorApp.second_character = [' he saw a man', ' he saw a young lady']
StoryGeneratorApp.age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
StoryGeneratorApp.work = [' searching something.', ' digging a well on roadside.']

# Create the main application window
root = tk.Tk()
app = StoryGeneratorApp(root)

# Run the application
root.mainloop()
