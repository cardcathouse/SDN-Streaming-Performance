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
h8 wget http://10.0.0.1:8000/dl_test.mp4 -O "test5.mp4" &

h9 echo "Starting in 5 seconds..."
h9 sleep 5
h9 wget http://10.0.0.1:8000/dl_test.mp4 -O "test6.mp4" &

h10 echo "Starting in 5 seconds..."
h10 sleep 5
h10 wget http://10.0.0.1:8000/dl_test.mp4 -O "test7.mp4" &

h11 echo "Starting in 5 seconds..."
h11 sleep 5
h11 wget http://10.0.0.1:8000/dl_test.mp4 -O "test8.mp4" &

h12 echo "Starting in 5 seconds..."
h12 sleep 5
h12 wget http://10.0.0.1:8000/dl_test.mp4 -O "test9.mp4" &

h13 echo "Starting in 5 seconds..."
h13 sleep 5
h13 wget http://10.0.0.1:8000/dl_test.mp4 -O "test10.mp4" &

h14 echo "Starting in 5 seconds..."
h14 sleep 5
h14 wget http://10.0.0.1:8000/dl_test.mp4 -O "test11.mp4" &

h15 echo "Starting in 5 seconds..."
h15 sleep 5
h15 wget http://10.0.0.1:8000/dl_test.mp4 -O "test12.mp4" &

h16 echo "Starting in 5 seconds..."
h16 sleep 5
h16 wget http://10.0.0.1:8000/dl_test.mp4 -O "test13.mp4" &

h17 echo "Starting in 5 seconds..."
h17 sleep 5
h17 wget http://10.0.0.1:8000/dl_test.mp4 -O "test14.mp4" &

h18 echo "Starting in 5 seconds..."
h18 sleep 5
h18 wget http://10.0.0.1:8000/dl_test.mp4 -O "test15.mp4"