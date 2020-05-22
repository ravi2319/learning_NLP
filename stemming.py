import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

para = '''
The ten months that have passed have seen very terrible catastrophic events in the world--ups and downs, misfortunes-- but can anyone sitting here this afternoon, this October afternoon, not feel deeply thankful for what has happened in the time that has passed and for the very great improvement in the position of our country and of our home?

Why, when I was here last time we were quite alone, desperately alone, and we had been so for five or six months. We were poorly armed. We are not so poorly armed today; but then we were very poorly armed. We had the unmeasured menace of the enemy and their air attack still beating upon us, and you yourselves had had experience of this attack; and I expect you are beginning to feel impatient that there has been this long lull with nothing particular turning up!

But we must learn to be equally good at what is short and sharp and what is long and tough. It is generally said that the British are often better at the last. They do not expect to move from crisis to crisis; they do not always expect that each day will bring up some noble chance of war; but when they very slowly make up their minds that the thing has to be done and the job put through and finished, then, even if it takes months - if it takes years - they do it.

Another lesson I think we may take, just throwing our minds back to our meeting here ten months ago and now, is that appearances are often very deceptive, and as Kipling well says, we must "...meet with Triumph and Disaster. And treat those two impostors just the same."

You cannot tell from appearances how things will go. Sometimes imagination makes things out far worse than they are; yet without imagination not much can be done. Those people who are imaginative see many more dangers than perhaps exist; certainly many more than will happen; but then they must also pray to be given that extra courage to carry this far-reaching imagination.
'''

sentences = nltk.sent_tokenize(para)
stemmer = nltk.PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)
