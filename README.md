# Reddit Video Maker

Generates videos of narrated Reddit articles or compilations of videos from subreddits.

## Installation

```
./setup.py install
```

## Example Usage

### Setup

Navigate to the example directory for generating compilations of videos from subreddits.

```
cd examples/reddit-video-compilations
```

#### Reddit API Authorization

Sign up for the Reddit API with a registered Reddit account and create an application. [See this guide](https://alpscode.com/blog/how-to-use-reddit-api/). Then copy the client ID and client secret for the application into `reddit_api_config.toml`.

#### YouTube API Authorization

Obtain OAuth 2.0 authorization credentials for the YouTube API through the Google API Console. [See this guide](https://developers.google.com/youtube/registering_an_application). Then download and place your OAuth 2.0 client secrets in `client_secrets.json`.

Now that OAuth 2.0 is setup, authorize a YouTube account using the authorization script. This account will have a video uploaded to its YouTube channel later in this guide.

```
./auth.py
```

### Generating a Video

Now we can generate a video. Here we use the configuration profile defined in `profile.toml`. Words will be censored in the video using words and phrases in `censor.txt`, and metadata like the video's title and tags will exclude words and phrases in `blocklist.txt`. All generated files will be placed in the directory `output`.

```
./create.py profile.toml -o output -c censor.txt -b blocklist.txt
```

You will want to populate `censor.txt` and `blocklist.txt` with your own words. Here is a [list of English swear words](https://github.com/RobertJGabriel/Google-profanity-words) and here's a [list of demonitized words for YouTube](https://docs.google.com/spreadsheets/d/1ozg1Cnm6SdtM4M5rATkANAi07xAzYWaKL7HKxyvoHzk/edit#gid=674179785).
