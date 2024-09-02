elif 'play music' in query:
            music_dir = "C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Snake_Game/Music/bgm1.mp3"
            songs = os.listdir("C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Snake_Game/Music/bgm1.mp3")
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))