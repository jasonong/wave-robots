from waveapi import events
from waveapi import model
from waveapi import robot
import random

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    Notify(context)

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("I'm alive!")

def Notify(context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hi everybody!")

def OnPictureAdded(properties, context):
  """Invoked when a picture attachment has been added."""
  root_wavelet = context.GetRootWavelet()
  response_array = ["Yukes", "Yawn", "Hmm...", "Woah", "WOW", "HOT!!!"]
  response = random.choice(response_array)
  root_wavelet.CreateBlip().GetDocument().SetText(response)

if __name__ == '__main__':
  myRobot = robot.Robot('jasonong_gwave_robot', 
      image_url='http://jasonong_gwave_robot.appspot.com/icon.png',
      version='1',
      profile_url='http://jasonong_gwave_robot.appspot.com/')
  """myRobot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED, OnParticipantsChanged)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  """
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnPictureAdded)
  myRobot.Run()
