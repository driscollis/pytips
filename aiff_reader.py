import aifc


with aifc.open("sound.aiff") as obj:
    print(f"Number of channels: {obj.getnchannels()}",)
    print(f"Sample width: {obj.getsampwidth()}")
    print(f"Frame rate: {obj.getframerate()}.")
    print(f"Number of frames: {obj.getnframes()}",)
    print(f"parameters: {obj.getparams()}")
