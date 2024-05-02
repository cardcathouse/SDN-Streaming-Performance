# Test suite for multimedia streaming over SDN performance evaluation

This test suite was created to evaluate the performance of a multimedia streaming service over a software-defined network when stressed with external TCP and UDP traffic. The test suite was designed to run on Arch based distros.

More about this work can be read [here.](https://dev.to/cardcathouse/an-exploration-of-software-defined-networks-in-video-streaming-part-three-performance-of-a-streaming-system-over-a-sdn-c55)

# Requirements

* Java 8 as provided by [OpenJDK8](https://archlinux.org/packages/?name=jdk8-openjdk)
* [Python 3](https://archlinux.org/packages/?name=python)
	* [RangeHTTPServer](https://pypi.org/project/rangehttpserver/) (1.3.3) should be installed through pip. I used Miniconda for environment managing.
* [Mininet](https://aur.archlinux.org/packages/mininet) 2.3.0-2
	* If installing on Manjaro, the following packages should be installed **before** installing Mininet to avoid compilation errors:
		* [byacc](https://archlinux.org/packages/extra/x86_64/byacc/) (20230521-1)
		* [flex](https://archlinux.org/packages/core/x86_64/flex/) (2.6.4-5)
		* [libcgroup](https://aur.archlinux.org/packages/libcgroup) (3.1.0-0)
		* [patch](https://archlinux.org/packages/core/x86_64/patch/) (2.7.6-10)
		* [autoconf](https://archlinux.org/packages/core/any/autoconf/) (2.72-1)
		* [automake](https://archlinux.org/packages/core/any/automake/) (1.16.5-2)
		* [pkgconf](https://archlinux.org/packages/core/x86_64/pkgconf/) (2.1.0-2)
* [OpenDaylight](https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip) (0.8.4)
* [xterm](https://archlinux.org/packages/extra/x86_64/xterm/) (390-1)
* [Wireshark](https://wiki.archlinux.org/title/wireshark) (4.2.3-1)
* [VLC Media Player](https://archlinux.org/packages/extra/x86_64/vlc/) (3.0.20-7)
* [GPAC](https://archlinux.org/packages/extra/x86_64/gpac/) (1:2.2.1-2)
* [ffmpeg](https://archlinux.org/packages/extra/x86_64/ffmpeg/) (2:6.1.1-6)
* [CMake](https://archlinux.org/packages/extra/x86_64/cmake/) 3.28.3-1
* [GCC](https://archlinux.org/packages/core/x86_64/gcc/) (13.2.1-5)
* [Ninja](https://archlinux.org/packages/extra/x86_64/ninja/) (1.11.1-3)
* [Git](https://archlinux.org/packages/extra/x86_64/git/) (2.44.0-1)

Additionally, a 4K video in MP4 format is also required. It should have a minimum runtime of 5 minutes. This video should be named "video_4k.mp4" to ensure compatibility with the files used for this project. This video will be downscaled to 1080, 720, 480, 360, and 240p resolutions.

# Test environment setup steps

1. Install the latest version of [Python](https://wiki.archlinux.org/title/Python#Installation) and [Java 8](https://wiki.archlinux.org/title/Java#OpenJDK)
	- It is **very** important that you set Java version 8 as default in case you also have other newer releases installed. OpenDaylight won't work with any other Java version.
2. Install HTTPRangeServer and the Mininet Python library with command `pip install HTTPRangeServer mininet`
3. Install xterm, Wireshark, VLC Media Player, GPAC, ffmpeg, CMake, gcc, ninja and git. 
4. Install byacc, flex, libcgroup, patch, autoconf, automake and pkgconf
5. Install Mininet
6. Ensure Mininet has been installed correctly by running command `sudo mn`. Mininet should automatically deploy a default network. When done, type `exit` in the Mininet command prompt, then run `sudo mn -c`. 
7. Run the following comands in superuser mode
	```
	# systemctl enable ovs-vswitchd
	# systemctl start ovs-vswitchd
	```
8. Create a new directory with command 
	```
	mkdir streaming-sdn
	cd streaming-sdn
	```
9. Clone this project's repository with command
	```
	git clone https://github.com/cardcathouse/SDN-Streaming-Performance.git
	```
10. Download OpenDaylight with command
	 ```
	 wget https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
	 ```
11. Unzip the contents of the downloaded file. You should now have a folder labeled `karaf-0.8.4`
12. Run `./od.sh` to start OpenDaylight.
13. When OpenDaylight has finished booting up, copy and paste the following command in the terminal to install the required modules:
	 ```
	 feature:install odl-openflowplugin-drop-test odl-openflowplugin-nxm-extensions odl-openflowplugin-app-bulk-o-matic odl-openflowplugin-app-lldp-speaker odl-openflowplugin-app-southbound-cli odl-openflowplugin-flow-services-rest odl-openflowplugin-app-table-miss-enforcer odl-openflowplugin-app-topology-lldp-discovery odl-dluxapps-nodes odl-dluxapps-yangui odl-dluxapps-yangman odl-dluxapps-topology odl-dluxapps-yangutils odl-dluxapps-applications odl-dluxapps-yangvisualizer odl-restconf-all odl-openflowplugin-app-topology-manager odl-openflowplugin-app-notifications odl-openflowplugin-onf-extensions odl-openflowplugin-app-forwardingrules-sync odl-l2switch-all odl-mdsal-all odl-yanglib odl-dlux-core
	 ```
14. When module installation has finished, close OpenDaylight by pressing Ctrl+D.
15. Put your video in the `streaming-cdn` folder. Run `./video_prepare.sh`. The folder should now have a considerable amount of new files with the `.m4s` file extension. ***Do not rename or modify these files!***


# UDP test reproduction steps

## Reproduction steps
1. Open a terminal in the `streaming-sdn` folder. All commands should run on this folder.
2. Run OpenDaylight with `./od.sh` and wait for boot process to finish
3. Run the topology with command `sudo python udp_test_Xm.py`, where `X` is the bandwith limit (1, 3, 5 or 10 Mbps).
4. The network will start running and execute a script that automates some tasks in the setup process. VLC and Wireshark will open. A couple of manual configurations are needed, and the script will give you 60 seconds to make them. 
	1. On VLC, press Ctrl+P to open the 'Preferences' menu.
	2. Look for the 'Show Settings' option in the bottom left corner. Select 'All'. A new menu will appear.
	3. On the menu at the left side of the window, navigate to the "Input/Codecs" section. Click on 'Demuxers' twice to show the dropdown options. Click on 'Adaptive' and change the video streaming algorithm to 'Adaptive bandwidth'.
	4. On the same "Input/Codecs" section, click on 'Stream Filters' once. Select "HTTP Dyanmic Streaming" from the list
	5. Click on 'Save'.
		1. It's likely VLC will tell you the settings can't be written to the config file. You can ignore this message, although these steps will have to be done each time VLC is opened under Mininet.
	6. Move to the Wireshark window. Select `h2-eth0` from the menu displayed on-screen.
	7. On the new screen, select the bar on the upper part of the interface that says "Apply a display filter" and type `http`, then click on the arrow button.
	8. Select 'Statistics' from the top menu, then the 'I/O Graphs' option.
	9. On the new screen, deselect every option except for the one that has 'http' in the "Display Filter" column.
	10. Click on the "+" button to add a new row. Select the blank space at the "Display Filter" column of this new row and type `udp`, then hit Enter.
	11. Return to the VLC window, and from the "Medium" menu located at the top of the screen, choose "Open network stream".
	12. Type in `http://localhost:8000/video4k.mpd` as the input HTTP URL, but **don't click play yet!**
5. When the 60 seconds for initial config have passed, a new 30 second timer will start. You can now click the 'Play' button on the network stream window on VLC. Make sure to click play during this 30 second window.
6. After this timer, the test will start. Monitor the behavior of the traffic on Wireshark and observe the changes to playback on VLC.

# TCP test reproduction steps

For this test a heavy `.mp4` file is needed to provide the file each host will download, to be referred from here onward as the **download test file**. I recommend a file with a size above 5GB. Theoretically, any file type should work, as long as the size requirement is met and is appropriately named as specified in the following steps.

### Reproduction steps
1. Place your test download file in the `streaming-cdn` folder. Rename it `dl_test.mp4`.
2. Open a terminal in the `streaming-sdn` folder. All commands should run on this folder.
3. Run OpenDaylight with `./od.sh` and wait for boot process to finish
4. Run the topology with command `sudo python tcp_Xh.py`, where `X` is the number of hosts (5 to 50).
5. Refer to the instructions for the previous test and repeat steps 4 to 6