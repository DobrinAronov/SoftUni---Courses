from collections import deque

suggested_links_dqu = deque(int(el) for el in input().split())
featured_articles_lst = list(map(int, input().split()))

target_value = int(input())

final_feed_collections = []

while suggested_links_dqu and featured_articles_lst:
    current_link = suggested_links_dqu.popleft()
    current_article = featured_articles_lst.pop()

    if current_article > current_link:
        remainder = current_article % current_link
        final_feed_collections.append(abs(remainder))
        if remainder != 0:
            featured_articles_lst.append(remainder * 2)

    elif current_link > current_article:
        remainder = current_link % current_article
        final_feed_collections.append(-abs(remainder))
        if remainder != 0:
            suggested_links_dqu.append(remainder * 2)

    else:
        final_feed_collections.append(0)

total_engagement_value = sum(final_feed_collections)

print(f"Final Feed: {', '.join(map(str, final_feed_collections))}")

if total_engagement_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
