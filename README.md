# Zoom Automation
There are many students and professionals who are too lazy to join the Zoom Meeting manually <i>(including me :stuck_out_tongue_winking_eye: )</i>.
<br>So this is a simple python script that lets you join a zoom meeting at a scheduled time, without any human interference.
<br>
<hr>
<h2> Prerequisites</h2>
Make sure the following module are installed:<br><br>
<ul>
  <li><a href = 'https://pypi.org/project/PyAutoGUI/' target = '_blank'> PyAutoGUI</a></li>
</ul>
<br>
Install this by typing the following code into Powershell or Terminal:
<br>
<code> pip install PyAutoGUI</code>
<br>
<hr>
<br>
<h2> Usage</h2>

Just import the <em>.py</em> file, change the following parts in the <i>data (links.txt)</i> and the script:
<ul>
  <li>Change the timings of the meeting in the <i>.py</i> file (if necessary add more meetings by creating more <em>elif</em> statements but rest if the code will remain same).</li>
  <br><br>
<img src = '/.imgs/elif.jpg/' alt = 'Changing time in elif statement/adding more elif statements'>
  <br><br>
  <li>Change the time between subsequent meetings as continuous execution of the program may lead to unnecessary memory usage.
    Make sure to set the interval of 2-3 minutes before scheduled meet.</li>
  <br><br>
<img src = '/.imgs/time.png/' alt = 'Changing time interval between subsequent meetings'>
  <br><br>
  <li>Change the meeting links in the <em>Links.txt</i> (mind the sequence of the links according to time)</li>
<img src = '/.imgs/links.png/' alt = 'Changing links of zoom meeting.'>
</ul>
