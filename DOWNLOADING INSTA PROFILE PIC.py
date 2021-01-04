import instaloader

ig = instaloader.Instaloader()

while True:
    username = input("enter the username:")

    print(ig.download_profile(username,profile_pic_only=True))
