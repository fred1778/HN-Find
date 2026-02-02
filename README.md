# HN-Find
Tool to search for occurrences of a term in the front page links on Hacker News.

Python script which uses BS4 to search text from page content by following links posted on [Hacker News](https://news.ycombinator.com). Outputs a CSV file with all occurences of search term, with +/- 150 characters around occurence for context. 

Screenshot below is of CSV output from a search for ' AI ':

<img width="1444" height="349" alt="Screenshot 2026-02-02 at 22 19 24" src="https://github.com/user-attachments/assets/7238b00d-8ecf-4231-9776-5aa6584d5590" />

TODO:
- Highlight HTTP 403 exceptions (flag in output) (or change user-agent in request header)
- Exclude text from HTML tags likley to be non-relevant (banners, buttons, etc.)
- Consume text file for search terms + options
  
