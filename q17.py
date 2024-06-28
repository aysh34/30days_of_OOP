class Media:
    def __init__(self, duration):
        self.duration = duration

    def play(self):
        print("Playing the media...")

    def stop(self):
        print("Stopping the media...")

    def set_duration(self):
        return f"Duration: {self.duration}"


class Video(Media):
    def play(self):
        print("Playing video...")

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"Brightness set to level {self.brightness}")


class Audio(Media):
    def play(self):
        print("Playing audio...")

    def adjust_volume(self, volume):
        self.volume = volume
        print(f"Volume adjusted to level {self.volume}")


class AudioVideo(Audio, Video):
    def play(self):
        Video.play(self)
        Audio.play(self)

    def stop(self):
        super().stop()

    def get_details(self):
        print("\nThe details of media file is")
        print(f"{self.set_duration()}")
        print(f"Brightness: {self.brightness}")
        print(f"Volume: {self.volume}")


av = AudioVideo("23 minutes")
av.play()
av.set_brightness(7)
av.adjust_volume(21)
av.get_details()
av.stop()
