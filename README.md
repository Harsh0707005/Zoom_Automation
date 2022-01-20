# Zoom Automation
There are many students and professionals who are too lazy to join the Zoom Meeting manually <i>(including me ;P )</i>.
<br>So this is a simple python script that lets you join a zoom meeting at a scheduled time, without any human interference.
<br>
<h2> Prerequisites</h2>
Make sure the following module are installed:
<ul>
  <li><a href = 'https://pypi.org/project/PyAutoGUI/' target = '_blank'> PyAutoGUI</a></li>
</ul>
Install this by typing the following code into Powershell or Terminal:
<br>
<code> pip install PyAutoGUI</code>
<br>
<h2> Usage</h2>

Just import the <em>.py</em> file, change the following parts in the <i>data (links.txt)</i> and the script:
<ul>
  <li>Change the timings of the meeting in the <i>.py</i> file (if necessary add more meetings by creating more <em>elif</em> statements but the code will be same as others).</li>
  <li>Change the time between subsequent meetings as continuous execution of the program may lead to unnecessary memory usage.
    Make sure the set the interval of 2-3 minutes before scheduled meet.</li>
  <li>Change the meeting links in the <em>Links.txt</i> (mind the sequence of the links according to time)</li>
</ul>
