from models.film import Film
from models.genre import Genre
from models.node import Node

def main():
    film_list = [Film('Divergent', 2014, 140, Genre.FANTASY, 'Lionsgate Films'),
    Film('Avatar', 2009, 162, Genre.FANTASY, '20th Century Fox'),
    Film('Green Book', 2018, 130, Genre.DRAMA, 'Universal Pictures'),
    Film("Hachi: A Dog's Tale", 2009, 93, Genre.DRAMA, '20th Century Studios'),
    Film('Spirited away', 2001, 125, Genre.ANIMATION, 'Studio Ghibli'),
    Film('The Intern', 2015, 121, Genre.COMEDY, 'Paramount Pictures')]
 
    root = Node(Film('The Mule', 2018, 116, Genre.CRIME, 'Warner Bros. Pictures'))
    for film in film_list:
        root.add(film)
    root.print()
    print('='*30,'printing by genre:')
    root.print_by_genre(Genre.FANTASY)
    print('='*30,'delete by studio:')
    root.delete_by_studio('20th Century Fox')
    root.print()

if __name__ == '__main__':
    main()