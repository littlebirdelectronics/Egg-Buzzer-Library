from Egg_Buzzer import Passive_Buzzer
import time

buzzer = Passive_Buzzer.Buzzer(13)

buzzer.Start(1000, 50)
time.sleep(1)
buzzer.ChangeFrequency(1500)
time.sleep(1)
buzzer.Stop();