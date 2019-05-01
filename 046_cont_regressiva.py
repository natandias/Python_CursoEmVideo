import  time
from pygame import mixer
mixer.init()
mixer.music.load("beep.mp3")

for i in range(10, 0, -1):
   mixer.music.play(-1)
   print (i)   
   time.sleep (1)

mixer.music.load("fogos.mp3")
print ("FELIZ ANO NOVO !!!!")


mixer.music.play()
time.sleep (15)
      
