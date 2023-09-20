# Stable Marriage Algorithm Implementation

This repository contains a Python implementation of the Stable Marriage Algorithm, a mechanism for solving the stable marriage problem. The algorithm is widely used in the field of matching theory to find a stable matching between two sets of elements, such as job applicants and employers or medical students and residency programs.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Algorithm Description](#algorithm-description)
- [Test Files](#test-files)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Stable Marriage Algorithm is a mechanism designed to find a stable matching between two sets of elements, each with their own preferences. It ensures that there are no pairs of elements who would both prefer to be matched with each other over their current partners.

## Usage

To use this Python implementation of the Stable Marriage Algorithm, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MohammadYasinKarbasian/Stable-Marriage.git
2. Run the algorithm by executing the main Python script:

    ```bash

    python 'stable marriage.py'
3. Follow the prompts to provide the input data or specify the test file you want to use for matching.

4. The algorithm will perform the matching and display the results.

## Algorithm Description
1. The Stable Marriage Algorithm works as follows:

2. Two sets of elements, each with their preferences, are given as input.

3. The algorithm proceeds in rounds, where each element in one set proposes to the most preferred element in the other set who has not already rejected them.

4. The receiving elements compare the proposals and either accept the proposal or reject it in favor of a more preferred proposer.

5. This process continues until no more proposals can be made.

6. The result is a stable matching, where no element has an incentive to break their current match in favor of another.

## Test Files
This repository includes four test.txt files, which contain sample input data for testing the Stable Marriage Algorithm. You can use these files to validate the correctness and performance of the implementation. Each test file contains a description of the problem and the preferences of the elements.

* Test1.txt
* Test2.txt
* Test3.txt
* Test4.txt
## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or bug fixes, please open an issue or create a pull request. For major changes, please discuss them in an issue first.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
