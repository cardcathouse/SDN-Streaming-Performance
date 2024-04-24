h1 python -m RangeHTTPServer &
h2 wireshark &
h2 vlc-wrapper &

h4 echo "2 minutes for configuration. Waiting..."
h4 sleep 120

h4 echo "Starting in 20 seconds, run the video..."
h4 sleep 20
h4 wget http://10.0.0.1:8000/dl_test.mp4 -O "test1.mp4" &

h5 echo "Starting in 5 seconds..."
h5 sleep 5
h5 wget http://10.0.0.1:8000/dl_test.mp4 -O "test2.mp4" &

h6 echo "Starting in 5 seconds..."
h6 sleep 5
h6 wget http://10.0.0.1:8000/dl_test.mp4 -O "test3.mp4" &

h7 echo "Starting in 5 seconds..."
h7 sleep 5
h7 wget http://10.0.0.1:8000/dl_test.mp4 -O "test4.mp4" &

h8 echo "Starting in 5 seconds..."
h8 sleep 5
h8 wget http://10.0.0.1:8000/dl_test.mp4 -O "test5.mp4"