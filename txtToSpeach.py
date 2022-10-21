
from gtts import gTTS
import os

mytext = "Once upon a time there was a Princess.  Many a suitor came to the palace to win her hand in marriage, but it seemed to the Princess that each one of them looked at her without really seeing her at all. They act like there’s nothing more to a princess than her fine crown and royal dresses, she said to herself with a frown. ne afternoon after one of these visits, the Princess thought, “Sometimes I wish I were little again.” She found her favorite ball from childhood, the one that sparkled when she threw it up high to the sun.  She took the ball to the palace yard and threw it higher and higher."
language = 'en'
 
myobj = gTTS(text=mytext, lang=language, slow=False,  tld='co.in')

myobj.save("welcome.mp3")
  
os.system("welcome.mp3")