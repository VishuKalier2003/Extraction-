from bs4 import BeautifulSoup
# BeautifulSoup is used to perform operations on web pages and HTML tags like the objects of python

# We can use double slashes to overcome unicode error
with open('C:\\Users\\VISHU\\3D Objects\\Data\\Data\\test.html') as file:
    content = file.read()  # Method to read a file
    print(content)
    # Arguments as the file and the parser method string via 'lxml'
    soup = BeautifulSoup(content, 'lxml')   # Creating instance of the BeautifulSoup

    # This allows to see the HTML file in a more prettier way
    print(soup.prettify())    # soup as the instance of the file created
    print()
    # Specifically searching for HTML tags in the file chosen
    tag = soup.find('h2')     # Searching for h2 tags in the file
    print(tag)
    print()
    tags = soup.find_all('h2')  # Finds all h2 tags in the HTML document
    print(tags)

    #Printing only the text content of the tags chosen or searched
    for loop in tags:     # Since they are stored as an list iteration is easy
        print(loop.text)      # Printing the text of the tag only
    #Specifically searching div tags with the class named cards
    print()
    cards = soup.find_all('div', class_='cards')
    for loop in cards:          # Since they are stored as an list iteration is easy
        print(loop.text)     # Printing the text of the card