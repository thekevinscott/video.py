# Blog Post

Depending on who you ask, self-driving cars are either right around the corner or will never work.

> Chris Urmson claims, with his son's 16th birthday and driver's test fast approaching, that "My team are committed to making sure that doesn't happen." [TED](https://www.ted.com/talks/chris_urmson_how_a_driverless_car_sees_the_road
).

Among all the other things a self-driving car must do, perhaps the most crucial is pedestrian recognition: recognizing people from video.

At Pachyderm, we build tools that help data scientists create repeatable
experiments. Part of how we do that is by breaking tasks into
composable subtasks.

In this set of posts, we'll build a pipeline capable of taking an ingesting a video stream and identifying people in the frames. This post will tackle the very first step: breaking an incoming video into frames for further analysis.

##Prerequisites

This guide assumes that you already have Pachyderm running locally. [Check out our Local Installation](http://docs.pachyderm.io/en/latest/getting_started/local_installation.html) instructions if haven’t done that yet and then come back here to continue.

##Getting running

*You can view the full code at http://github.com/thekevinscott/videos.py*

Start by creating a Pachyderm repository:

```
pachctl create-repo videos
```

We name our repo `videos`. This is important - we'll refer to this later to
retrieve our exported frames. You can see all the repos in Pachyderm with:

```
pachctl list-repo
```

Next, download a sample video and add it to your repository with:

```
pachctl put-file videos master sample.mp4 -f https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4
```

You can grab sample videos from https://sample-videos.com has. We call our video `sample.mp4`. When you add a file to Pachyderm, it's tagged with a specific commit. You can see all your commits with:

```
pachctl list-commit videos
```

To see the file you just added, specify the commit id:

```
pachctl list-file videos <COMMIT_ID>
```

The next step is to create a pipeline, so the video can be processed:

```
pachctl create-pipeline -f https://raw.githubusercontent.com/thekevinscott/videos.py/master/videos.json
```

This JSON file is our pipeline spec. Here's how it looks:


```
{
  "pipeline": {
    "name": "split-video"
  },
  "transform": {
    "cmd": [
        "python3",
        "/split-video-frames.py",
        "--source",
        "/pfs/videos/sample.mp4",
        "--target",
        "/pfs/out/written-images"
    ],
    "image": "videos"
  },
  "input": {
    "atom": {
      "repo": "thekevinscott/videos.py",
      "glob": "/*"
    }
  }
}
```

It defines a Python script, `split-video-frames.py`, that will split our video into frames, along with arguments for calling that script. If you'd like, you can clone the [repo locally](http://github.com/thekevinscott/videos.py) and invoke the script with:

```
python3 split-video-frames.py --source sample.mp4 --target ./out
```

Our pipeline hardcodes the input video - `sample.mp4` - along with the output folder. Pachyderm automatically provides two folders for us:

* `/pfs/videos`, which matches your repo name, contains any files you've imported with `pachyderm put-file`.
* `/pfs/out` contains all the output that your scripts write.

## Seeing your frames

As soon as you created your pipeline, Pachyderm should start running. You can see progress with:

```
pachctl list-pipeline
```

And you can see output from the script with:

```
pachctl get-logs video
```

Finally, once the script has completed, you can preview your frames with:

```
pachctl get-file split-video master written-images/10.jpg | open -f -a /Applications/Preview.app
```

## Next

Great! We now have a pipeline that takes our videos and splits them into
frames. Next we can begin running person detection on them.
