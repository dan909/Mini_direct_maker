import os

def make_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Place = os.getcwd() + '/VerTestXX/'

Name_List = [x for x in range(0, 12)]

for i in Name_List:
    Name_List[i] = 'Day' + str('%02d' % Name_List[i])

Name_List.extend(['Background', 'End Img', 'END summry', 'Flor', 'Start'])

for i in Name_List:
    Locate = Place + i
    make_if_not_exist(Locate)

# Make the readme file

f = open(Place + 'ReadMe.html','w')

message = """<html>
<head>Read Me</head>
<br>
<body><p>Make a folder coled start name the imeges as below but you dont run the cut and save macro in the folder</p>
<p>Place each days pichers in a folder caled 'DayXX'</p>
<p>Rename the files to {a 5 leter discripter folowed by the number of that plate then '_' then Time or another 4 leter tern like Rday folowed by day} the same as the folder eg 'PlateXX_TimeXX.JPG' or 'OXAtpXX_RunTXX.JPG'</p>
<p>Run the cut and save macro in the folder by opining the first file in imajej</p>
<p>when all days are done like this</p>
<p>make a folder called 'END summry' and one callad 'Flor' [with the floresence img in named as the emeges wher but whith a 2 leter substitute for time] and a folder caled 'End Img' in this folder coppy just the hole plate imgs form your last time point</p>
<hr>
<p>then the end macro can be run</p>
<p>it must be run in hole plates</p>
<p>if you whant to carry on from where you left off just deleat the done ing from 'End Img'</p>
</body>
</html>"""

f.write(message)
f.close()