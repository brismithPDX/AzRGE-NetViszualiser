<!-- Top Level Warnings and Notices -->

<!-- ABOUT THE PROJECT -->
## About The Project


This project lets us visualize the entirety of the an azure network environment across all subscriptions as a interactive web graph based on Az Resource Graph Explorer query results. 

### Project History

This project is the result of a 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python3
- Azure Resource Graph Access
- Python3 pip repo dependencies : csv, matplotlib, networkx, pyvis


<!-- USAGE EXAMPLES -->
## Usage

0. install the required python dependencies to your runtime environment
1. Run the two kusto quires to generate the export.csv (from the VMnetworkinfo.kusto query) and export1.csv (from the NetworkPeeringInfo.kusto query)
2. Execute the visualize.py 
3. Open the resulting example.html file to explore the network graph


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Repo Manager

Brian Smith 


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Project Citations and External References

Documentation to project includes and dependency resources

* [Pyvis](https://pyvis.readthedocs.io/en/latest/tutorial.html)
* [visjs](https://visjs.github.io/vis-network/docs/network/)
* [Python3 CSV](https://docs.python.org/3/library/csv.html)
* [Azure Resource Graph](https://docs.microsoft.com/en-us/azure/governance/resource-graph/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png