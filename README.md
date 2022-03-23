<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

<h1 align="center">Autonomous Package Retrieval: TurtleBot3</h1>

  <p align="center">
    METE 4300U Course Project @ Ontario Tech University
    <br />
    <br />
    <a href="https://github.com/shafinmahmed/waffle-pi-pancake/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project uses a TurtleBot3 Waffle Pi to map and navigate an enclosed arbitrary area to locate packages marked with ArUco Markers, retrieve the desired package, and return to the starting pose. 

### Built With

* [ROS Kinetic](http://wiki.ros.org/kinetic)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This package is only compatible with **ROS Kinetic (Ubuntu 16.04)**. 
Make sure to have the following installed:
</br>
* The [ROBOTIS TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/) package. 
* [explore_lite](http://wiki.ros.org/explore_lite)
* [vision_msgs](http://wiki.ros.org/vision_msgs)
* [aruco_detect](http://wiki.ros.org/aruco_detect)


### Installation
Install the package on both your _Remote PC_ and the _TB3 Onboard Raspberry Pi_. Do the following for both.

1. Clone the repo to `[your_workspace]/src/`

   ```sh
   git clone https://github.com/shafinmahmed/waffle-pi-pancake.git
   ```
2. Build with `catkin_make` or [catkin command line tools](https://catkin-tools.readthedocs.io/en/latest/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Always begin by initiating **roscore**. Each milestones have their own dedicated launch files. 
#### Remote PC
For the Remote PC, choose the desired launch file. For example, run the following for milestone 1
```sh
roslaunch mobile_robo ms1_tb3.launch
```

#### Raspberry Pi
Launch **bringup**
```sh
roslaunch mobile_robo tb3_bringup.launch
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Milestone 1: map arbitrary enclosed area and return to starting pose
- [x] Milestone 2: Milestone 1 + detect and mark packages in the enclosed area
- [ ] Milestone 3: Milestone 2 + perform obstacle avoidance in the enclosed area
- [ ] Milestone 4: Milestone 3 + pick up the desired package
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[Shafin Ahmed](mailto:shafin.ahmed@ontariotechu.net) </br>
[Mashaal Jawad](mailto:mashaal.jawad@ontariotechu.net) </br>
[Noor Khabbaz](mailto:noor.khabbaz@ontariotechu.net) </br>
[Shahram Mohsini](mailto:shahram.mohsini@ontariotechu.net) </br>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Dr. Scott Nokleby](https://ontariotechu.ca/experts/feas/scott-nokleby.php)
* [Lillian Goodwin](mailto:lillian.goodwin@ontariotechu.ca)
* [Christopher Baird](mailto:Christopher.Baird@ontariotechu.ca)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shafinmahmed/waffle-pi-pancake.svg?style=for-the-badge
[contributors-url]: https://github.com/shafinmahmed/waffle-pi-pancake/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shafinmahmed/waffle-pi-pancake.svg?style=for-the-badge
[forks-url]: https://github.com/shafinmahmed/waffle-pi-pancake/network/members
[stars-shield]: https://img.shields.io/github/stars/shafinmahmed/waffle-pi-pancake.svg?style=for-the-badge
[stars-url]: https://github.com/shafinmahmed/waffle-pi-pancake/stargazers
[issues-shield]: https://img.shields.io/github/issues/shafinmahmed/waffle-pi-pancake.svg?style=for-the-badge
[issues-url]: https://github.com/shafinmahmed/waffle-pi-pancake/issues
[license-shield]: https://img.shields.io/github/license/shafinmahmed/waffle-pi-pancake.svg?style=for-the-badge
[license-url]: https://github.com/shafinmahmed/waffle-pi-pancake/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
