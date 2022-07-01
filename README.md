# keylight
KeyLight inputs creates simple 3D animations from a midi live signal (ex: musical keyboard).<br>
You could test this application with any midi software editor (Ableton Live, Cubase, Ardour, Acid Pro, Ardour, LMMS - this last one is which I use). Just open a virtual keyboard in a midi editor, and put it to send midi signal through a port. Select this port in Keylight. See 'how to use' section below.<br>

<img src=https://imgur.com/opYXC3yl.png></img>

# Install
Dependencies: UPBGE >=0.3 https://upbge.org/#/download<br>
              Python>=3.0 https://www.python.org/downloads/<br>
Sourcecode is in the keylight.blend file and 'plano.py' library<br>

# How to Use
# 1 - Adjust settings:
from powershell/command prompt/shell run:<br>
          python config.py<br>
          <img src=https://i.imgur.com/7W9Xcyy.png /><br>
          It uses 'interface_support.py' and 'tela.py' to show an interface to create a configuration file called 'param.cfg'.
# 2 - Run!
Option 1: Run the keylight.blend file from UPBGE.<br>
          It automatically loads the param.cfg file<br>
Option 2: If you use Linux x86-64 (like me) you can use a ready release:<br>
          https://github.com/codesearcher/keylight/releases<br>
          <img src=https://i.imgur.com/kcQTtQv.png /><br>
#

# Explaining...
#To Do

# Next steps
-Bugs fixes<br>
-Create functions that join repetitive tasks in one block of code<br>

Dedicated to all music lovers!<br>
