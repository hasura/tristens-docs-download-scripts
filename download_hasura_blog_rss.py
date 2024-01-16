import json
import xml.etree.ElementTree as ElementTree
import requests
from bs4 import BeautifulSoup


def parse_rss_feed(rss_feed_url):
    try:
        # Fetch the RSS feed content
        response = requests.get(rss_feed_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the RSS feed
        root = ElementTree.fromstring(response.content)

        rss_feed = []
        for item in root.findall("./channel/item"):
            content_element = item.find("{http://purl.org/rss/1.0/modules/content/}encoded")
            content = content_element.text if content_element is not None else None
            content_text = BeautifulSoup(content, "html.parser").get_text()

            feed_item = {
                "title": item.find("title").text,
                "description": item.find("description").text,
                "link": item.find("link").text,
                "creator": item.find("{http://purl.org/dc/elements/1.1/}creator").text,
                "pubDate": item.find("pubDate").text,
                "content": content_text
            }
            rss_feed.append(feed_item)

        return rss_feed

    except requests.RequestException as e:
        print(f"Error fetching the RSS feed: {e}")
        return []


def message_creator(feed_item: dict):
    message = {
        "messages": [
            {
                "role": "system",
                "content": "You are a blogger for the Hasura Blog."
            },
            {
                "role": "user",
                "content": f"Title: {feed_item.get('title')} Description: {feed_item.get('description')} Author: {feed_item.get('creator')}"
            },
            {
                "role": "assistant",
                "content": feed_item.get("content")
            }
        ]
    }
    return message


# Replace with your RSS feed URL
rss_feed_url = 'https://hasura.io/blog/rss'
feed_items = parse_rss_feed(rss_feed_url)

# If you have a very long RSS feed, beware of training costs
with open("blogrss.jsonl", "w") as f:
    for item in feed_items:
        m = message_creator(item)
        f.write(json.dumps(m) + "\n")

# Fine-tuning requires 10 examples, so while practicing it might be useful to take a slice of the first ten items
# Once you have a good idea what system prompts you will use things feel "pointed in the right direction" you can
with open("miniblogrss.jsonl", "w") as f:
    for item in feed_items[0:10]:
        m = message_creator(item)
        f.write(json.dumps(m) + "\n")
