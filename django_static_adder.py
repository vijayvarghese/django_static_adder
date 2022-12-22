from bs4 import BeautifulSoup
import re
import sys

http_pattern = re.compile(f"^http")
mailto_pattern = re.compile(f"^mailto")

def add_static(file_name):
    # Open the HTML file and create a BeautifulSoup object
    with open('index.html') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    # Find all the links in the HTML
    links_in_a = soup.find_all('a')
    links_in_link = soup.find_all('link')
    links_in_script = soup.find_all('script')
    links_in_img = soup.find_all('img')

    # Iterate over the links and edit the href attribute
    for link in links_in_a:
        href = link.get('href')
        if href:
            if not (http_pattern.search(href) or mailto_pattern.search(href)):

                link['href'] = "{% static '" + href + "'%}"
                # Replace the old link with the edited link
                link.replace_with(link)

    for link in links_in_link:
        href = link.get('href')
        if href:
            if not http_pattern.search(href):

                link['href'] = "{% static '" + href + "'%}"
                # Replace the old link with the edited link
                link.replace_with(link)

    for link in links_in_script:
        src = link.get('src')
        if src:
            if not http_pattern.search(src):

                link['src'] = "{% static '" + src + "'%}"
                # Replace the old link with the edited link
                link.replace_with(link)

    for link in links_in_img:
        src = link.get('src')
        if src:
            if not http_pattern.search(src):

                link['src'] = "{% static '" + src + "'%}"
                # Replace the old link with the edited link
                link.replace_with(link)

    # Save the updated HTML to a new file
    with open('updated.html', 'w') as updated_file:
        updated_file.write(str(soup))


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print("Must Provide a File Name or Path")

    try:
        add_static(filename)
        print("Operaion Sucessfull ! ")
    except:
        print("An unexpeted Error occured !")