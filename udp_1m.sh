h1 python -m RangeHTTPServer &
h2 wireshark &
h2 vlc-wrapper &
h3 iperf -s -u &

h4 echo '1 minute for configuration..."'
h4 sleep 60

h4 echo 'Starting in 30 seconds...'
h4 sleep 30

h4 iperf -c 10.0.0.3 -u -b 200k -t 30
h4 sleep 10

h4 iperf -c 10.0.0.3 -u -b 400k -t 30
h4 sleep 10

h4 iperf -c 10.0.0.3 -u -b 600k -t 30
h4 sleep 10

h4 iperf -c 10.0.0.3 -u -b 800k -t 30
h4 sleep 10

h4 iperf -c 10.0.0.3 -u -b 1.1m -t 30
h4 sleep 10

h4 iperf -c 10.0.0.3 -u -b 1.2m -t 30