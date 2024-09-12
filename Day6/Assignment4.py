import re
from collections import Counter

def find_hashtags(post):
    
    post = post.lower()

    
    pattern = r'#\w{4,}'

   
    hashtags = re.findall(pattern, post)

    
    hashtags = [hashtag[1:] for hashtag in hashtags]

    
    frequency = Counter(hashtags)

    return dict(frequency)


post = "I love #Python and #python programming. #AI is also cool, but #MachineLearning is my favorite."
hashtags = find_hashtags(post)
print(hashtags)
