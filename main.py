import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stopword_list = stopwords.words("english")

lyrics = """
I look up from the ground
To see your sad and teary eyes
You look away from me
And I see there's something you're trying to hide
And I reach for your hand but it's cold
You pull away again
And I wonder what's on your mind
And then you say to me you made a dumb mistake
You start to tremble and your voice begins to break
You say the cigarettes on the counter weren't your friends
They were my mates
And I feel the color draining from my face
And my friend said
I know you love her, but it's over, mate
It doesn't matter, put the phone away
It's never easy to walk away, let her go
It'll be alright
So I asked to look back at all the messages you'd sent
And I know it wasn't right, but it was fucking with my head
And everything deleted like the past, it was gone
And when I touched your face, I could tell you're moving on
But it's not the fact that you kissed him yesterday
It's the feeling of betrayal, that I just can't seem to shake
And everything I know tells me that I should walk away
But I just want to stay
And my friend said
I know you love her, but it's over, mate
It doesn't matter, put the phone away
It's never easy to walk away, let her go
It'll be okay
It's gonna hurt for a bit of time
So bottoms up, let's forget tonight
You'll find another and you'll be just fine
Let her go
But nothing heals the past like time
And they can't steal
The love you're born to find
But nothing heals the past like time
And they can't steal
The love you're born to find
I know you love her, but it's over, mate
It doesn't matter, put the phone away
It's never easy to walk away, let her go
It'll be okay
It's gonna hurt for a bit of time
So bottoms up, let's forget tonight
You'll find another and you'll be just fine
Let her go
It'll be alright
It'll be alright
It'll be alright
It'll be alright
It'll be alright
""".strip()


def preprocess(line):
    accu = []
    accu.append(line)
    line = line.lower()
    accu.append(line)
    import re

    line = re.sub(r"[^\w\s]", "", line)
    accu.append(line)
    line = [x for x in line.split(" ") if x not in stopword_list]
    line = " ".join(line)
    accu.append(line)
    return accu


def build_csv(preprocessed_data):
    import csv

    fields = ["Original Lyrics", "Lowercase", "Punctuation Removal", "Stopword Removal"]
    with open("output.csv", "w+") as output:
        writer = csv.writer(output)
        writer.writerow(fields)
        writer.writerows(preprocessed_data)


parsed_data = list(map(preprocess, lyrics.splitlines()))
build_csv(parsed_data)
