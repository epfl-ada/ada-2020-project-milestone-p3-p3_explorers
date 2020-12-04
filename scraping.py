import requests
from bs4 import BeautifulSoup


def scrape_wikipedia_pageviews(start_year, start_month, end_year, end_month,
                               data_directory, articles_file, output_file):
    """scrape_wikipedia_pageviews stores in a CSV file the pageviews of the
    articles for the given time period."""

    root_url = 'https://wikipediaviews.org/displayviewsformultiplemonths.php?'

    # Read the list of wikipedia articles
    with open(data_directory + articles_file) as file:
        articles = [article[:-1] for article in file.readlines()]

    # Generate the list of (year, month) tuples
    dates = []
    year = start_year
    month = start_month
    while year <= end_year and (year < end_year or month <= end_month):
        dates.append((year, month))
        month += 1
        if month > 12:
            month = 1
            year += 1

    # Put the dates in the format expected by the website
    params_dates_formatted = {}
    for i, date in enumerate(dates):
        key = 'months[{}]'.format(i)
        params_dates_formatted[key] = "{}{:02d}".format(date[0], date[1])
    dates_formatted = params_dates_formatted.values()

    # Make a request for each article and process the pageviews
    triples = []
    for article in articles:
        # Prepare query parameters
        params = params_dates_formatted.copy()
        params['language'] = 'en'
        params['drilldown'] = 'desktop'
        params['page'] = article
        # Make the request
        r = requests.get(root_url, params)
        if r.status_code != 200:
            print('Failed to fetch article "{}"'.format(article))
            continue
        # Parse the HTML response
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            date = cells[0].string
            if date in dates_formatted:
                views_raw = cells[1].a['title'].split()[0]
                try:
                    views = int(views_raw)
                except ValueError:
                    views = 'NaN'
                date_pretty = date[:4] + "-" + date[4:]
                triples.append((article, date_pretty, views))

    # Write the result in a CSV file
    with open(data_directory + output_file, 'w') as file:
        file.write("id,article,date,views\n")
        id = 0
        for triple in triples:
            file.write("{},{},{},{}\n".format(id, *triple))
            id += 1
