import datetime
def response_handler(body):
    
    x = datetime.datetime.today().weekday() 

    if x == 0:
        return "Happy Monday! You're 4 days away from Friday. Faith is taking the first step even when you don't see the whole staircase." , "http://7-themes.com/data_images/out/9/6796558-gorgeous-cave-wallpaper.jpg"
    if x == 1:
        return "Happy Tuesday! The ultimate measure of a man is not where he stands in moments of comfort and convenience, but where he stands at times of challenge and controversy." , "http://7-themes.com/data_images/out/78/7038133-beautiful-eiffel-pictures.jpg"
    if x == 2:  
        return "Happy Wednesday! Hump Dayyy! ;) " , "http://7-themes.com/data_images/out/71/7014545-butterflies-hd.jpg"
    if x == 3:
        return "Happy Thursday! Almost there!" , "http://images.nationalgeographic.com/wpf/media-live/photos/000/936/cache/bear-road-denali_93621_990x742.jpg"
    if x == 4:
        return "Friday, I've seen the promised land! I may not get there with you, but I want you to know tonight that we as a people will get to the promised land. -MLK" , "http://science-all.com/image.php?pic=/images/wallpapers/happy-image/happy-image-25.jpg"
    if x == 5:
        return "Happy Saturday, more like Sadder Day. We're gonna miss you guys :( ", "notalink"
    if x == 6:
        return "Happy Sunday, I look to a day when people will not be judged by the color of their skin, but by the content of their character.", "notalink"
