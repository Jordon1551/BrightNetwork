"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = None
        self.pause = True
        self.playlists = {}
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        all_videos = self._video_library.get_all_videos()
        
        for each in sorted(all_videos, key=lambda Video: Video.title):
            print("{0} ({1}) [{2}]".format(each.title, each.video_id,
                                           str(each.tags)[1:-1].replace("'","").replace(",","")))


    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if(video == None):
            print("Cannot play video: Video does not exist")
        elif(self.playing!= None):
            print("Stopping video: {0}".format(self.playing.title))
            self.playing = video
            self.pause=False
            print("Playing video: {0}".format(self.playing.title))
        else:
            self.playing = video
            self.pause=False
            print("Playing video: {0}".format(self.playing.title))

    def stop_video(self):
        """Stops the current video."""
        if(self.playing != None):
            self.pause = True
            print("Stopping video: {0}".format(self.playing.title))
            self.playing = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        if(self.playing!= None):
            print("Stopping video: {0}".format(self.playing.title))
        all_videos = self._video_library.get_all_videos()
        vid_num = random.randint(1, len(all_videos))
        counter = 1
        for each in all_videos:
            if counter == vid_num:
                self.playing = each
                print("Playing video: {0}".format(self.playing.title))
                break
            counter=counter+1

    def pause_video(self):
        if(self.pause==False):
            print("Pausing video: {0}".format(self.playing.title))
            self.pause = True
        elif(self.playing==None):
            print("Cannot pause video: No video is currently playing")
        else:
            print("Video already paused: {0}".format(self.playing.title))


    def continue_video(self):
        if(self.playing==None):
            print("Cannot continue video: No video is currently playing")
        elif(self.pause==False):
            print("Cannot continue video: Video is not paused")
        else:
            self.pause=False
            print("Continuing video: {0}".format(self.playing.title))

    def show_playing(self):
        if(self.playing != None):
            if(self.pause==False):
                print("Currently playing: {0} ({1}) [{2}]".format(self.playing.title, self.playing.video_id,
                                                                  str(self.playing.tags)[1:-1].replace("'","").replace(",","")))
            else:
                print("Currently playing: {0} ({1}) [{2}] - PAUSED".format(self.playing.title, self.playing.video_id,
                                                                  str(self.playing.tags)[1:-1].replace("'","").replace(",","")))
        else:
            print("No video is currently playing")
            
        """Displays video currently playing."""


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name2 = playlist_name.lower()
        if(playlist_name2 not in self.playlists):
            self.playlists[playlist_name2] = ""
            print("Successfully created new playlist: " + playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_name=playlist_name.lower()
        if(playlist_name in self.playlists):
            if(video_id not in self.playlists[playlist_name]):
               video = self._video_library.get_video(video_id)
               if(video!=None):
                   self.playlists[playlist_name] = self.playlists[playlist_name] + video_id + "|"
                   print("Added video to {0}: {1}".format(playlist_name,video.title))
               
               else:
                   print("Cannot add video to {0}: Video does not exist".format(playlist_name))
            else:
                print("Cannot add video to {0}: Video already added".format(playlist_name))
        else:
            print("Cannot add video to {0}: Playlist does not exist".format(playlist_name))
            

    def show_all_playlists(self):
        """Display all playlists."""
        if(not self.playlists):
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            playlists = list(self.playlists.keys())
            for each in playlists:
                print("  " + each)


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name2=playlist_name.lower()
        if(not self.playlists):
            print("Cannot show playlist {0}: Playlist does not exist".format(playlist_name))
        else:
            print("Showing playlist: {0}".format(playlist_name))
            if(bool(self.playlists[playlist_name2])):
                playlists = self.playlists[playlist_name2].split("|")
                for each in playlists:
                    if(each != playlists[-1]):
                        video = self._video_library.get_video(each)
                        print("  {0} ({1}) [{2}]".format(video.title, video.video_id,
                                           str(video.tags)[1:-1].replace("'","").replace(",","")))
            else:
                print("  No videos here yet")
                

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_name=playlist_name.lower()
        if(not self.playlists):
            print("Cannot remove video from {0}: Playlist does not exist".format(playlist_name))
        elif(self._video_library.get_video(video_id)==None):
            print("Cannot remove video from {0}: Video does not exist".format(playlist_name))
        elif(video_id in self.playlists.get()):
            self.playlists = {key:val for key, val in self.playlists.items() if key!=playlist_name and val!=video_id}
            video = self._video_library.get_video(each)
            print("Removed video from {0}: {1}".format(playlist_name, video.title))
        else:
            print("Cannot remove video from {0}: Video is not in playlist")
        
            

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name=playlist_name.lower()
        if(not self.playlists):
            print("Cannot clear playlist {0}: Playlist does not exist".format(playlist_name))
        else:
            self.playlist[playlist_name] = None
            print("Successfully removed all videos from {0}".format(playlist_name))
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name=playlist_name.lower()
        if(not self.playlists):
            print("Cannot delete playlist {0}: Playlist does not exist".format(playlist_name))
        else:
            del self.playlists[playlist_name]
            print("Deleted playlist: {0}".format(playlist_name))
        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
