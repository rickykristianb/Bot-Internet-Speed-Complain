import botbrain

PROMISED_DOWNLOAD = 100.00
PROMISED_UPLOAD = 100.00


def main():
    brain = botbrain.InternetSpeedTwitterBot()
    speed = brain.get_internet_speed()
    download_speed = speed[0]
    upload_speed = speed[1]
    print(download_speed, upload_speed)
    if download_speed < PROMISED_DOWNLOAD or upload_speed < PROMISED_UPLOAD:
        brain.tweet_at_provider()


if __name__ == "__main__":
    main()
