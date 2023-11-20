# You will receive lines of input:
#  On the first line, you will receive a title of an article
#  On the second line, you will receive the content of that article
#  On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
#  The title should be in "h1" tag (<h1></h1>)
#  The content in article tag (<article></article>)
#  Each comment should be in div tag (<div></div>

article_title = input()
article_content = input()
all_comments = []

while True:
    article_comments = input()
    if article_comments == "end of comments":
        break
    else:
        all_comments.append(article_comments)

print(f"<h1>\n    {article_title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")
for comment in all_comments:
    print(f"<div>\n    {comment}\n</div>")

