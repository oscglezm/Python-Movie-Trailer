import webbrowser


class Movie():

    """ This class provides a way to store movies info"""
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url , rating, duration, category, ranking):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating
        self.duration = duration
        self.category = category
        self.ranking = ranking

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_head_info(self):
        head_info = self.rating + " | "+ self.duration + " | " + self.category + " | " + self.ranking
        return head_info


class Series(Movie):
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url , rating, duration, category, ranking, seasons, episodes):
        Movie.__init__(self,title, storyline, poster_image_url, trailer_youtube_url , rating, duration, category, ranking)
        self.seasons = seasons
        self.episodes = episodes

    def show_head_info(self):
        head_info = self.rating + " | " + self.duration + " | " + self.category + " | " + self.ranking + " | " + self.seasons + " | " + self.episodes
        return head_info
