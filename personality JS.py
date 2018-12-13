import pyautogui as pg
import webbrowser as wb
import time as t
show = pg.prompt("What's your favorite show?")

if show == "Parks and Rec":
    pg.alert("Eh, it's ok...")
elif show == "The Office":
    pg.alert("I love that show!!")
    wb.open("https://www.youtube.com/watch?v=AXW9Hfoneuk")
    t.sleep(10)
elif show == "How I Met your Mother":
    pg.alert("I love that show!!")
    wb.open("https://www.youtube.com/watch?v=mYb0B_-jaBU")
    t.sleep(20)
elif show == "how i met your mother":
    pg.alert("I love that show!!")
    wb.open("https://www.youtube.com/watch?v=mYb0B_-jaBU")
    t.sleep(20)
elif show == "How I met your mother":
    pg.alert("I love that show!!")
    wb.open("https://www.youtube.com/watch?v=mYb0B_-jaBU")
    t.sleep(20)
elif show == "Keeping up with the Kardashians":
    pg.alert("I love that show!!")
elif show == "The Suit Life of Zach and Cody":
    pg.alert("I love that show!!")
elif show == "Barbie Life in the Dreamhouse":
    pg.alert("I love that show!!")
else:
    pg.alert("Your favorite show is  " +  show)
          

food = pg.prompt("Whats your favorite food?")

if food == "pizza":
    pg.alert("yumm")
    wb.open ("https://www.google.com/search?q=pizza&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjb6uCJ9PneAhVikuAKHYngDMEQ_AUIDygC&biw=1361&bih=616#imgrc=NU5IXc-7TBz_tM:")
    t.sleep(7)
elif food == "pasta":
    pg.alert("I love pasta!")
    wb.open ("https://www.google.com/search?q=pasta&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjhwImQ8IvfAhWIZd8KHVW6AYcQ_AUIDigB&biw=946&bih=466#imgrc=3Jb6yGVI0ouQnM:")
    t.sleep(4)
elif food == "Mac and Cheese":
    pg.alert("I love Mac and Cheese!")
    wb.open("https://www.google.com/search?q=mac+n+cheese&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwidpOXT8IvfAhVsmeAKHU6SC4kQ_AUIDigB&biw=946&bih=466#imgrc=jOlTmG9Khz02BM:")
    t.sleep(4)
elif food == "Brownies":
    pg.alert("I love to bake brownies!")
    wb.open ("https://www.google.com/search?q=brownies&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj0lrS99PneAhWKTt8KHaiBC1QQ_AUIDigB&biw=1361&bih=616#imgrc=PoUpUZJ8MhK2uM:")
    t.sleep(6)
elif food == "Ice Cream":
    pg.alert("Yum!")
elif food == "nutella":
    pg.alert("Yummy in my tummy!")
else:
    pg.alert("Your favorite food is  " +  food)

color = pg.prompt("What's your favorite color?")

if color == "red":
    wb.open("https://www.google.com/search?q=red&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjPi6SO8YvfAhWict8KHU-zD3EQ_AUIDigB&biw=946&bih=466#imgrc=9sW5vanh738I5M:")
    t.sleep(3)
    pg.alert("cool!")
elif color == "yellow":
    wb.open("https://www.google.com/search?q=yellow&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjPj9bl8YvfAhWDmeAKHVF7DWEQ_AUIDigB&biw=946&bih=466#imgrc=lXbAbg1jvrLnyM:")
    t.sleep(3)
    pg.alert("Thats my favorite color!")
elif color == "orange":
    wb.open("https://www.google.com/search?q=orange&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiqqvT18YvfAhWPnOAKHSJcCycQ_AUIDigB&biw=946&bih=466#imgrc=LA913WkZHUUsjM:")
    t.sleep(3)
    pg.alert("nice!")
elif color == "green":
    wb.open("https://www.google.com/search?q=green&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiB0peD8ovfAhUjiOAKHY75CY4Q_AUIDigB&biw=946&bih=466#imgrc=xL0IT6JvkA7_kM:")
    t.sleep(3)
    pg.alert("Love!")
elif color == "Blue":
    pg.alert("Love that color!")
elif color == "Purple":
    pg.alert("Cool!")
else:
    pg.alert("Your favorite color is " +  color)

sport = pg.prompt("What's your favorite sport?")

if sport == "soccer":
    pg.alert("cool!")
elif sport == "football":
    pg.alert("Thats my favorite sport!")
elif sport == "volleyball":
    pg.alert("nice!")
elif sport == "field hockey":
    pg.alert("Awsome!")
elif sport == "lacrosse":
    pg.alert("Love that!")
elif sport == "hockey":
    pg.alert("Cool!")
else:
    pg.alert("Your favorite sport is " +  sport)


movie = pg.prompt("What's your favorite movie?")

if movie == "Frozen":
    pg.alert("Icy Answer!")
elif movie == "Anything Disney":
    pg.alert("I love disney!")
elif movie == "Divergent":
    pg.alert("nice!")
elif movie == "To all the Boys I Loved Before":
    pg.alert("I love Noah Centineo!")
elif movie == "Muppets Most Wanted":
    pg.alert("Love that!")
elif movie == "Star Wars":
    pg.alert("Cool!")
else:
    pg.alert("Your favorite movie is " +  movie)




          

          
