import media
import fresh_tomatillos

toy_story = media.Movie(
    "Toy Story",
    "A cowboy and a space ranger go on a crusade to liberate an alien \
    species from their captor (and deity), the Claw.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4",
    "22 November 1995", "4860 secs",
    "John Lasseter",
    "John Lasseter",
    "John Lasseter",
    "Forrest Gump, and Tim from Home Improvement")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "18 December 2009", "forever, but worth it",
    "James Cameron",
    "James Cameron",
    "James Cameron",
    "Sigourney Weaver, Zoe Saldana, Sam Worthington")

zissou = media.Movie(
    "The Life Aquatic",
    "A man goes on a quest to find the rare shark that ate his best friend... \
    then blow it up.",
    "http://ibraheemyoussef.com/ibraheemshop/images/zissou.jpg",
    "https://www.youtube.com/watch?v=yh401Rmkq0o",
    "10 December 2004", "0.0826389 days",
    "Wes Anderson",
    "Wes Anderson",
    "there's definitely a pattern here...",
    "Bill Murray, Angelica Houston, Owen Wilson, Cate Blanchett, \
    and Dr. Ian Malcolm")

school_of_rock = media.Movie(
    "School of Rock",
    "A destitute rocker poses as a substitute teacher and convinces his \
    class to start a band.",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74",
    "3 October 2003", "109 min",
    "Richard Linklater, really?",
    "Jack White",
    "Robert Plant and Jimmy Page (part of the contract for the rights to use \
    Immigrant Song (!True))",
    "Jack Black. There are others, but he's all that matters here.")

ratatouille = media.Movie(
    "Ratatouille",
    "In Paris, anyone can cook, and a rat with big dreams decides to \
    prove it.",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    "29 June 2007", "115 min",
    "Brad Bird",
    "Brad Bird",
    "Pinky, the Brain",
    "Patton Oswalt, everyone else is an animator")

midnight_in_paris = media.Movie(
    "Midnight In Paris",
    "On his honeymoon, Owen Wilson time travels solo to crash parties \
    in Paris past. The highly anticipated sequel to Wedding Crashers.",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=atLg2wqqXVu",
    "Decembre 1921",
    "100 min",
    "Woody Allen",
    "Woody Allen",
    "Woody Allen?",
    "Owen Wilson, Rachel McAdams")

hunger_games = media.Movie(
    "Hunger Games",
    "A girl kills everyone...",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo",
    "23 March 2012", "142 mins",
    "Gary Ross",
    "Suzanne Collins, annnd Gary Ross",
    "Tywin Lannister",
    "That Jennifer Lawrence, she's so hot right now.")

mad_max = media.Movie(
    "Mad Max: Fury Road",
    "Charlize Theron drives a Big Rig. So Shiny. So Chrome.",
    "http://d1oi7t5trwfj5d.cloudfront.net/0c/71/6a48f0b74b27b795f5c8ecca5f6a/mad-max-fury-road.jpg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8",
    "15 May 2015",
    "120 min",
    "George Miller",
    "George Miller",
    "George Miller",
    "Charlize Theron, Tom Hardy")

dune = media.Movie(
    "Dune",
    "Drug Wars... In Space...",
    "http://i1191.photobucket.com/albums/z471/posterocalypse/Posters%205/KilianEngDune.jpg",
    "https://www.youtube.com/watch?v=jg4OCeSTL08",
    "Well, never.",
    "NaN",
    "Alejandro Jodorowsky",
    "Frank Herbert",
    "Alejandro Jodorowsky",
    "Sting? That scary overprotective dad from Agents of Shield?")

movies = [mad_max, toy_story, avatar, zissou, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games, dune]

# Call open_movies_page function from fresh_tomatillos module
fresh_tomatillos.open_movies_page(movies)
