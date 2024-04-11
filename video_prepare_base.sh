#!/bin/zsh

fe="video4k.mp4"
f="video4k"

ffmpeg -i "${fe}" -c:a copy -vn "${f}_audio.mp4"

ffmpeg -i "${fe}" -an -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 5300k -maxrate 5300k -bufsize 2650k -vf 'scale=-1:1080' "${f}_1080.mp4"
ffmpeg -i "${fe}" -an -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 2400k -maxrate 2400k -bufsize 1200k -vf 'scale=-1:720' "${f}_720.mp4"
ffmpeg -i "${fe}" -an -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 1060k -maxrate 1060k -bufsize 530k -vf 'scale=-1:478' "${f}_480.mp4"
ffmpeg -i "${fe}" -an -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 600k -maxrate 600k -bufsize 300k -vf 'scale=-1:360' "${f}_360.mp4"
ffmpeg -i "${fe}" -an -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 260k -maxrate 260k -bufsize 130k -vf 'scale=-1:242' "${f}_242.mp4"

MP4Box -dash 1000 -rap -frag-rap -profile main "${f}_1080.mp4" "${f}_720.mp4" "${f}_480.mp4" "${f}_360.mp4" "${f}_240.mp4" "${f}_audio.mp4" -out "${f}.mpd"
