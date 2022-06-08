from facebook_scraper import get_posts

for post in get_posts('SALE HERE', pages=1):
     print(post['text'][:50])
   